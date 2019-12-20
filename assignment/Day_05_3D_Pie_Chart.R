# Create data for the graph
x <- c(21,62,10,53)
lbl <- c("London","New YOrk", "Singapore", "Mumbai")

# Give the chart file name
png(file="city_3d_pie.jpg")

# Plot the chart
pie3D(x,labels=lbl, col=rainbow(length(x)), explode=0.1)

# Save the file
dev.off()