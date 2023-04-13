import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import seaborn as sns
from matplotlib.patches import Patch

# Set plotting style
sns.set_style("whitegrid")

def plot_vaccination_and_covid_cases(data):
    # Convert 'date' column to datetime with desired format
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

    # Filter data for the specified date range
    date_range = pd.date_range(start='2021-01-12', end='2021-03-07')
    filtered_data = data[data['date'].isin(date_range)]
    print(filtered_data.head())
    if filtered_data.empty:
        print("No data available for the specified date range.")
        return

    # Set color palette
    colors = sns.color_palette("Greys", n_colors=9)

    # Create a scatter plot for the number of people vaccinated and COVID-19 cases
    plt.figure(figsize=(16, 6))
    plt.scatter(filtered_data['date'], filtered_data['peopleVaccinated'], color=colors[0], alpha=0.8)
    plt.scatter(filtered_data['date'], filtered_data['positive'], color=colors[1], alpha=0.8)
    plt.scatter(filtered_data['date'], filtered_data['negative'], color=colors[2], alpha=0.8)
    plt.title("Number of People Vaccinated and COVID-19 Cases between date 01/12/2021 and 03/07/2021")
    plt.ylabel("Number of People Vaccinated and COVID Cases")
    plt.xlabel("Date")

    # Set x-axis ticks and format labels as mm-dd
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

    # Add legend color patches
    legend_handles = [Patch(facecolor=colors[i], label=lab) for i, lab in
                      enumerate(['People Vaccinated', 'Positive Cases', 'Negative Cases'])]
    plt.legend(handles=legend_handles)

    plt.tick_params(axis='x', labelrotation=90, labelsize=10)
    plt.tight_layout()
    plt.savefig("1_people_vaccinated_and_covid_cases_vs_date.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("1_people_vaccinated_and_covid_cases_by_date.png saved.")

def plot_total_cases(data):
    # Filter data for the specified date
    data = data[data['date'] == '2021-03-07']

    # Set color palette
    colors = sns.color_palette("Greys", n_colors=9)

    # Create pie charts for the total number of cases
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    # Convert series objects to float before formatting
    positive_percent = float(data['positive']) * 100 / (float(data['positive']) + float(data['negative']) + float(data['pending']))
    negative_percent = float(data['negative']) * 100 / (float(data['positive']) + float(data['negative']) + float(data['pending']))
    pending_percent = float(data['pending']) * 100 / (float(data['positive']) + float(data['negative']) + float(data['pending']))
    hospitalized_percent = float(data['hospitalized']) * 100 / (float(data['hospitalized']) + float(data['death']) + float(data['recovered']))
    death_percent = float(data['death']) * 100 / (float(data['hospitalized']) + float(data['death']) + float(data['recovered']))
    recovered_percent = float(data['recovered']) * 100 / (float(data['hospitalized']) + float(data['death']) + float(data['recovered']))

    axs[0].pie(data[['positive', 'negative', 'pending']].values[0].tolist(),
               labels=[
                   f"Positive\n({positive_percent:.1f}%)",
                   f"Negative\n({negative_percent:.1f}%)",
                   f"Pending\n({pending_percent:.1f}%)"],
               autopct='',
               startangle=90, colors=colors[3:6], pctdistance=0.7, textprops={'fontsize': 10}, radius=1)
    axs[0].set_title('COVID-19 Cases')

    axs[1].pie(data[['hospitalized', 'death', 'recovered']].values[0].tolist(),
               labels=[
                   f"Hospitalized\n({hospitalized_percent:.1f}%)",
                   f"Deaths\n({death_percent:.1f}%)",
                   f"Recovered\n({recovered_percent:.1f}%)"],
               autopct='',
               startangle=90, colors=colors[3:6], pctdistance=0.7, textprops={'fontsize': 10})
    axs[1].set_title('COVID-19 Outcomes')

    plt.savefig("2_cumulative_covid_cases.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("2_cumulative_covid_cases.png saved.")

if __name__ == "__main__":
    # Read the merged data from the Excel file
    merged_data = pd.read_excel("7_summary_usa_covid+vaccination_data.xlsx", engine='openpyxl')

    # Call the visualization functions
    plot_vaccination_and_covid_cases(merged_data)
    plot_total_cases(merged_data)