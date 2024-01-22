from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        data_frame = load("population_total.csv")
        belgium_data = data_frame[data_frame['country'] == 'Belgium'].iloc[:, 1:]
        france_data = data_frame[data_frame['country'] == 'France'].iloc[:, 1:]
        if not belgium_data.empty and not france_data.empty:

            belgium_popu = [(float(popu[:-1]) * 1e6) for popu, year in zip(belgium_data.values.flatten(), belgium_data.columns.astype(int)) if year <= 2050]
            france_popu = [(float(popu[:-1]) * 1e6) for popu, year in zip(france_data.values.flatten(), france_data.columns.astype(int)) if year <= 2050]

            years = [year for year in france_data.columns.astype(int) if year <= 2050]
            plt.plot(years, belgium_popu, label='Belgium')
            plt.plot(years, france_popu, label='France')

            years_x = [year for year in years if 1800 <= year <= 2050 and year % 40 == 0]
            plt.xticks(years_x)
            mpopu = max(max(belgium_popu), max(france_popu))
            ypopu = [i * 1e7 for i in range(int(mpopu / 1e7) + 1) if (i * 1e7) % 2e7 == 0 and i != 0]
            plt.yticks(ypopu, ["{:,.0f}M".format(popu / 1e6) for popu in ypopu])

            plt.title(f'Population Projections')
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.legend(loc="lower right")
            plt.show()
        else:
            print(f"Data not available for {'Belgium'}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
