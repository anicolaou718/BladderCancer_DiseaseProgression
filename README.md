# BladderCancer_DiseaseProgression
Identifying key features that can be used to predict whether a patient will survive or progress after BCG failure. 

The patients in this dataset were given Bacillus Calmette-Guerin (BCG) treatment which is a vaccine that was used to treat Tuberculosis when it was a more prevalent disease. 
BCG has seen great success (70% remission) in treating Non-muscle invasive Bladder cancer. The great part of BCG in treating patients is that the negative side effects that chemotherapy and radiation cause is avoided. 
Even though BCG can be very helpful for Bladder Cancer patients, there are patients where BCG does not alleviate their condition and instead the disease progresses (BCG failure). 

This project looks into patients that have experienced BCG failure and identifies prominent features in these patients that contributed to the failure of the condition as well as signifiers on to whether the patient will survive post-BCG failure. 

The following tools and steps were taken to better understand and evaluate the dataset:

**Data Cleaning** : 

Removing Outliers -- Capping, 
Removing Nulls -- Replace with mean, 
Standardization, 
Conversion of objects/strings to numerical values

**Visualization Tools**:

Bar charts,
Histograms,
Heatmaps,
Point Plot,
Swarm Plot,
Box Plots,

**Cross Validation** :

Repeated Stratified K Fold,
K Fold

**Machine Learning Models**:

Logistic Regression,
Support Vector Machine,
Sequential Keras Neural Model

**Feature Selection Methods**:

Recursive Feature Elimination (Wrapper),
Mutual Information ,
Chi Square ,

**Evaluation Metrics**
Confusion Matrix,
Classification Report,
Roc curve- ROC AUC
