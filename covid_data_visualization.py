import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

# Set plotting style
sns.set_style("whitegrid")


def plot_vaccination_and_covid_cases_trend(data):
    # Convert 'date' column to datetime with desired format
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

    # Filter data for the specified date range
    date_range = pd.date_range(start='2021-01-12', end='2021-03-07')
    filtered_data = data[data['date'].isin(date_range)]

    if filtered_data.empty:
        print("No data available for the specified date range.")
        return

    # Set color palette
    colors = sns.color_palette("Greys", n_colors=9)

    # Create a scatter plot for the number of people vaccinated and COVID-19 cases
    plt.figure(figsize=(16, 6))
    sns.scatterplot(x='date', y='peopleVaccinated', data=filtered_data, color=colors[0], alpha=0.8)
    sns.scatterplot(x='date', y='positive', data=filtered_data, color=colors[1], alpha=0.8)
    sns.scatterplot(x='date', y='negative', data=filtered_data, color=colors[2], alpha=0.8)

    # Add lines connecting the points
    sns.lineplot(x='date', y='peopleVaccinated', data=filtered_data, color=colors[0], alpha=0.8)
    sns.lineplot(x='date', y='positive', data=filtered_data, color=colors[1], alpha=0.8)
    sns.lineplot(x='date', y='negative', data=filtered_data, color=colors[2], alpha=0.8)

    plt.title("Number of People Vaccinated and COVID-19 Cases between 01/12/2021 and 03/07/2021")
    plt.ylabel("Number of People Vaccinated and COVID Cases")
    plt.xlabel("Date")

    # Set x-axis ticks and format labels as mm-dd
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

    # Add units to the y-axis scale
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'{x:,.0f}'))

    # Add legend color patches
    legend_handles = [Patch(facecolor=colors[i], label=lab) for i, lab in
                      enumerate(['People Vaccinated', 'Positive Cases', 'Negative Cases'])]
    plt.legend(handles=legend_handles)

    plt.tick_params(axis='x', labelrotation=90, labelsize=10)
    plt.tight_layout()
    plt.savefig("1_people_vaccinated_and_covid_cases_trend.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("1_people_vaccinated_and_covid_cases_trend.png saved.")


def plot_vaccination_and_covid_outcomes_trend(data):
    # Convert 'date' column to datetime with desired format
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

    # Filter data for the specified date range
    date_range = pd.date_range(start='2021-01-12', end='2021-03-07')
    filtered_data = data[data['date'].isin(date_range)]

    if filtered_data.empty:
        print("No data available for the specified date range.")
        return

    # Set color palette
    colors = sns.color_palette("Greys", n_colors=9)

    # Create a scatter plot for the number of people vaccinated and COVID-19 outcomes
    plt.figure(figsize=(16, 6))
    sns.scatterplot(x='date', y='peopleVaccinated', data=filtered_data, color=colors[0], alpha=0.8)
    sns.scatterplot(x='date', y='death', data=filtered_data, color=colors[2], alpha=0.8)
    sns.scatterplot(x='date', y='recovered', data=filtered_data, color=colors[3], alpha=0.8)

    # Add lines connecting the points
    sns.lineplot(x='date', y='peopleVaccinated', data=filtered_data, color=colors[0], alpha=0.8)
    sns.lineplot(x='date', y='death', data=filtered_data, color=colors[2], alpha=0.8)
    sns.lineplot(x='date', y='recovered', data=filtered_data, color=colors[3], alpha=0.8)

    plt.title("Number of People Vaccinated and COVID-19 Outcomes between 01/12/2021 and 03/07/2021")
    plt.ylabel("Number of People Vaccinated and COVID Outcomes")
    plt.xlabel("Date")

    # Set x-axis ticks and format labels as mm-dd
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

    # Add units to the y-axis scale
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'{x:,.0f}'))

    # Add legend color patches
    legend_handles = [Patch(facecolor=colors[i], label=lab) for i, lab in
                      enumerate(['People Vaccinated', 'Deaths', 'Recovered'])]
    plt.legend(handles=legend_handles)

    plt.tick_params(axis='x', labelrotation=90, labelsize=10)
    plt.tight_layout()
    plt.savefig("2_people_vaccinated_and_covid_outcomes_trend.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("2_people_vaccinated_and_covid_outcomes_trend.png saved.")


def plot_total_cases_and_outcomes(data):
    # Filter data for the specified date
    data = data[data['date'] == '2021-03-07']

    # Set color palette
    colors = sns.color_palette("Greys", n_colors=9)

    # Create bar plots for the total number of cases
    fig, ax = plt.subplots(figsize=(8, 4))

    categories = ['Positive', 'Negative', 'Pending', 'Hospitalized', 'Deaths', 'Recovered']
    values = data[['positive', 'negative', 'pending', 'hospitalized', 'death', 'recovered']].values[0].tolist()

    bars = ax.bar(categories, values, color=colors[4])

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:,.0f}', ha='center', va='bottom',
                fontsize=10)

    ax.set_title('COVID-19 Cases and Outcomes')
    ax.set_ylabel('Number of People')

    # Add units to the y-axis scale
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))

    plt.savefig("3_cumulative_covid_cases_and_outcomes.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("3_cumulative_covid_cases_and_outcomes.png saved.")


def plot_us_map(data):
    # Filter data for the specified date
    data = data[data['date'] == '2021-03-07'].copy()

    # Dictionary to map state abbreviations to full names
    state_abbr_to_name = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
        'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
        'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
        'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
        'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
        'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
        'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
    }

    # Add full state name to the DataFrame
    data['state_full'] = data['state'].map(state_abbr_to_name)

    # Fill missing values with 'No Value'
    data['peopleVaccinated'] = data['peopleVaccinated'].fillna("No Data")
    data['positive'] = data['positive'].fillna("No Data")
    data['negative'] = data['negative'].fillna("No Data")
    data['pending'] = data['pending'].fillna("No Data")
    data['hospitalized'] = data['hospitalized'].fillna("No Data")
    data['onVentilator'] = data['onVentilator'].fillna("No Data")
    data['recovered'] = data['recovered'].fillna("No Data")
    data['death'] = data['death'].fillna("No Data")

    # Create the interactive map
    fig = px.choropleth(
        data,
        locations='state',
        color='peopleVaccinated',
        hover_name='state_full',
        hover_data={
            'peopleVaccinated': True,
            'positive': True,
            'negative': True,
            'pending': True,
            'hospitalized': True,
            'onVentilator': True,
            'recovered': True,
            'death': True
        },
        locationmode='USA-states',
        scope='usa',
        color_continuous_scale='Greys'
    )

    # Customize the colorbar
    fig.update_layout(
        coloraxis_colorbar=dict(
            title='People Vaccinated',
            tickvals=list(range(1000000, 8000000, 1000000)),
            tickformat=',.0f',
        )
    )

    # Customize title alignment
    fig.update_layout(
        title={
            'text': 'COVID Cases and Outcomes in each State',
            'x': 0.5,
            'xanchor': 'center'
        }
    )

    # Save the interactive map as an HTML file
    fig.write_html("4_map_covid_cases_and_outcomes.html")
    print("4_map_covid_cases_and_outcomes.html saved.")


if __name__ == "__main__":
    # Read the summary data from the Excel file
    summary_data = pd.read_excel("7_summary_usa_covid+vaccination_data.xlsx", engine='openpyxl')

    # Read the merged data from the Excel file
    merged_data = pd.read_excel("6_merged_usa_covid+vaccination_data.xlsx", engine='openpyxl')

    # Call the visualization functions
    plot_vaccination_and_covid_cases_trend(summary_data)
    plot_vaccination_and_covid_outcomes_trend(summary_data)
    plot_total_cases_and_outcomes(summary_data)
    plot_us_map(merged_data)
