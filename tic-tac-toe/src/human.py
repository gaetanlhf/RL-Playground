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

class Human():
    def __init__(self, board, terminal, id):
        self.board = board
        self.terminal = terminal
        self.id = id

    def update(self):
        if self.board.finish == False:
            self.terminal.message("It's your turn!")
            self._play()
            self.board.checkIfEmpty()

    def _play(self):
        i = int(self.terminal.input("Row: "))
        j = int(self.terminal.input("Column: "))
        if (i <= 0) or (i > self.board.nbColRow + 1) or (i <= 0) or (i > self.board.nbColRow + 1):
            self.terminal.message("Invalid entry, please try again.")
            self._play()
        if self.board.matrix[i-1, j-1] == 0:
            self.board.matrix[i-1, j-1] = self.id
            if self.board.checkIfWin(self.id, self.board.matrix) == True:
                self.terminal.message("You won!")
                self.board.finish = True
        else:
            self.terminal.message("This field is already in use!")
            self._play()
