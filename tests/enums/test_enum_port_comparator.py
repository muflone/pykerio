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


class TestCase_PortComparator(unittest.TestCase):
    def test_00_Any(self):
        """
        Test PortComparator with Any
        """
        value = pykerio.enums.PortComparator(name='Any')
        self.assertEqual(value.dump(), 'Any')
        self.assertEqual(value.get_name(), 'Any')
        self.assertEqual(value.get_value(), 0)

    def test_01_Equal(self):
        """
        Test PortComparator with Equal
        """
        value = pykerio.enums.PortComparator(name='Equal')
        self.assertEqual(value.dump(), 'Equal')
        self.assertEqual(value.get_name(), 'Equal')
        self.assertEqual(value.get_value(), 1)

    def test_02_LessThan(self):
        """
        Test PortComparator with LessThan
        """
        value = pykerio.enums.PortComparator(name='LessThan')
        self.assertEqual(value.dump(), 'LessThan')
        self.assertEqual(value.get_name(), 'LessThan')
        self.assertEqual(value.get_value(), 2)

    def test_03_GreaterThan(self):
        """
        Test PortComparator with GreaterThan
        """
        value = pykerio.enums.PortComparator(name='GreaterThan')
        self.assertEqual(value.dump(), 'GreaterThan')
        self.assertEqual(value.get_name(), 'GreaterThan')
        self.assertEqual(value.get_value(), 3)

    def test_04_Range(self):
        """
        Test PortComparator with Range
        """
        value = pykerio.enums.PortComparator(name='Range')
        self.assertEqual(value.dump(), 'Range')
        self.assertEqual(value.get_name(), 'Range')
        self.assertEqual(value.get_value(), 4)

    def test_05_List(self):
        """
        Test PortComparator with List
        """
        value = pykerio.enums.PortComparator(name='List')
        self.assertEqual(value.dump(), 'List')
        self.assertEqual(value.get_name(), 'List')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test PortComparator with FAIL
        """
        value = pykerio.enums.PortComparator(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
