# BlinkIT-Sales-Performance-Analysis
````markdown
# 🛒 BlinkIT Grocery Sales Analysis using Python

## 📌 Project Overview
This project focuses on analyzing BlinkIT grocery sales data using Python.  
The analysis helps uncover sales trends, customer preferences, outlet performance, and product distribution through data cleaning, preprocessing, and visualization techniques.

---

## 🎯 Objectives
- Perform data cleaning and preprocessing
- Analyze grocery sales performance
- Identify top-selling product categories
- Study outlet establishment trends
- Visualize customer and sales patterns
- Generate business insights using charts and graphs

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📂 Dataset Information
The dataset contains:
- Item Details
- Outlet Information
- Sales Data
- Product Categories
- Item Ratings
- Outlet Types and Sizes

Total Records: **8523 Rows × 12 Columns**

---

## 🔍 Data Cleaning Process
The following preprocessing steps were performed:

### ✅ Handling Missing Values
```python
df.fillna(0, inplace=True)
````

### ✅ Removing Duplicate Records

```python
df.drop_duplicates(inplace=True)
```

### ✅ Standardizing Categorical Values

```python
df["Item Fat Content"] = df["Item Fat Content"].replace({
    "low fat":"Low Fat",
    "LF":"Low Fat",
    "reg":"Regular"
})
```

### ✅ Formatting Data

* Rounded Sales values
* Rounded Item Visibility values
* Converted Rating datatype into Integer

---

## 📊 Exploratory Data Analysis (EDA)

### ✔ Sales by Item Type

Bar chart visualization showing sales performance across different item categories.

### ✔ Item Type Distribution

Pie chart displaying product category distribution.

### ✔ Sales Distribution

Histogram used to understand overall sales spread.

### ✔ Item Weight vs Sales

Scatter plot used to identify relationship between item weight and sales.

### ✔ Outlet Tier by Item Fat Content

Grouped bar chart comparing sales across outlet tiers and fat content.

### ✔ Outlet Establishment Year vs Total Sales

Line chart visualizing sales trend based on outlet establishment year.

---

## 📈 Key Insights

* Fruits & Vegetables and Snack Foods recorded the highest sales.
* Tier 3 outlets generated strong sales performance.
* Most products belong to Low Fat category.
* Sales distribution shows moderate variation across products.
* Older outlets also maintain stable sales performance.

---

## 📌 Project Metrics

| Metric              | Value     |
| ------------------- | --------- |
| Total Sales         | 1,197,436 |
| Average Sales       | 140.49    |
| Total Products Sold | 8523      |
| Average Rating      | 3         |

---

## 📷 Visualizations Included

* Bar Plot
* Pie Chart
* Histogram
* Scatter Plot
* Line Chart
* Grouped Bar Chart

---

## 🚀 Future Improvements

* Build interactive Power BI dashboard
* Add machine learning sales prediction
* Deploy project using Streamlit
* Perform customer segmentation analysis

---

## 📁 Project Structure

```text
BlinkIT-Grocery-Analysis/
│
├── BlinkIT_Analysis.ipynb
├── BlinkIT Grocery Data.xlsx
├── README.md
└── visualizations/
```

---


## ⭐ Conclusion

This project demonstrates practical data analytics skills including:

* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Business Insight Generation

using real-world grocery sales data with Python.

```
```
