import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch

# Set plotting style
sns.set_style("whitegrid")

def plot_vaccination_and_covid_cases(data):
    # Sort data by the number of people vaccinated
    data = data.sort_values(by='peopleVaccinated', ascending=False)

    # Set color palette
    colors = ['#4c72b0', '#c44e52', '#55a868']

    # Create a bar chart for the number of people vaccinated, positive cases, and negative cases
    plt.figure(figsize=(16, 6))
    sns.barplot(data=data, x='state', y='peopleVaccinated', color=colors[0], alpha=0.8)
    sns.barplot(data=data, x='state', y='positive', color=colors[1], alpha=0.8)
    sns.barplot(data=data, x='state', y='negative', color=colors[2], alpha=0.8)
    plt.title("Number of People Vaccinated and COVID-19 Cases in each state as of 2021-03-07")
    plt.ylabel("Number of People Vaccinated and COVID Cases")
    plt.xlabel("State")
    plt.legend(['People Vaccinated', 'Positive Cases', 'Negative Cases'])
    plt.tick_params(axis='x', labelrotation=90, labelsize=10)
    # Add legend color patches
    legend_handles = [Patch(facecolor=colors[i], label=lab) for i, lab in
                      enumerate(['People Vaccinated', 'Positive Cases', 'Negative Cases'])]
    plt.legend(handles=legend_handles)
    plt.tight_layout()
    plt.savefig("people_vaccinated_and_covid_cases_in_each_state.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("people_vaccinated_and_covid_cases_in_each_state.png saved.")

def plot_total_cases(data):
    # Calculate the total number of cases
    total_negative = data['negative'].sum()
    total_positive = data['positive'].sum()
    total_pending = data['pending'].sum()
    total_hospitalized = data['hospitalized'].sum()
    total_onVentilator = data['onVentilator'].sum()
    total_recovered = data['recovered'].sum()
    total_deaths = data['death'].sum()

    # Create pie charts for the total number of cases
    fig, axs = plt.subplots(2, 2, figsize=(16, 16))
    axs[0, 0].pie([total_negative, total_positive, total_pending], labels=['Negative', 'Positive', 'Pending'], autopct='%1.1f%%', startangle=90, colors=['#55a868', '#c44e52', '#4c72b0'])
    axs[0, 0].set_title('COVID-19 Cases')
    axs[0, 1].pie([total_hospitalized, total_onVentilator, total_recovered, total_deaths], labels=['Hospitalized', 'On Ventilator', 'Recovered', 'Deaths'], autopct='%1.1f%%', startangle=90, colors=['#4c72b0', '#55a868', '#f6c85f', '#c44e52'])
    axs[0, 1].set_title('COVID-19 Outcomes')
    axs[1, 0].remove()
    axs[1, 1].remove()
    plt.savefig("total_cases_combined.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("total_cases_combined.png saved.")

if __name__ == "__main__":
    # Read the merged data from the Excel file
    merged_data = pd.read_excel("merged_usa_covid+vaccination_data.xlsx", engine='openpyxl')

    # Call the visualization functions
    plot_vaccination_and_covid_cases(merged_data)
    plot_total_cases(merged_data)