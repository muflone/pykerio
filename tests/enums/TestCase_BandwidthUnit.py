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


class TestCase_BandwidthUnit(unittest.TestCase):
    def test_00_BandwidthUnit_BandwidthUnitBits(self):
        """
        Test BandwidthUnit with BandwidthUnitBits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitBits')
        self.assertEquals(value.dump(), 'BandwidthUnitBits')
        self.assertEquals(value.get_name(), 'BandwidthUnitBits')
        self.assertEquals(value.get_value(), 0)

    def test_01_BandwidthUnit_BandwidthUnitBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitBytes')
        self.assertEquals(value.dump(), 'BandwidthUnitBytes')
        self.assertEquals(value.get_name(), 'BandwidthUnitBytes')
        self.assertEquals(value.get_value(), 1)

    def test_02_BandwidthUnit_BandwidthUnitKilobits(self):
        """
        Test BandwidthUnit with BandwidthUnitKilobits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitKilobits')
        self.assertEquals(value.dump(), 'BandwidthUnitKilobits')
        self.assertEquals(value.get_name(), 'BandwidthUnitKilobits')
        self.assertEquals(value.get_value(), 2)

    def test_03_BandwidthUnit_BandwidthUnitKiloBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitKiloBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitKiloBytes')
        self.assertEquals(value.dump(), 'BandwidthUnitKiloBytes')
        self.assertEquals(value.get_name(), 'BandwidthUnitKiloBytes')
        self.assertEquals(value.get_value(), 3)

    def test_04_BandwidthUnit_BandwidthUnitMegabits(self):
        """
        Test BandwidthUnit with BandwidthUnitMegabits
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitMegabits')
        self.assertEquals(value.dump(), 'BandwidthUnitMegabits')
        self.assertEquals(value.get_name(), 'BandwidthUnitMegabits')
        self.assertEquals(value.get_value(), 4)

    def test_05_BandwidthUnit_BandwidthUnitMegaBytes(self):
        """
        Test BandwidthUnit with BandwidthUnitMegaBytes
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitMegaBytes')
        self.assertEquals(value.dump(), 'BandwidthUnitMegaBytes')
        self.assertEquals(value.get_name(), 'BandwidthUnitMegaBytes')
        self.assertEquals(value.get_value(), 5)

    def test_06_BandwidthUnit_BandwidthUnitPercent(self):
        """
        Test BandwidthUnit with BandwidthUnitPercent
        """
        value = pykerio.enums.BandwidthUnit(name='BandwidthUnitPercent')
        self.assertEquals(value.dump(), 'BandwidthUnitPercent')
        self.assertEquals(value.get_name(), 'BandwidthUnitPercent')
        self.assertEquals(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_BandwidthUnit_FAIL(self):
        """
        Test BandwidthUnit with FAIL
        """
        value = pykerio.enums.BandwidthUnit(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
