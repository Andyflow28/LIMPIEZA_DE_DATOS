# 🛒 Café Sales Analytics Dashboard

> 📊 Data-driven insights into product sales, customer behavior, and operational trends for a food and beverage business.

---

## 📁 Project Overview

This project explores and analyzes transactional data from a food retail environment (e.g., café, bakery, or takeaway shop). The main objective is to extract meaningful business insights, identify high-performing products, understand customer purchasing patterns, and provide actionable recommendations based on the data.

We use **Python (Pandas, Seaborn, Matplotlib)** for data cleaning and visual analysis, with the goal of enabling strategic decisions in product offerings, marketing, and operations.

---

## 🧹 Data Cleaning Process

The dataset was first processed to ensure data integrity and consistency:
- Converted `Transaction Date` to `datetime` format.
- Ensured numerical columns (`Quantity`, `Price Per Unit`, `Total Spent`) were properly typed.
- Removed invalid or missing entries.

---

## 📈 Key Business Questions & Insights

### 📌 1. Top-Selling Products
- **Top 5 by Units Sold**: Identify the products with highest total quantity sold.
- **Top 5 by Revenue**: Find the items that generate the most income.

### 💳 2. Payment Method Distribution
- Analyze how customers are paying: credit card, cash, or other.
- Results shown in % distribution.

### 📍 3. Location-Based Performance
- **Which location (In-store or Takeaway) generates more revenue?**
- **What are the top products sold in each location?**

### 🕒 4. Temporal Sales Analysis
- Determine **which months have the most transactions**.
- Visualize **daily revenue trends** to analyze consistency and seasonality.

### 👥 5. Customer Behavior
- Calculate **average ticket value**.
- Estimate **common product combinations** (basic co-purchasing insights).

---

## 📊 Visualizations

The project includes clear, professional charts created with **Seaborn**:
- Colorful bar charts using themed palettes (e.g., `viridis`, `magma`, `coolwarm`).
- Time series line plots for trend analysis.
- Bar charts with percentage normalization for categorical distributions.

All visualizations are optimized for:
- Legibility 📐
- Consistent styling 🎨
- Readable English labels 📝

---

## 🛠️ Tools Used

| Tool / Library     | Purpose                            |
|--------------------|------------------------------------|
| Python             | Main programming language          |
| Pandas             | Data manipulation and wrangling    |
| Seaborn            | High-level statistical visualization |
| Matplotlib         | Plot customization                 |
| Jupyter Notebook   | Interactive development            |

---

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/Andyflow28/LIMPIEZA_DE_DATOS.git
   cd LIMPIEZA_DE_DATOS
