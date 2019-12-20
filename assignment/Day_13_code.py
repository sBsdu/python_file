
#Analysis of Salaries Data ( Hand On Activity )

#1. Which Male and Female Professor has the highest and the lowest salaries
import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Data_Analytics\\Salaries.csv")
df_salary_max= df.groupby('sex')[['salary']].max()
df_salary_min= df.groupby('sex')[['salary']].min()
print(df_salary_max)
print(df_salary_min)

#2. Which Professor takes the highest and lowest salaries.
import pandas as pd
df = pd.read_csv("C:\\Users\\BSDU ADMIN\\Desktop\\Data_Analytics\\Salaries.csv")
df_max= df.groupby('rank').max()
df_min= df.groupby('rank').min()
print(df_max)
print(df_min)
#3. Missing Salaries - should be mean of the matching salaries of those 
#   whose service is the same

df_service = df[('service')]

   
   
#4. Missing phd - should be mean of the matching service 
phd = df['phd'].fillna(round(df['phd'].mean()))
print(phd)

#5. How many are Male Staff and how many are Female Staff. 
df['sex'].value_counts()

#   Show both in numbers and Graphically using Pie Chart.  
import matplotlib.pyplot as plt
labels = ['male', 'female']
colors = ['r', 'g']
plt.pie(df['sex'].value_counts(normalize=True),labels=labels, colors=colors, autopct='%.1f%%')
plt.show()

#   Show both numbers and in percentage
df['sex'].value_counts(normalize = True)


 

#6. How many are Prof, AssocProf and AsstProf. 

df['rank']
df['rank'].value_counts()
#   Show both in numbers adn Graphically using a Pie Chart
import matplotlib.pyplot as plt
labels = ['Prof', 'AssocProf', 'AsstProf']
colors = ['r', 'g','b']
plt.pie(df['rank'].value_counts(normalize=True),labels=labels, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()

#7. Who are the senior and junior most employees in the organization.

df_senior = df[(df['service'] ==df['service'].max())]
print(df_senior)

df_junior = df[(df['service'] ==df['service'].min())]
print(df_junior)

#8. Draw a histogram of the salaries divided into bin starting 
#   from 50K and increment of 15K
import matplotlib.pyplot as plt
x=df['salary']
plt.hist(x,bins=range(50000,200000,15000))
plt.xlabel("salaries")
plt.show()


