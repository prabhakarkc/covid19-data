import pandas as pd
import requests

# Fetch covid data
def fetch_usa_states_data():
    url = "https://api.covidtracking.com/v1/states/daily.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Fetch vaccination data
def fetch_usa_vaccination_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv"
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(url)

usa_states_data = fetch_usa_states_data()
usa_vaccination_data = fetch_usa_vaccination_data()

# Save data to Excel files
def save_to_excel_usa_covid_data(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    df.to_excel("1_usa_covid_data.xlsx", index=False, engine='openpyxl')
    print("USA states COVID-19 data has been saved to 1_usa_covid_data.xlsx")

def save_to_excel_usa_covid_vaccination_data(data):
    data.to_excel("2_usa_covid_vaccination_data.xlsx", index=False, engine='openpyxl')
    print("USA vaccination data has been saved to 2_usa_covid_vaccination_data.xlsx")

save_to_excel_usa_covid_data(usa_states_data)
save_to_excel_usa_covid_vaccination_data(usa_vaccination_data)

def read_usa_covid_data(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    columns_to_keep = [
        'state', 'positive', 'negative', 'pending', 'hospitalizedCumulative',
        'onVentilatorCumulative', 'recovered', 'death', 'date'
    ]
    df = df[columns_to_keep]
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')  # Format the date column

    # Rename columns
    df = df.rename(columns={'hospitalizedCumulative': 'hospitalized', 'onVentilatorCumulative': 'onVentilator'})

    # Keep only data from 2021-01-12 to 2021-03-07
    df = df[(df['date'] >= '2021-01-12') & (df['date'] <= '2021-03-07')]

    # Keep only valid states using state_map
    state_map = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
        'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
        'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
        'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    }
    df = df[df['state'].isin(state_map)]

    return df

# Filter vaccination data
def filter_usa_vaccination_data(data):
    columns_to_keep = ['location', 'people_vaccinated', 'date']
    filtered_data = data[columns_to_keep]
    filtered_data = filtered_data.rename(columns={'people_vaccinated': 'peopleVaccinated'})  # Rename the column

    # Keep only data from 2021-01-12 to 2021-03-07
    filtered_data = filtered_data[(filtered_data['date'] >= '2021-01-12') & (filtered_data['date'] <= '2021-03-07')]

    return filtered_data

usa_covid_data = read_usa_covid_data("1_usa_covid_data.xlsx")
filtered_usa_covid_vaccination_data = filter_usa_vaccination_data(usa_vaccination_data)

# Save filtered data to Excel files
def save_filtered_to_excel_usa_covid(filtered_data):
    filtered_data.to_excel("3_filtered_usa_covid_data.xlsx", index=False, engine='openpyxl')
    print("Filtered USA states COVID-19 data has been saved to 3_filtered_usa_covid_data.xlsx")

def save_filtered_to_excel_usa_covid_vaccination_data(filtered_data):
    filtered_data.to_excel("4_filtered_usa_covid_vaccination_data.xlsx", index=False, engine='openpyxl')
    print("Filtered USA vaccination data has been saved to 4_filtered_usa_covid_vaccination_data.xlsx")

save_filtered_to_excel_usa_covid(usa_covid_data)
save_filtered_to_excel_usa_covid_vaccination_data(filtered_usa_covid_vaccination_data)

# Clean up filtered data
def clean_up_filtered_data(covid_data, vaccination_data):
    # Modify column name location to state in filtered vaccination data
    vaccination_data = vaccination_data.rename(columns={'location': 'state'})

    # Modify state name from full name to Shorthand two letters as in filtered covid data
    state_map = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
        'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
        'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
        'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
        'New York State': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    covid_data['state'] = covid_data['state'].apply(lambda x: state_map.get(x, x))
    vaccination_data['state'] = vaccination_data['state'].apply(lambda x: state_map.get(x, x))

    # Filter data to keep only actual states defined in state_map
    valid_states = list(state_map.values())
    covid_data = covid_data[covid_data['state'].isin(valid_states)]
    vaccination_data = vaccination_data[vaccination_data['state'].isin(valid_states)]

    # Return cleaned up data
    return covid_data, vaccination_data

cleaned_usa_covid_data, cleaned_filtered_usa_covid_vaccination_data = clean_up_filtered_data(
    usa_covid_data, filtered_usa_covid_vaccination_data
)

# Save cleaned up filtered vaccination data to Excel file
def save_cleaned_up_filtered_to_excel_usa_covid_vaccination_data(filtered_data):
    filtered_data.to_excel("5_cleaned_up_filtered_usa_covid_vaccination_data.xlsx", index=False, engine='openpyxl')
    print(
        "Cleaned up filtered USA vaccination data has been saved to 5_cleaned_up_filtered_usa_covid_vaccination_data.xlsx")

save_cleaned_up_filtered_to_excel_usa_covid_vaccination_data(cleaned_filtered_usa_covid_vaccination_data)

# Print cleaned up data
print(cleaned_usa_covid_data.head())
print(cleaned_filtered_usa_covid_vaccination_data.head())

# Merge covid and vaccination data
merged_data = pd.merge(cleaned_usa_covid_data, cleaned_filtered_usa_covid_vaccination_data, how='inner',
                       on=['state', 'date'])

# Save merged data to Excel file
def save_to_excel_merged_usa_covid_vaccination_data(data):
    data.to_excel("6_merged_usa_covid+vaccination_data.xlsx", index=False, engine='openpyxl')
    print("Merged USA COVID-19 and vaccination data has been saved to 6_merged_usa_covid+vaccination_data.xlsx")

save_to_excel_merged_usa_covid_vaccination_data(merged_data)

# Print merged data
print(merged_data.head())

def merge_and_summarize_data(merged_data_path):
    merged_data = pd.read_excel(merged_data_path, engine='openpyxl')
    unique_dates = merged_data['date'].unique()
    unique_dates.sort()  # Sort unique_dates in ascending order

    summary_data = []
    for date in unique_dates:
        daily_data = merged_data[merged_data['date'] == date]
        daily_summary = {
            'date': date,
            'positive': daily_data['positive'].sum(),
            'negative': daily_data['negative'].sum(),
            'pending': daily_data['pending'].sum(),
            'hospitalized': daily_data['hospitalized'].sum(),
            'onVentilator': daily_data['onVentilator'].sum(),
            'recovered': daily_data['recovered'].sum(),
            'death': daily_data['death'].sum(),
            'peopleVaccinated': daily_data['peopleVaccinated'].sum()
        }
        summary_data.append(daily_summary)

    # Convert summary_data to DataFrame
    summary_data_df = pd.DataFrame(summary_data)

    # Replace NaN values with 0
    summary_data_df.fillna(0, inplace=True)

    # Save summary data to Excel file
    def save_to_excel_summary_data(data):
        data.to_excel("7_summary_usa_covid+vaccination_data.xlsx", index=False, engine='openpyxl')
        print("Summary USA COVID-19 and vaccination data has been saved to 7_summary_usa_covid+vaccination_data.xlsx")

    save_to_excel_summary_data(summary_data_df)

    # Print summary data
    print(summary_data_df.head())

# Execute merge_and_summarize_data function
merge_and_summarize_data("6_merged_usa_covid+vaccination_data.xlsx")