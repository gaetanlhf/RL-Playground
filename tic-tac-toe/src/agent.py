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
import pickle
from ast import literal_eval as safe_eval


class Agent():
    def __init__(self, board, window, terminal, id, ta, gamma, epsilon):
        self.board = board
        self.window = window
        self.terminal = terminal
        self.id = id
        self.epsilon = epsilon
        self.gamma = gamma
        self.ta = ta
        self.q_table = pandas.DataFrame(
            columns=self.board.actions, dtype=numpy.float64)
        self.savemax = None
        self.saveq_cible = None
        self.saveE = None
        self.saveA = None

    def update(self):
        if (self.board.finish == False) and (self.board.full == False):
            self._chooseAction(self.board.getState())
            self.window.update()
            self.board.checkIfEmpty()

    def _chooseAction(self, E):
        try:
            self.q_table.loc[str(E)]
        except KeyError as err:
            self.q_table.loc[str(E)] = numpy.zeros(
                self.board.nbColRow*self.board.nbColRow)
        if random.uniform(0, 1) < 0.1:
            self._move(E)
        else:
            if self.q_table.loc[str(E)].max() != 0:
                max = self.q_table.idxmax(axis=1)
                self._move(E, max[str(E)])
            else:
                self._move(E)

    def _move(self, E, dir=None):
        if dir == None:
            dir = safe_eval(random.choice(self.board.getPossibleActions()))
        else:
            dir = safe_eval(dir)

        newMatrix = self.board.matrix.copy()
        newMatrix[dir[0], dir[1]] = self.id
        self._learn(E, dir, newMatrix.flatten(), newMatrix)
        self.board.matrix = newMatrix

    def _learn(self, E=None, a=None, Eprime=None, newMatrix=None):
        q_cible = 0
        if (a == None):
            r = -1
            q_cible = r + self.gamma*self.savemax
            self.q_table.loc[self.saveE, self.saveA] += self.ta * \
                (q_cible - self.q_table.loc[self.saveE][self.saveA])
        else:
            try:
                self.q_table.loc[str(Eprime)]
            except KeyError as err:
                self.q_table.loc[str(Eprime)] = numpy.zeros(
                    self.board.nbColRow*self.board.nbColRow)
            if (str(E) != str(Eprime)):
                if self.board.checkIfWin(self.id, newMatrix) == True:
                    r = 1
                    self.saveq_cible = q_cible = r
                    self.board.finish = True
                    self.terminal.showWinner(self.id)
                else:
                    r = 0
                    self.savemax = max = self.q_table.loc[str(Eprime)].max()
                    self.saveq_cible = q_cible = r + self.gamma*max
                self.q_table.loc[str(E), str(a)] += self.ta * \
                    (q_cible - self.q_table.loc[str(E)][str(a)])
                self.saveE = str(E)
                self.saveA = str(a)

    def punish(self):
        self._learn()

    def saveQtable(self):
        f = open("qtable.save", "wb")
        pickle.dump(self.q_table, f)
        f.close()

    def restoreQtable(self):
        f = open("qtable.save", "rb")
        self.q_table = pickle.load(f)
        f.close()
