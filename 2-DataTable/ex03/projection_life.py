from load_csv import load
import matplotlib.pyplot as plt


def main():
    life_expenctancy = load("life_expectancy_years.csv")
    income_person = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life_expenctancy_1900 = life_expenctancy["1900"]
    income_person_1900 = income_person["1900"]
    plt.scatter(income_person_1900, life_expenctancy_1900, marker='o')
    x_ticks = []
    plt.show()
    # print(income_person_1900)
    # print(life_expenctancy_1900)
    # print(life_expenctancy)
    # print(income_person)



if __name__ == "__main__":
    main()
