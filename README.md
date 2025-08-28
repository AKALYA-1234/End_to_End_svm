🌸 Iris Flower Classification with SVM + Streamlit:

Iris flower classification Streamlit link:
https://endtoendsvm-m4bqjdwwkzghrp6lswgjkk.streamlit.app/

📝 Task Description

This project classifies Iris flowers into three species:

Setosa 🌼

Versicolor 🌸

Virginica 🌺

using a Support Vector Machine (SVM) classifier.

Goal: Predict the species of an Iris flower based on its sepal and petal measurements.


📊 Features (Dataset Columns)

🌿 Sepal length (cm)

🌿 Sepal width (cm)

🌸 Petal length (cm)

🌸 Petal width (cm)

🏷️ Target: Flower species (Setosa, Versicolor, Virginica)

📌 Total rows: 150 samples


⚡ Steps Performed

1️⃣ Data Loading and Preprocessing

Loaded the Iris dataset (iris_svm.csv / sklearn.datasets version).

Converted data into a Pandas DataFrame.

Encoded target labels using LabelEncoder.

Standardized features with StandardScaler for better SVM performance.

2️⃣ Model Training

Split dataset into 80% training and 20% testing.

Trained an SVM classifier (RBF kernel) on the scaled data.

3️⃣ Model Evaluation

Predicted species on the test set.

Calculated accuracy score.

Plotted confusion matrix to analyze per-class performance.

4️⃣ Prediction

Tested trained model with new flower measurements.

Model predicts the species (Setosa / Versicolor / Virginica).

5️⃣ Visualization

Pairplot: Feature relationships colored by species.

Decision boundary plot: Visual separation of classes using first two features.


🎯 Results

✅ High accuracy achieved on test set.

✅ Decision boundary clearly separates species.

✅ Confusion matrix shows strong per-class performance.


🛠 Tools and Libraries

🐍 Python 3.12.5

📦 scikit-learn (SVM, preprocessing, metrics)

📊 Pandas & NumPy

🎨 Matplotlib & Seaborn (visualizations)

🌐 Streamlit (interactive prediction web app)


🚀 How to Run

1️⃣ Train the Model
Run:
    python train_model.py

2️⃣ Launch the Web App
Run:
    streamlit run app.py


✨ This project demonstrates the complete ML workflow:
data loading → preprocessing → model training → evaluation → deployment as an interactive web app.

Screenshot for this frontend:

<img width="977" height="711" alt="Screenshot 2025-08-28 093802" src="https://github.com/user-attachments/assets/99d2d6df-39e0-438c-857b-175ffa802a51" />


