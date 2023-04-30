# USA COVID-19 Vaccination and Case Data Analysis

This project analyzes COVID-19 vaccination and case data in the United States. The data is gathered from multiple sources, merged into a single dataset, and visualized using various plotting techniques.

## Data Sources

The data used in this project comes from the following sources:

- COVID-19 Vaccination Data: [Our World in Data](https://ourworldindata.org/us-states-vaccinations)
- COVID-19 Case Data: [COVID Tracking Project](https://covidtracking.com/data)

## Data Preprocessing

- Fetch COVID-19 and vaccination data from external sources
- Filter and clean the data to keep relevant columns and rows
- Combine all states data based on date
- Merge the COVID-19 and vaccination datasets for given dates
- Save raw, filtered, cleaned, and merged datasets as Excel files

## Visualizations

- A scatter plot showing the relationship between the number of people vaccinated, negative and positive cases over time
- A scatter plot showing the relationship between the number of people vaccinated and COVID-19 outcomes over time
- A bar chart showing the cumulative number of COVID-19 cases and outcomes as of March 7, 2021
- An interactive map showing the distribution of COVID-19 cases and outcomes across states

## Dependencies

- Python 3.x
- pandas
- requests
- openpyxl
- matplotlib
- seaborn
- plotly

You can install all dependencies using:
pip install pandas requests openpyxl matplotlib seaborn plotly

## Usage

- Clone or download the project from GitHub.
- Install the required dependencies using the following command:
   - pip install pandas requests openpyxl matplotlib seaborn plotly
- Open the project in your Python editor of choice.
- Open the file covid_data_analysis.py and run the script to fetch data, process it, and save the results in Excel files in the same directory.
- Open the file covid_data_visualization.py and run the script to generate the visualizations and save them as .png and .html files.

Command line:
- Run the Python script using the following command (must run them in sequence since covid_data_visualization.py is dependent on excel file generated using covid_data_analysis.py):
- python covid_data_analysis.py
- python covid_data_visualization.py

The output files will be saved in the same directory.

## Output Files

- 1_usa_covid_data.xlsx: Raw USA COVID-19 data
- 2_usa_covid_vaccination_data.xlsx: Raw USA vaccination data
- 3_filtered_usa_covid_data.xlsx: Filtered USA COVID-19 data
- 4_filtered_usa_covid_vaccination_data.xlsx: Filtered USA vaccination data
- 5_cleaned_up_filtered_usa_covid_vaccination_data.xlsx: Cleaned up filtered USA vaccination data
- 6_merged_usa_covid+vaccination_data.xlsx: Merged USA COVID-19 and vaccination data
- 7_summary_usa_covid+vaccination_data.xlsx: Summary of USA COVID-19 and vaccination data
- 1_people_vaccinated_and_covid_cases_trend.png: A scattered plot showing the number of people vaccinated, positive cases, and negative cases all state combined
- 2_people_vaccinated_and_covid_outcomes_trend.png: A scattered plot showing the distribution of number of people vaccinated, deaths, and recovered all state combined
- 3_cumulative_covid_cases_and_outcomes.png: Bar chart showing the cumulative number of COVID-19 cases and outcomes as of March 7, 2021
- 4_map_covid_cases_and_outcomes.html: Interactive map showing the distribution of COVID-19 cases and outcomes across states.