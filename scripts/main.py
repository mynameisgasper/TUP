import pyodbc
import pandas as pd
import math


continents = {
    0: 'Africa',
    1: 'Asia',
    2: 'Europe',
    3: 'North America',
    4: 'Oceania',
    5: 'South America'
}


def handleNan(value):
    if math.isnan(value):
        return 0
    else:
        return value


def get_continent_id(name):
    for x in continents:
        if continents[x].lower() == name.lower():
            return x


def insert_continents():
    try:
        cursor = connection.cursor()

        for x in continents:
            command = "INSERT INTO continent (id_continent, continent_name) VALUES ({0}, '{1}')"
            cursor.execute(command.format(x, continents[x]))
            print(command.format(x, continents[x]))
        cursor.commit()
    except:
        print("No new continents inserted")


def insert_countries():
    try:
        f = pd.read_csv("../datasets/covid-19-world-cases-deaths-testing_dataset_covid-19-world-cases-deaths-testing.csv")
        keep_col = ['iso_code', 'continent', 'location', 'population', 'population_density', 'median_age', 'aged_65_older',
                    'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence',
                    'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
                    'life_expectancy', 'human_development_index']
        new_f = f[keep_col]

        cursor = connection.cursor()
        last_country = ''
        for row in new_f.itertuples():
            if row[3] == 'International' or row[3] == 'World' or last_country == row[1]:
                continue

            query = "INSERT INTO country (iso, id_continent, country_name, population, population_density, median_age, aged_65_or_older, aged_70_or_older, gdp_per_capita, extreme_poverty, cardio_vasc_death_rate, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index) VALUES" \
                    "('{0}', {1}, '{2}', {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})"

            cursor.execute(query.format(row[1], get_continent_id(row[2]), row[3].replace('\'', ''), handleNan(row[4]),
                                        handleNan(row[5]), handleNan(row[6]), handleNan(row[7]), handleNan(row[8]),
                                        handleNan(row[9]), handleNan(row[10]), handleNan(row[11]), handleNan(row[12]),
                                        handleNan(row[13]), handleNan(row[14]), handleNan(row[15]), handleNan(row[16]),
                                        handleNan(row[17]), handleNan(row[18])))
            last_country = row[1]
            cursor.commit()
    except:
        print("No new countries inserted")

def insert_severity():
    f = pd.read_csv("../datasets/covid-19-yu-group_dataset_severity-index.csv")
    keep_col = ['severity_1-day', 'severity_2-day', 'severity_3-day', 'severity_4-day', 'severity_6-day',
                'severity_7-day', 'latitude', 'longitude']
    new_f = f[keep_col]
    #new_f.to_csv("severity.csv", index=False)

def insert_unemployment():
    f = pd.read_csv("../datasets/STLABOUR_06012021210015887_1.csv")
    keep_col = ['ISO', 'Number date', 'Value']
    new_f = f[keep_col]
    #new_f.to_csv("unemployment.csv", index=False)


connection_string = 'DSN=Seminarska'
#connection = pyodbc.connect(connection_string)

insert_continents()
insert_countries()
insert_severity()
insert_unemployment()



