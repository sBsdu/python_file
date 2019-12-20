data<-read.csv("C:\\Users\\Om\\Desktop\\Statistics with R-MAI1303-S-2019-20\\student.xlsx",sheet-Index=1)
print(data)

sal <- max(data$Salary)
print(sal)

fetch <- subset(data, Department == "ML")
print(fetch)

info <- subset(data, Salary > "77000" & Department == "ML")
print(info)


