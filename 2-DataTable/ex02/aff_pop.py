from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data_frame = load("population_total.csv")
        country_data_1 = data_frame[data_frame['country'] == 'Belgium']
        # country_data_2 = data_frame[data_frame['country'] == 'Belgium']
        if not country_data_1.empty:
            years = [year for year in country_data_1.columns if year.isdigit() and 1800 <= int(year) <= 2050 and int(year) % 40 == 0]
            
            print(country_data_1)
            plt.plot(country_data_1.columns[1:], country_data_1.iloc[0, 1:])
            plt.xticks(years)
            plt.title(f'Population Projections')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.show()
        else:
            print(f"Data not available for {'Belgium'}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
