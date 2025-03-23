---
layout: home
title: "Home"
---

<img src="https://www.makeintern.com/admin/uploaded_images/blog/images/summer-internship.jpg" height="250" alt="Summer Internship">

We have 3 summer intern slots for international students in the year 2025. The wage is 20K NTD per month for 2 months to participate in the Companion-robot Nurse Helper project. We aim to develop features including occlusion-aware facial feature recognition, voice recognition, LLM-based dialog sentence generation. Please contact me if you are interested.
- Goal: Develop the features of our Companion-robot Nurse Helper project.
- Required skill: C++ on Ubuntu, Java on Android, or Python to train models.
- Required Knowledge: Programming on the Ubuntu or Android system, Azure Open AI APIs, Computer Vision, Voice Recognition, or LLM.
- Mentoring: I will mentor you.
- Practice: For most time, you will stay in our lab on the CGU campus. In some cases, we will go to the Chang-Gung Memorial Hospital Lingko branch to test our robots in practice.
- Opportunity: You can tour Taiwan in holidays, be familiar with CGU if you are interested in taking an AI Master's program at CGU.
- Training: You will learn experience of using robots such as Zenbo, Zenbo Junior II, Kebbi Air-S, and Alice.
- Accommodation: There are plenty of dorms available during summer vacation. The price is 520 NTD per week, very affordable.

<h3 class="fw-bold">Current Projects</h3>

#### Companion-robot helper for nurses in a pediatric ward
![PICU Scenario](http://yangchihyuan.github.io/assets/img/PICU_Scenario_1.jpg)

This is a project for developing a companion robot to help nurses in a pediatric ward. There is a shortage of nurses in Taiwan, due to the change of population structure caused by sub-replacement fertility. Our goal is to enable a social to take some nurse tasks to reduce the working load of human nurses. Our first task is to monitor pediatric patients' emotion and their levels of painfulness.
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

#### Digestive system diseases prediction from tongue images
<img src="http://yangchihyuan.github.io/assets/img/Tongue_capture.jpg" height="250" alt="Tongue_capture">
<img src="http://yangchihyuan.github.io/assets/img/Tongue_mask.jpg" height="250" alt="Tongue_mask">
<br/>Image courtesy: Tongue Image Segmentation and Constitution Identification with Deep Learning, Master's thesis of Mr. Chien-Ho Lin (林建和) of the Traditional Chinese Medicine Institute at Chang Gung University 2022, advised by Prof. Hsien-Hung Yang (楊賢鴻) and Prof. Jiann-Der Lee (李建德).

The primary researcher of this project is a Ph.D. student of the CGU school of Traditional Chinese Medicine and I am a consultant of this project. We want to compile a dataset consisting of tongue images and syndromes of digestive system diseases. Thereafter, we can train a computer vision model to predict digestive system diseases from tongue images. In the theory of traditional Chinese medicine, digestive system diseases and tongue appearance are highly related. But modern western medicine system totally ignores it. The most challenging part of this research lies in the data collection, segmentation and labeling. 
Because this is an application-oriented research project, they plan to use the well-developed ResNet as their prediction model. Thus, the contribution of this project is to validate the traditional Chinese medicine theory and develop a practical method to apply it rather than exploring computer vision techniques.

