
import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# 1. LOAD ALL DATASETS
# ==================================================

files = {
    "IPL Team Standings 2024": "ipl_2024_team_standings.csv",
    "IPL Top Batters 2024": "ipl_2024_top_batters.csv",
    "IPL Top Batters 2026": "ipl_career_top_batters_2026.csv",
    "T20 WC Batting": "t20_world_cup_2024_batting.csv",
    "T20 WC Bowling": "t20_world_cup_2024_bowling_leaders.csv",
    "T20 WC Knockouts": "t20_world_cup_2024_knockout_matches.csv"
}

datasets = {}

for name, filename in files.items():
    try:
        datasets[name] = pd.read_csv(filename)
        print(name, "loaded successfully!")

    except FileNotFoundError:
        print("File not found:", filename)


# ==================================================
# 2. DATASET CONFIGURATION
# ==================================================

dataset_settings = {

    "IPL Team Standings 2024": {
        "name_column": "team",
        "parameters": [
            "matches", "wins", "losses",
            "ties", "no_results", "points"
        ]
    },

    "IPL Top Batters 2024": {
        "name_column": "player",
        "parameters": [
            "matches", "innings", "runs",
            "batting_average", "strike_rate",
            "fours", "sixes", "boundary_runs"
        ]
    },

    "IPL Top Batters 2026": {
        "name_column": "player",
        "parameters": [
            "matches", "innings", "runs",
            "balls_faced", "highest_score",
            "batting_average", "strike_rate",
            "not_outs", "fours", "sixes",
            "fifties", "hundreds"
        ]
    },

    "T20 WC Batting": {
        "name_column": "player",
        "parameters": [
            "matches", "innings", "runs",
            "batting_average", "strike_rate",
            "fours", "sixes"
        ]
    },

    "T20 WC Bowling": {
        "name_column": "player",
        "parameters": [
            "wickets", "bowling_average"
        ]
    },

    "T20 WC Knockouts": {
        "name_column": "stage",
        "parameters": [
            "team_1_runs", "team_2_runs"
        ]
    }
}


# ==================================================
# 3. PREPARE KNOCKOUT MATCH DATA
# ==================================================

if "T20 WC Knockouts" in datasets:

    knockout_data = datasets["T20 WC Knockouts"]

    # Extract runs from scores such as 171/7
    knockout_data["team_1_runs"] = pd.to_numeric(
        knockout_data["team_1_score"].str.extract(
            r"(\d+)"
        )[0],
        errors="coerce"
    )

    knockout_data["team_2_runs"] = pd.to_numeric(
        knockout_data["team_2_score"].str.extract(
            r"(\d+)"
        )[0],
        errors="coerce"
    )


# ==================================================
# 4. INPUT VALIDATION FUNCTION
# ==================================================

def get_choice(message, minimum, maximum):

    while True:

        try:
            choice = int(input(message))

            if minimum <= choice <= maximum:
                return choice

            print("Invalid choice! Please try again.")

        except ValueError:
            print("Please enter a valid number.")


# ==================================================
# 5. VISUALIZATION FUNCTION
# ==================================================

def visualize_data(data, dataset_name):

    settings = dataset_settings[dataset_name]

    name_column = settings["name_column"]
    numeric_columns = settings["parameters"]

    # Check whether the selected dataset has valid columns
    numeric_columns = [
        column for column in numeric_columns
        if column in data.columns
    ]

    if name_column not in data.columns:
        print("Name column not found!")
        return

    if not numeric_columns:
        print("No numerical parameters available!")
        return

    # Display available parameters
    print("\nAvailable Parameters:")

    for i, column in enumerate(numeric_columns, 1):
        print(i, ":", column)

    parameter_choice = get_choice(
        "\nSelect parameter: ",
        1,
        len(numeric_columns)
    )

    parameter = numeric_columns[parameter_choice - 1]

    # Display graph options
    print("\n========== GRAPH MENU ==========")
    print("1 : Bar Graph")
    print("2 : Horizontal Bar Graph")
    print("3 : Line Graph")
    print("4 : Histogram")

    graph_choice = get_choice(
        "\nSelect graph type: ", 1, 4
    )

    # Convert selected column into numerical data
    values = pd.to_numeric(
        data[parameter],
        errors="coerce"
    )

    # Remove missing or invalid values
    valid_data = data.loc[values.notna()].copy()

    if valid_data.empty:
        print("No valid numerical data available!")
        return

    valid_values = pd.to_numeric(
        valid_data[parameter],
        errors="coerce"
    )

    # Create graph
    plt.figure(figsize=(10, 6))

    if graph_choice == 1:

        plt.bar(
            valid_data[name_column].astype(str),
            valid_values,
            color="red"
        )

        plt.xlabel(name_column)
        plt.ylabel(parameter)
        plt.xticks(rotation=45, ha="right")

    elif graph_choice == 2:

        plt.barh(
            valid_data[name_column].astype(str),
            valid_values,
            color="steelblue"
        )

        plt.xlabel(parameter)
        plt.ylabel(name_column)

    elif graph_choice == 3:

        plt.plot(
            valid_data[name_column].astype(str),
            valid_values,
            marker="o",
            color="green"
        )

        plt.xlabel(name_column)
        plt.ylabel(parameter)
        plt.xticks(rotation=45, ha="right")

    elif graph_choice == 4:

        plt.hist(
            valid_values,
            bins=10,
            color="orange",
            edgecolor="black"
        )

        plt.xlabel(parameter)
        plt.ylabel("Frequency")

    # Graph formatting
    plt.title(dataset_name + " - " + parameter)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    plt.show()


# ==================================================
# 6. MAIN PROGRAM
# ==================================================

print("\n======================================")
print("       CRICKET DATA ANALYSIS")
print("======================================")

print("\n1 : Indian Premier League (IPL)")
print("2 : T20 World Cup")

league_choice = get_choice(
    "\nSelect league: ", 1, 2
)


# ==================================================
# 7. DATASET SELECTION
# ==================================================

if league_choice == 1:

    selected_datasets = [
        "IPL Team Standings 2024",
        "IPL Top Batters 2024",
        "IPL Top Batters 2026"
    ]

else:

    selected_datasets = [
        "T20 WC Batting",
        "T20 WC Bowling",
        "T20 WC Knockouts"
    ]


# Display available datasets only
available_datasets = [
    name for name in selected_datasets
    if name in datasets
]

if not available_datasets:

    print("\nNo datasets available!")

else:

    print("\n========== DATASET MENU ==========")

    for i, name in enumerate(available_datasets, 1):
        print(i, ":", name)

    dataset_choice = get_choice(
        "\nSelect dataset: ",
        1,
        len(available_datasets)
    )

    dataset_name = available_datasets[
        dataset_choice - 1
    ]

    data = datasets[dataset_name]

    print("\nSelected Dataset:", dataset_name)

    # Display dataset
    print("\nDataset Preview:")
    print(data.head())

    # Generate visualization
    visualize_data(data, dataset_name)


# ==================================================
# 8. END OF PROGRAM
# ==================================================

print("\n======================================")
print("       ANALYSIS COMPLETED")
print("======================================")
