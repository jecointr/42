import matplotlib.pyplot as plt
from load_csv import load

def draw_country(df, country_name):
    """
    Affiche l'évolution d'un pays à partir d'un DataFrame.
    
    Args:
        df (pd.DataFrame): Dataset de vie/life expectancy.
        country_name (str): Nom du pays à afficher.
    """
    if df is None or country_name not in df['country'].values:
        print(f"Country {country_name} not found in dataset.")
        return
    
    country_data = df[df['country'] == country_name].iloc[0, 1:]
    years = list(map(int, country_data.index))
    
    plt.figure(figsize=(10,5))
    plt.plot(years, country_data.values, label=country_name)
    plt.title(f"Life expectancy of {country_name} over the years")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.show()

def main():
    df = load("life_expectancy_years.csv")
    draw_country(df, "France")  # remplacer par le pays de ton campus

if __name__ == "__main__":
    main()

