import matplotlib.pyplot as plt
from load_csv import load


def parse_number(value):
    """Convertit une valeur type '29M', '540k', '1.2B' en float."""
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


def draw_projection(df_gdp, df_life, year):
    """
    Affiche projection PIB vs espérance de vie pour une année donnée.
    """
    if df_gdp is None or df_life is None:
        return

    col = str(year)
    if col not in df_gdp.columns or col not in df_life.columns:
        print(f"Year {year} not available in datasets.")
        return

    countries = df_gdp["country"]
    gdp_values = [parse_number(v) for v in df_gdp[col]]
    life_values = [parse_number(v) for v in df_life[col]]

    # Filtrer les valeurs valides
    filtered = [
        (gdp, life)
        for gdp, life in zip(gdp_values, life_values)
        if gdp is not None and life is not None
    ]
    if not filtered:
        print("No valid data to plot.")
        return

    gdp_values, life_values = zip(*filtered)

    plt.figure(figsize=(10, 6))
    plt.scatter(gdp_values, life_values, alpha=0.7)
    plt.title(f"Life expectancy vs GDP per capita in {year}")
    plt.xlabel("GDP per capita (PPP, inflation adjusted)")
    plt.ylabel("Life expectancy")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")
    if df_gdp is None or df_life is None:
        return

    draw_projection(df_gdp, df_life, 1900)


if __name__ == "__main__":
    main()
