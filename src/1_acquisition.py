import sqlite3
import csv

db_file_path = './data/wdi_database.db'
print("Attempting to connect to the database at:", db_file_path)

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# CO2 emissions (kg per 2015 US$ of GDP)
# CO2 emissions (kt)
# CO2 emissions (metric tons per capita)
# CO2 emissions from electricity and heat production, total (% of total fuel combustion)
# CO2 emissions from gaseous fuel consumption (% of total)
# CO2 emissions from gaseous fuel consumption (kt)
# CO2 emissions from liquid fuel consumption (% of total)
# CO2 emissions from liquid fuel consumption (kt)
# CO2 emissions from manufacturing industries and construction (% of total fuel combustion)
# CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion)
# CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion)
# CO2 emissions from solid fuel consumption (% of total)
# CO2 emissions from solid fuel consumption (kt)
# CO2 emissions from transport (% of total fuel combustion)
# CO2 intensity (kg per kg of oil equivalent energy use)

indicators = [
    "Access to electricity (% of population)",
    "Adjusted net national income per capita (annual % growth)",
    "Adjusted net national income per capita (constant 2015 US$)",
    "CO2 emissions (kg per 2015 US$ of GDP)",
    "CO2 emissions (metric tons per capita)",

    "CO2 intensity (kg per kg of oil equivalent energy use)",

    "Electric power consumption (kWh per capita)",
    "Electric power transmission and distribution losses (% of output)",

    "Electricity production from coal sources (% of total)",
    "Electricity production from hydroelectric sources (% of total)",
    "Electricity production from natural gas sources (% of total)",
    "Electricity production from nuclear sources (% of total)",
    "Electricity production from oil sources (% of total)",
    "Electricity production from oil, gas and coal sources (% of total)",
    "Electricity production from renewable sources, excluding hydroelectric (% of total)",
    "Electricity production from renewable sources, excluding hydroelectric (kWh)",

    "Electricity production from renewable sources, excluding hydroelectric (kWh)",
    "Fossil fuel energy consumption (% of total)",

    "Fuel exports (% of merchandise exports)",
    "Fuel imports (% of merchandise imports)",

    "GDP per capita (constant 2015 US$)",
    "GDP per capita growth (annual %)",
    "GDP per unit of energy use (PPP $ per kg of oil equivalent)",
    "GDP per unit of energy use (constant 2017 PPP $ per kg of oil equivalent)",

    "Investment in energy with private participation (current US$)",
    "Manufacturing, value added (% of GDP)",
    "Manufacturing, value added (annual % growth)",
    "Manufacturing, value added (constant 2015 US$)",

    "Natural gas rents (% of GDP)",
    "Nitrous oxide emissions (% change from 1990)",
    "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
    "Other greenhouse gas emissions (% change from 1990)",
    "Renewable electricity output (% of total electricity output)",
    "Renewable energy consumption (% of total final energy consumption)",
    "Total greenhouse gas emissions (% change from 1990)",
    "Total greenhouse gas emissions (kt of CO2 equivalent)"
]
years = range(1990, 2020)

sql_query = "SELECT \"Indicator Name\", " + ", ".join(
    f'COUNT(CASE WHEN "{year}" NOT IN (\'\', \'-\', \'N/A\') THEN "{year}" ELSE NULL END) AS "{year}"'
    for year in years
)
sql_query += " FROM WDICSV WHERE " + " OR ".join(
    f'"Indicator Name" LIKE \'{indicator}\'' for indicator in indicators
) + " GROUP BY \"Indicator Name\";"

# Execute the query
try:
    cursor.execute(sql_query)
    results = cursor.fetchall()
    if results:
        print("Success")
    else:
        print("No results found.")
except Exception as e:
    print(f"An error occurred: {e}")

# File path for CSV
csv_file_path = './data/indicator_count_by_year.csv'

# Write results to CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    header = ["Indicator Name"] + [str(year) for year in years]
    csvwriter.writerow(header)
    
    # Write the data rows
    for result in results:
        csvwriter.writerow(result)

print(f"Data successfully saved to {csv_file_path}")

cursor.close()
conn.close()

extracted_indicators = [result[0] for result in results]

# Display the extracted indicators
print("Extracted Indicators:")
for indicator in extracted_indicators:
    print(indicator)


# CO2 emissions (metric tons per capita)
# Electric power consumption (kWh per capita)
# GDP per capita (constant 2015 US$)

# GDP per capita growth (annual %)

