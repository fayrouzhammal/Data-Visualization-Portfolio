library(Rtsne)

# Remove duplicates
iris_unique <- unique(iris[, 1:4])

# t-SNE
embedding <- Rtsne(iris_unique)$Y

# Since we've removed some rows, we need to adjust the color vector too
unique_species <- iris$Species[!duplicated(iris[, 1:4])]

# Plot
pdf('tSNE_Iris_R.pdf')
plot(embedding, col=unique_species, main='t-SNE of Iris Dataset')
dev.off()

