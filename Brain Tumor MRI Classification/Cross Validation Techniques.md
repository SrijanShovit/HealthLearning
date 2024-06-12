# Cross Validation Techniques for Brain Tumor MRI Classification
____

The dataset on which the cross validation is carried out can be found [on kaggle](https://www.kaggle.com/datasets/theiturhs/brain-tumor-mri-classification-dataset/data). Find the implementation of this CrossValidation_Techniques.ipynb notebook.

### Cross Validation Teachniques carried out are as follows:
*Different techniques for distributing dataset into training and testing dataset*
* Hold-Out CV
* K-Fold Cross Validation
* Repeated K-Fold
* Leave-One-Out (LOO)
* Stratified K-Fold

### Different techniques and their obtained training accuracies¶
| Technique	| Average Accuracy across all classes |	Pituitary |	No Tumor | Meningioma | Glioma |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Hold-Out CV |	0.9380 |	0.9860 |	0.9760 |	0.8210 |	0.9690 |
| K-Fold CV	| 0.9604	| 0.9858 |	0.9858 |	0.9196 | 	0.9420|
| Repeated K-Fold CV	| 0.9585 |	0.9504 |	0.9838 |	0.9255 |	0.9703|
| Stratified K-Fold CV	| 0.9548 |	0.9544	| 0.9838 |	0.9096 |	0.9667|

**Out of these techniques, K-Fold CV technique gives better overall accuracy and class wise accuracy. Therefore, this technique can be used to divide our dataset into training and testing set.**

1. Hold Out Technique: Randomly the dataset was distributed into 80% training set and 20% validation set. The aacuracy achieved was 93.80%.
2. K-Fold Cross Validation: This divides data into k equal-sized folds, trains the model k times, each time using k-1 folds as training data and one fold as validation data. The accuracy achieved was 96.04%.
3. Repeated K-Fold: This repeats the k-fold CV process multiple times with different random splits of the data. It achieved 95.85% accuracy.
4. Leave One Out: It is a special case of k-fold CV where k is equal to the number of samples in the dataset. Each sample is used as a validation set once. So this was not implemented. It was computationally expensive, would have required a lot of training time.
5. Stratified K-Fold: It is like k-fold CV, but ensures that each fold preserves the percentage of samples for each class. It achieved an accuracy of 95.48%.
