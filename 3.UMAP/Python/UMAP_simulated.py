import numpy as np
import umap
import matplotlib.pyplot as plt

# Setting the seed for reproducibility
np.random.seed(123)

# Parameters for the simulation
n_genes = 10000
n_samples = 1000
n_clusters = 20
samples_per_cluster = n_samples // n_clusters

# Distinct means and standard deviations for each cluster
cluster_means = np.linspace(-2, 2, n_clusters)
cluster_sds = np.linspace(-30000000, 30000000, n_clusters)

# Simulating the base data
data = np.random.randn(n_genes, n_samples)

# Introducing variations for each cluster
for cluster in range(n_clusters):
    selected_samples = list(range(cluster * samples_per_cluster, (cluster + 1) * samples_per_cluster))
    selected_genes = np.random.choice(n_genes, 500, replace=False)
    
    # Add variations using distinct means and standard deviations
    data[selected_genes[:, None], selected_samples] += np.random.randn(500, samples_per_cluster) * cluster_sds[cluster] + cluster_means[cluster]

# Compute individual mean and SD for each sample and then normalize the data
sample_means = np.mean(data, axis=0)
sample_sds = np.std(data, axis=0)
data_normalized = (data - sample_means) / sample_sds

# Sample labels (cancer types)
cancer_types = ["Leukemia", "Lymphoma", "Melanoma", "Breast", "Ovarian", "Lung", "Colon", 
                "Prostate", "Pancreatic", "Liver", "Stomach", "Cervical", "Bladder", 
                "Thyroid", "Kidney", "Brain", "Esophageal", "Bone", "Sarcoma", "Myeloma"]

labels = np.array(cancer_types * samples_per_cluster)

# Performing UMAP on normalized data
reducer = umap.UMAP()
embedding = reducer.fit_transform(data_normalized.T)

# Plotting
plt.figure(figsize=(10, 8))
for i, cancer_type in enumerate(cancer_types):
    idx = labels == cancer_type
    plt.scatter(embedding[idx, 0], embedding[idx, 1], label=cancer_type)

plt.title("UMAP of Normalized Simulated Cancer Gene Expression Data with Increased SDs")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("UMAP_Normalized_Simulated_Cancer_Data.pdf")
plt.show()
