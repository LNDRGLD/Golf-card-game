from random import shuffle

class Card:
    SUITS = {
        "spades": "\u2664",
        "hearts": "\u2661",
        "diamonds": "\u2662",
        "clubs": "\u2667",
    }

    def __init__(self, rank, suit):
        if rank not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            raise ValueError("Invalid rank. Rank must be one of 'A', '2', ..., 'K'.")
        self.rank = rank
        self.suit = suit.lower()
        self.faceUp = True

    def flip(self):
        self.faceUp = not self.faceUp

    def show_card(self):
        if self.faceUp:
            return f"{self.rank.upper()}{self.SUITS[self.suit]}"
        else:
            return "🂠"

    def get_value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 1
        else:
            return int(self.rank) if self.rank.isdigit() else 10  # Return 10 for 'T'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['hearts', 'diamonds', 'clubs', 'spades']:  # lowercase suits
            for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
                self.cards.append(Card(rank, suit))

    def draw(self) -> Card:
        card = self.cards.pop()
        card.flip()
        return card
    
    def shuffle(self):
        shuffle(self.cards)

    def draw_face_up(self) -> Card:
        card = self.cards.pop()
        card.flip()
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck, face_up=False):
        if face_up:
            card = deck.draw_face_up()
        else:
            card = deck.draw()
        self.hand.append(card)

    def show_hand(self):
        rows = [""] * 2
        for i, card in enumerate(self.hand):
            row_index = i // 3
            rows[row_index] += f"{card.show_card()} "
        for row in rows:
            print(row)

    def calculate_score(self):
        score = 0
        for card in self.hand:
            score += card.get_value()
        return score

def main():
    deck = Deck()
    deck.shuffle()

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for _ in range(6):
        player1.draw_card(deck)
        player2.draw_card(deck)

    print("Player 1's hand (face down):")
    player1.show_hand()

    print("=============================")
    print("\nPlayer 2's hand (face down):")
    player2.show_hand()

    print("\nPlayers choose two cards to flip (1-6):")
    for _ in range(2):  # Each player flips two cards
        for player in [player1, player2]:
            print(f"\n{player.name}'s turn:")
            for i in range(2):  # Each player flips two cards
                while True:
                    choice = int(input("Choose a card to flip (1-6): "))
                    if 1 <= choice <= 6:
                        if not player.hand[choice - 1].faceUp:
                            player.hand[choice - 1].flip()
                            break
                        else:
                            print("Card is already face up. Choose another card.")
                    else:
                        print("Invalid choice. Choose a number between 1 and 6.")

            # Display hands after each player's turn
            print("\nPlayer 1's hand:")
            player1.show_hand()
            print("\nPlayer 2's hand:")
            player2.show_hand()

    # Open all cards before calculating scores
    for player in [player1, player2]:
        for card in player.hand:
            card.flip()

    print("\nFinal hands:")
    print("Player 1's hand:")
    player1.show_hand()
    for card in player1.hand:
        if not card.faceUp:  # If the card is not face up, flip it
            card.flip()
    print("\nPlayer 2's hand:")
    player2.show_hand()
    for card in player2.hand:
        if not card.faceUp:  # If the card is not face up, flip it
            card.flip()

    # Calculate and display final scores
    print("\nPlayer 1's score:", player1.calculate_score())
    print("Player 2's score:", player2.calculate_score())
    # Determine the winner
    score1 = player1.calculate_score()
    score2 = player2.calculate_score()

    if score1 < score2:
        print("Player 1 wins!")
    elif score1 > score2:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
