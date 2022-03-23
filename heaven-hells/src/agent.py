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

import pandas
import numpy
import random


class Agent():
    def __init__(self, window, paradisList, enferList, terminal, col, row, ta, gamma, speed, epsilon, periode, color):
        self.window = window
        self.paradisList = paradisList
        self.enferList = enferList
        self.terminal = terminal
        self.col = col - 1
        self.row = row - 1
        self.epsilon = epsilon
        self.speed = speed
        self.gamma = gamma
        self.ta = ta
        self.periode = periode
        self.color = color
        self.defaultCol = self.col
        self.defaultRow = self.row
        self.actualPeriode = 1
        self.posXRect = self.defaultCol * 100
        self.posYRect = self.defaultRow * 100
        self.window.matrix[self.row, self.col] = 1
        self.actions = ["left", "right", "top", "bottom"]
        self.finish = False
        self.rect = self.window.canvas.create_rectangle(
            self.posXRect, self.posYRect, self.posXRect+100, self.posYRect+100, fill=self.color)
        self.q_table = pandas.DataFrame(
            columns=self.actions, dtype=numpy.float64)

    def update(self):
        self.window.canvas.delete(self.rect)
        self.rect = self.window.canvas.create_rectangle(
            self.posXRect, self.posYRect, self.posXRect+100, self.posYRect+100, fill=self.color)
        if not self.finish:
            self._chooseAction([self.posYRect, self.posXRect])
        else:
            self.posXRect, self.posYRect = self.defaultCol*100, self.defaultRow*100
            self.window.matrix[self.row, self.col] = 0
            self.row, self.col = self.defaultRow, self.defaultCol
            self.window.matrix[self.row, self.col] = 1
            for hell in self.enferList:
                self.window.matrix[hell.row, hell.col] = 3
            for heaven in self.paradisList:
                self.window.matrix[heaven.row, heaven.col] = 2
            self.finish = False
            self.actualPeriode += 1
            if self.ta > 0.01:
                self.ta -= 0.0005
        if self.periode >= self.actualPeriode:
            self.window.canvas.after(self.speed, self.update)

    def _chooseAction(self, E):
        try:
            self.q_table.loc[str(E)]
        except KeyError as err:
            self.q_table.loc[str(E)] = [0, 0, 0, 0]
        if random.uniform(0, 1) < self.epsilon:
            self._move(E)
        else:
            if self.q_table.loc[str(E)].max() != 0:
                max = self.q_table.idxmax(axis=1)
                self._move(E, max[str(E)])
            else:
                self._move(E)

    def _move(self, E, dir=None):
        if dir == None:
            dir = random.choice(self.actions)
        if dir == "left":
            if self.posXRect - 100 > 0:
                self.posXRect -= 100
                Eprime = [self.posYRect, self.posXRect]
                self._learn(E, dir, Eprime)
                self.window.matrix[self.row, self.col] = 0
                self.col -= 1
                self.window.matrix[self.row, self.col] = 1
        if dir == "right":
            if self.posXRect + 100 <= self.window.width - 100:
                self.posXRect += 100
                Eprime = [self.posYRect, self.posXRect]
                self._learn(E, dir, Eprime)
                self.window.matrix[self.row, self.col] = 0
                self.col += 1
                self.window.matrix[self.row, self.col] = 1
        if dir == "top":
            if self.posYRect - 100 >= 0:
                self.posYRect -= 100
                Eprime = [self.posYRect, self.posXRect]
                self._learn(E, dir, Eprime)
                self.window.matrix[self.row, self.col] = 0
                self.row -= 1
                self.window.matrix[self.row, self.col] = 1
        if dir == "bottom":
            if self.posYRect + 100 <= self.window.height - 100:
                self.posYRect += 100
                Eprime = [self.posYRect, self.posXRect]
                self._learn(E, dir, Eprime)
                self.window.matrix[self.row, self.col] = 0
                self.row += 1
                self.window.matrix[self.row, self.col] = 1

    def _learn(self, E, a, Eprime):
        try:
            self.q_table.loc[str(Eprime)]
        except KeyError as err:
            self.q_table.loc[str(Eprime)] = [0, 0, 0, 0]
        if (E != Eprime):
            for i in range(self.window.nbRow):
                for j in range(self.window.nbCol):
                    if self.window.matrix[Eprime[0]//100][Eprime[1]//100] == 2:
                        r = 1
                        q_cible = r
                        self.finish = True
                    elif self.window.matrix[Eprime[0]//100][Eprime[1]//100] == 3:
                        r = -1
                        q_cible = r
                        self.finish = True
                    else:
                        r = 0
                        max = self.q_table.loc[str(Eprime)].max()
                        q_cible = r + self.gamma*max
                    self.q_table.loc[str(E), a] += self.ta * \
                        (q_cible - self.q_table.loc[str(E)][a])
            self.terminal.showState(self.actualPeriode, self.q_table)
