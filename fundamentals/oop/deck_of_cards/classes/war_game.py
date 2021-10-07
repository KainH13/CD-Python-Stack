import player

class War:
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        self.player1 = player.Player(player1_name)
        self.player2 = player.Player(player2_name)


    def play_round(self):
        self.player1.flip_card()
        player1_card = self.player1.current_card.point_val
        self.player2.flip_card()
        player2_card = self.player2.current_card.point_val
        
        if player1_card > player2_card:
            self.player1.score += 1
            print(f"{self.player1.name} wins the round! Their score is now {self.player1.score}")
            return self
        if player2_card > player1_card:
            self.player2.score += 1
            print(f"{self.player2.name} wins the round! Their score is now {self.player2.score}")
            return self
        if player1_card == player2_card:
            print("We have a draw! Each player must now draw three cards and reveal the last.")
            self.player1.flip_card().flip_card().flip_card()
            player1_card = self.player1.current_card.point_val
            self.player2.flip_card().flip_card().flip_card()
            player2_card = self.player2.current_card.point_val
            if player1_card > player2_card:
                self.player1.score += 3
                print(f"{self.player1.name} wins the draw! Their score is now {self.player1.score}")
                return self
            if player2_card > player1_card:
                self.player2.score += 3
                print(f"{self.player2.name} wins the draw! Their score is now {self.player2.score}")
                return self
            if player1_card == player2_card:
                print("Stalemate: No Score")
                return self


if __name__ == "__main__":
    war_game = War()
    war_game.play_round()
