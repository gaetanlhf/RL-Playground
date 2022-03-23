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

import time


class Monitor():
    def __init__(self, board, window, terminal, p1, p2, speed=None, wait=None, period=None):
        self.board = board
        self.window = window
        self.terminal = terminal
        self.p1 = p1
        self.p2 = p2
        self.speed = speed
        self.wait = wait
        self.period = None
        if period != None:
            self.period = period+1
            self.actualPeriod = 1

    def update(self):
        if self.period != None:
            if self.actualPeriod < self.period:
                if self.board.finish == True:
                    if self.board.winner == self.p1.id:
                        self.p2.punish()
                        self.board.winner = None
                    elif self.board.winner == self.p2.id:
                        self.p1.punish()
                        self.board.winner = None
                    self.terminal.learningLevel(self.actualPeriod, self.period)
                    self.window.update()
                    self.actualPeriod += 1
                    time.sleep(self.wait)
                    self.board.clean()
                    self.window.clean()
                    self.board.finish = False
                self.p1.update()
                self.p2.update()
                self.window.canvas.after(self.speed, self.update)
            else:
                self.p1.saveQtable()
                self.terminal.message("Learning completed.")
                exit()
        else:
            if self.board.finish == True:
                self.board.clean()
                self.window.clean()
                self.board.finish = False
            # print(self.p1.q_table)
            self.p1.update()
            self.p2.update()
            self.update()
