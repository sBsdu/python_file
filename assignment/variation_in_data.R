#invartion in data

#Range:->R=max(x1,x2,x3,x4,.....xn)-min(x1,x2,x3,x4......xn)
  
  
time = c(32,35,44,45,55,74,74,65,56.55,54,44,44,44,4,56,32,14,88,44)
max(time)-min(time))
range(time)
time.na = NA,NA

#//----------------------------------------

#interquartle Range:->diff betweemn first 2 third quartiles 
IQR = Q3-Q2=50%

#IQR(x)
IQR(time)
IQR(time,na.rm = TRUE)

#//-------------------------------------------------------
# Quintile division half of diff. between third and  first quartiles
Q=1/2(Q3-Q2)

#IQR(time)/2


#//------------------------------------------------------
#absolute deviation

D(A)=1/sumation(xi-A)
#mean data (A=xbar)
#absolute mean deviation data 

#//-------------------------------------------------

time = c(32,35,44,45,55,74,74,65,56.55,54,44,44,44,4,56,32,14,88,44)
A= 10
mean(abs(time-A))

# for missing value
mean(abs(time-A)),na.rm = TRUE


#//---------------------------------
#absolute mediean deviation
# a is not given 
#calculate mediean
median(time)
mean(abs(time-median(time)))

#//----------------------
#grouped data
breaks = seq(30,90,by = 10)
print(breaks)
time.cut = cut(time, breaks,right=FALSE)
table(time.cut)
f=as.numeric(table(time.cut))
print(f)

#grouped data
a=10
sum(f*abs(time-A))/sum(f)

#//-------------------------------------------------------
#variance
sd(time)
var(time)
sqrt(var(time))
#----------------------------
timemean = sum(f*time)/sum(f)
print(timemean)
sqrt(sum(f*(time-mean(time)))^2/sum(f))








