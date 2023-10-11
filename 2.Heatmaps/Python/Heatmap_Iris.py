import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset('iris')

iris_pivot = iris.pivot_table(index='species', columns='sepal_width', values='sepal_length', aggfunc='mean')

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(iris_pivot, cmap='YlGnBu', annot=True)  # 'annot=True' will display the values in each cell
plt.title('Heatmap of Sepal Length by Species and Sepal Width')

# Save the plot
plt.savefig("Heatmap_Iris.pdf")
plt.show()
