import umap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
data, labels = load_iris(return_X_y=True)
iris_labels = ["Setosa", "Versicolour", "Virginica"]

# Perform UMAP
reducer = umap.UMAP()
embedding = reducer.fit_transform(data)

# Plotting
plt.figure(figsize=(10, 8))
sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], hue=labels, palette=sns.color_palette("hls", 3), legend='full')

# Labels and legend
plt.title("UMAP of Iris Dataset")
plt.xlabel("UMAP1")
plt.ylabel("UMAP2")
legend_labels = plt.legend().get_texts()
for t, l in zip(legend_labels, iris_labels):
    t.set_text(l)

plt.tight_layout()
plt.savefig("UMAP_Iris.pdf")
plt.show()

