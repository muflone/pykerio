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


class TestCase_SpeedDuplexType(unittest.TestCase):
    def test_00_SpeedDuplexType_SpeedDuplexAuto(self):
        """
        Test SpeedDuplexType with SpeedDuplexAuto
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexAuto')
        self.assertEquals(value.dump(), 'SpeedDuplexAuto')
        self.assertEquals(value.get_name(), 'SpeedDuplexAuto')
        self.assertEquals(value.get_value(), 0)

    def test_01_SpeedDuplexType_SpeedDuplexHalf10(self):
        """
        Test SpeedDuplexType with SpeedDuplexHalf10
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexHalf10')
        self.assertEquals(value.dump(), 'SpeedDuplexHalf10')
        self.assertEquals(value.get_name(), 'SpeedDuplexHalf10')
        self.assertEquals(value.get_value(), 1)

    def test_02_SpeedDuplexType_SpeedDuplexFull10(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull10
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexFull10')
        self.assertEquals(value.dump(), 'SpeedDuplexFull10')
        self.assertEquals(value.get_name(), 'SpeedDuplexFull10')
        self.assertEquals(value.get_value(), 2)

    def test_03_SpeedDuplexType_SpeedDuplexHalf100(self):
        """
        Test SpeedDuplexType with SpeedDuplexHalf100
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexHalf100')
        self.assertEquals(value.dump(), 'SpeedDuplexHalf100')
        self.assertEquals(value.get_name(), 'SpeedDuplexHalf100')
        self.assertEquals(value.get_value(), 3)

    def test_04_SpeedDuplexType_SpeedDuplexFull100(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull100
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexFull100')
        self.assertEquals(value.dump(), 'SpeedDuplexFull100')
        self.assertEquals(value.get_name(), 'SpeedDuplexFull100')
        self.assertEquals(value.get_value(), 4)

    def test_05_SpeedDuplexType_SpeedDuplexFull1000(self):
        """
        Test SpeedDuplexType with SpeedDuplexFull1000
        """
        value = pykerio.enums.SpeedDuplexType(name='SpeedDuplexFull1000')
        self.assertEquals(value.dump(), 'SpeedDuplexFull1000')
        self.assertEquals(value.get_name(), 'SpeedDuplexFull1000')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_SpeedDuplexType_FAIL(self):
        """
        Test SpeedDuplexType with FAIL
        """
        value = pykerio.enums.SpeedDuplexType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
