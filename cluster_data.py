import pandas as pd
from models.clustering import cluster_elephants

# Load cleaned dataset
data = pd.read_csv("data/processed/elephant_cleaned.csv")

# Apply clustering
clustered = cluster_elephants(data, n_clusters=4)

# Save result
clustered.to_csv("data/processed/elephant_clustered.csv", index=False)

print("Clustering complete!")