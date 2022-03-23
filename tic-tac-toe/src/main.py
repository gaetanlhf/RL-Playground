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

from monitor import Monitor
from board import Board
from agent import Agent
from human import Human
from window import Window
from terminal import Terminal


class Main():
    def __init__(self, backgroundColor, nbColRow):
        self.board = Board(nbColRow)
        self.window = Window(self.board, backgroundColor, nbColRow)
        self.terminal = Terminal()
        self.p1 = Agent(self.board, self.window,
                        self.terminal, 1, 0.01, 0.9, 0.1)

    def run(self):
        saveQtable = True
        try:
            f = open("qtable.save")
        except:
            saveQtable = False
        if saveQtable == True:
            a = self.terminal.input(
                "Do you want to restore the AI data? [y/n]")
            if (a == "y") or (a == "n"):
                if a == "y":
                    self.p1.restoreQtable()
                    self.terminal.message("Data restored.")
                    self._humainPlay()
                else:
                    self._learning()
            else:
                self.terminal.message("Incorrect input!")
                exit()
        else:
            self._learning()
        self.window.root.mainloop()

    def _learning(self):
        p2 = Agent(self.board, self.window, self.terminal, 10, 0.1, 0.5, 0.5)
        self.terminal.message("Learning...")
        monitor = Monitor(self.board, self.window,
                          self.terminal, self.p1, p2, 1, 1, 20000)
        monitor.update()

    def _humainPlay(self):
        p2 = Human(self.board, self.terminal, 10)
        monitor = Monitor(self.board, self.window,
                          self.terminal, self.p1, p2, 1)
        monitor.update()


if __name__ == "__main__":
    main = Main("white", 3)
    main.run()
