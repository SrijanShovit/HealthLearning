# Hepatitis C Dataset 🩺🔬

Welcome to the Hepatitis C Dataset! 🎉 This dataset contains laboratory values of blood donors and patients diagnosed with Hepatitis C, along with demographic information such as age and sex. The data was obtained from the UCI Machine Learning Repository.

- [Hepatitis C Dataset](https://www.kaggle.com/datasets/fedesoriano/hepatitis-c-dataset)

## Context 📋

Hepatitis C is a viral infection that causes inflammation of the liver. This dataset provides valuable information about patients' laboratory values and demographic characteristics, aiding in the diagnosis and monitoring of Hepatitis C. Understanding the relationship between laboratory data and patient demographics can inform medical interventions and treatment strategies.

## Attribute Information 📝

The dataset includes the following attributes:

1. **X (Patient ID/No.)**: Unique identifier for each patient.
2. **Category (Diagnosis)**: Diagnosis category indicating the patient's condition ('0=Blood Donor', '0s=suspect Blood Donor', '1=Hepatitis', '2=Fibrosis', '3=Cirrhosis').
3. **Age**: Age of the patient in years.
4. **Sex**: Gender of the patient (f for female, m for male).
5. **ALB**: Albumin level in blood.
6. **ALP**: Alkaline phosphatase level in blood.
7. **ALT**: Alanine transaminase level in blood.
8. **AST**: Aspartate transaminase level in blood.
9. **BIL**: Bilirubin level in blood.
10. **CHE**: Cholinesterase level in blood.
11. **CHOL**: Cholesterol level in blood.
12. **CREA**: Creatinine level in blood.
13. **GGT**: Gamma-glutamyl transferase level in blood.
14. **PROT**: Protein level in blood.

## Target Attribute 🎯

The target attribute for classification is Category (Diagnosis), distinguishing between blood donors and Hepatitis C patients, including disease progression (from 'just' Hepatitis C to Fibrosis and Cirrhosis).

## Acknowledgements 🙏

The dataset creators and donors are Ralf Lichtinghagen, Frank Klawonn, and Georg Hoffmann. Relevant papers associated with the dataset include:

- Lichtinghagen R et al. J Hepatol 2013; 59: 236-42
- Hoffmann G et al. Using machine learning techniques to generate laboratory diagnostic pathways – a case study. J Lab Precis Med 2018; 3: 58-67
