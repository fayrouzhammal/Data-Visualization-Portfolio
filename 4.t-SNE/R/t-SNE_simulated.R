library(Rtsne)

# Simulate data
set.seed(0)
n.clusters <- 20
samples.per.cluster <- 50
n.samples <- n.clusters * samples.per.cluster
n.genes <- 10000
data <- matrix(rnorm(n.samples * n.genes), n.samples, n.genes)
for (i in 1:n.clusters) {
  data[((i-1)*samples.per.cluster+1):(i*samples.per.cluster), ] <- data[((i-1)*samples.per.cluster+1):(i*samples.per.cluster), ] + (i*5)
}

# t-SNE
embedding <- Rtsne(data)$Y

# Plot
pdf('tSNE_Simulated_Data_R.pdf')
plot(embedding, col=rep(1:n.clusters, each=samples.per.cluster), main='t-SNE of Simulated Data')
dev.off()
