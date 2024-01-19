from load_csv import load
import matplotlib.pyplot as plt


def aff_life():
    try:
        data_frame = load("life_expectancy_years.csv")
        country_data = data_frame[data_frame['country'] == 'Belgium']
        if not country_data.empty:
            years = country_data.columns[1::40]
            plt.plot(country_data.columns[1:], country_data.iloc[0, 1:])
            plt.xticks(years)
            plt.title(f'Life Expectancy Over the Years - Belgium')
            plt.xlabel('Year')
            plt.ylabel('Life Expectancy')
            plt.show()
        else:
            print(f"Data not available for {'Belgium'}")
    except Exception as e:
        print(f"An error occurred: {e}")

aff_life()