#!/usr/bin/env python
# coding: utf-8

#    # TP1 : Initiation et prise en main du langage Python 
#                        (Modules : NumPy, matplotlib, Pandas,
#                                 fichiers CSV, etc)

# In[24]:


#After loading the data using Pandas with the code below, we can display our CSV file.

import pandas as pd 
df=pd.read_csv(r"C:\Users\user\Downloads\titanic-passengers.csv",delimiter=';')

#The `df.isnull().sum()` function counts the number of null (or missing) values for each column in a DataFrame,
#providing a quick view of data quality, which is essential for data preparation and analysis.

df.isnull().sum()


# In[7]:


#After executing the command df.info, the result displays a document containing 891 rows and 12 columns.

df.info


# In[8]:


#To inspect the data in the 'Cabin' column of a DataFrame, you should use the following command to display the first 5 rows.
print(df['Cabin'].head())


# In[9]:


# This code starts by displaying the first 5 rows of the "Cabin" column in the DataFrame using the head() method.
# Then, it uses the isnull() method to check for the presence of null values in these first 5 rows. This quickly identifies missing entries in the "Cabin" column.
# If a value is missing, it is represented as "True"; otherwise, it is represented as "False".


print(df['Cabin'].head().isnull()) 


# In[68]:


Number_of_elements =len(df["Cabin"])
print("Number of elements:" ,Number_of_elements)

#We notice that there are 891 elements.


# In[10]:


#This code, using the "value_counts()" method on the "Cabin" column of a DataFrame, 
#performs a count of the occurrences of each unique value in that column.
#This process provides an overview of the different categories present in the "Cabin" column and helps us better understand the distribution of the data.

print(df["Cabin"].value_counts())


# In[11]:


df["Cabin"].fillna('G6',inplace=True)
df.tail()

# We replaced NaN with the most frequent value G6 in the Cabin column of the DataFrame.

# The use of the inplace=True argument indicates that the modification should be performed directly on the DataFrame.

# The inplace function is used to record the performed change (the deletion of the Cabin column).

# The tail() function is employed to display the last 5 rows of the DataFrame.


# In[12]:


print(df["Age"].value_counts())
#This program prints the count of each age occurrence in the "Age" column of a DataFrame (df).


# In[58]:


df["Age"].fillna(24,inplace=True)
df.tail()

#This program fills missing values in the "Age" column of a DataFrame (represented by the variable `df`) by replacing them with 24. 
#Then, it displays the last five rows of the modified DataFrame using the `tail()` method.


# In[50]:


print(df["Embarked"].value_counts())
#This program prints the count of each age occurrence in the "Embardek" column of a DataFrame (df).


# In[51]:


df["Embarked"].fillna('S',inplace=True)
df.tail()

#This program fills missing values in the "Embarked" column of a DataFrame (represented by the variable `df`) by replacing them with S. 
#Then, it displays the last five rows of the modified DataFrame using the `tail()` method.


# In[52]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Sex',data=df)
plt.xticks(rotation=-45)

# The provided code uses the matplotlib library to generate a histogram of ages based on the data from the 'Sex' column of the DataFrame.
# plt.xlabel("Sex")` adds a label to the x-axis, indicating that it represents Sex.
# Finally, `df['sex'].plot.hist()` creates the histogram itself by taking the data from the 'sex' column and graphically representing it. Each bar in the histogram represents an age range, and its height indicates the number of occurrences within that range.


# In[59]:


plt.title("Histogram of different ages")
plt.xlabel("Age")
df['Age'].plot.hist()



# The provided code uses the matplotlib library to generate a histogram of ages based on the data from the 'Age' column of the DataFrame.
# plt.title("Histogram of different ages")` sets the chart's title as "Histogram of different ages."
# plt.xlabel("Age")` adds a label to the x-axis, indicating that it represents age.
# Finally, `df['Age'].plot.hist()` creates the histogram itself by taking the data from the 'Age' column and graphically representing it. Each bar in the histogram represents an age range, and its height indicates the number of occurrences within that range.


# In[72]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Embarked',data=df)
plt.xticks(rotation=-45)

# This program uses the Python libraries Seaborn and Matplotlib to create a "countplot" chart. 
# It displays the count of occurrences of values in the 'Embarked' column of a DataFrame (represented by 'df'). 
# The unique values in 'Embarked' are shown on the x-axis, and the bars represent the number of occurrences of each value. 
#Additionally, the "plt.xticks(rotation=-45)" option tilts the x-axis labels by 45 degrees for improved chart readability.


# In[23]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df['Cabin'] = pd.factorize (df['Cabin'])[0] 
cabin_intervals = pd.cut(df['Cabin'], bins=5) 
sns.countplot(x=cabin_intervals, data=df)
plt.xticks (rotation=-45)
plt.xlabel('Cabine', fontsize=14)
plt.ylabel('FrÃ©quence', fontsize=14)
plt.title('FrÃ©quence des Cabines', fontsize=16)
plt.show()

#This program uses Python libraries, including Pandas for tabular data manipulation, Seaborn for creating plots, 
#and Matplotlib for visualization. It assumes you have a DataFrame (presumably named `df`) and converts the 'Cabin' column into numerical values. 
#It then creates intervals for this column and generates a bar plot showing the frequency of 'Cabin' values within specific intervals. 
#This plot helps visualize the distribution of cabins based on the created intervals.


# In[99]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\user\Downloads\titanic-passengers.csv", delimiter=';')
numeric_columns = df.select_dtypes(include=['number'])

corr = numeric_columns.corr()
s, ax = plt.subplots(figsize=(12, 10))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
s = sns.heatmap(corr, cmap=cmap, square=True, cbar_kws={'shrink': 0.9}, annot=True, annot_kws={'fontsize': 12})

plt.show()


# A value of 1 signifies a perfect positive correlation, meaning that as one variable increases, the other also increases in a linear manner.
# On the other hand, a value of -1 indicates a perfect negative correlation, where as one variable increases, the other decreases linearly.
# When the correlation coefficient is 0, it denotes a lack of linear correlation between the variables.
                                                


# In[ ]:


#conclusion:
#In this TP, we utilized various data manipulation and visualization techniques in Python to create a DataFrame.
#Our work revolved around the following steps: data loading and inspection, handling missing data, data exploration, data visualization, and correlation analysis.
#All of these steps are of paramount importance in the data analysis process, enabling us to comprehend the data's content and extract meaningful insights from the dataset.

