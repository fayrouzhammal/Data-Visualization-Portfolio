# Importing necessary libraries
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Loading the iris dataset
data = load_iris()
# Creating a DataFrame from the dataset
df = pd.DataFrame(data.data, columns=data.feature_names)
# Adding the target labels to the DataFrame
df['species'] = data.target

# Excluding the 'species' column to separate out features
features = df.columns[:-1]
# Extracting the feature values from the DataFrame
x = df.loc[:, features].values
# Standardizing the feature values to have mean=0 and variance=1
x = StandardScaler().fit_transform(x)

# Initializing PCA with 2 components
pca = PCA(n_components=2)
# Applying PCA on the standardized data
principalComponents = pca.fit_transform(x)
# Storing the principal components in a DataFrame
principalDf = pd.DataFrame(data=principalComponents, columns=['PC1', 'PC2'])
# Combining the principal components with species column for plotting
finalDf = pd.concat([principalDf, df[['species']]], axis=1)

# Plotting the 2D PCA
fig, ax = plt.subplots()
colors = ['r', 'g', 'b']
targets = [0, 1, 2]
# Plotting data points of each species with a unique color
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['species'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'PC1'], 
               finalDf.loc[indicesToKeep, 'PC2'], 
               c=color, 
               s=50)
# Adding legend, grid, title, and axis labels
ax.legend(data.target_names)
ax.grid()
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("2D PCA of Iris Dataset")

# Save the plot as a high-quality PDF
fig.savefig("PCA_Iris.pdf", format="pdf", dpi=300)

# Display the plot
plt.show()
