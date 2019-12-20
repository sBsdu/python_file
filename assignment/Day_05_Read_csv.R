data <- read.csv("C:\\Users\\dell\\Desktop\\New\\3rd Semester\\R Language\\Day_05\\New.csv")
# data <- read.xlsx("PATH",shut-index=1)
print(data)

print(ncol(data))
print(nrow(data))
print(max(data[3]))

x <- subset(data, Dept=="ML&AI")
print(x)

y <- subset(data, Name=="Lavish Sharma")
print(y)

z <- subset(data, Dept=="IT" & Salary>=50000)
print(z)