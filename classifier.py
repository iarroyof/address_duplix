import pandas as pd
from scipy import sparse
import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix


def metric(A, B):
    TN, FP, FN, TP = confusion_matrix(A, B).ravel()
    TNR = TN / (TN + FP)
    TPR = TP / (TP + FN)
    return (TPR + 2 * TNR) / 3

# Set the regularization parameter
C = 100
# Load the dataset
df=pd.read_csv("address_matching_data.csv")
# Replace missing values by zero
df=df.applymap(lambda x: 0 if "?" in str(x) else x)
# Sparsify the data
y = np.delete(df.values, 0, 1).astype(np.float64)[:,-1]
X = sparse.csr_matrix(np.delete(df.values, 0, 1).astype(np.float64)[:,:-1])
# Split the dataset into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Instanciate and train the SVM classifier
clf = SVC(C=C)
clf.fit(X_train, y_train)

# Making predictions
y_pred = clf.predict(X_test)

# Report results on test (unseen) data
print("Personalized metric (specificity & sensitivity): %f" % metric(y_test, y_pred))
print("Macro F1 score: %f" % f1_score(y_test, y_pred, average='macro'))

