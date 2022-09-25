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

import pykerio


class TestCase_HistogramType(unittest.TestCase):
    def test_00_HistogramOneDay(self):
        """
        Test HistogramType with HistogramOneDay
        """
        value = pykerio.enums.HistogramType(name='HistogramOneDay')
        self.assertEqual(value.dump(), 'HistogramOneDay')
        self.assertEqual(value.get_name(), 'HistogramOneDay')
        self.assertEqual(value.get_value(), 0)

    def test_01_HistogramTwoHours(self):
        """
        Test HistogramType with HistogramTwoHours
        """
        value = pykerio.enums.HistogramType(name='HistogramTwoHours')
        self.assertEqual(value.dump(), 'HistogramTwoHours')
        self.assertEqual(value.get_name(), 'HistogramTwoHours')
        self.assertEqual(value.get_value(), 1)

    def test_02_HistogramOneWeek(self):
        """
        Test HistogramType with HistogramOneWeek
        """
        value = pykerio.enums.HistogramType(name='HistogramOneWeek')
        self.assertEqual(value.dump(), 'HistogramOneWeek')
        self.assertEqual(value.get_name(), 'HistogramOneWeek')
        self.assertEqual(value.get_value(), 2)

    def test_03_HistogramOneMonth(self):
        """
        Test HistogramType with HistogramOneMonth
        """
        value = pykerio.enums.HistogramType(name='HistogramOneMonth')
        self.assertEqual(value.dump(), 'HistogramOneMonth')
        self.assertEqual(value.get_name(), 'HistogramOneMonth')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test HistogramType with FAIL
        """
        value = pykerio.enums.HistogramType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
