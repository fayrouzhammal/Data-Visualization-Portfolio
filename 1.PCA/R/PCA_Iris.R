# Loading necessary libraries
#install.packages(c("ggplot2", "rgl"))


library(ggplot2)
library(rgl)

# Load iris dataset
data(iris)

# Standardizing the data (important for PCA)
iris.scaled <- scale(iris[, -5])  # Exclude the species column

# Perform PCA
pca.result <- prcomp(iris.scaled)

# Plot 2D PCA
pca.data <- as.data.frame(pca.result$x)
pdf("2D_PCA_plot_Iris.pdf", width = 8, height = 6)
ggplot(pca.data, aes(x = PC1, y = PC2, color = iris$Species)) +
  geom_point(aes(shape = iris$Species), size = 3) +
  theme_minimal() +
  ggtitle("2D PCA on iris dataset") +
  labs(x = paste("PC1: ", round(pca.result$sdev[1] * 100 / sum(pca.result$sdev), 2), "% variance"),
       y = paste("PC2: ", round(pca.result$sdev[2] * 100 / sum(pca.result$sdev), 2), "% variance")) +
  scale_color_discrete(name = 'Species') +
  scale_shape_discrete(name = 'Species')
dev.off()

# Plot 3D PCA
open3d()  # open new rgl device
plot3d(pca.data$PC1, pca.data$PC2, pca.data$PC3, col = as.numeric(iris$Species), size = 3,
       xlab = paste("PC1: ", round(pca.result$sdev[1] * 100 / sum(pca.result$sdev), 2), "% variance"),
       ylab = paste("PC2: ", round(pca.result$sdev[2] * 100 / sum(pca.result$sdev), 2), "% variance"),
       zlab = paste("PC3: ", round(pca.result$sdev[3] * 100 / sum(pca.result$sdev), 2), "% variance"))

# Save the current 3D rgl plot view to PDF
rgl.postscript("3D_PCA_plot_Iris.pdf", fmt = "pdf")
close3d()

