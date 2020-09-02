#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np


class Easy21:
    """
    - The game is played with an infinite deck of cards (i.e. cards are sampled with replacement)
    - Each draw from the deck results in a value between 1 and 10 (uniformly distributed) \
      with a colour of red (probability 1/3) or black (probability 2/3).
    - There are no aces or pictures (face) cards in this game.
    - At the start of the game both the player and the dealer draw one black card (fully observed)
    - Each turn the player may either `stick` or `hit`
    - If the player hits then she draws another card from the deck
    - If the player sticks she receives no further cards
    - The values of the player's cards are added (black cards) or subtracted (red cards)
    - If the player's sum exceeds 21, or becomes less than 1, then she "goes bust" and loses the game (reward -1)
    - If the player sticks then the dealer starts taking turns. The dealer always sticks \
      on any sum of 17 or greater, and hits otherwise. If the dealer goes bust, \
      then the player wins; otherwise, the outcome - win (reward +1), lose (reward -1), or draw (reward 0) \
      - is the player with the largest sum.
    """
    ACTION_STICK = 0
    ACTION_HIT = 1

    def __init__(self):
        self.action_space = (0, 1)

    def reset(self):
        dealer = self.draw_card(True)
        player = self.draw_card(True)
        return dealer, player

    def step(self, state, action):
        """
        Args:
            state: dealer's first card 1-10 and the player's sum 1-21. None if terminated.
            action: hit or stick
        Returns:
            a sample of the next state s`, which may be terminal
            if the game is finished, and reward r.
        """
        dealer, player_sum = state
        if action == Easy21.ACTION_STICK:
            next_state = None
            reward = self.__play_out(player_sum, dealer)
        elif action == Easy21.ACTION_HIT:
            new_player_sum = player_sum + self.draw_card()
            if self.goes_bust(new_player_sum):
                next_state = None
                reward = -1
            else:
                next_state = (dealer, new_player_sum)
                reward = 0
        return next_state, reward

    def draw_card(self, start_of_the_game=False):
        value_variable = np.random.uniform()
        value = int(value_variable * 10) + 1
        color_variable = np.random.uniform()
        red_probability = 1 / 3
        if start_of_the_game:
            sign = 1.0
        else:
            sign = np.sign(color_variable - red_probability)
        return int(value * sign)

    def goes_bust(self, score):
        return not 1 <= score <= 21

    def __play_out(self, player, dealer):
        while dealer < 17:  # stick threshold
            dealer += self.draw_card()
            if self.goes_bust(dealer):
                return 1
        return int(np.sign(player - dealer))


if __name__ == "__main__":
    pass
