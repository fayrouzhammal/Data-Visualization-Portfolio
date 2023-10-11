import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

np.random.seed(42)
genes = 10000
samples_per_condition = 50

# Simulating base gene expression values
healthy = np.random.normal(0, 1, (samples_per_condition, genes))

# No change for the majority of genes
disease = np.random.normal(0, 1, (samples_per_condition, genes))

# Introduce upregulation for a subset of genes
upregulated_genes = 1000
disease[:, :upregulated_genes] = np.random.normal(0.5, 1, (samples_per_condition, upregulated_genes))

# Introduce downregulation for another subset of genes
downregulated_genes = 1000
disease[:, upregulated_genes:upregulated_genes+downregulated_genes] = np.random.normal(-0.5, 1, (samples_per_condition, downregulated_genes))

p_values = []
fold_changes = []

for i in range(genes):
    _, p_val = ttest_ind(healthy[:, i], disease[:, i])
    p_values.append(p_val)
    
    fold_change = np.mean(disease[:, i]) / (np.mean(healthy[:, i]) + 1e-7)  # Added small constant to avoid division by zero
    fold_changes.append(fold_change)

plt.figure(figsize=(10,6))
plt.scatter(np.log2(fold_changes), -np.log10(p_values), s=5)
plt.axhline(y=-np.log10(0.05), color='r', linestyle='--')
plt.title('Volcano plot - Refined Simulated Gene Expression Data')
plt.xlabel('Log2 Fold Change')
plt.ylabel('-log10(p-value)')
plt.savefig("gene_expression_volcano_plot.pdf", format="pdf")
plt.show()
