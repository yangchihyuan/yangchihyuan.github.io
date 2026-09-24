import os
from urllib.request import urlretrieve

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


INPUT_DIR = "Tools/Crop_face/input_images"
OUTPUT_DIR = "Tools/Crop_face/output_images"
TARGET_WIDTH = 350
TARGET_HEIGHT = 450

# The eye x positions are intentionally not fixed.
EYES_TARGET_Y = 235
MOUTH_TARGET_Y = 342

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "face_landmarker.task",
)

MODEL_PATH = r"C:\temp\face_landmarker.task"

MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/face_landmarker/"
    "face_landmarker/float16/1/face_landmarker.task"
)


def ensure_model_file():
    if os.path.exists(MODEL_PATH):
        return

    print("Downloading Face Landmarker model...")
    try:
        urlretrieve(MODEL_URL, MODEL_PATH)
    except Exception as exc:
        raise RuntimeError(
            f"Unable to download the model: {MODEL_URL}\n"
            f"Save it as: {MODEL_PATH}"
        ) from exc


def get_face_points(face_landmarks, image_width, image_height):
    def point(index):
        landmark = face_landmarks[index]
        return np.array(
            [landmark.x * image_width, landmark.y * image_height],
            dtype=np.float32,
        )

    # Average several landmarks for a stable eye center.
    eye_a = np.mean([point(i) for i in (33, 133, 159, 145)], axis=0)
    eye_b = np.mean([point(i) for i in (263, 362, 386, 374)], axis=0)

    # Average mouth corners and upper/lower lip centers.
    mouth_center = np.mean([point(i) for i in (61, 291, 13, 14)], axis=0)

    left_eye, right_eye = sorted((eye_a, eye_b), key=lambda eye: eye[0])
    return left_eye, right_eye, mouth_center


def align_face_by_eyes_and_mouth(image, left_eye, right_eye, mouth_center):
    """Align eye and mouth y coordinates without fixing eye x coordinates."""
    eye_midpoint = (left_eye + right_eye) / 2
    eye_vector = right_eye - left_eye
    if np.linalg.norm(eye_vector) < 1:
        return None

    # Rotate so that both eyes are on the same horizontal line.
    angle = -np.arctan2(eye_vector[1], eye_vector[0])
    cos_angle, sin_angle = np.cos(angle), np.sin(angle)
    rotation = np.array(
        [[cos_angle, -sin_angle], [sin_angle, cos_angle]],
        dtype=np.float32,
    )

    rotated_eye_midpoint = rotation @ eye_midpoint
    rotated_mouth_center = rotation @ mouth_center
    mouth_eye_distance = rotated_mouth_center[1] - rotated_eye_midpoint[1]
    target_mouth_eye_distance = MOUTH_TARGET_Y - EYES_TARGET_Y

    if mouth_eye_distance <= 1:
        return None

    # Scale based on eye-to-mouth distance, preserving the natural eye spacing.
    scale = target_mouth_eye_distance / mouth_eye_distance
    linear_transform = scale * rotation

    # Center the midpoint between the eyes horizontally.
    translation = np.array(
        [
            TARGET_WIDTH / 2 - (linear_transform @ eye_midpoint)[0],
            EYES_TARGET_Y - (linear_transform @ eye_midpoint)[1],
        ],
        dtype=np.float32,
    )
    transform = np.column_stack((linear_transform, translation))

    # Find how far the requested output reaches beyond the original image.
    # Pad first, so rotation/cropping never creates black corners.
    inverse_transform = cv2.invertAffineTransform(transform)
    output_corners = np.array(
        [[0, 0], [TARGET_WIDTH - 1, 0], [0, TARGET_HEIGHT - 1],
         [TARGET_WIDTH - 1, TARGET_HEIGHT - 1]],
        dtype=np.float32,
    ).reshape(-1, 1, 2)
    source_corners = cv2.transform(
        output_corners,
        inverse_transform,
    ).reshape(-1, 2)

    image_height, image_width = image.shape[:2]
    pad_left = int(max(0, np.ceil(-source_corners[:, 0].min()))) + 2
    pad_right = int(
        max(0, np.ceil(source_corners[:, 0].max() - (image_width - 1)))
    ) + 2
    pad_top = int(max(0, np.ceil(-source_corners[:, 1].min()))) + 2
    pad_bottom = int(
        max(0, np.ceil(source_corners[:, 1].max() - (image_height - 1)))
    ) + 2

    expanded_image = cv2.copyMakeBorder(
        image,
        pad_top,
        pad_bottom,
        pad_left,
        pad_right,
        borderType=cv2.BORDER_REFLECT_101,
    )

    # Adjust the transform because the original image moved by the padding.
    padding_vector = np.array([pad_left, pad_top], dtype=np.float32)
    expanded_transform = transform.copy()
    expanded_transform[:, 2] -= linear_transform @ padding_vector

    return cv2.warpAffine(
        expanded_image,
        expanded_transform,
        (TARGET_WIDTH, TARGET_HEIGHT),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )


if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

ensure_model_file()

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
landmarker_options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_faces=1,
    min_face_detection_confidence=0.5,
    min_face_presence_confidence=0.5,
    min_tracking_confidence=0.5,
)


with vision.FaceLandmarker.create_from_options(landmarker_options) as landmarker:
    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        image_path = os.path.join(INPUT_DIR, filename)
        image = cv2.imread(image_path)
        if image is None:
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=image_rgb,
        )
        result = landmarker.detect(mp_image)

        if not result.face_landmarks:
            print(f"No face found: {filename}")
            continue

        image_height, image_width = image.shape[:2]
        left_eye, right_eye, mouth_center = get_face_points(
            result.face_landmarks[0],
            image_width,
            image_height,
        )
        aligned_image = align_face_by_eyes_and_mouth(
            image,
            left_eye,
            right_eye,
            mouth_center,
        )

        if aligned_image is None:
            print(f"Invalid landmarks: {filename}")
            continue

        # Always write JPEG, even when the input is PNG.
        output_filename = f"{os.path.splitext(filename)[0]}.jpg"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        cv2.imwrite(
            output_path,
            aligned_image,
            [cv2.IMWRITE_JPEG_QUALITY, 95],
        )
        print(f"Done: {output_filename}")
