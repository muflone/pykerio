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

from pykerio.enums import RotationPeriod


class TestCase_RotationPeriod(unittest.TestCase):
    def test_00_RotateNever(self):
        """
        Test RotationPeriod with RotateNever
        """
        value = RotationPeriod.RotateNever
        self.assertEqual(value.dump(), 'RotateNever')
        self.assertEqual(value.name, 'RotateNever')
        self.assertEqual(value.value, 0)

    def test_01_RotateHourly(self):
        """
        Test RotationPeriod with RotateHourly
        """
        value = RotationPeriod.RotateHourly
        self.assertEqual(value.dump(), 'RotateHourly')
        self.assertEqual(value.name, 'RotateHourly')
        self.assertEqual(value.value, 1)

    def test_02_RotateDaily(self):
        """
        Test RotationPeriod with RotateDaily
        """
        value = RotationPeriod.RotateDaily
        self.assertEqual(value.dump(), 'RotateDaily')
        self.assertEqual(value.name, 'RotateDaily')
        self.assertEqual(value.value, 2)

    def test_03_RotateWeekly(self):
        """
        Test RotationPeriod with RotateWeekly
        """
        value = RotationPeriod.RotateWeekly
        self.assertEqual(value.dump(), 'RotateWeekly')
        self.assertEqual(value.name, 'RotateWeekly')
        self.assertEqual(value.value, 3)

    def test_04_RotateMonthly(self):
        """
        Test RotationPeriod with RotateMonthly
        """
        value = RotationPeriod.RotateMonthly
        self.assertEqual(value.dump(), 'RotateMonthly')
        self.assertEqual(value.name, 'RotateMonthly')
        self.assertEqual(value.value, 4)
