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


class TestCase_BandwidthUnit(unittest.TestCase):
    def test_00_BandwidthUnitBits(self):
        """
        Test BandwidthUnit with BandwidthUnitBits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitBits')
        self.assertEqual(value.dump(), 'BandwidthUnitBits')
        self.assertEqual(value.get_name(), 'BandwidthUnitBits')
        self.assertEqual(value.get_value(), 0)

    def test_01_BandwidthUnitBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitBytes')
        self.assertEqual(value.dump(), 'BandwidthUnitBytes')
        self.assertEqual(value.get_name(), 'BandwidthUnitBytes')
        self.assertEqual(value.get_value(), 1)

    def test_02_BandwidthUnitKilobits(self):
        """
        Test BandwidthUnit with BandwidthUnitKilobits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitKilobits')
        self.assertEqual(value.dump(), 'BandwidthUnitKilobits')
        self.assertEqual(value.get_name(), 'BandwidthUnitKilobits')
        self.assertEqual(value.get_value(), 2)

    def test_03_BandwidthUnitKiloBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitKiloBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitKiloBytes')
        self.assertEqual(value.dump(), 'BandwidthUnitKiloBytes')
        self.assertEqual(value.get_name(), 'BandwidthUnitKiloBytes')
        self.assertEqual(value.get_value(), 3)

    def test_04_BandwidthUnitMegabits(self):
        """
        Test BandwidthUnit with BandwidthUnitMegabits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitMegabits')
        self.assertEqual(value.dump(), 'BandwidthUnitMegabits')
        self.assertEqual(value.get_name(), 'BandwidthUnitMegabits')
        self.assertEqual(value.get_value(), 4)

    def test_05_BandwidthUnitMegaBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitMegaBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitMegaBytes')
        self.assertEqual(value.dump(), 'BandwidthUnitMegaBytes')
        self.assertEqual(value.get_name(), 'BandwidthUnitMegaBytes')
        self.assertEqual(value.get_value(), 5)

    def test_06_BandwidthUnitPercent(self):
        """
        Test BandwidthUnit with BandwidthUnitPercent
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitPercent')
        self.assertEqual(value.dump(), 'BandwidthUnitPercent')
        self.assertEqual(value.get_name(), 'BandwidthUnitPercent')
        self.assertEqual(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test BandwidthUnit with FAIL
        """
        value = pykerio.enums.BandwidthUnit(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
