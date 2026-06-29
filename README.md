# ai-ml-task1-data-preprocessing-
# 🚢 Task 1: Data Cleaning & Preprocessing - Titanic Dataset

## 📌 Objective

The objective of this project is to clean and preprocess the Titanic dataset to make it suitable for Machine Learning models. This includes handling missing values, encoding categorical variables, scaling numerical features, and detecting/removing outliers.

---

## 📂 Dataset

* **Dataset:** Titanic Dataset
* **File Used:** `Titanic-Dataset.csv`

---

## 🛠️ Tools & Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📋 Steps Performed

### 1. Import Libraries

Imported the required Python libraries for data manipulation, visualization, and preprocessing.

### 2. Load Dataset

Loaded the Titanic dataset using Pandas.

### 3. Explore the Dataset

* Displayed the first five rows using `head()`.
* Displayed dataset information using `info()`.
* Checked for missing values using `isnull().sum()`.

### 4. Handle Missing Values

* Filled missing values in the **Age** column using the median.
* Filled missing values in the **Embarked** column using the mode.
* Dropped the **Cabin** column because it contained many missing values.

### 5. Encode Categorical Features

Converted categorical columns into numerical values using **Label Encoding**.

* Sex
* Embarked

### 6. Standardize Numerical Features

Applied **StandardScaler** to the following numerical columns:

* Age
* Fare

### 7. Detect Outliers

Visualized outliers in the **Fare** column using a boxplot.

### 8. Remove Outliers

Removed outliers using the **Interquartile Range (IQR)** method.

### 9. Save the Cleaned Dataset

Saved the processed dataset as:

`Cleaned_Titanic.csv`

---

## 📁 Project Structure

```text
Task-1-Data-Cleaning-Preprocessing/
│── Titanic-Dataset.csv
│── Cleaned_Titanic.csv
│── data_preprocessing.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/Task-1-Data-Cleaning-Preprocessing.git
```

2. Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Run the Python program.

```bash
python data_preprocessing.py
```

---

## 📌 Output

The program will:

* Load the Titanic dataset.
* Display dataset information.
* Handle missing values.
* Encode categorical variables.
* Standardize numerical features.
* Display a boxplot for outlier detection.
* Remove outliers using the IQR method.
* Save the cleaned dataset as `Cleaned_Titanic.csv`.

---

## 📚 Interview Questions

### 1. What are the different types of missing data?

* Missing Completely at Random (MCAR)
* Missing at Random (MAR)
* Missing Not at Random (MNAR)

### 2. How do you handle categorical variables?

By using Label Encoding or One-Hot Encoding.

### 3. What is the difference between normalization and standardization?

* **Normalization:** Scales values between 0 and 1.
* **Standardization:** Transforms data so it has a mean of 0 and a standard deviation of 1.

### 4. How do you detect outliers?

* Boxplots
* IQR (Interquartile Range)
* Z-score

### 5. Why is preprocessing important in Machine Learning?

It improves data quality, reduces errors, and helps improve the accuracy of machine learning models.

### 6. What is One-Hot Encoding vs Label Encoding?

* **One-Hot Encoding:** Creates separate binary columns for each category.
* **Label Encoding:** Assigns a unique integer to each category.

### 7. How do you handle data imbalance?

* Oversampling
* Undersampling
* SMOTE
* Class Weighting

### 8. Can preprocessing affect model accuracy?

Yes. Proper preprocessing improves model performance, reduces bias, and helps the model learn more effectively.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Data exploration using Pandas.
* Handling missing values.
* Encoding categorical variables.
* Feature scaling using StandardScaler.
* Outlier detection using boxplots.
* Outlier removal using the IQR method.
* Preparing data for Machine Learning.

---

## 👩‍💻 Author

**Rakshita**

---

## 📄 License

This project is created for educational purposes.
