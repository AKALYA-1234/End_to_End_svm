import pandas as pd
from sklearn.svm import SVC
import pickle

# Load dataset
df = pd.read_csv("iris_svm.csv")

print("✅ Dataset loaded. Columns are:", df.columns)

# Split features and target
X = df.drop('species', axis=1)   # if your CSV target column is different, change here
y = df['species']

# Train SVM
svm_clf = SVC(kernel='linear', probability=True)
svm_clf.fit(X, y)

# Save trained model
with open('trained_model.sav', 'wb') as f:
    pickle.dump(svm_clf, f)

print("🎉 Model trained and saved as trained_model.sav")
