import sqlite3
import pandas as pd

conn = sqlite3.connect('./data/wdi_database.db')

query = """
        SELECT
        "Country Name",
        "Indicator Name",
        "1990",
        "1991",
        "1992",
        "1993",
        "1994",
        "1995",
        "1996",
        "1997",
        "1998",
        "1999",
        "2000",
        "2001",
        "2002",
        "2003",
        "2004",
        "2005",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "2015",
        "2016",
        "2017",
        "2018",
        "2019",
        "2020"
        FROM WDICSV
        WHERE "Indicator Name" IN ('CO2 emissions (metric tons per capita)', 
                                'Electric power consumption (kWh per capita)', 
                                'GDP per capita (constant 2015 US$)')
        """

df = pd.read_sql_query(query, conn)

conn.close()

df.to_csv('./data/output.csv', index=False)

print("Data saved to 'output.csv'")