x <- c(10,2,15,6,2,54)
label <- c("Lion","Tiger","Zebra","Elephant","Panther","Fox")

pie(x, label)

color <- c("Blue","Green","Red","Brown","Purple","Pink")
pie(x, label, col=color)

pie(x, label, main="Zoo Animals", col=rainbow(length(x)))


# Create data for the graph
x <- c(21,62,10,53)
lbl <- c("London","New YOrk", "Singapore", "Mumbai")

# Give the chart file name
png(file="city.jpg")

# Plot the chart
pie(x,label=lbl, col=rainbow(length(x)), explode=0.1)

# Save the file
dev.off()
