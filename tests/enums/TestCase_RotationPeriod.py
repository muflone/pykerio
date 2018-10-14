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


class TestCase_RotationPeriod(unittest.TestCase):
    def test_00_RotationPeriod_RotateNever(self):
        """
        Test RotationPeriod with RotateNever
        """
        value = pykerio.enums.RotationPeriod(name='RotateNever')
        self.assertEquals(value.dump(), 'RotateNever')
        self.assertEquals(value.get_name(), 'RotateNever')
        self.assertEquals(value.get_value(), 0)

    def test_01_RotationPeriod_RotateHourly(self):
        """
        Test RotationPeriod with RotateHourly
        """
        value = pykerio.enums.RotationPeriod(name='RotateHourly')
        self.assertEquals(value.dump(), 'RotateHourly')
        self.assertEquals(value.get_name(), 'RotateHourly')
        self.assertEquals(value.get_value(), 1)

    def test_02_RotationPeriod_RotateDaily(self):
        """
        Test RotationPeriod with RotateDaily
        """
        value = pykerio.enums.RotationPeriod(name='RotateDaily')
        self.assertEquals(value.dump(), 'RotateDaily')
        self.assertEquals(value.get_name(), 'RotateDaily')
        self.assertEquals(value.get_value(), 2)

    def test_03_RotationPeriod_RotateWeekly(self):
        """
        Test RotationPeriod with RotateWeekly
        """
        value = pykerio.enums.RotationPeriod(name='RotateWeekly')
        self.assertEquals(value.dump(), 'RotateWeekly')
        self.assertEquals(value.get_name(), 'RotateWeekly')
        self.assertEquals(value.get_value(), 3)

    def test_04_RotationPeriod_RotateMonthly(self):
        """
        Test RotationPeriod with RotateMonthly
        """
        value = pykerio.enums.RotationPeriod(name='RotateMonthly')
        self.assertEquals(value.dump(), 'RotateMonthly')
        self.assertEquals(value.get_name(), 'RotateMonthly')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_RotationPeriod_FAIL(self):
        """
        Test RotationPeriod with FAIL
        """
        value = pykerio.enums.RotationPeriod(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
