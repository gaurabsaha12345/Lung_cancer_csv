#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[8]:


def read_csv():
    # Method to read the CSV file "lung_cancer_examples.csv" using pandas.
    df=pd.read_csv("C:/Users/HP/Downloads/lung_cancer_examples.csv")
    return df


# In[9]:


def check_duplicates():
    df = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    duplicates=df.duplicated()
    duplicate_count=duplicates.sum()
    return duplicate_count


# In[10]:


check_duplicates()


# In[11]:


def check_null_values():
    df = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    null_values_sum=df.isnull().sum()
    return null_values_sum


# In[12]:


check_null_values()


# In[13]:


def rename_column():
    # do not edit the predefined function name
    df = read_csv()
    # Rename columns 'Alkhol' to 'Alcohol'.
    df=df.rename(columns={'Alkhol':'Alcohol'})
    return df


# In[14]:


rename_column()


# In[15]:


def check_smoke_value():
    # do not edit the predefined function name
    data = rename_column()
    smoke_count=data['Smokes'].value_counts()
    # Count the occurrences of each unique value in the 'Smokes' column


    # Return the counts of each unique smoking habit value
    return smoke_count


# In[16]:


check_smoke_value()


# In[17]:


def categorize_smokers(x):
    #If x is 0, categorize the person as 'Non-Smokers'.
    if x==0:
        return 'Non-Smokers'
    # If x is less than or equal to 2, categorize the person as 'Light Smokers'.
    elif x<=2:
        return 'Light Smokers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Smokers'.
    elif x>2 and x<=10:
        return 'Mediocre Smokers'
    # If x is greater than 10, categorize the person as 'Heavy Smokers'.
    else:
        return 'Heavy Smokers'


# In[19]:


categorize_smokers(3)


# In[32]:


def smokes():
    # do not edit the predefined function name
    data = rename_column()
    
    # Applying the 'categorize_smokers' function to each value in the 'Smokes' column
    # and storing the result in a new column 'Smoking_Category'
    data['Smoking_Category']=data['Smokes'].apply(categorize_smokers)

    # Returning the modified dataset with the new 'Smoking_Category' column
    return data


# In[33]:


smokes()


# In[34]:


def check_alcohol_value():
    # do not edit the predefined function name
    data = smokes()


    # Count the occurrences of each unique value in the 'Alcohol' column
    alcohol_count=data['Alcohol'].value_counts()

    # Return the counts of each unique smoking habit value
    return alcohol_count


# In[35]:


def categorize_alcohol(x):

    # If x is 0, categorize the person as 'Non-Drinkers'.
    if x==0:
        return 'Non-Drinkers'
    # If x is less than or equal to 2, categorize the person as 'Light Drinkers'.
    elif x<=2:
        return 'Light Drinkers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Drinkers'.
    elif x>2 and x<=10:
        return 'Mediocre Drinkers'
    # If x is greater than 10, categorize the person as 'Heavy Drinkers'.
    else:
        return 'Heavy Drinkers'


# In[36]:


categorize_alcohol(6)


# In[37]:


def alkhol():
    # Assuming the 'smokes()' function retrieves the dataset with the 'Smokes' column and the 'Alcohol' column
    data = smokes()

    # Applying the 'categorize_alcohol' function to each value in the 'Alcohol' column
    # and storing the result in a new column 'Alcohol_Category'
    data['Alcohol_Category']=data['Alcohol'].apply(categorize_alcohol)

    # Returning the modified dataset with the new 'Alcohol_Category' column
    return data


# In[38]:


alkhol()


# In[44]:


def export_the_dataset():
    # do not edit the predefined function name
    df = alkhol()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv('C:/Users/HP/Downloads/lung_cancer.csv',index=False)
    return df


# In[45]:


export_the_dataset()


# In[ ]:




