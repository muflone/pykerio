##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import unittest

from pykerio.enums import WifiBandType


class TestCase_WifiBandType(unittest.TestCase):
    def test_00_WifiBandA(self):
        """
        Test WifiBandType with WifiBandA
        """
        value = WifiBandType.WifiBandA
        self.assertEqual(value.dump(), 'WifiBandA')
        self.assertEqual(value.name, 'WifiBandA')
        self.assertEqual(value.value, 0)

    def test_01_WifiBandBG(self):
        """
        Test WifiBandType with WifiBandBG
        """
        value = WifiBandType.WifiBandBG
        self.assertEqual(value.dump(), 'WifiBandBG')
        self.assertEqual(value.name, 'WifiBandBG')
        self.assertEqual(value.value, 1)

    def test_02_WifiBandAC(self):
        """
        Test WifiBandType with WifiBandAC
        """
        value = WifiBandType.WifiBandAC
        self.assertEqual(value.dump(), 'WifiBandAC')
        self.assertEqual(value.name, 'WifiBandAC')
        self.assertEqual(value.value, 2)
