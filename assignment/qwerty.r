x<-readline(prompt = "enter number>")
x<-as.integer(x)
factorial=1
for(i in 1:x) {
  factorial = factorial * i
  
}
print(factorial)