import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cluster_species(input_path, output_path, n_clusters=5):
    """
    Cluster any species into groups based on latitude and longitude.
    """

    # Load cleaned dataset
    data = pd.read_csv(input_path)

    # Coordinates
    coords = data[["latitude", "longitude"]]

    # Normalize coordinates
    scaler = StandardScaler()
    coords_scaled = scaler.fit_transform(coords)

    # KMeans clustering
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    data["group"] = kmeans.fit_predict(coords_scaled)

    # Save clustered dataset
    data.to_csv(output_path, index=False)

    print(f"✅ Clustered dataset saved at: {output_path}")

    return data


# ---------------------------------------------------
# Example Usage
# ---------------------------------------------------
if __name__ == "__main__":

    cluster_species(
        "data/processed/general_cleaned.csv",
        "data/processed/general_clustered.csv"
    )
    # cluster_species(
    #     "data/processed/barheadedgoose_cleaned.csv",
    #     "data/processed/barheadedgoose_clustered.csv"
    # )
    # cluster_species(
    #     "data/processed/saruscrane_cleaned.csv",
    #     "data/processed/saruscrane_clustered.csv"
    # )
    # cluster_species(
    #     "data/processed/steppeeagle_cleaned.csv",
    #     "data/processed/steppeeagle_clustered.csv"
    # )