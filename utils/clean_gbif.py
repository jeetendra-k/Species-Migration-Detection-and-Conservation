import pandas as pd
from pathlib import Path


def clean_gbif_data(input_path, output_path):
    """
    Cleans any GBIF occurrence dataset.

    Parameters:
        input_path (str): Raw GBIF TSV file
        output_path (str): Output cleaned CSV
    """

    # Load GBIF data (tab-separated)
    df = pd.read_csv(input_path, sep="\t", low_memory=False)

    # Required columns
    required = [
        "eventDate",
        "decimalLatitude",
        "decimalLongitude"
    ]

    # Keep only columns that exist
    available = [c for c in required if c in df.columns]
    df = df[available]

    # Remove missing values
    df = df.dropna()

    # Convert date
    df["eventDate"] = pd.to_datetime(
        df["eventDate"],
        errors="coerce"
    )

    df = df.dropna(subset=["eventDate"])

    # Extract year
    df["year"] = df["eventDate"].dt.year

    # Rename columns
    df = df.rename(columns={
        "decimalLatitude": "latitude",
        "decimalLongitude": "longitude"
    })

    # India bounds
    df = df[
        (df["latitude"] >= 8) &
        (df["latitude"] <= 37) &
        (df["longitude"] >= 68) &
        (df["longitude"] <= 97)
    ]

    # Remove duplicate observations
    df = df.drop_duplicates(
        subset=["latitude", "longitude", "year"]
    )

    # ----------------------------
    # Balance samples geographically
    # ----------------------------
    df["lat_bin"] = pd.cut(
        df["latitude"],
        bins=3,
        labels=[0, 1, 2]
    )

    balanced = []

    for b in df["lat_bin"].dropna().unique():

        region = df[df["lat_bin"] == b]

        sample_size = min(len(region), 300)

        balanced.append(
            region.sample(
                sample_size,
                random_state=42
            )
        )

    if balanced:
        df = pd.concat(balanced)

    df = df.drop(columns=["lat_bin"])

    # Sort by year
    df = df.sort_values("year")

    # Save
    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned dataset saved at: {output_path}")


# -------------------------------------------------
# Example Usage
# -------------------------------------------------
if __name__ == "__main__":

    # clean_gbif_data(
    #     "data/raw/gbif_tigers.csv",
    #     "data/processed/tigers_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_asianelephants.csv",
    #     "data/processed/asianelephants_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_barasingha.csv",
    #     "data/processed/barasingha_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_chital.csv",
    #     "data/processed/chital_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_chital.csv",
    #     "data/processed/chital_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_gaur.csv",
    #     "data/processed/gaur_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_goldenjackal.csv",
    #     "data/processed/goldenjackal_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_indianwolf.csv",
    #     "data/processed/indianwolf_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_macaque.csv",
    #     "data/processed/macaque_cleaned.csv"
    # )
    # clean_gbif_data(
    #     "data/raw/gbif_nilgai.csv",
    #     "data/processed/nilgai_cleaned.csv"
    # )

    # Add more species here whenever needed

    # clean_gbif_data(
    #     "data/raw/gbif_tiger.csv",
    #     "data/processed/tiger_cleaned.csv"
    # )

    clean_gbif_data(
         "data/raw/gbif_tigers.csv",
         "data/processed/general_cleaned.csv"
    )
    # clean_gbif_data(
    #      "data/raw/gbif_barheadedgoose.csv",
    #      "data/processed/barheadedgoose_cleaned.csv"
    # )
    # clean_gbif_data(
    #      "data/raw/gbif_saruscrane.csv",
    #      "data/processed/saruscrane_cleaned.csv"
    # )
    # clean_gbif_data(
    #      "data/raw/gbif_steppeeagle.csv",
    #      "data/processed/steppeeagle_cleaned.csv"
    # )
    # clean_gbif_data(
    #      "data/raw/gbif_wildboar.csv",
    #      "data/processed/wildboar_cleaned.csv"
    # )
    