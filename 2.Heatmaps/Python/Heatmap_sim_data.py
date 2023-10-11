import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Simulate the data
np.random.seed(42)  # for reproducibility
genes = [f"Gene_{i}" for i in range(1, 601)]
diseases = [f"Disease_{i}" for i in range(1, 101)]

# Generating data with some clusters by manipulating random expression values
data = np.random.rand(600, 100) * 100

# Create clusters by adding fixed offsets to different data portions for high expression (reds)
data[:150, :25] += 200
data[150:300, 25:50] += 200

# Create clusters by subtracting fixed offsets for low expression (blues)
data[300:450, 50:75] -= 100
data[450:, 75:] -= 100

# Convert to a DataFrame for easier handling
df = pd.DataFrame(data, index=genes, columns=diseases)

# Compute the log of the FPKM values
df_log = np.log(df + 101)  # Adding 101 to make sure all values are positive after subtraction

# Calculate vmin and vmax for the color range
vmax = df_log.values.max()
vmin = df_log.values.min()

# Generate the heatmap with clustering
clustergrid = sns.clustermap(df_log, method='average', cmap='RdBu_r', figsize=(20, 20), col_cluster=True, row_cluster=True, center=df_log.mean().mean(), vmin=vmin, vmax=vmax)

# Add title
plt.title("Gene Expression Heatmap")
plt.xlabel("Diseases")
plt.ylabel("Genes")

# Save the plot to PDF
clustergrid.savefig("Heatmap_GeneExpression_Simulation.pdf")
