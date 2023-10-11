# Loading necessary libraries
#install.packages(c("ggplot2", "rgl", "MASS"))
setwd("C:/Users/hamma/OneDrive/Documents/Portfolio/Data-Visualization-Portfolio/1.PCA/R")

library(ggplot2)
library(rgl)
library(MASS)  # for mvrnorm

# Simulate gene expression data
set.seed(123)  # For reproducibility
n_genes <- 10000
n_samples <- 1000
n_groups <- 4  # Simulating four distinct groups of samples

# Create a base expression matrix
base_expr <- matrix(rnorm(n_genes * n_samples, mean = 0, sd = 1), n_genes, n_samples)

# Introduce group-specific expression patterns
for (group in 1:n_groups) {
  samples_in_group <- ((group - 1) * n_samples / n_groups + 1):(group * n_samples / n_groups)
  genes_overexpressed <- ((group - 1) * n_genes / n_groups + 1):(group * n_genes / n_groups)
  
  base_expr[genes_overexpressed, samples_in_group] <- base_expr[genes_overexpressed, samples_in_group] + 3
}

# Add labels for each sample
sample_labels <- rep(1:n_groups, each = n_samples/n_groups)


# Perform PCA
expr.scaled <- t(scale(t(base_expr)))  # Scaling genes (rows), not samples (columns)
pca.result <- prcomp(expr.scaled, center = FALSE, scale. = FALSE)

# Extract principal components
pca.data <- as.data.frame(pca.result$x)
pca.data$sample_labels <- as.factor(sample_labels)

# Save 2D PCA to PDF
pdf("2D_PCA_plot_Sim.pdf", width = 8, height = 6)
ggplot(pca.data, aes(x = PC1, y = PC2, color = sample_labels)) +
  geom_point(size = 2, alpha = 0.7) +
  theme_minimal() +
  ggtitle("2D PCA on simulated gene expression data") +
  labs(x = paste("PC1: ", round(pca.result$sdev[1] * 100 / sum(pca.result$sdev), 2), "% variance"),
       y = paste("PC2: ", round(pca.result$sdev[2] * 100 / sum(pca.result$sdev), 2), "% variance")) +
  scale_color_discrete(name = 'Sample Group')
dev.off()

# Plot 3D PCA
open3d()  # open new rgl device
plot3d(pca.data$PC1, pca.data$PC2, pca.data$PC3, col = as.numeric(pca.data$sample_labels), size = 3,
       xlab = paste("PC1: ", round(pca.result$sdev[1] * 100 / sum(pca.result$sdev), 2), "% variance"),
       ylab = paste("PC2: ", round(pca.result$sdev[2] * 100 / sum(pca.result$sdev), 2), "% variance"),
       zlab = paste("PC3: ", round(pca.result$sdev[3] * 100 / sum(pca.result$sdev), 2), "% variance"))

# Save the current 3D rgl plot view to PDF
rgl.postscript("3D_PCA_plot_Sim.pdf", fmt = "pdf")
close3d()
