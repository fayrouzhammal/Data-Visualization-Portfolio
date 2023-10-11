# Loading necessary libraries
#install.packages(c("umap", "ggplot2"))
setwd("C:/Users/hamma/OneDrive/Documents/Portfolio/Data-Visualization-Portfolio/3.UMAP/R")
library(umap)
library(ggplot2)

# Setting the seed for reproducibility
set.seed(123)

# Parameters for the simulation
n_genes <- 10000
n_samples <- 1000
n_clusters <- 20
samples_per_cluster <- n_samples / n_clusters

# Distinct means and standard deviations for each cluster
cluster_means <- seq(-2, 2, length.out = n_clusters)
cluster_sds <- seq(1, 3, length.out = n_clusters)  # Increased range for standard deviations

# Simulating the base data
data <- matrix(rnorm(n_genes * n_samples), n_genes, n_samples)

# Introducing variations for each cluster
for (cluster in 1:n_clusters) {
  selected_samples <- ((cluster - 1) * samples_per_cluster + 1):(cluster * samples_per_cluster)
  selected_genes <- sample(1:n_genes, 500) # Number of genes to modulate
  
  # Add variations using distinct means and standard deviations
  data[selected_genes, selected_samples] <- data[selected_genes, selected_samples] + 
    matrix(rnorm(500 * samples_per_cluster, mean = cluster_means[cluster], sd = cluster_sds[cluster]), 500, samples_per_cluster)
}

# Sample labels (cancer types)
cancer_types <- c("Leukemia", "Lymphoma", "Melanoma", "Breast", "Ovarian", "Lung", "Colon", 
                  "Prostate", "Pancreatic", "Liver", "Stomach", "Cervical", "Bladder", 
                  "Thyroid", "Kidney", "Brain", "Esophageal", "Bone", "Sarcoma", "Myeloma")

labels <- rep(cancer_types, each=samples_per_cluster)

# Performing UMAP
umap_result <- umap(t(data))

# Preparing data for plotting
plot_data <- data.frame(X = umap_result$layout[,1], Y = umap_result$layout[,2], Cluster = labels)

# Plotting UMAP and saving to PDF
pdf("UMAP_Simulated_Cancer_Data.pdf", width=10, height=8)
ggplot(plot_data, aes(x = X, y = Y, color = Cluster)) +
  geom_point(alpha = 0.7, size = 2) +
  theme_minimal() +
  ggtitle("UMAP of Simulated Cancer Gene Expression Data with Increased SDs") +
  labs(color = 'Cancer Type') +
  theme(legend.position="bottom")
dev.off()
