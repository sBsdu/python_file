v<-c(7,18,12,3,21)
t<-c(8,16,5,14,23)
plot(v,type='o',col="green", xlab = "Month1", ylab = "Rain fall1")
lines(t,type="o",col="blue", xlab = "Month2", ylab = "Rain fall2")
plot()

#SCATTER PLOT
v<-c(7,18,12,3,21)
t<-c(8,16,5,14,23)
plot(v,t,xlab = "Month1", ylab = "Rain fall1",type="o")



input<-mtcars[,c("wt","mpg")]

plot(x=input$wt,y=input$mpg,xlab="weight",ylab="mileage",xlim=12)
pairs(~wt+mpg+disp+cyl,data=mtcars,main="Scatterplot Matrix")
boxplot(mpg~cyl,data=mtcars,xlab="number of cylinders",ylab="miles per gallon",main="Graph")
