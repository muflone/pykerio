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

from pykerio.enums import HistogramType


class TestCase_HistogramType(unittest.TestCase):
    def test_00_HistogramOneDay(self):
        """
        Test HistogramType with HistogramOneDay
        """
        value = HistogramType.HistogramOneDay
        self.assertEqual(value.dump(), 'HistogramOneDay')
        self.assertEqual(value.name, 'HistogramOneDay')
        self.assertEqual(value.value, 0)

    def test_01_HistogramTwoHours(self):
        """
        Test HistogramType with HistogramTwoHours
        """
        value = HistogramType.HistogramTwoHours
        self.assertEqual(value.dump(), 'HistogramTwoHours')
        self.assertEqual(value.name, 'HistogramTwoHours')
        self.assertEqual(value.value, 1)

    def test_02_HistogramOneWeek(self):
        """
        Test HistogramType with HistogramOneWeek
        """
        value = HistogramType.HistogramOneWeek
        self.assertEqual(value.dump(), 'HistogramOneWeek')
        self.assertEqual(value.name, 'HistogramOneWeek')
        self.assertEqual(value.value, 2)

    def test_03_HistogramOneMonth(self):
        """
        Test HistogramType with HistogramOneMonth
        """
        value = HistogramType.HistogramOneMonth
        self.assertEqual(value.dump(), 'HistogramOneMonth')
        self.assertEqual(value.name, 'HistogramOneMonth')
        self.assertEqual(value.value, 3)
