import random

# Create a deck of cards
deck = [value for value in range(2, 15) for _ in range(4)]

list_of_game_length = []

num_og_games_played = 100000

print_out_game = False

for iteration in range(num_og_games_played):

    # Shuffle the deck
    random.shuffle(deck)

    # Split the deck into two
    player_A_deck = deck[:len(deck)//2]
    player_B_deck = deck[len(deck)//2:]


    # Function to play a round
    def play_round(player_A_deck, player_B_deck, table_stack, round_number):
        # print(player_A_deck)
        # print(player_B_deck)

        # Deck sizes
        player_A_deck_size = len(player_A_deck)
        player_B_deck_size = len(player_B_deck)

        # Players play a card
        played_card_A = player_A_deck.pop()
        played_card_B = player_B_deck.pop()

        # Add played cards to the table stack in random order
        table_stack.extend(random.sample([played_card_A, played_card_B], 2))

        # Compare the cards
        if played_card_A > played_card_B:
            player_A_deck = table_stack + player_A_deck
            result = "Player A wins"
            table_stack = []
        elif played_card_B > played_card_A:
            player_B_deck = table_stack + player_B_deck
            result = "Player B wins"
            table_stack = []
        else:
            if print_out_game:
                print(f"round {round_number}:\tPlayer A ({player_A_deck_size}): {played_card_A}  \tPlayer B ({player_B_deck_size}): {played_card_B}\t\tDRAW, flip 3 extra")
            if len(player_A_deck) < 3 or len(player_B_deck) < 3:
                if len(player_A_deck) == len(player_B_deck):
                    return player_A_deck, player_B_deck, "It's a DRAW", True
                if len(player_A_deck) > len(player_B_deck):
                    return player_A_deck, player_B_deck, "Player A wins", True
                if len(player_A_deck) < len(player_B_deck):
                    return player_A_deck, player_B_deck, "Player B wins", True
            table_stack.extend(random.sample([player_A_deck.pop(), player_B_deck.pop()], 2))
            table_stack.extend(random.sample([player_A_deck.pop(), player_B_deck.pop()], 2))
            if print_out_game:
                print("1\n2\n3")
            return play_round(player_A_deck, player_B_deck, table_stack, round_number)

        if print_out_game:
            print(f"round {round_number}:\tPlayer A ({player_A_deck_size}): {played_card_A}  \tPlayer B ({player_B_deck_size}): {played_card_B}  \t\t{result}")
        return player_A_deck, player_B_deck, result, False

    # Game loop
    round_number = 1
    while player_A_deck and player_B_deck:
        # if round_number > 20:
        #     exit()
        player_A_deck, player_B_deck, result, game_over = play_round(player_A_deck, player_B_deck, [], round_number)
        if game_over:
            break
        round_number += 1

    if print_out_game:
        print("FINAL RESULT: " + result)
    list_of_game_length.append(round_number)

print("\n")
# print(list_of_game_length)
print(int(sum(list_of_game_length)/len(list_of_game_length)))