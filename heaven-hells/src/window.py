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
import numpy
from agent import Agent
from heaven import Heaven
from hell import Hell


class Window():
    def __init__(self, terminal, backgroundColor, nbCol, nbRow):
        self.terminal = terminal
        self.backgroundColor = backgroundColor
        self.nbCol = nbCol
        self.nbRow = nbRow
        self.height = 100 * nbRow
        self.width = 100 * nbCol
        self.root = Tk()
        self.canvas = Canvas(self.root, bg=self.backgroundColor,
                             height=self.height, width=self.width)
        self.rowSize = self.height//self.nbRow
        self.actualRowPos = 0
        self.actualColPos = 0
        self.colSize = self.width//self.nbCol
        self.matrix = numpy.zeros([nbRow, nbCol], dtype=int)
        self.heaven = Heaven(self, "yellow", 3, 3)
        self.hell1 = Hell(self, "black", 2, 3)
        self.hell2 = Hell(self, "black", 3, 2)
        self.agent = Agent(self, [self.heaven], [self.hell1, self.hell2], self.terminal,
                           1, 2, 0.1, 0.5, 100, 0.01, 200, "red")
        while self.actualRowPos <= self.height:
            self.canvas.create_line(0, self.actualRowPos,
                                    self.width, self.actualRowPos)
            self.actualRowPos += self.rowSize
        while self.actualColPos <= self.width:
            self.canvas.create_line(self.actualColPos, 0,
                                    self.actualColPos, self.width)
            self.actualColPos += self.colSize
        self.canvas.pack()

    def run(self):
        self.agent.update()
        self.root.mainloop()
