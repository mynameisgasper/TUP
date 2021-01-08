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

# built during creation
states = {}
states_inverse = {}
county = {}


def transformGender(gender):
    if gender == 'Male':
        return 'M'
    elif gender == 'Female':
        return 'F'
    else:
        return 'U'


def decide_measure(closed, opened):
    if not closed or closed is None:
        if not opened or opened is None:
            return 0
        else:
            return 1
    else:
        if not opened or opened is None:
            return 3
        else:
            return 2


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
    #try:
        f = pd.read_csv("../datasets/covid-19-yu-group_dataset_severity-index.csv")
        keep_col = ['severity_1-day', 'severity_2-day', 'severity_3-day', 'severity_4-day', 'severity_5-day', 'severity_6-day',
                    'severity_7-day', 'latitude', 'longitude']
        new_f = f[keep_col]
        #new_f.to_csv("severity.csv", index=False)
        cursor = connection.cursor()
        for row in new_f.itertuples():
            query = "INSERT INTO severityprediction (severity_1day, severity_2day, severity_3day, severity_4day, severity_5day, severity_6day, severity_7day, lat_hospital, lon_hospital) VALUES" \
                    "({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})"
            #cursor.execute(query.format(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        cursor.commit()

    #except:
       # print("No new severity records inserted")

def insert_unemployment():
    try:
        f = pd.read_csv("../datasets/STLABOUR_06012021210015887_1.csv")
        keep_col = ['ISO', 'Number date', 'Value']
        new_f = f[keep_col]

        cursor = connection.cursor()
        for row in new_f.itertuples():
            try:
                query = "INSERT INTO unemployment (iso, unemployment_date, value) VALUES" \
                        "('{0}', '{1}', {2})"
                cursor.execute(query.format(row[1], row[2] + "-01", row[3]))
            except:
                print(row[1] + " is not a country ISO code, skipped")
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


def insert_state_measurements():
    try:
        f = pd.read_csv("../datasets/nyt-states-reopen-status-covid-19_dataset_nyt-states-reopen-status-covid-19.csv")
        keep_col = ['state_abbreviation', 'state', 'opened_food_and_drink', 'closed_houses_of_worship',
                    'closed_food_and_drink', 'opened_retail', 'opened_outdoor_and_recreation',
                    'closed_outdoor_and_recreation', 'closed_entertainment', 'opened_industries',
                    'opened_entertainment', 'opened_personal_care', 'opened_houses_of_worship', 'population']
        new_f = f[keep_col]

        cursor = connection.cursor()
        for row in new_f.itertuples():
            measure_id = row[0]

            query = "INSERT INTO state (code, ISO, state_name, population) VALUES" \
                    "('{0}', 'USA', '{1}', {2})"
            cursor.execute(query.format(row[1], row[2], row[14]))
            cursor.commit()

            industry_measure = decide_measure(None, row[10])
            personal_care_measure = decide_measure(None, row[12])
            entertainment_measure = decide_measure(row[9], row[11])
            outdoor_measure = decide_measure(row[8], row[7])
            retail_measure = decide_measure(None, row[6])
            worship_measure = decide_measure(row[4], row[13])
            food_measure = decide_measure(row[5], row[3])
            command = "INSERT INTO measures (measure_id, code, industry, personal_care, entertainment, " \
                      "outdoor_recreation, retail, house_of_worship, food_drink) VALUES" \
                      "({0}, '{1}', {2}, {3}, {4}, {5}, {6}, {7}, {8})"

            cursor.execute(command.format(measure_id, row[1], industry_measure, personal_care_measure,
                                          entertainment_measure, outdoor_measure, retail_measure, worship_measure,
                                          food_measure))
            cursor.commit()

            command = "UPDATE state SET measure_id={0} WHERE code='{1}'"
            cursor.execute(command.format(measure_id, row[1]))

            states[row[1]] = row[2]
            states[row[2]] = row[1]
            cursor.commit()
    except:
        print("No new states inserted")
        cursor = connection.cursor()
        query = "SELECT code, state_name FROM state"
        cursor.execute(query)
        state_list = cursor.fetchall()
        for state in state_list:
            states[state[0]] = state[1]
            states_inverse[state[1]] = state[0]


def insert_by_age():
    try:
        f = pd.read_csv("../datasets/covid-19-death-counts-sex-age-state_dataset_covid-19-death-counts-sex-age-state.csv")
        keep_col = ['Data as of', 'State', 'Sex', 'Age group', 'COVID-19 Deaths', 'Total Deaths']
        new_f = f[keep_col]

        cursor = connection.cursor()
        for row in new_f.itertuples():
            if row[2] not in ['United States', 'Puerto Rico']:
                state = states_inverse[row[2]]
                sex = row[3]
                age_group = get_age_group_id(row[4])
                covid_deaths = handleNan(row[5])
                total_deaths = handleNan(row[6])

                if age_group is None and sex == 'All Sexes':
                    query = "UPDATE state SET covid_deaths={0}, total_deaths={1} WHERE code='{2}'"
                    cursor.execute(query.format(covid_deaths, total_deaths, state))
                elif age_group is not None and sex != 'All Sexes':
                    query = "INSERT INTO bygender (id_age_group, code, gender, report_date, covid_deaths_by_gender, total_deaths_by_gender) VALUES" \
                            "({0}, '{1}', '{2}', '{3}', {4}, {5})"
                    cursor.execute(query.format(age_group, state, transformGender(sex), row[1], covid_deaths, total_deaths))
        cursor.commit()
    except:
        print("No new data by gender and age added")


def insert_county():
    try:
        f = pd.read_csv("../datasets/published_PUBLIC_COVID-19-Activity_1609956124_COVID-19 Activity.csv")
        keep_col = ['COUNTY_FIPS_NUMBER', 'PROVINCE_STATE_NAME', 'COUNTY_NAME']
        new_f = f[keep_col]
        #new_f.to_csv("county.csv", index=False)

        cursor = connection.cursor()
        last_county = ''
        for row in new_f.itertuples():
            if row[1] in county or last_county == row[3] or row[3] == "" or row[3] == "Unknown" or handleNan(row[1]) == 0 or row[2] in ["Northern Mariana Islands", "Virgin Islands"]:
                continue
            county[int(row[1])] = row[2]
            query = "INSERT INTO county (fips, code, county_name) VALUES" \
                    "({0}, '{1}', '{2}')"
            cursor.execute(query.format(int(row[1]), states_inverse[row[2]], row[3].replace("'","")))
            last_county = row[3]
        cursor.commit()
    except:
        print("No new counties inserted")

def insert_hospital():
    try:
        f = pd.read_csv("../datasets/usa-hospital-beds_dataset_usa-hospital-beds.csv")
        keep_col = ['OBJECTID', 'FIPS', 'STATE_NAME', 'HOSPITAL_NAME', 'HOSPITAL_TYPE', 'HQ_ADDRESS', 'HQ_CITY', 'HQ_ZIP_CODE',
                    'NUM_LICENSED_BEDS', 'NUM_STAFFED_BEDS', 'NUM_ICU_BEDS', 'ADULT_ICU_BEDS', 'PEDI_ICU_BEDS', 'BED_UTILIZATION',
                    'Potential_Increase_In_Bed_Capac', 'AVG_VENTILATOR_USAGE', 'Y', 'X']
        #id severity je za STATE_NAME ampak ga nimamo in bo prazen
        new_f = f[keep_col]
        new_f.to_csv("hospital.csv", index=False)
    except:
        print("No new hospitals inserted")


def insert_covid_data():
    try:
        f = pd.read_csv("../datasets/covid-19-world-cases-deaths-testing_dataset_covid-19-world-cases-deaths-testing.csv")
        keep_col = ['iso_code', 'date', 'total_cases', 'new_cases', 'new_cases_smoothed', 'total_deaths', 'new_deaths',
                    'new_deaths_smoothed', 'total_cases_per_million', 'new_cases_per_million',
                    'new_cases_smoothed_per_million', 'total_deaths_per_million', 'new_deaths_per_million',
                    'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients', 'icu_patients_per_million',
                    'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions',
                    'weekly_icu_admissions_per_million', 'weekly_hosp_admissions', 'weekly_hosp_admissions_per_million',
                    'new_tests', 'total_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed',
                    'new_tests_smoothed_per_thousand', 'positive_rate', 'tests_per_case', 'tests_units',
                    'total_vaccinations', 'total_vaccinations_per_hundred', 'stringency_index', 'location']
        new_f = f[keep_col]

        cursor = connection.cursor()
        cursor.execute('BEGIN')
        cursor.execute('DELETE FROM covid19')

        for row in new_f.itertuples():
            if (row[36] in ['International', 'World']):
                continue
            query1 = "INSERT INTO covid19 (ISO, reproduction_rate, new_tests, new_tests_per_thousand, total_tests, " \
                     "total_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, positive_rate," \
                     "tests_per_case, tests_unit, total_vaccinations, total_vaccinations_per_hundred, stringency_index, " \
                     "date, new_cases, total_deaths, new_cases_smoothed, total_cases, new_deaths, " \
                     "new_deaths_smoothed, icu_patients, weekly_icu_admissions, weekly_hosp_admissions) " \
                     "VALUES ('{0}', {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, '{10}', {11}, {12}, {13}, '{14}', " \
                     "{15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23})"
            cursor.execute(query1.format(row[1], handleNan(row[15]), handleNan(row[24]), handleNan(row[27]),
                                handleNan(row[25]), handleNan(row[26]), handleNan(row[28]), handleNan(row[29]),
                                handleNan(row[30]), handleNan(row[31]), row[32], handleNan(row[33]),
                                handleNan(row[34]), handleNan(row[35]), row[2], handleNan(4), handleNan(6), handleNan(5),
                                handleNan(3), handleNan(7), handleNan(8), handleNan(16), handleNan(20), handleNan(22)))

        cursor.execute('COMMIT')
        cursor.commit()
    except:
        print("No new COVID-19 reports inserted")


def insert_approval():
    try:
        f = pd.read_csv("../datasets/fivethirtyeight-trump-approval-ratings_dataset_approval_topline.csv")
        keep_col = ['subgroup', 'modeldate', 'approve_estimate', 'approve_hi', 'approve_lo']
        new_f = f[keep_col]
        cursor = connection.cursor()
        for row in new_f.itertuples():
            if row[1] == 'All polls':
                query = "INSERT INTO approvalrating (approval_estimate, approval_high, approval_low, date) " \
                        "VALUES ({0}, {1}, {2}, '{3}') RETURNING id_approval"
                cursor.execute(query.format(row[3], row[4], row[5], row[2]))
                id = cursor.fetchall()[0][0]

                query = "UPDATE covid19 SET id_approval={0} WHERE iso='USA' AND date='{1}'"
                cursor.execute(query.format(id, row[2]))

                query = "SELECT id_record FROM covid19 WHERE iso='USA' AND date='{0}'"
                cursor.execute(query.format(row[2]))
                id_record = cursor.fetchall()
                if len(id_record) > 0:
                    id_record = id_record[0][0]
                    query = "UPDATE approvalrating SET id_record={0} WHERE id_approval={1}"
                    cursor.execute(query.format(id_record, id))
        cursor.commit()
    except:
        print("No new approvals inserted")


connection_string = 'DSN=Seminarska'
connection = pyodbc.connect(connection_string)

insert_continents()
insert_countries()
insert_severity()
insert_unemployment()
insert_age_group()
insert_state_measurements()
insert_by_age()
insert_county()
insert_hospital()
insert_covid_data()
insert_approval()
