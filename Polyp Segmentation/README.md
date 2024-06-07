# Polyp Segmentation in Endoscopy Images 🏥🔬

This project focuses on the automated segmentation of polyps in endoscopy images using deep learning techniques. By accurately identifying and delineating polyps, this work aims to assist medical professionals in early detection and prevention of colorectal cancer.

## What is a Polyp? 🔎

Polyps are abnormal tissue growths that arise from mucous membranes, commonly found in organs such as the colon, stomach, and intestines. While many polyps are benign, some can develop into cancer, making early detection and removal crucial for preventing colorectal cancer and other serious conditions.

## Importance of the Subject 💡

Early detection and accurate segmentation of polyps during endoscopy are vital for:
- Preventing colorectal cancer
- Improving patient outcomes
- Reducing the risk of complications

Automated polyp segmentation aids gastroenterologists in identifying and removing polyps efficiently.

## Methods 🛠️

This project utilizes the U-Net architecture, a powerful convolutional neural network designed for biomedical image segmentation. The model is trained to differentiate between polyp and non-polyp regions, providing detailed segmentation maps.

## Dataset 📊

The dataset consists of endoscopy images and their corresponding ground truth images, which indicate the presence and location of polyps.
![image](https://github.com/Kaushal-11/HealthLearning/assets/121329391/b9ae85f3-ca1a-4e86-8907-a99db4799245)

### Dataset Details
- Source: https://polyp.grand-challenge.org/CVCClinicDB/
- Number of Images: 612
- Image Format: .tif 
- Mask Format: .tif

## Model Architecture 🏗️

The U-Net architecture is used for its effectiveness in biomedical image segmentation:
- Encoder-decoder structure with skip connections
- Precise localization and segmentation
- Accurate delineation of polyp boundaries

