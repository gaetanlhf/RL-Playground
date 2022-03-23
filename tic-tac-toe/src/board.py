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

import numpy


class Board():
    def __init__(self, nbColRow):
        self.nbColRow = nbColRow
        self.matrix = numpy.zeros([self.nbColRow, self.nbColRow], dtype=int)
        self.actions = []
        self.finish = False
        self.winner = None
        for i in self.getPossibleActions():
            self.actions.append(i)

    def checkIfWin(self, id, matrix):
        idCalc = id * self.nbColRow
        for i in range(self.nbColRow):
            if sum(matrix[i, :]) == idCalc:
                self.winner = id
                return True
        for i in range(self.nbColRow):
            if sum(matrix[:, i]) == idCalc:
                self.winner = id
                return True
        diag_sum1 = 0
        for i in range(self.nbColRow):
            diag_sum1 += matrix[i, i]
        if diag_sum1 == idCalc:
            self.winner = id
            return True
        diag_sum2 = 0
        for i in range(self.nbColRow):
            diag_sum2 += matrix[i, self.nbColRow - i - 1]
        if diag_sum2 == idCalc:
            self.winner = id
            return True

    def getState(self):
        return self.matrix.flatten()

    def getPossibleActions(self):
        possibleActions = []
        for i in range(self.nbColRow):
            for j in range(self.nbColRow):
                if self.matrix[i][j] == 0:
                    row = i
                    col = j
                    possibleActions.append(str([row, col]))
        return possibleActions

    def checkIfEmpty(self):
        if self.getPossibleActions() == []:
            self.finish = True

    def clean(self):
        self.matrix = numpy.zeros([self.nbColRow, self.nbColRow], dtype=int)
