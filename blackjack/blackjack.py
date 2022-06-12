import random, sys

DIAMONDS = chr(9830)
SPADES = chr(9824)
HEARTS = chr(9829)
CLUBS = chr(9827)
BACKSIDE = "backside"


def main():
    show_rules()

    money = 100

    while True:
        check_has_money(money)

        print(f"Money: {money}")
        bet = get_bet(money)
        print(f"Bet: {bet}")

        deck = get_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        while True:
            display_hands(player_hand, dealer_hand, False)

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == "D":
                additional_bet = get_bet(min(bet, money - bet))
                bet += additional_bet
                print(f"Bet increased to {bet}")
                print(f"Bet: {bet}")

            if move in ("H", "D"):
                new_card = deck.pop()

                rank, suit = new_card
                print(f"You drew a {rank} of {suit}")

                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ("S", "D"):
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break

                input("Press enter to continue...")

        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif player_value > 21 or (player_value < dealer_value):
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won ${bet}!")
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, the bet is returned to you.")

        input("\nPress enter to continue...")

        print()


def show_rules():
    print(
        """
Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
    """
    )


def check_has_money(money):
    if money <= 0:
        print("You're broke!")
        print("Thanks for playing!")
        sys.exit()


def get_bet(max_bet):
    while True:
        bet = input(f"How much do you bet? (1 - {max_bet}) or QUIT: ").strip().upper()

        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)

        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []

    for suit in (DIAMONDS, SPADES, HEARTS, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("Q", "J", "K", "A"):
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    if show_dealer_hand:
        display_cards(dealer_hand)
        print(f"Dealer: {get_hand_value(dealer_hand)}")
    else:
        display_cards([BACKSIDE] + dealer_hand[1:])
        print(f"Dealer: ??")

    display_cards(player_hand)
    print(f"Player: {get_hand_value(player_hand)}")

    print()


def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]

        if rank == "A":
            number_of_aces += 1
        elif rank in ("Q", "J", "K"):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces

    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    rows = ["" for i in range(4)]

    for card in cards:
        rows[0] += " ___ "

        if card == BACKSIDE:
            rows[1] += "|## |"
            rows[2] += "|###|"
            rows[3] += "|_##|"
        else:
            rank, suit = card

            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:
        moves = ["(H)it", "(S)tand"]

        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        move_prompt = ", ".join(moves) + ": "

        move = input(move_prompt).upper()

        if move in ("H", "S"):
            return move
        elif move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()
