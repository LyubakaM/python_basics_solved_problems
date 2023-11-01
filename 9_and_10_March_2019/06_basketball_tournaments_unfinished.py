tournament_name = input()

wins = 0
loses = 0

while tournament_name != "End of tournaments":
    number_of_games = int(input())

    for game in range(1, number_of_games + 1):
        home_team = int(input())
        away_team = int(input())
        difference = abs(home_team - away_team)

        if home_team > away_team:
            wins += 1
            result = "win"

        elif home_team < away_team:
            loses += 1
            result = "lost"

        print(f"Game {game} of tournament {tournament_name}: {result} with {difference} points.")

    tournament_name = input()

print(f"{(wins / (wins + loses)) * 100:.2f}% matches win")
print(f"{(loses / (wins + loses)) * 100:.2f}% matches lost")


#won = 0
#loss = 0
#big_counter = 0
#while True:
    #command = input()
    #if command == "End of tournaments":
        #break
    #number_of_tournaments = int(input())
    #counter = 0
    #for games in range(number_of_tournaments):
        #first_score = int(input())
        #second_score = int(input())
        #counter += 1
        #big_counter += 1
        #if first_score - second_score > 0:
            #won += 1
            #print(f"Game {counter} of tournament {command}: win with {first_score - second_score} points.")
        #else:
            #loss += 1
            #print(f"Game {counter} of tournament {command}: lost with {abs(first_score - second_score)} points.")
#ave_won = (won / big_counter) * 100
#ave_loss = (loss / big_counter) * 100

#print(f"{ave_won:.2f}% matches win")
#