library(ggplot2)
setwd("C:/Users/hamma/OneDrive/Documents/Portfolio/Data-Visualization-Portfolio/5.Volcano_plot/R")
set.seed(42)
genes <- 10000
samples_per_condition <- 50
upregulated_genes <- 1000
downregulated_genes <- 1000

# Simulating base gene expression values
healthy <- matrix(rnorm(samples_per_condition*genes), ncol=genes)
disease <- matrix(rnorm(samples_per_condition*genes), ncol=genes)

# Introduce upregulation
disease[, 1:upregulated_genes] <- matrix(rnorm(samples_per_condition*upregulated_genes, mean=0.5), ncol=upregulated_genes)

# Introduce downregulation
disease[, (upregulated_genes+1):(upregulated_genes+downregulated_genes)] <- matrix(rnorm(samples_per_condition*downregulated_genes, mean=-0.5), ncol=downregulated_genes)

p_values <- sapply(1:genes, function(i) t.test(healthy[,i], disease[,i])$p.value)
fold_changes <- apply(disease, 2, mean) / (apply(healthy, 2, mean) + 1e-7)  # Added small constant to avoid division by zero

df <- data.frame(log2FoldChange=log2(fold_changes), neg_log10PValue=-log10(p_values))
ggplot(df, aes(x=log2FoldChange, y=neg_log10PValue)) + 
  geom_point(size=0.5) + 
  geom_hline(yintercept = -log10(0.05), color="red", linetype="dashed") +
  ggtitle("Volcano plot - Refined Simulated Gene Expression Data") +
  theme_minimal()

pdf("gene_expression_volcano_plot_R.pdf")
print(last_plot())
dev.off()
