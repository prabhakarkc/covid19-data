# USA COVID-19 Vaccination and Case Data Analysis

This project analyzes COVID-19 vaccination and case data in the United States. The data is gathered from multiple sources, merged into a single dataset, and visualized using various plotting techniques.

## Data Sources

The data used in this project comes from the following sources:

- COVID-19 Vaccination Data: [Our World in Data](https://ourworldindata.org/us-states-vaccinations)
- COVID-19 Case Data: [COVID Tracking Project](https://covidtracking.com/data)

## Data Preprocessing

- Fetch COVID-19 and vaccination data from external sources
- Filter and clean the data to keep relevant columns and rows
- Merge the COVID-19 and vaccination datasets based on the 'state' and 'date' columns
- Save raw, filtered, cleaned, and merged datasets as Excel files

## Visualizations

- A bar chart showing the number of people vaccinated, positive cases, and negative cases in each state
- A set of pie charts showing the distribution of total COVID-19 cases and outcomes

## Dependencies

- Python 3.x
- pandas
- requests
- openpyxl
- matplotlib
- seaborn

## Usage

1. Install the required dependencies using the following command:
   pip install pandas requests openpyxl matplotlib seaborn
2. Run the Python script using the following command:
   python covid_data_analysis.py
3. The script will fetch data, process it, and save the results in Excel files in the same directory. It will also generate the visualizations and save them as .png files.

## Output Files

- usa_covid_data.xlsx: Raw USA COVID-19 data
- usa_covid_vaccination_data.xlsx: Raw USA vaccination data
- filtered_usa_covid_data.xlsx: Filtered USA COVID-19 data
- filtered_usa_covid_vaccination_data.xlsx: Filtered USA vaccination data
- cleaned_up_filtered_usa_covid_vaccination_data.xlsx: Cleaned up filtered USA vaccination data
- merged_usa_covid+vaccination_data.xlsx: Merged USA COVID-19 and vaccination data
- people_vaccinated_and_covid_cases_in_each_state.png: A bar chart showing the number of people vaccinated, positive cases, and negative cases in each state
- total_cases_combined.png: A set of pie charts showing the distribution of total COVID-19 cases and outcomes
