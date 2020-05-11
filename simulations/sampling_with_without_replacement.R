
x = runif(100, -1, 1)
hist(x)

with_replacement = replicate(1000, mean(sample(x, 100, replace = T)))
without_replacement = replicate(1000, mean(sample(x, 100, replace = F)))


plot(density(sample_without_replacement), col="red")
lines(density(sample_with_replacement), col="blue")
