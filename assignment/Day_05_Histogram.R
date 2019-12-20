# Create data for the graph
x <- c(21,6,1,53)
lbl <- c("London","New YOrk", "Singapore", "Mumbai")

# Give the chart file name
png(file="city_hist.jpg")

# Plot the chart
hist(x, col="green")

# Save the file
dev.off()