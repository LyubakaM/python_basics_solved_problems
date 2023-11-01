player_one = input()
player_two = input()
player_one_score = 0
player_two_score = 0


while True:
    player_one_card = input()
    if player_one_card == "End of game":
        print(f"{player_one} has {player_one_score} points")
        print(f"{player_two} has {player_two_score} points")
        break
    player_two_card = int(input())
    player_one_card = int(player_one_card)

    difference_score = abs(player_one_card - player_two_card)

    if player_one_card > player_two_card:
        player_one_score += difference_score
    elif player_one_card < player_two_card:
        player_two_score += difference_score
    else:
        player_one_card = int(input())
        player_two_card = int(input())
        if player_one_card > player_two_card:
            winner = player_one
            winner_points = player_one_score + difference_score
        elif player_one_card < player_two_card:
            winner = player_two
            winner_points = player_two_score + difference_score
        print("Number wars!")
        print(f"{winner} is winner with {winner_points} points")
        break

#first_name = input()
#second_name = input()

#p1 = 0
#p2 = 0
#counter = 0

#while True:
    #command = input()
    ## command == "End of game":
        #print(f"{first_name} has {p1} points")
        #print(f"{second_name} has {p2} points")
        #break

    #p2_digit = int(input())
    #p1_digit = int(command)

    #if p1_digit > p2_digit:
        #result = p1_digit - p2_digit
        #p1 += result
    #elif p2_digit > p1_digit:
        #result = p2_digit - p1_digit
        #p2 += result
    #if p1_digit == p2_digit:
        #print(f"Number wars!")
        #p1_war = int(input())
        #p2_war = int(input())
        #if p1_war > p2_war:
            #print(f"{first_name} is winner with {p1} points")
            #break
        #else:
            #print(f"{second_name} is winner with {p2} points")
            #break


