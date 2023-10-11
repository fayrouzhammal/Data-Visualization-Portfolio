# Load necessary libraries
library(gplots)

# Load the iris dataset
data(iris)

# Remove the Species column to only work with numerical data
iris_numerical <- iris[, -5]

# Scaling the data can provide better visualization in heatmaps
scaled_data <- scale(iris_numerical)

# Create the heatmap and save it to PDF
pdf("Heatmap_Iris.pdf")

heatmap.2(scaled_data, 
          main = "Heatmap of Iris Dataset",
          trace="none",
          margin=c(5,10),
          col = colorRampPalette(c("blue", "white", "red"))(255),
          srtCol = 45, # text angle for columns
          dendrogram = "row", # only row side dendrogram
          scale="none", # data is already scaled
          Rowv = TRUE, # reorder rows
          Colv = FALSE, # don't reorder columns
          key = TRUE, # show color key
          keysize = 1.5, # size of color key
          cexRow = 0.8, # font size for rows
          cexCol = 0.8) # font size for columns

dev.off()
