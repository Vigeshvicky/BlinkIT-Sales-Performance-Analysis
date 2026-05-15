# 🛒 BLINKIT GROCERY SALES ANALYSIS

---

# 📌 OVERVIEW

The **BlinkIT Grocery Sales Analysis** project is a complete **Data Analytics & Visualization** project developed using **Python** and its powerful data analysis libraries.

This project focuses on analyzing grocery sales data to discover meaningful business insights related to:

* Product sales performance
* Outlet performance
* Customer ratings
* Item visibility
* Product categories
* Sales trends

The dataset was cleaned, transformed, analyzed, and visualized to understand customer purchasing patterns and outlet-level performance.

---

# 🎯 PROJECT OBJECTIVE

The main objective of this project is to analyze BlinkIT grocery sales data and generate actionable insights using data analytics and visualization techniques.

### Objectives Include:

* Analyze total sales performance
* Understand item category distribution
* Compare outlet performance
* Track sales trends over years
* Study customer ratings
* Explore item visibility and sales relationship

---

# 🛠️ TOOLS & TECHNOLOGIES USED

<p align="left">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>

<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>

<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Jupyter-FA0F00?style=for-the-badge&logo=jupyter&logoColor=white"/>

</p>

---

# 📂 DATASET INFORMATION

The dataset contains grocery product and outlet-related information including:

* Item Fat Content
* Item Type
* Outlet Establishment Year
* Outlet Type
* Outlet Size
* Outlet Location Type
* Item Visibility
* Item Weight
* Sales
* Rating

### Dataset Shape

* Rows: **8523**
* Columns: **12**

---

# 🧹 DATA CLEANING PROCESS

The following preprocessing steps were performed:

✔ Checked dataset structure using `info()` and `describe()`
✔ Handled missing values using `fillna()`
✔ Removed duplicate records
✔ Standardized inconsistent values in **Item Fat Content**
✔ Rounded sales and visibility values
✔ Converted rating datatype for analysis

### Example:

```python
df["Item Fat Content"]=df["Item Fat Content"].replace({
    "low fat":"Low Fat",
    "LF":"Low Fat",
    "reg":"Regular"
})
```

---

# 📊 EXPLORATORY DATA ANALYSIS (EDA)

Several visualizations were created to analyze the dataset.

## 📈 Sales by Item Type

* Compared sales across different product categories
* Identified high-performing item categories

## 🥧 Item Type Distribution

* Visualized percentage distribution of product categories

## 📉 Sales Distribution

* Analyzed overall sales frequency using histogram

## ⚖️ Item Weight vs Sales

* Studied relationship between item weight and sales

## 🏪 Outlet Tier vs Item Fat Content

* Compared outlet sales based on fat content categories

## 📅 Outlet Establishment Year vs Sales

* Analyzed sales trend across outlet establishment years

---

# 📌 KEY INSIGHTS

✔ Fruits & Vegetables had the highest product count
✔ Snack Foods generated strong sales performance
✔ Tier 3 outlets showed high sales contribution
✔ Sales distribution was moderately spread
✔ Customer ratings were generally high
✔ Some products had zero visibility values
✔ Older and established outlets contributed significantly to sales

---

# 📈 BUSINESS IMPACT

This analysis helps businesses:

* Understand customer purchasing behavior
* Improve inventory planning
* Identify high-performing product categories
* Optimize outlet performance
* Support data-driven business decisions

---

# 🔍 SKILLS DEMONSTRATED

✔ Data Cleaning
✔ Data Transformation
✔ Exploratory Data Analysis
✔ Data Visualization
✔ Business Analytics
✔ Python Programming
✔ Statistical Analysis

---

# 📷 VISUALIZATIONS INCLUDED

* Bar Plot
* Pie Chart
* Histogram
* Scatter Plot
* Line Chart

---

# 🚀 PROJECT OUTCOME

This project successfully transformed raw grocery sales data into meaningful business insights using Python-based analytics and visualization techniques.

The analysis improved understanding of:

* Product sales trends
* Outlet performance
* Customer preferences
* Business growth opportunities

---

# 📁 PROJECT FILES

```bash
BlinkIT Grocery Data Analysis.ipynb
BlinkIT Grocery Data.xlsx
README.md
```

---

# 📚 LIBRARIES USED

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# ✨ CONCLUSION

The **BlinkIT Grocery Sales Analysis** project demonstrates how data analytics can help businesses uncover valuable insights from raw data.

Using Python libraries like **Pandas, NumPy, Matplotlib, and Seaborn**, the project analyzed grocery sales performance, customer behavior, and outlet trends through effective visualizations and statistical analysis.

This project highlights practical skills in:

* Data Cleaning
* EDA
* Visualization
* Business Insight Generation
* Analytical Thinking

---

# ⭐ SUPPORT

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork the project
* 📢 Share your feedback

Thank you for visiting this project!
