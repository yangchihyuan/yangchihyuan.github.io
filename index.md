---
layout: home
title: "Home"
---

#### Companion-robot helper for nurses in a pediatric ICU

![PICU Scenario](http://yangchihyuan.github.io/assets/img/PICU_Scenario_1.jpg)

This is a project for developing a companion robot to help nurses in a pediatric intensive care unit (PICU). There is a shortage of nurses in Taiwan, due to several factors such as low salaries, unsatisfying working environment, and the reduction of young working labors in the population structure caused by sub-replacement fertility. In a PICU, children have to be separated from their parents for most time due to the sanity issue. In contrast, a companion robot can be totally sanitized and stay in the PICU. In practice, a PICU nurse usually needs to take care of multiple wards to make the operation economic. When a nurse is busy for one ward, she/he needs a helper to look after other wards. Currently such a duty is delegated to a nurse colleague, so there are multiple nurses on duty in a PICU.
Introduction slides [(Link)](https://www.dropbox.com/scl/fi/zmytc7e8zdvyo8svnumpc/Zenbo-Nurse-Helper.pptx?rlkey=yfq7dhkctzgfsa6h7bca49oe5&dl=0)
Code is available on my GitHub webpage [(Link)](https://github.com/yangchihyuan/ZenboNurseHelper).

#### Depth estimation in an eye ball

<img src="http://yangchihyuan.github.io/assets/img/microsurgery.jpg" height="250" alt="microsurgery">
<img src="http://yangchihyuan.github.io/assets/img/Eyeball.jpg" height="250" alt="Eyeball">
<img src="http://yangchihyuan.github.io/assets/img/007_MH_RD_3D_merged.jpg" height="250" alt="Stereo images">

For intraocular microsurgery, robotic assistance is a cutting-edge research field because it is promising for expanding human capabilities and improving the safety and efficiency of the intricate surgery process. Because depth is critical for intraocular microsurgery, in this project we want to estimate the depth of the medical devices in an eye ball. We want to develop a method which can warm the operator if the device is too close to the retina.

#### Zero-shot skeleton-based action recognition
<img src="http://yangchihyuan.github.io/publications/ECCV_2024_SA_DVAE.jpg" height="300" alt="SA_DVAE">

Current research results have been published in ECCV'24 and the paper is available in my publication webpage [(Link)](https://yangchihyuan.github.io/publications). However, there are some puzzles unsolved yet. For example, why does this method work poorly on some action datasets? How will the quality of text affect the method's performance? If we refine the text description of the NTU RGB+D dataset, what will happen? Is the skeleton data of the NTU RGB+D dataset so noisy that the proposed method works? Given a high-quality skeleton action dataset, will the proposed method still work?
To answer those questions, further research is required to be carried out.

#### Data augmentation for medical images
<img src="http://yangchihyuan.github.io/assets/img/MedMNISTv2.jpg" width="1200" alt="MedMNISTv2">

Motivation: There is a common problem among current medical datasets, which are either private or of a small scale. Because large-scale publicly available datasets are very rare, in particular in terms of high-resolution high-quality image ones, we wonder if we can adopt some effective ways to synthesize high-resolution high-quality medical images. <br/>
Approach: There are some knowledge distillation methods and generative models such as diffusion models. We take a survey among those methods to look for proper candidates for our purpose.

#### Text-and-drawing conditioned indoor scene synthesis
<img src="http://yangchihyuan.github.io/assets/img/GeneratedIndoorImages.jpg" width="1200" alt="GeneratedIndoorImages">

Motivation: Many image generative algorithms and tools rapidly become easy to use such as ControlNet, Krita, and ComfyUI. We wonder how to utilize them to effectively generate indoor scenes for the construction purpose. There are many programming tasks and research issues behind this goal. 

#### Shop drawing retrieval
<img src="http://yangchihyuan.github.io/assets/img/ShopDrawing.jpg" width="1200" alt="ShopDrawing.jpg">

This is an industry-cooperated project. Given a query shop drawing, we aim to retrieve similar shop drawings in a large dateset component-by-component. The purpose of this project is to encourage employees to use standard drawings and to reduce the cost of creating repeated or highly similar drawings. 

#### Digestive system diseases prediction from tongue images
<img src="http://yangchihyuan.github.io/assets/img/Tongue_capture.jpg" height="250" alt="Tongue_capture">
<img src="http://yangchihyuan.github.io/assets/img/Tongue_mask.jpg" height="250" alt="Tongue_mask">
<br/>Image courtesy: Tongue Image Segmentation and Constitution Identification with Deep Learning, Master's thesis of Mr. Chien-Ho Lin (林建和) of the Traditional Chinese Medicine Institute at Chang Gung University 2022, advised by Prof. Hsien-Hung Yang (楊賢鴻) and Prof. Jiann-Der Lee (李建德).

The primary researcher of this project is a Ph.D. student of the CGU school of Traditional Chinese Medicine and I am a consultant of this project. We want to compile a dataset consisting of tongue images and syndromes of digestive system diseases. Thereafter, we can train a computer vision model to predict digestive system diseases from tongue images. In the theory of traditional Chinese medicine, digestive system diseases and tongue appearance are highly related. But modern western medicine system totally ignores it. The most challenging part of this research lies in the data collection, segmentation and labeling. 
Because this is an application-oriented research project, they plan to use the well-developed ResNet as their prediction model. Thus, the contribution of this project is to validate the traditional Chinese medicine theory and develop a practical method to apply it rather than exploring computer vision techniques.

#### Transferred learning for brain tumor segmentation on MRI images
<img src="http://yangchihyuan.github.io/assets/img/BrainTumorSegmentation.jpg" width="1200" alt="BrainTumorSegmentation">

Motivation: We want to learn from publicly available large-scale brain tumor segmentation datasets, and apply the learned knowledge on our own small-scale private dataset. However, we do not have the ground-truth segmentation labels for our won private dataset and we do not have experts to label those MRI images. To validate our algorithm, we downloaded another small-scale brain tumor dataset with labeled segmentation data.

#### HarmonEld, an AI wristband for the elderly
This is my master student Brian Liu's research topic. He wants to develop an AI wristband to address the elderly care problem because there will be more aged people in Taiwan soon and the cost of caring them will be tremendous. He participated in several competitions to promote his idea and prototype. Rich information is available in his YouTube video below (language in Chinese and narration in Mandarin, suggested playing speed: 0.8).

<iframe width="560" height="315" src="https://www.youtube.com/embed/4m9hZWQi-_w?si=0X8EWaBrIjkEfDjs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>