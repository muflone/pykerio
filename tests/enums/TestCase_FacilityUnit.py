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


class TestCase_FacilityUnit(unittest.TestCase):
    def test_00_FacilityUnit_FacilityKernel(self):
        """
        Test FacilityUnit with FacilityKernel
        """
        value = pykerio.enums.FacilityUnit(name='FacilityKernel')
        self.assertEquals(value.dump(), 'FacilityKernel')
        self.assertEquals(value.get_name(), 'FacilityKernel')
        self.assertEquals(value.get_value(), 0)

    def test_01_FacilityUnit_FacilityUserLevel(self):
        """
        Test FacilityUnit with FacilityUserLevel
        """
        value = pykerio.enums.FacilityUnit(name='FacilityUserLevel')
        self.assertEquals(value.dump(), 'FacilityUserLevel')
        self.assertEquals(value.get_name(), 'FacilityUserLevel')
        self.assertEquals(value.get_value(), 1)

    def test_02_FacilityUnit_FacilityMailSystem(self):
        """
        Test FacilityUnit with FacilityMailSystem
        """
        value = pykerio.enums.FacilityUnit(name='FacilityMailSystem')
        self.assertEquals(value.dump(), 'FacilityMailSystem')
        self.assertEquals(value.get_name(), 'FacilityMailSystem')
        self.assertEquals(value.get_value(), 2)

    def test_03_FacilityUnit_FacilitySystemDaemons(self):
        """
        Test FacilityUnit with FacilitySystemDaemons
        """
        value = pykerio.enums.FacilityUnit(name='FacilitySystemDaemons')
        self.assertEquals(value.dump(), 'FacilitySystemDaemons')
        self.assertEquals(value.get_name(), 'FacilitySystemDaemons')
        self.assertEquals(value.get_value(), 3)

    def test_04_FacilityUnit_FacilitySecurity1(self):
        """
        Test FacilityUnit with FacilitySecurity1
        """
        value = pykerio.enums.FacilityUnit(name='FacilitySecurity1')
        self.assertEquals(value.dump(), 'FacilitySecurity1')
        self.assertEquals(value.get_name(), 'FacilitySecurity1')
        self.assertEquals(value.get_value(), 4)

    def test_05_FacilityUnit_FacilityInternal(self):
        """
        Test FacilityUnit with FacilityInternal
        """
        value = pykerio.enums.FacilityUnit(name='FacilityInternal')
        self.assertEquals(value.dump(), 'FacilityInternal')
        self.assertEquals(value.get_name(), 'FacilityInternal')
        self.assertEquals(value.get_value(), 5)

    def test_06_FacilityUnit_FacilityLinePrinter(self):
        """
        Test FacilityUnit with FacilityLinePrinter
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLinePrinter')
        self.assertEquals(value.dump(), 'FacilityLinePrinter')
        self.assertEquals(value.get_name(), 'FacilityLinePrinter')
        self.assertEquals(value.get_value(), 6)

    def test_07_FacilityUnit_FacilityNetworkNews(self):
        """
        Test FacilityUnit with FacilityNetworkNews
        """
        value = pykerio.enums.FacilityUnit(name='FacilityNetworkNews')
        self.assertEquals(value.dump(), 'FacilityNetworkNews')
        self.assertEquals(value.get_name(), 'FacilityNetworkNews')
        self.assertEquals(value.get_value(), 7)

    def test_08_FacilityUnit_FacilityUucpSubsystem(self):
        """
        Test FacilityUnit with FacilityUucpSubsystem
        """
        value = pykerio.enums.FacilityUnit(name='FacilityUucpSubsystem')
        self.assertEquals(value.dump(), 'FacilityUucpSubsystem')
        self.assertEquals(value.get_name(), 'FacilityUucpSubsystem')
        self.assertEquals(value.get_value(), 8)

    def test_09_FacilityUnit_FacilityClockDaemon1(self):
        """
        Test FacilityUnit with FacilityClockDaemon1
        """
        value = pykerio.enums.FacilityUnit(name='FacilityClockDaemon1')
        self.assertEquals(value.dump(), 'FacilityClockDaemon1')
        self.assertEquals(value.get_name(), 'FacilityClockDaemon1')
        self.assertEquals(value.get_value(), 9)

    def test_10_FacilityUnit_FacilitySecurity2(self):
        """
        Test FacilityUnit with FacilitySecurity2
        """
        value = pykerio.enums.FacilityUnit(name='FacilitySecurity2')
        self.assertEquals(value.dump(), 'FacilitySecurity2')
        self.assertEquals(value.get_name(), 'FacilitySecurity2')
        self.assertEquals(value.get_value(), 10)

    def test_11_FacilityUnit_FacilityFtpDaemon(self):
        """
        Test FacilityUnit with FacilityFtpDaemon
        """
        value = pykerio.enums.FacilityUnit(name='FacilityFtpDaemon')
        self.assertEquals(value.dump(), 'FacilityFtpDaemon')
        self.assertEquals(value.get_name(), 'FacilityFtpDaemon')
        self.assertEquals(value.get_value(), 11)

    def test_12_FacilityUnit_FacilityNtpSubsystem(self):
        """
        Test FacilityUnit with FacilityNtpSubsystem
        """
        value = pykerio.enums.FacilityUnit(name='FacilityNtpSubsystem')
        self.assertEquals(value.dump(), 'FacilityNtpSubsystem')
        self.assertEquals(value.get_name(), 'FacilityNtpSubsystem')
        self.assertEquals(value.get_value(), 12)

    def test_13_FacilityUnit_FacilityLogAudit(self):
        """
        Test FacilityUnit with FacilityLogAudit
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLogAudit')
        self.assertEquals(value.dump(), 'FacilityLogAudit')
        self.assertEquals(value.get_name(), 'FacilityLogAudit')
        self.assertEquals(value.get_value(), 13)

    def test_14_FacilityUnit_FacilityLogAlert(self):
        """
        Test FacilityUnit with FacilityLogAlert
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLogAlert')
        self.assertEquals(value.dump(), 'FacilityLogAlert')
        self.assertEquals(value.get_name(), 'FacilityLogAlert')
        self.assertEquals(value.get_value(), 14)

    def test_15_FacilityUnit_FacilityClockDaemon2(self):
        """
        Test FacilityUnit with FacilityClockDaemon2
        """
        value = pykerio.enums.FacilityUnit(name='FacilityClockDaemon2')
        self.assertEquals(value.dump(), 'FacilityClockDaemon2')
        self.assertEquals(value.get_name(), 'FacilityClockDaemon2')
        self.assertEquals(value.get_value(), 15)

    def test_16_FacilityUnit_FacilityLocal0(self):
        """
        Test FacilityUnit with FacilityLocal0
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal0')
        self.assertEquals(value.dump(), 'FacilityLocal0')
        self.assertEquals(value.get_name(), 'FacilityLocal0')
        self.assertEquals(value.get_value(), 16)

    def test_17_FacilityUnit_FacilityLocal1(self):
        """
        Test FacilityUnit with FacilityLocal1
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal1')
        self.assertEquals(value.dump(), 'FacilityLocal1')
        self.assertEquals(value.get_name(), 'FacilityLocal1')
        self.assertEquals(value.get_value(), 17)

    def test_18_FacilityUnit_FacilityLocal2(self):
        """
        Test FacilityUnit with FacilityLocal2
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal2')
        self.assertEquals(value.dump(), 'FacilityLocal2')
        self.assertEquals(value.get_name(), 'FacilityLocal2')
        self.assertEquals(value.get_value(), 18)

    def test_19_FacilityUnit_FacilityLocal3(self):
        """
        Test FacilityUnit with FacilityLocal3
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal3')
        self.assertEquals(value.dump(), 'FacilityLocal3')
        self.assertEquals(value.get_name(), 'FacilityLocal3')
        self.assertEquals(value.get_value(), 19)

    def test_20_FacilityUnit_FacilityLocal4(self):
        """
        Test FacilityUnit with FacilityLocal4
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal4')
        self.assertEquals(value.dump(), 'FacilityLocal4')
        self.assertEquals(value.get_name(), 'FacilityLocal4')
        self.assertEquals(value.get_value(), 20)

    def test_21_FacilityUnit_FacilityLocal5(self):
        """
        Test FacilityUnit with FacilityLocal5
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal5')
        self.assertEquals(value.dump(), 'FacilityLocal5')
        self.assertEquals(value.get_name(), 'FacilityLocal5')
        self.assertEquals(value.get_value(), 21)

    def test_22_FacilityUnit_FacilityLocal6(self):
        """
        Test FacilityUnit with FacilityLocal6
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal6')
        self.assertEquals(value.dump(), 'FacilityLocal6')
        self.assertEquals(value.get_name(), 'FacilityLocal6')
        self.assertEquals(value.get_value(), 22)

    def test_23_FacilityUnit_FacilityLocal7(self):
        """
        Test FacilityUnit with FacilityLocal7
        """
        value = pykerio.enums.FacilityUnit(name='FacilityLocal7')
        self.assertEquals(value.dump(), 'FacilityLocal7')
        self.assertEquals(value.get_name(), 'FacilityLocal7')
        self.assertEquals(value.get_value(), 23)

    @unittest.expectedFailure
    def test_99_FacilityUnit_FAIL(self):
        """
        Test FacilityUnit with FAIL
        """
        value = pykerio.enums.FacilityUnit(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
