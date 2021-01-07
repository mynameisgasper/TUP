import pandas as pd

f = pd.read_csv("../datasets/covid-19-world-cases-deaths-testing_dataset_covid-19-world-cases-deaths-testing.csv")
keep_col = ['iso_code', 'continent', 'location', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']
new_f = f[keep_col]
#new_f.to_csv("country.csv", index=False)

f = pd.read_csv("../datasets/STLABOUR_06012021210015887_1.csv")
keep_col = ['ISO', 'Country_name', 'Value']
new_f = f[keep_col]
#new_f.to_csv("unemployment.csv", index=False)

f = pd.read_csv("../datasets/covid-19-yu-group_dataset_severity-index.csv")
keep_col = ['severity_1-day', 'severity_2-day', 'severity_3-day', 'severity_4-day', 'severity_6-day', 'severity_7-day','latitude', 'longitude']
new_f = f[keep_col]
new_f.to_csv("severity.csv", index=False)