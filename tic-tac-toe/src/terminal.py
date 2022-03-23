# Copyright (C) 2022 Gaëtan LE HEURT-FINOT
# This file is part of RL Playground <https://github.com/gaetanlhf/RL-Playground>.

# RL Playground is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# RL Playground is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with RL Playground.  If not, see <http://www.gnu.org/licenses/>.

class Terminal():
    def __init__(self):
        print("Tic-tac-toe with reinforcement algorithm.")
        print("By Gaëtan LE HEURT-FINOT in L3 S&T-MN for AI course.")

    def learningLevel(self, actualPeriod, period):
        print("Learning: " + str(round((actualPeriod/period)*100, 2)) + "%")

    def showWinner(self, id):
        print("Agent " + str(id) + " won!")

    def message(self, text):
        print(text)

    def input(self, text):
        return input(text)
