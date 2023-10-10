import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Generate a synthetic gene expression dataset
np.random.seed(0)
genes = [f'Gene_{i}' for i in range(1, 10001)]  # 10,000 genes
samples = [f'Sample_{i}' for i in range(1, 1001)]  # 1,000 samples

# Create a random expression matrix (1,000 samples x 10,000 genes)
expression_data = np.random.rand(1000, 10000)

# Simulate subtle differential expression with more noise for samples treated with DMSO
expression_data[334:667, 5000:7500] += np.random.normal(0.3, 2, size=(333, 2500))

# Simulate subtle differential expression with more noise for samples treated with DMSO + Hypoxanthine
expression_data[667:, 7500:] += np.random.normal(0.3, 1.5, size=(333, 2500))

# Convert the numpy array to a pandas DataFrame
df = pd.DataFrame(expression_data, columns=genes, index=samples)

# Standardize the data
x = StandardScaler().fit_transform(df.values)

# PCA transformation
pca = PCA(n_components=3)
principalComponents = pca.fit_transform(x)

# Convert PCA components to a DataFrame
principalDf = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2', 'PC3'])

# Label the samples based on treatment for visualization
labels = ['Control'] * 334 + ['Treated with DMSO'] * 333 + ['Treated with DMSO + Hypoxanthine'] * 333
principalDf['label'] = labels

# 3D Plot
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

colors = {'Control': 'r', 'Treated with DMSO': 'g', 'Treated with DMSO + Hypoxanthine': 'b'}

for label, color in colors.items():
    idx = principalDf['label'] == label
    ax.scatter(principalDf.loc[idx, 'PC1'], principalDf.loc[idx, 'PC2'], principalDf.loc[idx, 'PC3'], c=color, s=50, label=label, alpha=0.5)

ax.set_xlabel('Principal Component 1 - {0}%'.format(np.round(pca.explained_variance_ratio_[0]*100, 2)))
ax.set_ylabel('Principal Component 2 - {0}%'.format(np.round(pca.explained_variance_ratio_[1]*100, 2)))
ax.set_zlabel('Principal Component 3 - {0}%'.format(np.round(pca.explained_variance_ratio_[2]*100, 2)))
ax.set_title('PCA of Synthetic Gene Expression Data')
ax.legend()

# Save the figure as a high-quality PDF
plt.savefig('PCA_GeneExpression_Simulation.pdf', format='pdf', dpi=300)

plt.show()
