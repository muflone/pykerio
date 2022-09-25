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

from pykerio.enums import FacilityUnit


class TestCase_FacilityUnit(unittest.TestCase):
    def test_00_FacilityKernel(self):
        """
        Test FacilityUnit with FacilityKernel
        """
        value = FacilityUnit.FacilityKernel
        self.assertEqual(value.dump(), 'FacilityKernel')
        self.assertEqual(value.name, 'FacilityKernel')
        self.assertEqual(value.value, 0)

    def test_01_FacilityUserLevel(self):
        """
        Test FacilityUnit with FacilityUserLevel
        """
        value = FacilityUnit.FacilityUserLevel
        self.assertEqual(value.dump(), 'FacilityUserLevel')
        self.assertEqual(value.name, 'FacilityUserLevel')
        self.assertEqual(value.value, 1)

    def test_02_FacilityMailSystem(self):
        """
        Test FacilityUnit with FacilityMailSystem
        """
        value = FacilityUnit.FacilityMailSystem
        self.assertEqual(value.dump(), 'FacilityMailSystem')
        self.assertEqual(value.name, 'FacilityMailSystem')
        self.assertEqual(value.value, 2)

    def test_03_FacilitySystemDaemons(self):
        """
        Test FacilityUnit with FacilitySystemDaemons
        """
        value = FacilityUnit.FacilitySystemDaemons
        self.assertEqual(value.dump(), 'FacilitySystemDaemons')
        self.assertEqual(value.name, 'FacilitySystemDaemons')
        self.assertEqual(value.value, 3)

    def test_04_FacilitySecurity1(self):
        """
        Test FacilityUnit with FacilitySecurity1
        """
        value = FacilityUnit.FacilitySecurity1
        self.assertEqual(value.dump(), 'FacilitySecurity1')
        self.assertEqual(value.name, 'FacilitySecurity1')
        self.assertEqual(value.value, 4)

    def test_05_FacilityInternal(self):
        """
        Test FacilityUnit with FacilityInternal
        """
        value = FacilityUnit.FacilityInternal
        self.assertEqual(value.dump(), 'FacilityInternal')
        self.assertEqual(value.name, 'FacilityInternal')
        self.assertEqual(value.value, 5)

    def test_06_FacilityLinePrinter(self):
        """
        Test FacilityUnit with FacilityLinePrinter
        """
        value = FacilityUnit.FacilityLinePrinter
        self.assertEqual(value.dump(), 'FacilityLinePrinter')
        self.assertEqual(value.name, 'FacilityLinePrinter')
        self.assertEqual(value.value, 6)

    def test_07_FacilityNetworkNews(self):
        """
        Test FacilityUnit with FacilityNetworkNews
        """
        value = FacilityUnit.FacilityNetworkNews
        self.assertEqual(value.dump(), 'FacilityNetworkNews')
        self.assertEqual(value.name, 'FacilityNetworkNews')
        self.assertEqual(value.value, 7)

    def test_08_FacilityUucpSubsystem(self):
        """
        Test FacilityUnit with FacilityUucpSubsystem
        """
        value = FacilityUnit.FacilityUucpSubsystem
        self.assertEqual(value.dump(), 'FacilityUucpSubsystem')
        self.assertEqual(value.name, 'FacilityUucpSubsystem')
        self.assertEqual(value.value, 8)

    def test_09_FacilityClockDaemon1(self):
        """
        Test FacilityUnit with FacilityClockDaemon1
        """
        value = FacilityUnit.FacilityClockDaemon1
        self.assertEqual(value.dump(), 'FacilityClockDaemon1')
        self.assertEqual(value.name, 'FacilityClockDaemon1')
        self.assertEqual(value.value, 9)

    def test_10_FacilitySecurity2(self):
        """
        Test FacilityUnit with FacilitySecurity2
        """
        value = FacilityUnit.FacilitySecurity2
        self.assertEqual(value.dump(), 'FacilitySecurity2')
        self.assertEqual(value.name, 'FacilitySecurity2')
        self.assertEqual(value.value, 10)

    def test_11_FacilityFtpDaemon(self):
        """
        Test FacilityUnit with FacilityFtpDaemon
        """
        value = FacilityUnit.FacilityFtpDaemon
        self.assertEqual(value.dump(), 'FacilityFtpDaemon')
        self.assertEqual(value.name, 'FacilityFtpDaemon')
        self.assertEqual(value.value, 11)

    def test_12_FacilityNtpSubsystem(self):
        """
        Test FacilityUnit with FacilityNtpSubsystem
        """
        value = FacilityUnit.FacilityNtpSubsystem
        self.assertEqual(value.dump(), 'FacilityNtpSubsystem')
        self.assertEqual(value.name, 'FacilityNtpSubsystem')
        self.assertEqual(value.value, 12)

    def test_13_FacilityLogAudit(self):
        """
        Test FacilityUnit with FacilityLogAudit
        """
        value = FacilityUnit.FacilityLogAudit
        self.assertEqual(value.dump(), 'FacilityLogAudit')
        self.assertEqual(value.name, 'FacilityLogAudit')
        self.assertEqual(value.value, 13)

    def test_14_FacilityLogAlert(self):
        """
        Test FacilityUnit with FacilityLogAlert
        """
        value = FacilityUnit.FacilityLogAlert
        self.assertEqual(value.dump(), 'FacilityLogAlert')
        self.assertEqual(value.name, 'FacilityLogAlert')
        self.assertEqual(value.value, 14)

    def test_15_FacilityClockDaemon2(self):
        """
        Test FacilityUnit with FacilityClockDaemon2
        """
        value = FacilityUnit.FacilityClockDaemon2
        self.assertEqual(value.dump(), 'FacilityClockDaemon2')
        self.assertEqual(value.name, 'FacilityClockDaemon2')
        self.assertEqual(value.value, 15)

    def test_16_FacilityLocal0(self):
        """
        Test FacilityUnit with FacilityLocal0
        """
        value = FacilityUnit.FacilityLocal0
        self.assertEqual(value.dump(), 'FacilityLocal0')
        self.assertEqual(value.name, 'FacilityLocal0')
        self.assertEqual(value.value, 16)

    def test_17_FacilityLocal1(self):
        """
        Test FacilityUnit with FacilityLocal1
        """
        value = FacilityUnit.FacilityLocal1
        self.assertEqual(value.dump(), 'FacilityLocal1')
        self.assertEqual(value.name, 'FacilityLocal1')
        self.assertEqual(value.value, 17)

    def test_18_FacilityLocal2(self):
        """
        Test FacilityUnit with FacilityLocal2
        """
        value = FacilityUnit.FacilityLocal2
        self.assertEqual(value.dump(), 'FacilityLocal2')
        self.assertEqual(value.name, 'FacilityLocal2')
        self.assertEqual(value.value, 18)

    def test_19_FacilityLocal3(self):
        """
        Test FacilityUnit with FacilityLocal3
        """
        value = FacilityUnit.FacilityLocal3
        self.assertEqual(value.dump(), 'FacilityLocal3')
        self.assertEqual(value.name, 'FacilityLocal3')
        self.assertEqual(value.value, 19)

    def test_20_FacilityLocal4(self):
        """
        Test FacilityUnit with FacilityLocal4
        """
        value = FacilityUnit.FacilityLocal4
        self.assertEqual(value.dump(), 'FacilityLocal4')
        self.assertEqual(value.name, 'FacilityLocal4')
        self.assertEqual(value.value, 20)

    def test_21_FacilityLocal5(self):
        """
        Test FacilityUnit with FacilityLocal5
        """
        value = FacilityUnit.FacilityLocal5
        self.assertEqual(value.dump(), 'FacilityLocal5')
        self.assertEqual(value.name, 'FacilityLocal5')
        self.assertEqual(value.value, 21)

    def test_22_FacilityLocal6(self):
        """
        Test FacilityUnit with FacilityLocal6
        """
        value = FacilityUnit.FacilityLocal6
        self.assertEqual(value.dump(), 'FacilityLocal6')
        self.assertEqual(value.name, 'FacilityLocal6')
        self.assertEqual(value.value, 22)

    def test_23_FacilityLocal7(self):
        """
        Test FacilityUnit with FacilityLocal7
        """
        value = FacilityUnit.FacilityLocal7
        self.assertEqual(value.dump(), 'FacilityLocal7')
        self.assertEqual(value.name, 'FacilityLocal7')
        self.assertEqual(value.value, 23)
