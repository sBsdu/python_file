

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Titanic
  Filename: 
      titanic.py
  Dataset:
      training_titanic.csv
  Data Description:      
      survival: Survival (0 = No; 1 = Yes)
      pclass: Passenger Class (1 = Upper; 2 = Middle; 3 = Lower)
      name: Name
      sex: Sex
      age: Age 
      sibsp: Number of Siblings/Spouses Aboard
      parch: Number of Parents/Children Aboard
      ticket: Ticket Number
      fare: Passenger Fare
      cabin: Cabin
      embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

  Problem Statement:
      Titanic ship that crashed in April, 1912.
      Real-world data containing the details of titanic ships passengers list.
      There were lifeboats for only 1178 people
      There were 2224 passengers on board
      Answer the Following:
      0. Total number of Passengers in the dataset
      0. Find all large families (Sibsp > 3)
      0. Find all the features which has missing
      0. Drop the column which has the max missing
      0. Embarked Feature missing values needs to be fixed
      0. Age missing value needs to be fixed
      1. How many people survived the disaster ?
      2. How many people died the disaster ?
      3. Plot the people who survived Vs died appropriately.
      4. Calculate and print the survival rates as proportions (percentage) 
      5. Which gender have greater survival rate ?
         Were females given high priority while rescue.
         Males that survived vs males that passed away
         Females that survived vs Females that passed away
         Also plot it
      6. Does age play a role for survival?
         Since it's probable that children were saved first.
  
  Advanced Problem Statements:
     7. Does Pclass feature plays role in survival
         Survived Vs Died according to Pclass and sex
         Plot it (FactorPlot and CrossTab)
      8. Who was the oldest person survived 
      9. Yougest person survived
      10. Is there a relationship between Pclass and the survival 
          Draw violen plots PClass and Age Vs Survived 
          Sex and Age Vs Survived 
      11. Find the title from the name and show its value counts
          train['title'] = train.Name.str.extract('\, ([A-Z][^ ]*\.)',expand=False)
      12. If a passanger is alone in ship with no siblings, survival rate is 
          If I have a family onboard, I will save them instead of saving myself.
          But there’s something wrong, the survival rate for families 
          with 5–8 members is 0%. Is this because of PClass? Yes this is PClass,
          large families in Pclass3(>3) died.
      13. Everything except ‘PassengerId’, ‘Ticket’ and ‘Name’ would be 
          correlated with a high survival rate
      14. Do Not Delete the Cabin Column, but recreate using Deck
      
      
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
 
     You can test this by creating a new column with a Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.

      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
      
"""

import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Data_Analytics\\training_titanic.csv")
print(df)

#0. Total number of Passengers in the dataset
print(df['Pclass'].count())

#0. Find all large families (Sibsp > 3)
df['SibSp'] > 3
df_sub= df[(df['SibSp'] > 3) ]
print(df_sub)

#0. Find all the features which has missing
col=df.columns 
for i in col:
    print(df[df[i].isnull()])


#0. Drop the column which has the max missing

col=df.columns 
for i in col:
    df=(df[df[i].isnull()])
    print(i,df_.dropna())

   
#0. Embarked Feature missing values needs to be fixed
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].count())
print(df['Embarked'].count())
df_rank=df.groupby(['Embarked'])
print(df_rank.groups)

#0. Age missing value needs to be fixed


#1. How many people survived the disaster ?
len(df[df['Survived']==1])

#2. How many people died the disaster ?
len(df[df['Survived']==0])  

#3. Plot the people who survived Vs died appropriately.
import pandas as pd 
import matplotlib.pyplot as plt    
data=df.groupby(['Survived','died']).count()
plt.xticks([1,0],("male Survived","female died"))
plt.bar(len(df[df['Survived']==1]),len(df[df['Survived']==0]))
      
#4. Calculate and print the survival rates as proportions (percentage) 


# 5. Which gender have greater survival rate ?
import pandas as pd 
import matplotlib.pyplot as plt    
data=df.groupby(['Sex','Survived']).count()
plt.xticks([0,1],("male Survived","female Survived"))
plt.bar([0,1],[data.loc[('male'),0][1],data.loc[('female'),1][2]],color=("red","green"))



#Were females given high priority while rescue.
#Males that survived vs males that passed away 
import pandas as pd 
import matplotlib.pyplot as plt    
data=df.groupby(['Sex','Survived']).count()
plt.xticks([0,1],("male Survived","male died"))
plt.bar([0,1],[data.loc[('male'),0][1],data.loc[('male'),1][2]],color=("red","green"))



#Females that survived vs Females that passed away Also plot it
import pandas as pd 
import matplotlib.pyplot as plt    
data=df.groupby(['Sex','Survived']).count()
plt.xticks([0,1],("female Survived","female died"))
plt.bar([0,1],[data.loc[('female'),0][1],data.loc[('female'),1][2]],color=("red","green"))


#6. Does age play a role for survival?
#Since it's probable that children were saved first.
import pandas as pd 
import matplotlib.pyplot as plt 
data=df.groupby(['Age']).count()
print(data)


a = df[(df['Age']>18) & (df['Survived']==1)]

df[df]

df[df['Age']<18]















