import to_df as f
import matplotlib.pyplot as plt

teamStandings = f.data_organizer('ipl_2024_team_standings.csv')
topBatters = f.data_organizer('ipl_2024_top_batters.csv')
topBatters26 = f.data_organizer('ipl_career_top_batters_2026.csv')
ttwcBatting = f.data_organizer('t20_world_cup_2024_batting.csv')
ttwcBowling = f.data_organizer('t20_world_cup_2024_bowling_leaders.csv')
ttwcKnockouts = f.data_organizer('t20_world_cup_2024_knockout_matches.csv')

def main():
    while True:
        # Choose League
        choice = int(input('Select league(1 : IPL, 2 : T20 World Cup): '))
        if (choice == 1):
            choice = int(input('Select Base Data(1 : Team Standings 2024, 2 : Top Batters 2024, 3 : Top Batters 2026): '))
            match choice:
                case 1:
                    print(teamStandings.columns[3:])
                    choice1 = input('Select the parameter against name to visualize: ')
                    print("1 : Bar, 2 : HBar, 3 : Line, 4 : Histogram")
                    choice2 = int(input('What type of graph do you want: '))
                    match choice2:
                        case 1:
                            plt.bar(teamStandings['team'], teamStandings[choice1], color='red')
                        case 2:
                            plt.barh(teamStandings['team'], teamStandings[choice2])
                        case 3:
                            plt.plot(teamStandings['team'], teamStandings[choice1])
                        case 4:
                            plt.hist(teamStandings['team'], teamStandings[choice2])
                    plt.xlabel('Team')
                    plt.ylabel(choice1)
                    plt.show()
                case 2:
                    print(topBatters.columns[3:])
                    choice1 = input('Select the parameter against name to visualize: ')
                    print("1 : Bar, 2 : HBar, 3 : Line, 4 : Histogram")
                    choice2 = int(input('What type of graph do you want: '))
                    match choice2:
                        case 1:
                            plt.bar(topBatters['team'], topBatters[choice1], color='red')
                        case 2:
                            plt.barh(topBatters['team'], topBatters[choice2])
                        case 3:
                            plt.plot(topBatters['team'], topBatters[choice1])
                        case 4:
                            plt.hist(topBatters['team'], topBatters[choice2])
                    plt.xlabel('Player')
                    plt.ylabel(choice1)
                    plt.show()
                case 3:
                    print(topBatters26.columns[4:])
                    choice1 = input('Select the parameter against name to visualize: ')
                    print("1 : Bar, 2 : HBar, 3 : Line, 4 : Histogram")
                    choice2 = int(input('What type of graph do you want: '))
                    match choice2:
                        case 1:
                            plt.bar(topBatters26['team'], topBatters26[choice1], color='red')
                        case 2:
                            plt.barh(topBatters26['team'], topBatters26[choice2])
                        case 3:
                            plt.plot(topBatters26['team'], topBatters26[choice1])
                        case 4:
                            plt.hist(topBatters26['team'], topBatters26[choice2])
                    plt.xlabel('Player')
                    plt.ylabel(choice1)
                    plt.show()
        elif (choice == 2):
            choice = int(input('Select Base Data(1 : Batting Data, 2 : Bowling Data, 3 : Knockout Matches Data): '))
            match choice:
                case 1:
                    print(ttwcBatting.columns[4:])
                    choice1 = input('Select the parameter against name to visualize: ')
                    print("1 : Bar, 2 : HBar, 3 : Line, 4 : Histogram")
                    choice2 = int(input('What type of graph do you want: '))
                    match choice2:
                        case 1:
                            plt.bar(ttwcBatting['team'], ttwcBatting[choice1], color='red')
                        case 2:
                            plt.barh(ttwcBatting['team'], ttwcBatting[choice2])
                        case 3:
                            plt.plot(ttwcBatting['team'], ttwcBatting[choice1])
                        case 4:
                            plt.hist(ttwcBatting['team'], ttwcBatting[choice2])
                    plt.xlabel('Team')
                    plt.ylabel(choice1)
                    plt.show()
                case 2:
                    print(ttwcBowling.columns[4:7])
                    choice1 = input('Select the parameter against name to visualize: ')
                    print("1 : Bar, 2 : HBar, 3 : Line, 4 : Histogram")
                    choice2 = int(input('What type of graph do you want: '))
                    match choice2:
                        case 1:
                            plt.bar(ttwcBowling['team'], ttwcBowling[choice1], color='red')
                        case 2:
                            plt.barh(ttwcBowling['team'], ttwcBowling[choice2])
                        case 3:
                            plt.plot(ttwcBowling['team'], ttwcBowling[choice1])
                        case 4:
                            plt.hist(ttwcBowling['team'], ttwcBowling[choice2])
                    plt.xlabel('Player')
                    plt.ylabel(choice1)
                    plt.show()
                case 3:
                    print(ttwcKnockouts)
        else:
            print('Invalid choice, try again!')
            continue

main()