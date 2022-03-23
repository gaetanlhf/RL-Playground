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

from window import Window
from terminal import Terminal


class Main():
    def __init__(self, backgroundColor, nbCol, nbRow):
        self.terminal = Terminal()
        self.window = Window(self.terminal, "white", 4, 4)

    def run(self):
        self.window.run()


if __name__ == "__main__":
    main = Main("white", 4, 4)
    main.run()
