new_data<-data.frame(
  emp_id=c(1:5),
  emp_name<-c('ria','sapna','dushyant','ayush','ritu'),
  emp_sal<-c(77000,67000,75000,23000,54000),
  start_data<-as.Date(c('2012-01-01','2013-03-21','2015-11-11','2012-09-01','2012-07-01')),
  stringsAsFactors = FALSE
)
print(new_data)
print(str(new_data))
print(summary(new_data))
result<-new_data[1:2,]
print(result)