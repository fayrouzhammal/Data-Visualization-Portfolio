import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Simulate data
np.random.seed(0)
n_clusters = 20
samples_per_cluster = 50
n_samples = n_clusters * samples_per_cluster
n_genes = 10000
data = np.random.randn(n_samples, n_genes)
for i in range(n_clusters):
    data[i*samples_per_cluster: (i+1)*samples_per_cluster, :] += (i*5)

# t-SNE
embedding = TSNE(n_components=2).fit_transform(data)

# Plot
plt.scatter(embedding[:, 0], embedding[:, 1], c=np.repeat(range(n_clusters), samples_per_cluster))
plt.title('t-SNE of Simulated Data')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.colorbar().set_label('Cluster')
plt.savefig('tSNE_Simulated_Data_Python.pdf')
plt.show()
