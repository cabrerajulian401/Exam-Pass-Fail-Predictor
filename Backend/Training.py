from Backend.Pre_Processing import Preprocessing_Data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import numpy as np 

process = Preprocessing_Data('student_exam_data.csv')

process.read_csv()

process.feature_selection()

process.shape_x()

process.shape_y()

process.split_data()

process.standardize_data()




# Initialize an instance of the LogisticRegression 

logreg_model = LogisticRegression(random_state = 1)

logreg_model = logreg_model.fit(process.x_train_std, process.y_train)

# Testing Model on the Training Data 

y_pred_train = logreg_model.predict(process.x_train_std)

accuracy_train = accuracy_score(process.y_train, y_pred_train)

print(accuracy_train)

print("Accuracy for Train: ", accuracy_train)

# Testing Model on the Testing Data

y_pred_test = logreg_model.predict(process.x_test_std)

accuracy_test = accuracy_score(process.y_test, y_pred_test)

print("Accuracy for Test: ", accuracy_test)



new_instance = np.array([[5, 99]]) # shape (1, number_of_features)

# Standardize the new instance (CRITICAL STEP)
new_instance_std = process.standardize_instance(new_instance)

# Predict class
predicted_label = logreg_model.predict(new_instance_std)

# Predict probability (optional, but useful):
predicted_prob = logreg_model.predict_proba(new_instance_std)

# Print clear results:
print("Predicted Class:", predicted_label[0])
print("Predicted Probability:", predicted_prob[0])

model = LogisticRegression()

# Perform 5-Fold Cross-Validation
cv_scores = cross_val_score(model, process.x_train_std, process.y_train, cv=5, scoring='accuracy')

print("K-Fold CV Accuracy Scores:", cv_scores)
print("Mean CV Accuracy:", cv_scores.mean())




