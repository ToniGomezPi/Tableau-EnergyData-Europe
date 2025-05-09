import pandas as pd
import country_converter as coco # For country conversion in case we want data for EU or Africa, Asia... 
# leemos el dataset
energyData = pd.read_csv(r'owid-energy-data.csv')

print(energyData.head())
# printing NaN or 0 values from the columns
print(energyData.isnull().sum())

# We have lots of invalid data in lots of columns we are going to filter and clean for 5 columns.

energyData_cleaned = energyData[['country', 'year', 'renewables_consumption', 'renewables_share_energy', 'population']]

# We compare the data with the columns selected and see how many nulls we have in
print(energyData_cleaned.head())
print(energyData_cleaned.isnull().sum())

# We are going to drop the null values
energyData_cleaned = energyData_cleaned.dropna()

# Data cleaned from nulls
print(energyData_cleaned.head())
print(energyData_cleaned.isnull().sum())

# -------- Filter countries that are inside EU --------
country_eu = coco.CountryConverter()

# Getting EU names by DB from country_converter
european_countries = country_eu.data[country_eu.data['continent'] == 'Europe']['name_short'].tolist()

# Filtrar solo países europeos
energyData_europe = energyData_cleaned[energyData_cleaned['country'].isin(european_countries)]

print(energyData_europe) # 1559 rows of data from EU countries

# Saving the cleaned data for tableau
energyData_europe.to_csv('energyData_europe.csv', index=False)