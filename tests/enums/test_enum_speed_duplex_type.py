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

from pykerio.enums import SpeedDuplexType


class TestCase_SpeedDuplexType(unittest.TestCase):
    def test_00_SpeedDuplexAuto(self):
        """
        Test SpeedDuplexType with SpeedDuplexAuto
        """
        value = SpeedDuplexType.SpeedDuplexAuto
        self.assertEqual(value.dump(), 'SpeedDuplexAuto')
        self.assertEqual(value.name, 'SpeedDuplexAuto')
        self.assertEqual(value.value, 0)

    def test_01_SpeedDuplexHalf10(self):
        """
        Test SpeedDuplexType with SpeedDuplexHalf10
        """
        value = SpeedDuplexType.SpeedDuplexHalf10
        self.assertEqual(value.dump(), 'SpeedDuplexHalf10')
        self.assertEqual(value.name, 'SpeedDuplexHalf10')
        self.assertEqual(value.value, 1)

    def test_02_SpeedDuplexFull10(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull10
        """
        value = SpeedDuplexType.SpeedDuplexFull10
        self.assertEqual(value.dump(), 'SpeedDuplexFull10')
        self.assertEqual(value.name, 'SpeedDuplexFull10')
        self.assertEqual(value.value, 2)

    def test_03_SpeedDuplexHalf100(self):
        """
        Test SpeedDuplexType with SpeedDuplexHalf100
        """
        value = SpeedDuplexType.SpeedDuplexHalf100
        self.assertEqual(value.dump(), 'SpeedDuplexHalf100')
        self.assertEqual(value.name, 'SpeedDuplexHalf100')
        self.assertEqual(value.value, 3)

    def test_04_SpeedDuplexFull100(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull100
        """
        value = SpeedDuplexType.SpeedDuplexFull100
        self.assertEqual(value.dump(), 'SpeedDuplexFull100')
        self.assertEqual(value.name, 'SpeedDuplexFull100')
        self.assertEqual(value.value, 4)

    def test_05_SpeedDuplexFull1000(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull1000
        """
        value = SpeedDuplexType.SpeedDuplexFull1000
        self.assertEqual(value.dump(), 'SpeedDuplexFull1000')
        self.assertEqual(value.name, 'SpeedDuplexFull1000')
        self.assertEqual(value.value, 5)
