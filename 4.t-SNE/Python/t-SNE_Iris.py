import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris

# Load Iris data
data, labels = load_iris(return_X_y=True)

# t-SNE
embedding = TSNE(n_components=2).fit_transform(data)

# Plot
plt.scatter(embedding[:, 0], embedding[:, 1], c=labels)
plt.title('t-SNE of Iris Dataset')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.colorbar(ticks=range(3)).set_label('Species')
plt.savefig('tSNE_Iris_Python.pdf')
plt.show()
