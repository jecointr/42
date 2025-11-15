import matplotlib.pyplot as plt
from load_csv import load


def parse_number(value):
    """Convertit les valeurs style '29M', '540k', '1.2B' en float."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)

    value = str(value).strip()

    if value == "" or value.lower() == "nan":
        return None

    if value.endswith("k"):
        return float(value[:-1]) * 1_000
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    if value.endswith("B"):
        return float(value[:-1]) * 1_000_000_000

    return float(value)


def compare_countries(df, country_a, country_b):
    """
    Compare l'évolution de la population entre deux pays.
    """
    if df is None:
        return

    if country_a not in df['country'].values:
        print(f"Country {country_a} not found.")
        return

    if country_b not in df['country'].values:
        print(f"Country {country_b} not found.")
        return

    row_a = df[df['country'] == country_a].iloc[0]
    row_b = df[df['country'] == country_b].iloc[0]

    # Colonnes année
    years = [c for c in df.columns if c.isdigit()]
    years = sorted(years, key=lambda y: int(y))
    years = [y for y in years if 1800 <= int(y) <= 2050]

    # Extraction & parsing des valeurs
    values_a = [parse_number(row_a[y]) for y in years]
    values_b = [parse_number(row_b[y]) for y in years]

    plt.figure(figsize=(10, 5))
    plt.plot([int(y) for y in years], values_a, label=country_a)
    plt.plot([int(y) for y in years], values_b, label=country_b)

    plt.title(f"Population comparison: {country_a} vs {country_b}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    df = load("population_total.csv")
    if df is None:
        return
    compare_countries(df, "France", "Germany")


if __name__ == "__main__":
    main()
