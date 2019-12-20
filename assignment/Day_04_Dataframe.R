# Create the dataframe
emp.data = data.frame(
  emp_id = c(1:5),
  emp_name = c('Rick', 'Dan', 'Michelle', 'Ryan', 'Gary'),
  salary = c(623.3, 515.2,611.0,729.0,843.25),
  start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11", "2015-03-27")),
  stringAsFactors = FALSE
)

# Print the data frame
print(emp.data)
str(emp.data)
print(summary(emp.data))

result <- data.frame(emp.data$emp_name,emp.data$salary)
print(result)

# Extract first two rows
result <- emp.data[1:2,]
print(result)

# Add the "dept" column
emp.data$dept <- c("IT", "ML", "AI", "CC", "ITC")
v<-emp.data
print(v)


# Create the second data frame
emp.newdata <- data.frame(
  emp_id = c(6:8),
  emp_name = c("Rasmi", "Pranab", "Tusar"),
  salary = c(578.0,722.5,632.8),
  start_date = as.Date(c("2012-05-21","2013-07-30","2014-06-17")),
  dept = c("IT", "Operation", "Finance"),
  stringAsFactors = FALSE
)

# Bind two columns
emp.finaldata <- rbind(emp.data,emp.newdata)
print(emp.finaldata)


# Create vector object
city = c("Tampa", "Seattle", "Martford", "Denver")
state = c("FL", "WA", "CT", "CO")
zipcode = c(33602, 98104, 06161, 80294)

# Combine above three vectors into one data frame
addresses = cbind(city,state,zipcode)

# Print a header
cat("# # # # The First data frame\n")

# Print the data frame
print(addresses)

# Create another dataframe with similar columns
new.address = data.frame(
  city = c("Lowry","Charlotte"),
  state = c("CO","FL"),
  zipcode = c("80230","33949"),
  stringsAsFactors = FALSE
)

data.address <- rbind(addresses,new.address)
print(data.address)
