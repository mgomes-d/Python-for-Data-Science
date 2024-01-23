from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    life_expenctancy = load("life_expectancy_years.csv")
    income_person = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life_expenctancy_1900 = life_expenctancy["1900"]
    income_person_1900 = income_person["1900"]
    plt.scatter(income_person_1900, life_expenctancy_1900)
    x_ticks = np.array([300.0, 1000.0, 10000.0])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.xlim(300)
    plt.xscale("log")
    plt.xticks(x_ticks, ["{:,.0f}k".format(pers / 1e3) if pers >= 1000 else "{:,.0f}".format(pers) for pers in x_ticks])
    plt.show()


if __name__ == "__main__":
    main()
