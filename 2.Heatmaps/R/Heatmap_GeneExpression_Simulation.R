#install.packages("pheatmap")
library(pheatmap)

set.seed(42)  # for reproducibility

# Simulate the data
genes <- paste0("Gene_", 1:600)
diseases <- paste0("Disease_", 1:100)

# Generating data with some clusters
data <- matrix(runif(600 * 100) * 100, nrow = 600)

# Create clusters by adding fixed offsets to different data portions for high expression
data[1:150, 1:25] <- data[1:150, 1:25] + 200
data[151:300, 26:50] <- data[151:300, 26:50] + 200

# Create clusters by subtracting fixed offsets for low expression
data[301:450, 51:75] <- data[301:450, 51:75] - 100
data[451:600, 76:100] <- data[451:600, 76:100] - 100

# Compute the log of the values
log_data <- log(data + 101)

# Generate the heatmap with clustering
pdf("Heatmap_GeneExpression_Simulation_R.pdf", width=20, height=20)
pheatmap(log_data, clustering_distance_rows="euclidean", clustering_distance_cols="euclidean", clustering_method="average", main="Gene Expression Heatmap", col=colorRampPalette(c("blue", "white", "red"))(100))
dev.off()
