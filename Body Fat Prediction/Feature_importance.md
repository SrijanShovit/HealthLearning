# Feature Importance Analysis using Chi-squared, and ANOVA

## Introduction
In this analysis, we explore the importance of features in predicting body density. We use Principal Component Analysis (PCA) to understand the variance explained by the features and Chi-squared and ANOVA tests to rank the features based on their importance contribution towards the label.

## PCA Analysis
Refer PCA_description.md

## Feature Importance Ranking
We utilized Chi-squared and ANOVA tests to rank the features based on their importance contribution towards predicting body density.

### Chi-squared Test
The Chi-squared test assesses the independence between categorical features and the target variable. Here, we discretized the target variable and computed Chi-squared scores and p-values for each feature.


### ANOVA Test
ANOVA (Analysis of Variance) is used to determine whether there are any statistically significant differences between the means of two or more groups. We applied ANOVA to quantify the relationship between continuous features and the target variable.


## Conclusion
we can conclude that 'BodyFat', 'Weight', and 'Abdomen' are the most important features for predicting body density, followed by 'Age', 'Chest', 'Hip', 'Thigh', 'Biceps', 'Knee', 'Neck', and 'Forearm'. 'Ankle', 'Height', and 'Wrist' show weaker associations with the target variable and may have less predictive power in this context.

## Repository Structure
- `PCA_analysis.ipynb`: Jupyter Notebook containing PCA analysis
- `Feature_importance_analysis.ipynb`: Jupyter Notebook containing Chi-squared and ANOVA tests
- `Feature_importance.md`: This file explaining the analysis and repository structure

