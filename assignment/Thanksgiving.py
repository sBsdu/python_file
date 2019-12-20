"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :
 """       

#Discover regional and income-based patterns in what Americans eat for 
#Thanksgiving dinner
import pandas as pd

data = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\sapna_saini\\Data_Analytics\\thanksgiving-2015-poll-data.csv")
print(data)
grouped = data.groupby(["What type of cranberry sauce do you typically have?", "What is typically the main dish at your Thanksgiving dinner?"])
grouped.agg(np.mean)
 
#-----------------------------------------------------------------------------
#Convert the column name to single word names
import pandas as pd

data = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\sapna_saini\\Data_Analytics\\thanksgiving-2015-poll-data.csv")
print(data)

columns1 = list(data.columns)
list1=["food"+str(i) if "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply." in columns1[i] else columns1[i] for i in range(0,len(columns1))]

list1=["pie"+str(i) if "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply."in list1[i] else list1[i] for i in range(0,len(columns1))]

list1=["dishes"+str(i) if "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]

list1=["desserts"+str(i) if "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply." in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["cranberry saucedo"+str(i) if "What type of cranberry saucedo you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["stuffing/dressing"+str(i) if "What kind of stuffing/dressing do you typically have?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["main dish"+str(i) if "What is typically the main dish at your Thanksgiving dinner?" in list1[i] else list1[i] for i in range(0,len(columns1))]
list1=["cooked"+str(i) if "How is the main dish typically cooked?" in list1[i] else list1[i] for i in range(0,len(columns1))]


dict1=dict()
for i in range(0,len(list1)):
    dict1[columns1[i]]=list1[i]
data.rename(columns = dict1,inplace = True)
data.columns
#------------------------------------------------------------------------------------------
#Using the apply method to Gender column to convert Male & Female
import math
data["What is your gender?"].value_counts(dropna=False)


def gender_code(gender_string):
    if isinstance(gender_string, float) and math.isnan(gender_string):
        return gender_string
    return int(gender_string == "Female")
data["gender"] = data["What is your gender?"].apply(gender_code)
data["gender"].value_counts(dropna=False)

#--------------------------------------------------------------------------------------
#Using the apply method to clean up income
#(Range to a average number, X and up to X, Prefer not to answer to NaN)
#'''import numpy as np
#def clean_income(value):
#    if value == "$200,000 and up":
#        return 200000
#    elif value == "Prefer not to answer":
#        return np.nan
#    elif isinstance(value, float) and math.isnan(value):
#        return np.nan
#    value = value.replace(",", "").replace("$","")
#    income_high,income_low = value.split(" to ")
#    return (float(income_high) + float(income_low)) / 2
#data["income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(clean_income)
#data["income"].head()'''

import numpy as np
#data.apply(lambda x: x.dtype).head()
data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna=False)
data["How much total combined money did all members of your HOUSEHOLD earn last year?"].astype(str)
data["How much total combined money did all members of your HOUSEHOLD earn last year?"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].replace("Prefer not to answer",np.nan)
def clean_income(i):
    if "to" in str(i):
        i = i.replace(",","")
        i = i.replace("$","")
        a,b = i.split(" to ")
        return (float(a) + float(b))/2
    elif i == "$200,000 and up" :
        return int(200000)

data["income"]=data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(clean_income)
data["income"]
data.columns        
#-------------------------------------------------------------------------------------------   
#    compare income between people who tend to eat homemade cranberry sauce for
#    Thanksgiving vs people who eat canned cranberry sauce?

data["cranberry saucedo8"].value_counts()
homemade = data[data["cranberry saucedo8"] == "Homemade"]
canned = data[data["cranberry saucedo8"] == "Canned"]
a=homemade["income"].mean()
b=canned["income"].mean()
import matplotlib.pyplot as plt
plt.bar(['Homemade','Canned'],[a,b])
plt.show()


#-------------------------------------------------------------------------------------------------
#  find the average income for people who served each type of cranberry sauce
 #for Thanksgiving (Canned, Homemade, None, etc).
grouped = data.groupby("cranberry saucedo8")
average_income = grouped["cranberry saucedo8"].mean()
print(average_income)

 
#--------------------------------------------------------------------------------------------    
 #Plotting the results of aggregation
import matplotlib.pyplot as plt
import numpy as np
average_income = grouped["income"].mean()
average_income.plot.bar()
plt.show()

 
#------------------------------------------------------------------------------------------------   
#Do people in Suburban areas eat more Tofurkey than people in Rural areas?
grouped = data.groupby("How would you describe where you live?")["What is typically the main dish at your Thanksgiving dinner?"]
grouped.apply(lambda x:x.value_counts())

#----------------------------------------------------------------------------------
#Where do people go to Black Friday sales most often?
sales= data[(data["Will you shop any Black Friday sales on Thanksgiving Day? "]=='Yes')]
sales['US Region'].value_counts()

    
#---------------------------------------------------------------------------------------------------------
#Is there a correlation between praying on Thanksgiving and income?
     



#------------------------------------------------------------------------------
#What income groups are most likely to have homemade cranberry sauce?

"""
    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
"""
#-------------------------------------------------------------------------------        
#Find the number of people who live in each area type (Rural, Suburban, etc)
#who eat different kinds of main dishes for Thanksgiving:
grouped = data.groupby("How would you describe where you live?")["main dish4"]
grouped.apply(lambda x:x.value_counts())   



    
    
    
    
    
    
    