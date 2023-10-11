# Load necessary libraries
#install.packages("umap")
#install.packages("ggplot2")
setwd("C:/Users/hamma/OneDrive/Documents/Portfolio/Data-Visualization-Portfolio/3.UMAP/R")

library(umap)
library(ggplot2)

# Load the iris dataset
data(iris)

# Extract numerical data
iris_data <- iris[, 1:4]

# Apply UMAP
set.seed(123) # for reproducibility
umap_results <- umap(iris_data)

# Convert the results to a data frame for visualization
umap_df <- as.data.frame(umap_results$layout)
colnames(umap_df) <- c("UMAP1", "UMAP2")
umap_df$Species <- iris$Species

# Plot the UMAP results using ggplot2
p <- ggplot(umap_df, aes(x = UMAP1, y = UMAP2, color = Species)) +
  geom_point(size = 3, alpha = 0.8) +
  theme_minimal() +
  labs(title = "UMAP on Iris Dataset") +
  scale_color_discrete(name = 'Species')

# Save the plot as a PDF
ggsave(filename = "UMAP_Iris.pdf", plot = p, device = "pdf", width = 8, height = 6)

