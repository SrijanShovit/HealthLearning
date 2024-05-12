# Breast Cancer Prediction Dataset 🔬📊

Welcome to the Breast Cancer Prediction Dataset! 🎉 This dataset contains information regarding the type of tumor and based on its type, it would classify if a person has breast cancer or not.

-[Breast Cancer Wisconsin(Diagnostic) Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data)

## Context 📋

Breast cancer is a disease in which cells in the breast grow out of control. There are different kinds of breast cancer. The kind of breast cancer depends on which cells in the breast turn into cancer.
There are majorly two types of tumor:
1) Malignant Tumor:
   -Cancerous
   -Non-capsulated
   -Fast growing 
   -Metastasize to other parts of the body
   -cells have large dark nuclei;abnormal shape

2) Benign tumor:
   -Non-cancerous
   -Capsulated
   -non-invasive
   -Slow growing
   -Cells are normal

This Dataset is derived from a particular test called "Fine Needle Aspiration" & the sample collected during this will help in making a diagnosis depending upon the properties of the cell.

## Column Descriptors 📝

the dataset includes the following columns:

1.**id**:id number for each cell

2.**diagnosis**:M or B;where M represents malignant tumor & B represents Benign tumor.

3.**radius**:mean of distances from center to points on the perimeter.

4.**texture**:standard deviation of gray-scale values.

5.**perimeter**:perimeter of a particular cell.

6.**area**: area of cell.

7.**smoothness**:local variation in radius lengths.

8.**compactness**:perimeter^2 / area - 1.0

9.**concaity**:severity of concave portions of the contour

10.**concave points**:number of concave portions of the contour

11.**symmetry**:checking for symmetry 

12.**fractal dimension**:"coastline approximation" - 1

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

All feature values are recoded with four significant digits.

**Class distribution**: 357 benign, 212 malignant

**Missing attribute values**: none

## Conclusion📝

This dataset can inspire researchers and analysis aimed at predicting breast cancer depending upon the type of tumor . By examining the relationship between various properties of the cell researchers can develop accurate prediction models to predict the diagnosis.


