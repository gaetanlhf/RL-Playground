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

from tkinter import *
from tkinter import messagebox


class Window():
    def __init__(self, board, backgroundColor, nbColRow):
        self.board = board
        self.backgroundColor = backgroundColor
        self.nbColRow = nbColRow
        self.height = 100 * nbColRow
        self.width = 100 * nbColRow
        self.colSize = self.width//self.nbColRow
        self.root = Tk()
        self.canvas = Canvas(self.root, bg=self.backgroundColor,
                             height=self.height, width=self.width)
        self.rowSize = self.height//self.nbColRow
        self.actualRowPos = 0
        self.actualColPos = 0
        self.listPoly = []

        while self.actualRowPos <= self.height:
            self.canvas.create_line(0, self.actualRowPos,
                                    self.width, self.actualRowPos)
            self.actualRowPos += self.rowSize
        while self.actualColPos <= self.width:
            self.canvas.create_line(self.actualColPos, 0,
                                    self.actualColPos, self.width)
            self.actualColPos += self.colSize
        self.root.protocol("WM_DELETE_WINDOW", self._close)
        self.canvas.pack()

    def update(self):
        for i in range(self.nbColRow):
            for j in range(self.nbColRow):
                if self.board.matrix[i, j] == 1:
                    self.listPoly.append(self.canvas.create_rectangle(
                        (j)*self.rowSize, (i)*self.colSize, (j+1)*self.rowSize, (i+1)*self.colSize, fill="red"))
                elif self.board.matrix[i, j] == 10:
                    self.listPoly.append(self.canvas.create_oval(
                        (j)*self.rowSize, (i)*self.colSize, (j+1)*self.rowSize, (i+1)*self.colSize, fill="yellow"))

    def clean(self):
        for i in self.listPoly:
            self.canvas.delete(i)

    def _close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            exit()
