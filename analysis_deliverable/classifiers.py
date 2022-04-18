import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ttest_ind
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import KFold, cross_val_score
from sklearn.decomposition import PCA

df = pd.read_csv('combined_ri_data.csv')
#limit to one to four family dwellings
df = df[df['property_type_name']== 'One-to-four family dwelling (other than manufactured housing)']
#limit to co_applicant_race == 'No co_applicant' 
df = df[df['co_applicant_ethnicity_name'] == 'No co-applicant']
df['is_denial'] = (df['action_taken_name'] == 'Application denied by financial institution')

#machine learning models
'''
classifier to predict denial vs non denial
'''
#x = race, sex, income, loan amount, median hud income, county, census tract, tract_to_msamd_income, population, minority population
#y = is_denied

categorical_features = ['applicant_race_name_1', 'applicant_sex_name', 'county_name', 'hud_median_family_income', 'census_tract_number']
continuous_features = ['applicant_income_000s', 'loan_amount_000s']
label = ['is_denial']
real_df = df[label + continuous_features]
for feature in categorical_features:
	sub_df = pd.get_dummies(df[feature])
	real_df = pd.merge(real_df, sub_df, left_index=True, right_index=True)
	
real_df = real_df.fillna(0)

real_df = real_df.sample(10000)

og_Y = real_df[label].values
og_Y = np.reshape(og_Y, (len(og_Y),))
og_X = real_df.drop(columns = ['is_denial'])


#PCA with visualization
pca = PCA(n_components = 3)
scale_x = (og_X - og_X.min(axis=0)) / (og_X.max(axis=0) - og_X.min(axis=0))
scale_x = scale_x.fillna(0)
pca.fit(scale_x)
reduced = pca.transform(scale_x)

zero_ind = np.where(og_Y == 0)
one_ind = np.where(og_Y == 1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_title('PCA applied to the HMDA Mortgage Data Sample')
ax.set_xlabel('Principle Component 1')
ax.set_ylabel('Principle Component 2')
ax.set_zlabel('Principle Component 3')

ax.scatter(reduced[zero_ind,0], reduced[zero_ind,1], reduced[zero_ind,2], c='orange', label = 'not denied')
ax.scatter(reduced[one_ind,0], reduced[one_ind,1], reduced[one_ind,2], c='blue', label = 'denied')

plt.legend(loc="right")

plt.show()

X, X_Test, Y, Y_Test = train_test_split(og_X, og_Y, test_size = 0.20)
#Y_Test = Y_Test['is_denial'].values
#Y = Y['is_denial'].values
print(' ')
print('dummy accuracy', 1- sum(Y_Test)/len(Y_Test))


'''
#Logistic Regression
clf = LogisticRegression(random_state=0).fit(X,Y)
Y_Pred = clf.predict(X_Test)
print(clf.predict_proba(X_Test))
accuracy = sum(Y_Pred == Y_Test)/len(Y_Pred)
print('log regression', accuracy)
confusion = confusion_matrix(Y_Test,Y_Pred)
print(confusion)


#Decision Tree
print(' ')
print('Decision Tree')
decision_tree = tree.DecisionTreeClassifier().fit(X, Y)
Y_Pred = decision_tree.predict(X_Test)
decision_acc = sum((Y_Pred == Y_Test))/len(Y_Pred)
print("testing accuracy:", decision_acc)
decision_fp = sum(((Y_Pred == 1) == (Y_Test == 0)))/len(Y_Pred)
print('FPR:',decision_fp)
confusion = confusion_matrix(Y_Test,Y_Pred)
print(confusion)


#SVM
print(' ')
print('SVM')
svc = SVC(kernel='poly')
svc.fit(X, Y)
Y_Pred = svc.predict(X_Test)
svm_acc = sum((Y_Pred == Y_Test))/len(Y_Pred)
print("testing accuracy:", svm_acc)

svm_fp = sum(((Y_Pred == 1) == (Y_Test == 0)))/len(Y_Pred)
print('FPR:', svm_fp)
'''

'''KNN'''
print(' ')
print('KNN')
ks = range(1,50, 5)
accuracies = []
for k in ks:
	KNN = KNeighborsClassifier(n_neighbors=k)
	kf= KFold(n_splits=5)
	score = cross_val_score(KNN,og_X,og_Y,cv=kf)
	print(' ')
	print('k=', k)
	print("Cross Validation Scores are {}".format(score))
	print("Average Cross Validation score :{}".format(score.mean()))
	accuracies.append(score.mean())
	'''
	KNN.fit(X, Y)
	#Y_Pred = KNN.predict(X_Test)
	Y_Pred = (KNN.predict_proba(X_Test)[:,1] >= 0.5).astype(bool)
	accuracy = sum(Y_Pred == Y_Test)/len(Y_Pred)
	#accuracies.append(accuracy)
	print('accuracy:', accuracy)
	confusion = confusion_matrix(Y_Test,Y_Pred)
	print('confusion:', confusion)
	'''

plt.plot(ks, accuracies)
plt.title("Average Cross Validation Accuracy for K-Nearest-Neighbors vs. K")
plt.ylabel("Accuracy (%)")
plt.xlabel("K")
#plt.ylim(0,1.1)
plt.show()
plt.show()





