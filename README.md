# HR Attrition Analytics — IBM HR Dataset

End-to-end HR analytics project analyzing employee attrition using SQL, Python, and Power BI. Covers data cleaning, exploratory analysis, and an interactive dashboard to identify who is most likely to leave and why.

## Objective

Analyze the IBM HR Analytics Employee Attrition dataset to identify the key drivers of employee attrition and surface actionable insights for HR decision-making — which departments, roles, and employee segments carry the highest turnover risk.

## Dataset

**Source:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) (Kaggle)
**Size:** 1,470 employee records, 35 columns
**Fields include:** Age, Attrition, Department, Job Role, Monthly Income, Job Satisfaction, OverTime, Years at Company, Distance From Home, Work-Life Balance, and more.

## Tools Used

| Tool | Purpose |
|---|---|
| Python (Pandas, Matplotlib, Seaborn) | Data cleaning, outlier detection, exploratory data analysis |
| SQL (MySQL) | Business-question querying — aggregation, subqueries, CTEs, window functions |
| Power BI | Interactive dashboard with DAX measures and slicers |

## Project Workflow

```
Raw Data → Python Cleaning → SQL Analysis → Python EDA/Visualization → Power BI Dashboard
```

---

## 1. Data Cleaning (Python)

- Checked for null values and duplicates — dataset is synthetic and pre-cleaned, so no nulls/duplicates were found (verified and documented).
- Dropped zero-variance columns (`EmployeeCount`, `StandardHours`, `Over18`) — no analytical value.
- Verified logical consistency across tenure-related fields (e.g., `YearsInCurrentRole` cannot exceed `YearsAtCompany`).
- Performed IQR-based outlier detection across all numeric columns. Outliers found in `MonthlyIncome`, `YearsAtCompany`, and `TotalWorkingYears` were cross-verified against `JobLevel` and retained — they represent genuine senior/long-tenured employees, not data errors.
- Encoded categorical fields (`Attrition`, `Gender`, `OverTime`) into binary flags for rate calculations and correlation analysis.
- Engineered derived features for deeper segmentation:
  - `Age_Group` (18-25, 26-35, 36-45, 46-60) — fixed-range bins via `pd.cut()`
  - `Tenure_Group` (0-2, 3-5, 6-10, 10+ years) — fixed-range bins via `pd.cut()`
  - `Income_Band` (Low, Medium, High, Very High) — equal-frequency quartile bins via `pd.qcut()`, chosen due to income's right-skewed distribution

## 2. SQL Analysis

22 business questions answered using MySQL, progressing from fundamentals to advanced querying:

- **Aggregation & Grouping:** Overall attrition rate, attrition by department/job role/tenure group/income band, average income by department and gender
- **HAVING with subqueries:** Departments with attrition above the company average
- **CASE WHEN:** Attrition by job satisfaction level, custom high-risk employee flag (low satisfaction + overtime + short tenure)
- **Subqueries (including correlated):** Employees earning above their department's average income, employees with below-average tenure among leavers
- **CTEs:** Departments with below-average tenure, departments with attrition above 15% (solved two ways — CTE and HAVING — to compare approaches)
- **Window Functions:** Department ranking by attrition rate (`RANK()`), income ranking within department (`PARTITION BY`), running total of attrition by tenure, income comparison to department average, top-3 earners per department (`ROW_NUMBER()`)

Full query file: [`SQL_Analysis/hr_attrition_queries.sql`](./SQL_Analysis/hr_attrition_queries.sql)

## 3. Exploratory Data Analysis (Python)

18 visualizations covering univariate, bivariate, and correlation analysis using Matplotlib and Seaborn — including distribution plots, grouped attrition comparisons across every major dimension (department, role, gender, marital status, overtime, tenure, satisfaction, work-life balance), income analysis by job level and department, and a correlation heatmap of key HR metrics.

Full notebook: [`Cleaning & Analysis/eda_visualization.ipynb`](./Cleaning%20&%20Analysis/eda_visualization.ipynb)

## 4. Interactive Dashboard (Power BI)

Built a fully interactive dashboard with DAX measures, KPI cards, and three cross-filtering slicers (Department, Gender, Overtime).

**Dashboard preview:**
![HR Attrition Dashboard](images/dashboard_screenshot.png)

🎥 [Watch dashboard walkthrough](Dashboard/demo_video.mp4)

**Includes:**
- KPI cards: Total Employees, Attrition Rate, Avg Monthly Income, Avg Tenure
- Attrition Rate by Department, Job Role (Top 5), Gender, Tenure Group, Age Bracket, Overtime Status
- Fully interactive slicers for on-the-fly filtering

---

## Key Insights

- **Overall attrition rate is 16.12%** — roughly 1 in every 6 employees has left.
- **Sales Representative** has by far the highest attrition rate among job roles at **39.76%**, more than double the next closest role.
- **New employees are the highest flight risk** — the 0-2 year tenure group shows a **29.82%** attrition rate, dropping sharply to 8.13% for employees with 10+ years.
- **Overtime is one of the strongest attrition drivers** — employees working overtime leave at **30.53%**, roughly 3x the rate of those who don't (**10.44%**).
- **Younger employees (18-25) show the steepest attrition**, declining consistently as age increases — reinforcing the tenure-based pattern.
- **Sales has the highest departmental attrition (20.63%)**, followed by HR (19.05%) and R&D (13.84%).
- **Lower job satisfaction and lower income bands correlate with higher attrition**, though job role, tenure, and overtime are stronger individual predictors than income alone.

**Overall takeaway:** attrition risk is concentrated among **young, short-tenured, overtime-working Sales Representatives** — a clear, actionable segment for HR to prioritize with retention efforts.

---

## Repository Structure

```
HR-Analytics-Attrition/
├── Source_data/
├── Cleaning & Analysis/
├── Cleaned_Dataset/
├── SQL_Analysis/
├── Visualization/
├── Dashboard/
├── images/
└── README.md
```
