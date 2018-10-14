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


class TestCase_NotificationType(unittest.TestCase):
    def test_00_NotificationType_NotificationUpdate(self):
        """
        Test NotificationType with NotificationUpdate
        """
        value = pykerio.enums.NotificationType(name='NotificationUpdate')
        self.assertEquals(value.dump(), 'NotificationUpdate')
        self.assertEquals(value.get_name(), 'NotificationUpdate')
        self.assertEquals(value.get_value(), 0)

    def test_01_NotificationType_NotificationDump(self):
        """
        Test NotificationType with NotificationDump
        """
        value = pykerio.enums.NotificationType(name='NotificationDump')
        self.assertEquals(value.dump(), 'NotificationDump')
        self.assertEquals(value.get_name(), 'NotificationDump')
        self.assertEquals(value.get_value(), 1)

    def test_02_NotificationType_NotificationLowMemory(self):
        """
        Test NotificationType with NotificationLowMemory
        """
        value = pykerio.enums.NotificationType(name='NotificationLowMemory')
        self.assertEquals(value.dump(), 'NotificationLowMemory')
        self.assertEquals(value.get_name(), 'NotificationLowMemory')
        self.assertEquals(value.get_value(), 2)

    def test_03_NotificationType_NotificationDomains(self):
        """
        Test NotificationType with NotificationDomains
        """
        value = pykerio.enums.NotificationType(name='NotificationDomains')
        self.assertEquals(value.dump(), 'NotificationDomains')
        self.assertEquals(value.get_name(), 'NotificationDomains')
        self.assertEquals(value.get_value(), 3)

    def test_04_NotificationType_NotificationSubWillExpire(self):
        """
        Test NotificationType with NotificationSubWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationSubWillExpire')
        self.assertEquals(value.dump(), 'NotificationSubWillExpire')
        self.assertEquals(value.get_name(), 'NotificationSubWillExpire')
        self.assertEquals(value.get_value(), 4)

    def test_05_NotificationType_NotificationSubExpired(self):
        """
        Test NotificationType with NotificationSubExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationSubExpired')
        self.assertEquals(value.dump(), 'NotificationSubExpired')
        self.assertEquals(value.get_name(), 'NotificationSubExpired')
        self.assertEquals(value.get_value(), 5)

    def test_06_NotificationType_NotificationLicWillExpire(self):
        """
        Test NotificationType with NotificationLicWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationLicWillExpire')
        self.assertEquals(value.dump(), 'NotificationLicWillExpire')
        self.assertEquals(value.get_name(), 'NotificationLicWillExpire')
        self.assertEquals(value.get_value(), 6)

    def test_07_NotificationType_NotificationLicExpired(self):
        """
        Test NotificationType with NotificationLicExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationLicExpired')
        self.assertEquals(value.dump(), 'NotificationLicExpired')
        self.assertEquals(value.get_name(), 'NotificationLicExpired')
        self.assertEquals(value.get_value(), 7)

    def test_08_NotificationType_NotificationBackupLine(self):
        """
        Test NotificationType with NotificationBackupLine
        """
        value = pykerio.enums.NotificationType(name='NotificationBackupLine')
        self.assertEquals(value.dump(), 'NotificationBackupLine')
        self.assertEquals(value.get_name(), 'NotificationBackupLine')
        self.assertEquals(value.get_value(), 8)

    def test_09_NotificationType_NotificationInterfaceSpeed(self):
        """
        Test NotificationType with NotificationInterfaceSpeed
        """
        value = pykerio.enums.NotificationType(name='NotificationInterfaceSpeed')
        self.assertEquals(value.dump(), 'NotificationInterfaceSpeed')
        self.assertEquals(value.get_name(), 'NotificationInterfaceSpeed')
        self.assertEquals(value.get_value(), 9)

    def test_10_NotificationType_NotificationSmtp(self):
        """
        Test NotificationType with NotificationSmtp
        """
        value = pykerio.enums.NotificationType(name='NotificationSmtp')
        self.assertEquals(value.dump(), 'NotificationSmtp')
        self.assertEquals(value.get_name(), 'NotificationSmtp')
        self.assertEquals(value.get_value(), 10)

    def test_11_NotificationType_NotificationLlbLine(self):
        """
        Test NotificationType with NotificationLlbLine
        """
        value = pykerio.enums.NotificationType(name='NotificationLlbLine')
        self.assertEquals(value.dump(), 'NotificationLlbLine')
        self.assertEquals(value.get_name(), 'NotificationLlbLine')
        self.assertEquals(value.get_value(), 11)

    def test_12_NotificationType_NotificationLlb(self):
        """
        Test NotificationType with NotificationLlb
        """
        value = pykerio.enums.NotificationType(name='NotificationLlb')
        self.assertEquals(value.dump(), 'NotificationLlb')
        self.assertEquals(value.get_name(), 'NotificationLlb')
        self.assertEquals(value.get_value(), 12)

    def test_13_NotificationType_NotificationConnectionOnDemand(self):
        """
        Test NotificationType with NotificationConnectionOnDemand
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionOnDemand')
        self.assertEquals(value.dump(), 'NotificationConnectionOnDemand')
        self.assertEquals(value.get_name(), 'NotificationConnectionOnDemand')
        self.assertEquals(value.get_value(), 13)

    def test_14_NotificationType_NotificationConnectionFailover(self):
        """
        Test NotificationType with NotificationConnectionFailover
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionFailover')
        self.assertEquals(value.dump(), 'NotificationConnectionFailover')
        self.assertEquals(value.get_name(), 'NotificationConnectionFailover')
        self.assertEquals(value.get_value(), 14)

    def test_15_NotificationType_NotificationConnectionBalancing(self):
        """
        Test NotificationType with NotificationConnectionBalancing
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionBalancing')
        self.assertEquals(value.dump(), 'NotificationConnectionBalancing')
        self.assertEquals(value.get_name(), 'NotificationConnectionBalancing')
        self.assertEquals(value.get_value(), 15)

    def test_16_NotificationType_NotificationConnectionPersistent(self):
        """
        Test NotificationType with NotificationConnectionPersistent
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionPersistent')
        self.assertEquals(value.dump(), 'NotificationConnectionPersistent')
        self.assertEquals(value.get_name(), 'NotificationConnectionPersistent')
        self.assertEquals(value.get_value(), 16)

    def test_17_NotificationType_NotificationCertificateError(self):
        """
        Test NotificationType with NotificationCertificateError
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateError')
        self.assertEquals(value.dump(), 'NotificationCertificateError')
        self.assertEquals(value.get_name(), 'NotificationCertificateError')
        self.assertEquals(value.get_value(), 17)

    def test_18_NotificationType_NotificationCertificateWillExpire(self):
        """
        Test NotificationType with NotificationCertificateWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateWillExpire')
        self.assertEquals(value.dump(), 'NotificationCertificateWillExpire')
        self.assertEquals(value.get_name(), 'NotificationCertificateWillExpire')
        self.assertEquals(value.get_value(), 18)

    def test_19_NotificationType_NotificationCertificateExpired(self):
        """
        Test NotificationType with NotificationCertificateExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateExpired')
        self.assertEquals(value.dump(), 'NotificationCertificateExpired')
        self.assertEquals(value.get_name(), 'NotificationCertificateExpired')
        self.assertEquals(value.get_value(), 19)

    def test_20_NotificationType_NotificationCaWillExpire(self):
        """
        Test NotificationType with NotificationCaWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationCaWillExpire')
        self.assertEquals(value.dump(), 'NotificationCaWillExpire')
        self.assertEquals(value.get_name(), 'NotificationCaWillExpire')
        self.assertEquals(value.get_value(), 20)

    def test_21_NotificationType_NotificationCaExpired(self):
        """
        Test NotificationType with NotificationCaExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationCaExpired')
        self.assertEquals(value.dump(), 'NotificationCaExpired')
        self.assertEquals(value.get_name(), 'NotificationCaExpired')
        self.assertEquals(value.get_value(), 21)

    def test_22_NotificationType_NotificationBackupFailed(self):
        """
        Test NotificationType with NotificationBackupFailed
        """
        value = pykerio.enums.NotificationType(name='NotificationBackupFailed')
        self.assertEquals(value.dump(), 'NotificationBackupFailed')
        self.assertEquals(value.get_name(), 'NotificationBackupFailed')
        self.assertEquals(value.get_value(), 22)

    def test_23_NotificationType_NotificationPacketDump(self):
        """
        Test NotificationType with NotificationPacketDump
        """
        value = pykerio.enums.NotificationType(name='NotificationPacketDump')
        self.assertEquals(value.dump(), 'NotificationPacketDump')
        self.assertEquals(value.get_name(), 'NotificationPacketDump')
        self.assertEquals(value.get_value(), 23)

    def test_24_NotificationType_NotificationUnknown(self):
        """
        Test NotificationType with NotificationUnknown
        """
        value = pykerio.enums.NotificationType(name='NotificationUnknown')
        self.assertEquals(value.dump(), 'NotificationUnknown')
        self.assertEquals(value.get_name(), 'NotificationUnknown')
        self.assertEquals(value.get_value(), 24)

    @unittest.expectedFailure
    def test_99_NotificationType_FAIL(self):
        """
        Test NotificationType with FAIL
        """
        value = pykerio.enums.NotificationType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
