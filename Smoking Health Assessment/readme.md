# Income Classification Model

## Overview
This project involves building and evaluating various machine learning models to classify gross income based on demographic and smoking-related features. The dataset is processed, and multiple models are trained and evaluated to find the best performing model.

## Dataset
The dataset includes demographic information, smoking habits, and gross income of individuals. Below is a sample of the dataset:

| | gender | age | marital_status  | highest_qualification | nationality | ethnicity | gross_income       | region    | smoke | amt_weekends | amt_weekdays | type     |
|---|--------|-----|----------------|-----------------------|-------------|-----------|--------------------|-----------|-------|--------------|--------------|----------|
| 1 | Male   | 38  | Divorced       | No Qualification      | British     | White     | 2,600 to 5,200     | The North | No    | NA           | NA           |          |
| 2 | Female | 42  | Single         | No Qualification      | British     | White     | Under 2,600        | The North | Yes   | 12           | 12           | Packets  |
| 3 | Male   | 40  | Married        | Degree                | English     | White     | 28,600 to 36,400   | The North | No    | NA           | NA           |          |
| 4 | Female | 40  | Married        | Degree                | English     | White     | 10,400 to 15,600   | The North | No    | NA           | NA           |          |
| 5 | Female | 39  | Married        | GCSE/O Level          | British     | White     | 2,600 to 5,200     | The North | No    | NA           | NA           |          |
| 6 | Female | 37  | Married        | GCSE/O Level          | British     | White     | 15,600 to 20,800   | The North | No    | NA           | NA           |          |
| 7 | Male   | 53  | Married        | Degree                | British     | White     | Above 36,400       | The North | Yes   | 6            | 6            | Packets  |
| 8 | Male   | 44  | Single         | Degree                | English     | White     | 10,400 to 15,600   | The North | No    | NA           | NA           |          |
| 9 | Male   | 40  | Single         | GCSE/CSE              | English     | White     | 2,600 to 5,200     | The North | Yes   | 8            | 8            | Hand-Rolled |
| 10| Female | 41  | Married        | No Qualification      | English     | White     | 5,200 to 10,400    | The North | Yes   | 15           | 12           | Packets  |
| 11| Male   | 72  | Widowed        | No Qualification      | English     | White     | 10,400 to 15,600   | The North | No    | NA           | NA           |          |
| 12| Male   | 49  | Married        | No Qualification      | British     | White     | Refused            | The North | No    | NA           | NA           |          |
| 13| Male   | 29  | Married        | Degree                | English     | White     | Above 36,400       | The North | No    | NA           | NA           |          |

## Data Preprocessing
1. **Handle Missing Values**:
    - `amt_weekends` and `amt_weekdays` missing values are filled with `0`.
    - `type` missing values are filled with `None`.

2. **Data Type Conversion**:
    - `age`, `amt_weekends`, and `amt_weekdays` are converted to integers.
    - `gross_income` is converted to a categorical type.

3. **Encoding Categorical Variables**:
    - Categorical variables (`gender`, `marital_status`, `highest_qualification`, `nationality`, `ethnicity`, `region`, `smoke`, `type`) are one-hot encoded.
    - `gross_income` is label encoded.

4. **Feature Scaling**:
    - `age`, `amt_weekends`, and `amt_weekdays` are scaled using `StandardScaler`.

## Exploratory Data Analysis
- **Age Distribution**:
    ```python
    sns.histplot(df['age'], kde=True)
    plt.title('Age Distribution')
    plt.show()
    ```
- **Gross Income Distribution**:
    ```python
    sns.boxplot(x=df['gross_income'])
    plt.title('Gross Income Distribution')
    plt.show()
    ```

## Model Training and Evaluation
The dataset is split into training (80%) and testing (20%) sets. Various machine learning models are trained and evaluated:

1. **Random Forest**
2. **Gradient Boosting**
3. **Logistic Regression**
4. **Support Vector Classifier**
5. **K-Nearest Neighbors**
6. **Naive Bayes**

For each model:
- Training and predictions are performed.
- Accuracy, classification report, confusion matrix, and ROC AUC scores are calculated.

### Model Performance
Performance metrics are stored in a dictionary and printed for each model. Example:
```python
for model_name, performance in model_performance.items():
    print(f"Model: {model_name}")
    print(f"Accuracy: {performance['accuracy']}")
    print(f"ROC AUC: {performance['roc_auc']}")
    print("Classification Report:")
    print(pd.DataFrame(performance['classification_report']).transpose())
    print("Confusion Matrix:")
    print(performance['confusion_matrix'])
    print("\n")
