
# HR Attrition Analytics — IBM HR Dataset

End-to-end HR analytics project analyzing employee attrition using SQL, Python, and Power BI. Covers data cleaning, exploratory analysis, and an interactive dashboard to identify who is most likely to leave and why.

## Objective

Analyze the IBM HR Analytics Employee Attrition dataset to identify the key drivers of employee attrition and surface actionable insights for HR decision-making — which departments, roles, and employee segments carry the highest turnover risk.

## Dataset

**Source:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) (Kaggle)
- **Size:** 1,470 employee records, 35 columns
- **Fields include:** Age, Attrition, Department, Job Role, Monthly Income, Job Satisfaction, OverTime, Years at Company, Distance From Home, Work-Life Balance, and more.

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
  
  Full Notebook : <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/blob/main/Cleaning/01_Cleaning.py">Python Cleaning

  Cleaned Data : <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/blob/main/Cleaned_data/Cleaned%20IBM%20HR.csv">Cleaned Dataset

## 2. SQL Analysis

22 business questions answered using MySQL, progressing from fundamentals to advanced querying:

- **Aggregation & Grouping:** Overall attrition rate, attrition by department/job role/tenure group/income band, average income by department and gender
- **HAVING with subqueries:** Departments with attrition above the company average
- **CASE WHEN:** Attrition by job satisfaction level, custom high-risk employee flag (low satisfaction + overtime + short tenure)
- **Subqueries (including correlated):** Employees earning above their department's average income, employees with below-average tenure among leavers
- **CTEs:** Departments with below-average tenure, departments with attrition above 15% (solved two ways — CTE and HAVING — to compare approaches)
- **Window Functions:** Department ranking by attrition rate (`RANK()`), income ranking within department (`PARTITION BY`), running total of attrition by tenure, income comparison to department average, top-3 earners per department (`ROW_NUMBER()`)

Full query file: <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/blob/main/Analysis/HR%20IBM%20SQL.sql">SQL Analysis

## 3. Exploratory Data Analysis (Python)

18 visualizations covering univariate, bivariate, and correlation analysis using Matplotlib and Seaborn — including distribution plots, grouped attrition comparisons across every major dimension (department, role, gender, marital status, overtime, tenure, satisfaction, work-life balance), income analysis by job level and department, and a correlation heatmap of key HR metrics.

Full notebook: <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/blob/main/Python%20Visualization%20file/02_Visualization.py">Code

Images(Charts): <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/commit/3f69d4e7653896f310779af0065479dd074d88c1">All Visualizations

Key Visualizations:


1)Attrition split (pie chart):

<img width="450" height="450" alt="3)Overall Attrition Split(pie)" src="https://github.com/user-attachments/assets/5b153f4a-d5ab-4644-aaf5-5d53a0770759" />

2)Attrition by Job Role(Bar Chart):

<img width="750" height="450" alt="6)Attrition by Job Role(Bar Chart)" src="https://github.com/user-attachments/assets/090efaf3-b0d3-438c-a2cf-04d859f7e7b6" />

3)Age distribution: left vs stayed (histogram):

<img width="750" height="450" alt="10)Age Dist  by Attrition(Hist+kde)" src="https://github.com/user-attachments/assets/38e7b69c-6312-42fc-9165-6320d5dccee7" />

4)Correlation heatmap:

<img width="750" height="550" alt="18)Correlation Of Numeric Variables(Heatmap)" src="https://github.com/user-attachments/assets/33c69402-becf-4046-aaec-2a2f65df7cc8" />






## 4. Interactive Dashboard (Power BI)

Built a fully interactive dashboard with DAX measures, KPI cards, and three cross-filtering slicers (Department, Gender, Overtime).

**Dashboard preview:**
<img width="1544" height="864" alt="IBM HR PBI" src="https://github.com/user-attachments/assets/0361976a-354c-477a-9986-291c0251eb6f" />

🎥 [Watch dashboard walkthrough]: <a href="https://github.com/shubhamganganmale77-ai/IBM-HR-ANALYSIS/blob/2f33fd36ea502e752dfb4cca066d1d2ffbbc17fa/Dashboard/IBM%20GIF.gif">Interactive Dashboard 


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
main/
├── Source_data/
├── Cleaning/
├── Cleaned_Dataset/
├── SQL_Analysis/
├── Visualization/
├── images(Visualizations)/
├── Dashboard/
└── README.md
```
