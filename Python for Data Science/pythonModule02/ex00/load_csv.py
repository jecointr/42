import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV en DataFrame pandas.

    Args:
        path (str): Chemin vers le fichier CSV.

    Returns:
        pd.DataFrame: Le dataset chargé, ou None si une erreur survient.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse the file at {path}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def main():
    df = load("../data/life_expectancy_years.csv")
    if df is not None:
        print(df.head())


if __name__ == "__main__":
    main()
