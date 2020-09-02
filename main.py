#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np

from easy21 import Easy21


if __name__ == "__main__":
    env = Easy21()

    dealer, player = env.reset()
    while True:
        state = (dealer, player)
        action = np.random.randint(0, 2)
        next_state, reward = env.step(state, action)

        print('(dealer, player):', next_state)

        if not next_state:  # terminated
            print('Reward:', reward)
            break

        dealer, player = next_state
