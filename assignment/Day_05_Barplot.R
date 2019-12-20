# Create data for the graph
x <- c(21,62,10,53)
lbl <- c("London","New YOrk", "Singapore", "Mumbai")

# Give the chart file name
png(file="city_bar.jpg")

# Plot the chart
barplot(x)

# Save the file
dev.off()