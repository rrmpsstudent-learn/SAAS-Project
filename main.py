from unittest import case

lazy import to_df as f
lazy import pandas as pd
lazy import matplotlib.pyplot as plt

teamStandings = f.data_organizer('ipl_2024_team_standings.csv')
topBatters = f.data_organizer('ipl_2024_top_batters.csv')
topBatters26 = f.data_organizer('ipl_career_top_batters_2026.csv')
ttwcBatting = f.data_organizer('t20_world_cup_2024_batting.csv')
ttwcBowling = f.data_organizer('t20_world_cup_2024_bowling_leaders.csv')
ttwcKnockouts = f.data_organizer('t20_world_cup_2024_knockout_matches.csv')

def main():
    while True:
        # Choose League
        choice = int(input('Select league(1 : IPL, 2 : T20): '))
        if (choice == 1):
            choice = int(input('Select Base Data(1 : Team Standings 2024, 2 : Top Batters 2024, 3 : Top Batters 2026): '))
            match choice:
                case 1:
                    print(teamStandings.columns[3:])
                    choice1 = input('Select the parameter against name to visualize: ')
                    plt.bar(teamStandings['team'], teamStandings[choice1], color='red')
                    plt.grid(True)
                    plt.xlabel('Team')
                    plt.ylabel(choice1)
                    plt.show()
                    plt.yticks(teamStandings[choice1])
                case 2:
                    pass
                case 3:
                    pass
        elif (choice == 2):
            choice = int(input('Select Base Data(1 : Batting, 2 : Bowling Leaders, 3 : Knockout Matches): '))
        else:
            print('Invalid choice, try again!')
            continue

main()