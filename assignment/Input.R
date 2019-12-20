# Take Input From User

name <- readline(prompt = "Enter your name : ")
age <- readline(prompt = "Enter your age : ")
age <- as.integer(age)
# age <- as.integer(readline(prompt = "Enter your age : "))
print(paste("Hi",name,". Your age is:",age))