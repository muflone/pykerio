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


class TestCase_HistogramIntervalType(unittest.TestCase):
    def test_00_HistogramInterval5m(self):
        """
        Test HistogramIntervalType with HistogramInterval5m
        """
        value = pykerio.enums.HistogramIntervalType(name='HistogramInterval5m')
        self.assertEqual(value.dump(), 'HistogramInterval5m')
        self.assertEqual(value.get_name(), 'HistogramInterval5m')
        self.assertEqual(value.get_value(), 0)

    def test_01_HistogramInterval20s(self):
        """
        Test HistogramIntervalType with HistogramInterval20s
        """
        value = pykerio.enums.HistogramIntervalType(name='HistogramInterval20s')
        self.assertEqual(value.dump(), 'HistogramInterval20s')
        self.assertEqual(value.get_name(), 'HistogramInterval20s')
        self.assertEqual(value.get_value(), 1)

    def test_02_HistogramInterval30m(self):
        """
        Test HistogramIntervalType with HistogramInterval30m
        """
        value = pykerio.enums.HistogramIntervalType(name='HistogramInterval30m')
        self.assertEqual(value.dump(), 'HistogramInterval30m')
        self.assertEqual(value.get_name(), 'HistogramInterval30m')
        self.assertEqual(value.get_value(), 2)

    def test_03_HistogramInterval2h(self):
        """
        Test HistogramIntervalType with HistogramInterval2h
        """
        value = pykerio.enums.HistogramIntervalType(name='HistogramInterval2h')
        self.assertEqual(value.dump(), 'HistogramInterval2h')
        self.assertEqual(value.get_name(), 'HistogramInterval2h')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test HistogramIntervalType with FAIL
        """
        value = pykerio.enums.HistogramIntervalType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
