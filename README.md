USA COVID-19 and Vaccination Data Analysis
This Python script retrieves, processes, and analyzes USA COVID-19 and vaccination data. It fetches data from external sources, filters and cleans it, and then merges the two datasets. The script saves intermediate and final results in Excel files for further analysis.

Features
Fetch COVID-19 and vaccination data from external sources
Filter and clean the data to keep relevant columns and rows
Merge the COVID-19 and vaccination datasets based on the 'state' and 'date' columns
Save raw, filtered, cleaned, and merged datasets as Excel files

Dependencies
Python 3.x
pandas
requests
openpyxl

Usage
Install the required dependencies using the following command:

pip install pandas requests openpyxl
Run the Python script using the following command:
python covid_data_analysis.py
The script will fetch data, process it, and save the results in Excel files in the same directory.

Output Files
usa_covid_data.xlsx: Raw USA COVID-19 data
usa_covid_vaccination_data.xlsx: Raw USA vaccination data
filtered_usa_covid_data.xlsx: Filtered USA COVID-19 data
filtered_usa_covid_vaccination_data.xlsx: Filtered USA vaccination data
cleaned_up_filtered_usa_covid_vaccination_data.xlsx: Cleaned up filtered USA vaccination data
merged_usa_covid+vaccination_data.xlsx: Merged USA COVID-19 and vaccination data