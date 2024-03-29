# -*- coding: utf-8 -*-
"""BCGenes1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oEfMb71_Lo8odOsXtMRB-NXjwphy3V4C
"""

import pandas as pd 
import numpy as np 
import os
from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error

df_1 = pd.read_csv('File 1.csv', squeeze=True)
df_1.head(5)

df_2 = pd.read_csv('File 2.csv', squeeze=True)
df_2.head(5)

df_2.columns

df_2.isnull().sum()

print(df_2['Tumor_Seq_Allele1'].value_counts().head(10))
print(df_1['Tumor_Seq_Allele1'].value_counts().head(10))

print(df_2['Hugo_Symbol'].value_counts().head(20))
print(df_1['Hugo_Symbol'].value_counts().head(20))

"""Data Frame 2 Genes"""

df_2_Tex15 = df_2[(df_2.Hugo_Symbol=="Tex15" )]
df_2_ANK2 = df_2[(df_2.Hugo_Symbol=="ANK2" )]
df_2_Genes2= df_2_Tex15.append(df_2_ANK2)

df_2_XIRP2 = df_2[(df_2.Hugo_Symbol=="XIRP2" )]
df_2_RYR2 = df_2[(df_2.Hugo_Symbol=="RYR2" )]
df_2_Genes1= df_2_XIRP2.append(df_2_RYR2)

df_2_TTN = df_2[(df_2.Hugo_Symbol=="TTN" )]
df_2_MUC16 = df_2[(df_2.Hugo_Symbol=="MUC16" )]
df_2_Genes= df_2_TTN.append(df_2_MUC16)

df_2_Genes= df_2_Genes1.append(df_2_Genes)

df_2_Genes= df_2_Genes2.append(df_2_Genes)

df_2_Genes.Hugo_Symbol.value_counts()

df_1_TTN = df_1[(df_1.Hugo_Symbol=="TTN" )]
df_1_MALAT1 = df_1[(df_1.Hugo_Symbol=="MALAT1" )]
df_1_Genes1= df_1_TTN.append(df_1_MALAT1)

df_1_MUC16 = df_1[(df_1.Hugo_Symbol=="MUC16" )]
df_1_TP53 = df_1[(df_1.Hugo_Symbol=="TP53" )]
df_1_Genes2= df_1_TP53.append(df_1_MUC16)

df_1_ARID1A = df_1[(df_1.Hugo_Symbol=="ARID1A" )]
df_1_ERBB3 = df_1[(df_1.Hugo_Symbol=="ERBB3" )]
df_1_Genes3= df_1_ARID1A.append(df_1_ERBB3)

df_1_ABCC5 = df_1[(df_1.Hugo_Symbol=="ABCC5" )]
df_1_SPTAN1 = df_1[(df_1.Hugo_Symbol=="SPTAN1" )]
df_1_Genes4= df_1_ABCC5.append(df_1_SPTAN1)
df_1_RYR1 = df_1[(df_1.Hugo_Symbol=="RYR1" )]
df_1_Genes4= df_1_Genes4.append(df_1_RYR1)

df_1_Genes2= df_1_Genes3.append(df_1_Genes2)
df_1_Genes2= df_1_Genes1.append(df_1_Genes2)
df_1_Genes2= df_1_Genes4.append(df_1_Genes2)

df_2_TTN = df_2[(df_2.Hugo_Symbol=="TTN" )]

df_1_Genes2.Hugo_Symbol.value_counts()

df_Genes= df_1_Genes2.append(df_2_Genes)

df_Genes.Hugo_Symbol.value_counts()

sns.countplot(df_Genes.Hugo_Symbol, color="pink")
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees

sns.heatmap(df_Genes.corr())

print(df_Genes['Protein_position'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(df_Genes['Protein_position'], color='g', bins=100, hist_kws={'alpha': 0.4});

df_Genes.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

df_Genes.columns

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.scatter(df_Genes['t_ref_count'], df_Genes['t_alt_count'], color ='maroon')
 
plt.xlabel("Disease Status")
plt.ylabel("Tumor Mutation Burden")
plt.title("TMB vs. D.S")
plt.show()

df_Genes.isnull().sum()

df_Genes.shape

df_Genes1 = df_Genes.drop(columns = ['Chromosome', 'Start_Position', 'End_Position',
        'Consequence', 'Variant_Classification', 'Variant_Type',
       'Reference_Allele', 'Tumor_Seq_Allele1', 'Tumor_Seq_Allele2','Match_Norm_Seq_Allele1','Match_Norm_Seq_Allele2', 't_ref_count', 't_alt_count', 'n_ref_count','n_alt_count', 'HGVSp', 'HGVSp_Short', 'Protein_position', 'Codons'])

df_Genes2 = df_Genes.drop(columns = ['Chromosome', 'Start_Position', 'End_Position',
        'Consequence', 'Variant_Classification', 'Variant_Type',
       'Reference_Allele', 'Tumor_Seq_Allele1', 'Tumor_Seq_Allele2'])

df_Genes3 = df_Genes.drop(columns = [ 'Start_Position', 'End_Position',
    'Match_Norm_Seq_Allele1','Match_Norm_Seq_Allele2', 'Consequence', 'n_ref_count', 'Reference_Allele', 'Tumor_Seq_Allele1', 'Tumor_Seq_Allele2'
      ,  'Codons','Variant_Type']) #TCGA-BT-A42C-01

df_Genes3.head(20)

df_Genes3.Variant_Classification.value_counts()

df_Genes.Consequence.value_counts()

df_Genes

#from google.colab import files
#df_Genes1.to_csv('filename.csv') 
#files.download('filename.csv')

#print(df_Genes1.transpose())

df_Genes.Tumor_Seq_Allele1.value_counts()

df_num_corr = df_Genes.corr()['t_alt_count'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df = pd.read_csv('GenesSamples1.csv', squeeze=True)
df.head(5)

df_BC = pd.read_csv('BC_df.csv', squeeze=True,index_col=[0])
df_BC.head(5)

df = df.rename(columns={'Sample_ID': 'SAMPLE_ID'})

df= pd.merge(df, df_BC)

df.shape

df.head()

df.DFS_STATUS.value_counts()

for i in df.columns:
 df[i].replace(('0:DiseaseFree','1:Recurred/Progressed'), (0, 1), inplace=True)

pd.crosstab(df.DFS_STATUS, df.TTN)

pd.crosstab(df.DFS_STATUS, df.TP53)

sns.heatmap(df.corr())

"""Combined BCG TCGA data"""



d1 = pd.read_csv('df.csv', squeeze=True,index_col=[0])
d1.head(5)

df.info()

df= pd.merge(df, d1)

df= df.drop(columns=['SAMPLE_ID'])

from scipy.stats import pearsonr
corr, _= pearsonr(df['TMB_NONSYNONYMOUS'], df['MUC16'])
print('Pearsons correlation: %.3f' % corr)

from scipy.stats import pearsonr
corr, _= pearsonr(df['RYR2'], df['TMB_NONSYNONYMOUS'])
print('Pearsons correlation: %.3f' % corr)

from scipy.stats import pearsonr
corr, _= pearsonr(df['MUC16'], df['TTN'])
print('Pearsons correlation: %.3f' % corr)

from scipy.stats import pearsonr
corr, _= pearsonr(df['MUC16'], df['RYR2'])
print('Pearsons correlation: %.3f' % corr)

sns.countplot(x='DFS_STATUS',data=df)

from scipy.stats import pearsonr
corr, _= pearsonr(df['TTN'], df['TMB_NONSYNONYMOUS'])
print('Pearsons correlation: %.3f' % corr)

df_num_corr = df.corr()['DFS_STATUS'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df_num_corr = df.corr()['M1'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df_num_corr = df.corr()['PATH_T_STAGE'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df.info()

#from google.colab import files
#df.to_csv('ddf.csv') 
#files.download('ddf.csv')

df_num_corr = df.corr()['TMB_NONSYNONYMOUS'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df_num_corr = df.corr()['DFS_STATUS'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

df_num_corr = df.corr()['MUC16'][:-1] # -1 because the latest row is SalePrice
golden_features_list = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)
print("There is {} strongly correlated values with Protein Position:\n{}".format(len(golden_features_list), golden_features_list))

sns.scatterplot(x="TMB_NONSYNONYMOUS", y="MUC16", data=df);

cormat = df.corr()
round(cormat,2)

sns.heatmap(df.corr())

#sns.boxplot(x=df['MUC16'], y=df['TTN'], showmeans=True);

import statsmodels.stats.api as sms
model = sms.CompareMeans.from_data(df[df['N0'] == 0]['DFS_STATUS'], df[df['N0'] == 1]['DFS_STATUS'])
model.summary( usevar='unequal')

import statsmodels.stats.api as sms
model = sms.CompareMeans.from_data(df[df['DFS_STATUS'] == 0]['TMB_NONSYNONYMOUS'], df[df['DFS_STATUS'] == 1]['TMB_NONSYNONYMOUS'])
model.summary( usevar='unequal')

import sys
IN_COLAB = 'google.colab' in sys.modules

if IN_COLAB:
   !pip install lifelines

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

T = df['DFS_STATUS']
T

E = df['TMB_NONSYNONYMOUS']
E

kmf.fit(T, E)

kmf.survival_function_

max(abs(kmf.survival_function_['KM_estimate'] - df['DFS_STATUS']).dropna())

ci = kmf.confidence_interval_survival_function_
ci

#sns.pairplot(df)

ax=sns.boxplot(x=df.PATH_T_STAGE, y= df.TMB_NONSYNONYMOUS)

ax=sns.boxplot(y=df.PATH_T_STAGE, x= df.DFS_STATUS)

sns.swarmplot(data = df, x = df.DFS_STATUS , y= df.MUC16)

sns.pointplot(data = df,x = df.DFS_STATUS , y= df.MUC16)

df= df.drop(columns=['N1','SPTAN1','N2','NX','M1','RADIATION_THERAPY','ABCC5','RYR1','PATH_T_STAGE','N3','ERBB3','PRIMARY_VS_SECONDARY','PRIOR_DX','WINTER_HYPOXIA_SCORE','Bacillus Calmette-Guerin (BCG)','M0','BUFFA_HYPOXIA_SCORE','ANEUPLOIDY_SCORE','TP53','MALAT1','RAGNUM_HYPOXIA_SCORE','MX','AGE', 'SEX','MSI_SCORE_MANTIS', 'MSI_SENSOR_SCORE'])

df=df.drop(columns=['N0'])

#df=df.drop(columns=['ARID1A'])

sns.heatmap(df.corr())

X = df.drop(['DFS_STATUS'], axis=1)
y = df['DFS_STATUS']

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

from sklearn.feature_selection import RFE
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
# define the method
rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=10)
model = DecisionTreeClassifier()
pipeline = Pipeline(steps=[('s',rfe),('m',model)])
# evaluate model
cv = RepeatedStratifiedKFold(n_splits=3, n_repeats=2, random_state=1)
n_scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
# report performance
print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

#Standardizing Variables
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

xgb.plot_importance(model)
plt.rcParams['figure.figsize'] = [15, 10]
plt.show()

from sklearn.svm import SVC
from sklearn.datasets import make_classification

from yellowbrick.model_selection import RFECV

# Instantiate RFECV visualizer with a linear SVM classifier
visualizer = RFECV(SVC(kernel='linear', C=1))

visualizer.fit(X, y)        # Fit the data to the visualizer
visualizer.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

#rom yellowbrick.model_selection import rfecv


#cv = StratifiedKFold(5)
#visualizer = rfecv(RandomForestClassifier(), X=X, y=y, cv=cv, scoring='f1_weighted')

model = LogisticRegression(solver='liblinear', random_state=0)

model.fit(X, y)

model.score(X, y)

confusion_matrix(y, model.predict(X))

from matplotlib import pyplot

from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(X, y, test_size = 0.25, random_state = 1)

#Standardizing Variables
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

train_features = scaler.fit_transform(train_features)

test_features = scaler.transform(test_features)

forest = RandomForestClassifier()
forest.fit(train_features,train_labels)

y_pred_test = forest.predict(test_features)

confusion_matrix(test_labels, y_pred_test)

##Confusion Matrix is the number of correct and incorrect predictions made by a classifier
result = confusion_matrix(test_labels, y_pred_test)
print("Confusion Matrix for Random Forest:")
print(result)
#Getting the classification report
result1 = classification_report(test_labels, y_pred_test)
print("Classification Report for Random Forest:",)
print (result1)
#Overall accuracy
result2 = accuracy_score(test_labels, y_pred_test)
print("Overall Accuracy For Random Forest Tree:",result2)

FP = result.sum(axis=0) - np.diag(result) 
FN = result.sum(axis=1) - np.diag(result)
TP = np.diag(result)
TN = result.sum() - (FP + FN + TP)
FP = FP.astype(float)
FN = FN.astype(float)
TP = TP.astype(float)
TN = TN.astype(float)
total=sum(sum(result))
# Sensitivity, hit rate, recall, or true positive rate
TPR = ((TP/(TP+FN))).mean()*100
# Specificity or true negative rate
TNR = ((TN/(TN+FP))).mean()*100 

print('Sensitivity:' ,TPR)
print('Specificity: ' ,TNR)

from sklearn .metrics import roc_auc_score
from sklearn .metrics import roc_curve
from sklearn .metrics import auc

fpr, tpr, thresholds = roc_curve(test_labels, y_pred_test)
fig, ax = plt.subplots()
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="--", c=".3")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.rcParams['font.size'] = 12
plt.title('ROC curve for Disease classifier')
plt.xlabel('False Positives')
plt.ylabel('True Positives')
plt.grid(True)

auc(fpr, tpr)

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(
      units=128,
      activation='relu',
      input_shape=[X_train.shape[1]]
    ),
    #tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.Dense(units=64, activation='relu'),
    #tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.Dense(units=32, activation='relu'),
    #tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.Dense(units=16, activation='relu'),
    #tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.Dense(units=8, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='sigmoid'),
  ])

model.compile(
  loss="binary_crossentropy",
  optimizer="adam",
  metrics=['accuracy']
)

model.fit(X_train,y_train,batch_size=32,epochs = 100)

model.evaluate(X_train, y_train)

m1=model.evaluate(X_train, y_train)

model.evaluate(X_test, y_test)

m2=model.evaluate(X_test, y_test)

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=300, verbose=0)

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=300, verbose=0)

_, train_acc = model.evaluate(X_train, y_train, verbose=0)
_, test_acc = model.evaluate(X_test, y_test, verbose=0)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))
# plot loss during training
pyplot.subplot(211)
pyplot.title('Loss')
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
# plot accuracy during training
pyplot.subplot(212)
pyplot.title('Accuracy')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='test')
pyplot.legend()
pyplot.show()

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))



from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

cv = KFold(n_splits=10, random_state=1, shuffle=True)

neural_network = KerasClassifier(build_fn=model, epochs=10, batch_size=100,verbose=0)

#cross_val_score(neural_network, X,y, cv=3)
#n_scores = cross_val_score(neural_network, X, y, scoring='accuracy', cv=3, n_jobs=-1, error_score='raise')

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=3, n_jobs=-1, error_score='raise')

a=0;
for i in n_scores:
  a+=i*100
print(a/3)

#OVersampling
from imblearn.over_sampling import SMOTE
smote=SMOTE()
x_smote,y_smote= smote.fit_resample(X,y)
print("Original Df shape : ", y.shape)
print('Current Df shape: ', y_smote.shape)

sns.countplot(x='DFS_STATUS',data=df)

X_train, X_test, y_train, y_test = train_test_split(x_smote,y_smote, test_size = .2, random_state=10) #split the data 80-20

rf = RandomForestClassifier()
rf.fit(X_train,y_train)

rf_pred = rf.predict(X_test)
print('AUC score is: ', roc_auc_score(y_test,rf_pred))
print('The Accuracy score is: ', accuracy_score(y_test, rf_pred))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, rf_pred)) # True negatives in the upper-left position, False negatives in the lower-left positionm, False positives in the upper-right position, True positives in the lower-right position
print(classification_report(y_test, rf_pred))

cm = confusion_matrix(y_test, rf_pred)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()

import time
import numpy as np

start_time = time.time()
importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

fpr, tpr, thresholds = roc_curve(y_test, rf_pred)
fig, ax = plt.subplots()
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="--", c=".3")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.rcParams['font.size'] = 12
plt.title('ROC curve for Disease classifier')
plt.xlabel('False Positives')
plt.ylabel('True Positives')
plt.grid(True)

from sklearn.svm import SVC
model = SVC(C=1.0, kernel='linear', class_weight='balanced')
model.fit(X, y)

model.score(X, y)

from sklearn.pipeline import make_pipeline
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(gamma='auto'))])

model.score(X, y, sample_weight=None)