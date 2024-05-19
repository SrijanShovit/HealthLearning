# About Brain Tumor MRI Dataset

##### _Dataset for Brain Tumor Classification_

The dataset can be found [here](https://www.kaggle.com/datasets/theiturhs/brain-tumor-mri-classification-dataset/data). The dataset contains the **brain MRI images**. This dataset is the modified version of [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data). Certain image processing techniques and augmentation are applied on these data.

## **Tasks implemented to obtain the dataset**

- Exploring class, class distribution, image size distribution for both training and testing dataset.
- Performing necessary dimension reduction
- Performing some Pre-processing tasks using Image processing techniques
- Performing augmentation

**In the original dataset, the number of samples in each class in training dataset is:**

- No. of samples for class pituitary = 1457
- No. of samples for class notumor = 1595
- No. of samples for class meningioma = 1339
- No. of samples for class glioma = 1321
- **Total training sample data: 5712**

**In the original dataset, the number of samples in each class in testing dataset is:**

- No. of samples for class pituitary = 300
- No. of samples for class notumor = 405
- No. of samples for class meningioma = 306
- No. of samples for class glioma = 300
- **Total testing sample data: 1311**

**In the modified dataset, the number of samples in each class in training dataset is:**

- No. of samples for class pituitary = 1557
- No. of samples for class notumor = 1595
- No. of samples for class meningioma = 1539
- No. of samples for class glioma = 1521
- **Total training sample data: 6212**

**In the modified dataset, the number of samples in each class in testing dataset is:**

- No. of samples for class pituitary = 400
- No. of samples for class notumor = 405
- No. of samples for class meningioma = 386
- No. of samples for class glioma = 400
- **Total testing sample data: 1591**

## **Dataset Analysis**

**Histogram of RGB Channels and its corresponding grayscale images**
The histograms obtained suggest that there may not be significant differences in the distribution of pixel values across the color channels. Therefore grayscale conversion of RGB images will be reasonable because of reduced complexity and improved generalization (as grayscale images contain illumination information only). So the RBG images are converted to Grayscale images for further processing.

**The image processing techniques applied on these image data:**

1. Converting RGB images to Grayscale images
2. Cropping Images
3. Normalizing images
4. Resizing to 256 x 256

**Cropping the images includes these steps:**

1. Applying median filter with kernal size 3x3 - Noise handling
2. Binary thresholding - Segments black region
3. Contour detection - finds contour in binary image
4. Largest contour selection
5. Bounding box calculation
6. Image cropping

# Distribution of Image sizes by class of

#### Training Dataset in original dataset
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/87cf7caf-d99c-430d-8d11-aff9247006c3)

#### Testing Dataset in original dataset
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/077a2b41-89bb-415e-aac5-6ad33417ca21)

#### Training dataset after pre-processing
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/275c0b72-87ad-4be0-829f-5689c7460b2f)

#### Testing dataset after pre-processing
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/d5821226-e896-4c3f-a477-4caf1a072408)

#### Training dataset after augmentation
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/749b6a03-5264-4cec-bc3d-c056bb209ca2)

#### Testing dataset after augmentation
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/c44f0554-00df-41c6-bb29-78b2275b6a7a)

# Augmented Images
![image](https://github.com/theiturhs/HealthLearning/assets/96874023/ddb45508-609b-4ffe-9e03-e0066301cb15)


# **About Dataset Folder**

The root directory contains four sub-folders. Training and Testing folders contains processed images and Training_Augmented and Testing_Augmented contains generated images. Each sub-folders contains other sub-folders which represents its class.

_Refer to brain_tumor_mri_dataset_generation.ipynb_ to see the implemention of described steps. Visit [here](https://www.kaggle.com/datasets/theiturhs/brain-tumor-mri-classification-dataset/data) to see the modified dataset.
