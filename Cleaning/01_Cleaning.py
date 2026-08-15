import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("IBM HR Analytics.csv")
# print(df)
# print(df.info())
# print(df.isnull().sum())# no null values find
# print(df.duplicated().sum())#No duplicate values found
# print(df["EmployeeCount"].nunique())
# print(df["Over18"].nunique())
# print(df["StandardHours"].nunique())
df.drop(columns=["EmployeeCount","Over18","StandardHours"],inplace=True)#No use(Same values whole rows)
df.rename(columns={"BusinessTravel":"Business_Travel",
                   "DistanceFromHome":"Distance_From_Home",
                   "DailyRate":"Daily_Rate",
                   "EducationField":"Education_Field",
                   "EmployeeNumber":"Employee_Number",
                   "EnvironmentSatisfaction":"Environment_Satisfaction",
                   "HourlyRate":"Hourly_Rate",
                   "JobInvolvement":"Job_Involvement",
                   "JobLevel":"Job_Level",
                   "JobRole":"Job_Role",
                   "JobSatisfaction":"Job_Satisfaction",
                   "MaritalStatus":"Marital_Status",
                   "MonthlyIncome":"Monthly_Income",
                   "NumCompaniesWorked":"Num_Companies_Worked",
                   "MonthlyRate":"Monthly_Rate",
                   "OverTime":"Over_Time",
                   "PercentSalaryHike":"Percent_Salary_Hike",
                   "PerformanceRating":"Performance_Rating",
                   "RelationshipSatisfaction":"Relationship_Satisfaction",
                   "StandardHours":"Standard_Hours",
                   "StockOptionLevel":"Stock_Option_Level",
                   "TotalWorkingYears":"Total_Working_Years",
                   "TrainingTimesLastYear":"Training_Times_Last_Year",
                   "WorkLifeBalance":"Work_Life_Balance",
                   "YearsAtCompany":"Years_At_Company",
                   "YearsInCurrentRole":"Years_In_Current_Role",
                   "YearsSinceLastPromotion":"Years_Since_Last_Promotion",
                   "YearsWithCurrManager":"Years_With_Curr_Manager"},inplace=True)#Rename columns for clarity
df["Attrition_binary"]=df["Attrition"].map({"Yes":1,"No":0})
df["Gender_binary"]=df["Gender"].map({"Male":1,"Female":0})
df["Over_Time_binary"]=df["Over_Time"].map({"Yes":1,"No":0})#For making analysis easier
sns.boxplot(y=df["Monthly_Income"])#We keep outliers because senior employees have higher salary
sns.boxplot(x=df["Job_Level"],y=df["Monthly_Income"])#As job level increases income also increases
# print(df[df['Years_In_Current_Role'] > df['Years_At_Company']])
# print(df[df['Years_At_Company']<df['Years_With_Curr_Manager']])
att_rate=df["Attrition_binary"].mean()*100 #Attrition Rate is 16%
# print(df["Employee_Number"].value_counts().nunique())#All Employees have unique ID
#IQR Outlier
def outlier_detection_iqr(df,column):
    Q1=df[column].quantile(0.25)
    Q3=df[column].quantile(0.75)
    IQR=Q3-Q1
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    outliers=df[(df[column]<lower) | (df[column]>upper)]
    return outliers
print(outlier_detection_iqr(df,"Monthly_Income"))#Oulier detected but cant be removed
print(outlier_detection_iqr(df,"Age"))
print(outlier_detection_iqr(df,"Daily_Rate"))
print(outlier_detection_iqr(df,"Distance_From_Home"))
print(outlier_detection_iqr(df,"Daily_Rate"))
print(outlier_detection_iqr(df,"Education"))
print(outlier_detection_iqr(df,"Hourly_Rate"))
print(outlier_detection_iqr(df,"Monthly_Rate"))
print(outlier_detection_iqr(df,"Num_Companies_Worked"))#Outlier detected but cant be remove because employees can be worked in 8 or more comapnies
print(df["Num_Companies_Worked"].value_counts())
print(outlier_detection_iqr(df,"Percent_Salary_Hike"))
print(outlier_detection_iqr(df,"Performance_Rating"))#More number of rating 3 is obtained therefore it shows rating 4 as outlier. cant remove outlier
print(outlier_detection_iqr(df,"Stock_Option_Level"))#Cant remove outliers
print(outlier_detection_iqr(df,"Total_Working_Years"))#In this dataset there are older and younger employees present with huge difference in working year
print(outlier_detection_iqr(df,"Work_Life_Balance"))
print(outlier_detection_iqr(df,"Training_Times_Last_Year"))#Cant remove outlier
print(outlier_detection_iqr(df,"Years_At_Company"))#Many employees have much more years in compalny they are not outliers
print(outlier_detection_iqr(df,"Years_In_Current_Role"))#Cant remove them they might be real
print(outlier_detection_iqr(df,"Years_Since_Last_Promotion"))#All are real values
print(outlier_detection_iqr(df,"Years_With_Curr_Manager"))#No extreme values

df["Age_Bracket"]=pd.cut(df["Age"],bins=[17,25,35,45,60],labels=["18-25","26-35","36-45","46-60"])#Creating Age bracket
df["Income_Band"]=pd.qcut(df["Monthly_Income"],q=4,labels=["Low","Medium","High","Very High"])#Creating Income Band
df["Tenure_Group"]=pd.cut(df["Years_At_Company"],bins=[-1,2,5,10,40],labels=["0-2","3-5","6-10","10+"])#Group according to working years

# df.to_csv('Cleaned IBM HR.csv', index=False)







