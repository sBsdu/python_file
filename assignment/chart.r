x<- c(9,11,15,21,34,21)
label<-c("health","education","polution","cleaness","others","food")
png(file="city.jpg")
pie(x,label,main = "city pie chart", col=rainbow(length(x)))
dev.off()


# 3D Exploded Pie Chart
library(plotrix)
x<- c(9,11,15,21,34,21)
label<-c("health","education","polution","cleaness","others","food")
png(file="city3D.jpg")
pie3D(x,labels=label,explode=0.3,main="city pie char",col=rainbow(length(x)))
dev.off()

x<- c(9,11,15,21,34,21)

barplot(x,main = "city pie chart", col=rainbow(length(x)))


x<- c(9,11,15,21,34,21)

hist(x,main = "city pie chart", col=rainbow(length(x)))

