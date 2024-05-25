# Hyper-Parameter Tuning Techniques for Brain Tumor MRI Classification

The dataset on which the cross validation is carried out can be found [on kaggle](https://www.kaggle.com/datasets/theiturhs/brain-tumor-mri-classification-dataset/data). Find the implementation of this in Hyper-parameter_Tuning.ipynb notebook. Learner module, FastAI, is considered to provide a convenient way to create and fine-tune convolutional neural network (CNN) models. vision.learner is a function that helps us to construct a learner object, which has the model architecture, data, training configuration, and other elements. We can specify a pre-trained model architecture and fine-tune it on the dataset.

### Hyper-Parameter Tuning Teachniques carried out are as follows:
*Different techniques to find out suitable hyper-parameters*
* Random Search optimization algorithm
* Hyperparameter Optimization with Optuna's Successive Halving Pruner

### Different techniques and their obtained training accuracies¶
| Technique | Accuracy Score | Architecture | Weight Decay | Epochs | Batch Size | Drop |
| -- | -- | -- | -- | -- | -- | -- |
| Random Search optimization algorithm - Run 1 | 95.27% | ResNet50 | 5.527e-5 | 7 | 64 | 0.4 |
| Random Search optimization algorithm - Run 2 | 95.53% | ResNet50 | 4e-6 | 5 | 64 | 0.2 |
| Hyperparameter Optimization with Optuna's Successive Halving Pruner | 98.51% | ResNet18 | 0.004016 | 13 | 32 | 0.2680 |

**Out of these techniques,Hyperparameter Optimization with Optuna's Successive Halving Pruner technique gives better overall accuracy. It almost take 40-50 minutes for each to fine-tune the model.**

NOTE: Since here we need to find the best technique that we can use for hyper-parameter tuning of our dataset, and it takes almost 40-50 minutes on an average to get results from each techniques (where we have only considered training dataset not augmented data), thus RandomSplitting is implemented to divide the dataset.

#### Random Search Optimizing Algorithm - Run 1

For n_trails = 10, the accuracy score and best hyper-parameter are as follows:

| Trail No. | Best Score | Architecture | Weight Decay | Epochs | Batch Size | Drop |
|-----------|------------|--------------|--------------|--------|------------|------|
| 0         | 0.9011     | ResNet34     | 0.00024      | 8      | 64         | 0.4  |
| 1         | 0.9413     | ResNet18     | 0.0090       | 15     | 64         | 0.2  |
| 2         | 0.9343     | ResNet18     | 0.0065       | 5      | 32         | 0.4  |
| 3         | 0.9080     | ResNet34     | 0.00062      | 5      | 32         | 0.4  |
| 4         | 0.9019     | ResNet34     | 0.00092      | 6      | 64         | 0.2  |
| **5**         | **0.9527**     | **ResNet50**     | **0.00005**      | **7**      | **64**         | **0.4**  |
| 6         | 0.9220     | ResNet34     | 0.00895      | 15     | 64         | 0.2  |
| 7         | 0.9404     | ResNet18     | 0.0035       | 11     | 64         | 0.4  |
| 8         | 0.9212     | ResNet18     | 0.0002       | 5      | 64         | 0.4  |
| 9         | 0.9203     | ResNet34     | 0.0007       | 13     | 32         | 0.4  |

The best accuracy score is 0.9527 with these hyperparameters:

- Architecture: ResNet 50
- Weight Decay: 5.527e-5
- Epochs: 7
- Batch Size: 64
- Drop: 0.4

#### Random Search Optimizing Algorithm - Run 2

For n_trails = 10, the accuracy score and best hyper-parameter are as follows:

| Trial | Best Score | Architecture | Weight Decay | Epochs | Batch Size | Drop |
|-------|------------|--------------|--------------|--------|------------|------|
| 0     | 0.9177     | ResNet34     | 0.000248     | 6      | 32         | 0.2  |
| 1     | 0.9492     | ResNet50     | 0.002137     | 7      | 64         | 0.4  |
| 2     | 0.9518     | ResNet50     | 0.000004     | 8      | 64         | 0.2  |
| 3     | 0.9046     | ResNet34     | 0.000269     | 6      | 64         | 0.2  |
| 4     | 0.9378     | ResNet50     | 0.000058     | 6      | 32         | 0.2  |
| 5     | 0.9352     | ResNet18     | 0.000154     | 7      | 32         | 0.2  |
| 6     | 0.9063     | ResNet34     | 0.000006     | 5      | 64         | 0.4  |
| **7**     | **0.9553**     | **ResNet50**     | **0.000004**     | **13**     | **64**         | **0.2**  |
| 8     | 0.9238     | ResNet34     | 0.000824     | 13     | 64         | 0.4  |
| 9     | 0.9361     | ResNet18     | 0.000018     | 8      | 32         | 0.2  |

The best accuracy score is 0.9553 with these hyperparameters:

- Architecture: ResNet 50
- Weight Decay: 4e-6
- Epochs: 5
- Batch Size: 64
- Drop: 0.2

#### Hyperparameter Optimization with Optuna's Successive Halving Pruner

For n_trails = 10, accuracy scores and hyper-paramters are:

| Trial | Best Score | Architecture | Weight Decay | Epochs | Batch Size | Drop               |
|-------|------------|--------------|--------------|--------|------------|--------------------|
| 0     | 0.9623     | resnet50     | 2.057e-06    | 8      | 32         | 0.2888             |
| 1     | 0.9518     | resnet50     | 0.001421     | 7      | 32         | 0.2707             |
| 2     | 0.9807     | resnet34     | 3.744e-06    | 9      | 32         | 0.3918             |
| 3     | 0.9641     | resnet18     | 2.667e-05    | 7      | 64         | 0.3196             |
| 4     | 0.9711     | resnet34     | 0.005883     | 8      | 64         | 0.2000             |
| 5     | 0.9650     | resnet18     | 5.694e-06    | 6      | 64         | 0.2266             |
| 6     | 0.9737     | resnet18     | 1.813e-05    | 6      | 64         | 0.3732             |
| **7**     | **0.9851**     | **resnet34**     | **0.004016**     | **13**     | **32**         | **0.2680**             |
| 8     | 0.9667     | resnet50     | 0.008095     | 15     | 32         | 0.3013             |
| 9     | 0.9632     | resnet50     | 0.0006995    | 6      | 32         | 0.3595             |

The best accuracy score is 0.9851 with these hyperparameters:

- Architecture: ResNet 34
- Weight Decay: 0.004016
- Epochs: 13
- Batch Size: 32
- Drop: 0.268

##### Summarizing

1. Random search optimization gives almost 95% accuracy when we ran it two times each with 10 iterations.
2. Hyperparameter Optimization with Optuna's Successive Halving Pruner, we are getting 98.51% which is a remarkable accuracy.

**So we will be using k-fold validation technique followed by Hyperparameter Optimization with Optuna's Successive Halving Pruner for getting the appropriate hyper-parameters.**
