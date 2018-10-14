##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio


class TestCase_PortComparator(unittest.TestCase):
    def test_00_PortComparator_Any(self):
        """
        Test PortComparator with Any
        """
        value = pykerio.enums.PortComparator(name='Any')
        self.assertEquals(value.dump(), 'Any')
        self.assertEquals(value.get_name(), 'Any')
        self.assertEquals(value.get_value(), 0)

    def test_01_PortComparator_Equal(self):
        """
        Test PortComparator with Equal
        """
        value = pykerio.enums.PortComparator(name='Equal')
        self.assertEquals(value.dump(), 'Equal')
        self.assertEquals(value.get_name(), 'Equal')
        self.assertEquals(value.get_value(), 1)

    def test_02_PortComparator_LessThan(self):
        """
        Test PortComparator with LessThan
        """
        value = pykerio.enums.PortComparator(name='LessThan')
        self.assertEquals(value.dump(), 'LessThan')
        self.assertEquals(value.get_name(), 'LessThan')
        self.assertEquals(value.get_value(), 2)

    def test_03_PortComparator_GreaterThan(self):
        """
        Test PortComparator with GreaterThan
        """
        value = pykerio.enums.PortComparator(name='GreaterThan')
        self.assertEquals(value.dump(), 'GreaterThan')
        self.assertEquals(value.get_name(), 'GreaterThan')
        self.assertEquals(value.get_value(), 3)

    def test_04_PortComparator_Range(self):
        """
        Test PortComparator with Range
        """
        value = pykerio.enums.PortComparator(name='Range')
        self.assertEquals(value.dump(), 'Range')
        self.assertEquals(value.get_name(), 'Range')
        self.assertEquals(value.get_value(), 4)

    def test_05_PortComparator_List(self):
        """
        Test PortComparator with List
        """
        value = pykerio.enums.PortComparator(name='List')
        self.assertEquals(value.dump(), 'List')
        self.assertEquals(value.get_name(), 'List')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_PortComparator_FAIL(self):
        """
        Test PortComparator with FAIL
        """
        value = pykerio.enums.PortComparator(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
