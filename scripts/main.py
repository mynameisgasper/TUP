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

age_groups = {
    0: 'Under 1 year',
    1: '0-17 years',
    2: '1-4 years',
    3: '5-14 years',
    4: '15-24 years',
    5: '18-29 years',
    6: '25-34 years',
    7: '30-49 years',
    8: '35-44 years',
    9: '45-54 years',
    10: '50-64 years',
    11: '55-64 years',
    12: '65-74 years',
    13: '75-84 years',
    14: '85 years and over'
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


def get_age_group_id(name):
    for x in age_groups:
        if age_groups[x].lower() == name.lower():
            return x


def insert_continents():
    try:
        cursor = connection.cursor()

        for x in continents:
            command = "INSERT INTO continent (id_continent, continent_name) VALUES ({0}, '{1}')"
            cursor.execute(command.format(x, continents[x]))
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
    try:
        f = pd.read_csv("../datasets/STLABOUR_06012021210015887_1.csv")
        keep_col = ['ISO', 'Number date', 'Value']
        new_f = f[keep_col]
        #new_f.to_csv("unemployment.csv", index=False)

        cursor = connection.cursor()
        for row in new_f.itertuples():
            query = "INSERT INTO unemployment (iso, unemployment_date, value) VALUES" \
                    "('{0}', '{1}', {2})"
            print(row[1], row[2]+"-01", row[3])
            cursor.execute(query.format(row[1], row[2], row[3]))
        cursor.commit()
    except:
        print("No new unemployment records inserted")


def insert_age_group():
    try:
        cursor = connection.cursor()

        for x in age_groups:
            command = "INSERT INTO agegroup (id_age_group, age_group) VALUES ({0}, '{1}')"
            cursor.execute(command.format(x, age_groups[x]))
        cursor.commit()
    except:
        print("No new age groups inserted")


connection_string = 'DSN=Seminarska'
connection = pyodbc.connect(connection_string)

insert_continents()
insert_countries()
insert_severity()
insert_unemployment()
insert_age_group()



