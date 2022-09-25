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

from pykerio.enums import NotificationType


class TestCase_NotificationType(unittest.TestCase):
    def test_00_NotificationUpdate(self):
        """
        Test NotificationType with NotificationUpdate
        """
        value = NotificationType.NotificationUpdate
        self.assertEqual(value.dump(), 'NotificationUpdate')
        self.assertEqual(value.name, 'NotificationUpdate')
        self.assertEqual(value.value, 0)

    def test_01_NotificationDump(self):
        """
        Test NotificationType with NotificationDump
        """
        value = NotificationType.NotificationDump
        self.assertEqual(value.dump(), 'NotificationDump')
        self.assertEqual(value.name, 'NotificationDump')
        self.assertEqual(value.value, 1)

    def test_02_NotificationLowMemory(self):
        """
        Test NotificationType with NotificationLowMemory
        """
        value = NotificationType.NotificationLowMemory
        self.assertEqual(value.dump(), 'NotificationLowMemory')
        self.assertEqual(value.name, 'NotificationLowMemory')
        self.assertEqual(value.value, 2)

    def test_03_NotificationDomains(self):
        """
        Test NotificationType with NotificationDomains
        """
        value = NotificationType.NotificationDomains
        self.assertEqual(value.dump(), 'NotificationDomains')
        self.assertEqual(value.name, 'NotificationDomains')
        self.assertEqual(value.value, 3)

    def test_04_NotificationSubWillExpire(self):
        """
        Test NotificationType with NotificationSubWillExpire
        """
        value = NotificationType.NotificationSubWillExpire
        self.assertEqual(value.dump(), 'NotificationSubWillExpire')
        self.assertEqual(value.name, 'NotificationSubWillExpire')
        self.assertEqual(value.value, 4)

    def test_05_NotificationSubExpired(self):
        """
        Test NotificationType with NotificationSubExpired
        """
        value = NotificationType.NotificationSubExpired
        self.assertEqual(value.dump(), 'NotificationSubExpired')
        self.assertEqual(value.name, 'NotificationSubExpired')
        self.assertEqual(value.value, 5)

    def test_06_NotificationLicWillExpire(self):
        """
        Test NotificationType with NotificationLicWillExpire
        """
        value = NotificationType.NotificationLicWillExpire
        self.assertEqual(value.dump(), 'NotificationLicWillExpire')
        self.assertEqual(value.name, 'NotificationLicWillExpire')
        self.assertEqual(value.value, 6)

    def test_07_NotificationLicExpired(self):
        """
        Test NotificationType with NotificationLicExpired
        """
        value = NotificationType.NotificationLicExpired
        self.assertEqual(value.dump(), 'NotificationLicExpired')
        self.assertEqual(value.name, 'NotificationLicExpired')
        self.assertEqual(value.value, 7)

    def test_08_NotificationBackupLine(self):
        """
        Test NotificationType with NotificationBackupLine
        """
        value = NotificationType.NotificationBackupLine
        self.assertEqual(value.dump(), 'NotificationBackupLine')
        self.assertEqual(value.name, 'NotificationBackupLine')
        self.assertEqual(value.value, 8)

    def test_09_NotificationInterfaceSpeed(self):
        """
        Test NotificationType with NotificationInterfaceSpeed
        """
        value = NotificationType.NotificationInterfaceSpeed
        self.assertEqual(value.dump(), 'NotificationInterfaceSpeed')
        self.assertEqual(value.name, 'NotificationInterfaceSpeed')
        self.assertEqual(value.value, 9)

    def test_10_NotificationSmtp(self):
        """
        Test NotificationType with NotificationSmtp
        """
        value = NotificationType.NotificationSmtp
        self.assertEqual(value.dump(), 'NotificationSmtp')
        self.assertEqual(value.name, 'NotificationSmtp')
        self.assertEqual(value.value, 10)

    def test_11_NotificationLlbLine(self):
        """
        Test NotificationType with NotificationLlbLine
        """
        value = NotificationType.NotificationLlbLine
        self.assertEqual(value.dump(), 'NotificationLlbLine')
        self.assertEqual(value.name, 'NotificationLlbLine')
        self.assertEqual(value.value, 11)

    def test_12_NotificationLlb(self):
        """
        Test NotificationType with NotificationLlb
        """
        value = NotificationType.NotificationLlb
        self.assertEqual(value.dump(), 'NotificationLlb')
        self.assertEqual(value.name, 'NotificationLlb')
        self.assertEqual(value.value, 12)

    def test_13_NotificationConnectionOnDemand(self):
        """
        Test NotificationType with NotificationConnectionOnDemand
        """
        value = NotificationType.NotificationConnectionOnDemand
        self.assertEqual(value.dump(), 'NotificationConnectionOnDemand')
        self.assertEqual(value.name, 'NotificationConnectionOnDemand')
        self.assertEqual(value.value, 13)

    def test_14_NotificationConnectionFailover(self):
        """
        Test NotificationType with NotificationConnectionFailover
        """
        value = NotificationType.NotificationConnectionFailover
        self.assertEqual(value.dump(), 'NotificationConnectionFailover')
        self.assertEqual(value.name, 'NotificationConnectionFailover')
        self.assertEqual(value.value, 14)

    def test_15_NotificationConnectionBalancing(self):
        """
        Test NotificationType with NotificationConnectionBalancing
        """
        value = NotificationType.NotificationConnectionBalancing
        self.assertEqual(value.dump(), 'NotificationConnectionBalancing')
        self.assertEqual(value.name, 'NotificationConnectionBalancing')
        self.assertEqual(value.value, 15)

    def test_16_NotificationConnectionPersistent(self):
        """
        Test NotificationType with NotificationConnectionPersistent
        """
        value = NotificationType.NotificationConnectionPersistent
        self.assertEqual(value.dump(), 'NotificationConnectionPersistent')
        self.assertEqual(value.name, 'NotificationConnectionPersistent')
        self.assertEqual(value.value, 16)

    def test_17_NotificationCertificateError(self):
        """
        Test NotificationType with NotificationCertificateError
        """
        value = NotificationType.NotificationCertificateError
        self.assertEqual(value.dump(), 'NotificationCertificateError')
        self.assertEqual(value.name, 'NotificationCertificateError')
        self.assertEqual(value.value, 17)

    def test_18_NotificationCertificateWillExpire(self):
        """
        Test NotificationType with NotificationCertificateWillExpire
        """
        value = NotificationType.NotificationCertificateWillExpire
        self.assertEqual(value.dump(), 'NotificationCertificateWillExpire')
        self.assertEqual(value.name, 'NotificationCertificateWillExpire')
        self.assertEqual(value.value, 18)

    def test_19_NotificationCertificateExpired(self):
        """
        Test NotificationType with NotificationCertificateExpired
        """
        value = NotificationType.NotificationCertificateExpired
        self.assertEqual(value.dump(), 'NotificationCertificateExpired')
        self.assertEqual(value.name, 'NotificationCertificateExpired')
        self.assertEqual(value.value, 19)

    def test_20_NotificationCaWillExpire(self):
        """
        Test NotificationType with NotificationCaWillExpire
        """
        value = NotificationType.NotificationCaWillExpire
        self.assertEqual(value.dump(), 'NotificationCaWillExpire')
        self.assertEqual(value.name, 'NotificationCaWillExpire')
        self.assertEqual(value.value, 20)

    def test_21_NotificationCaExpired(self):
        """
        Test NotificationType with NotificationCaExpired
        """
        value = NotificationType.NotificationCaExpired
        self.assertEqual(value.dump(), 'NotificationCaExpired')
        self.assertEqual(value.name, 'NotificationCaExpired')
        self.assertEqual(value.value, 21)

    def test_22_NotificationBackupFailed(self):
        """
        Test NotificationType with NotificationBackupFailed
        """
        value = NotificationType.NotificationBackupFailed
        self.assertEqual(value.dump(), 'NotificationBackupFailed')
        self.assertEqual(value.name, 'NotificationBackupFailed')
        self.assertEqual(value.value, 22)

    def test_23_NotificationPacketDump(self):
        """
        Test NotificationType with NotificationPacketDump
        """
        value = NotificationType.NotificationPacketDump
        self.assertEqual(value.dump(), 'NotificationPacketDump')
        self.assertEqual(value.name, 'NotificationPacketDump')
        self.assertEqual(value.value, 23)

    def test_24_NotificationUnknown(self):
        """
        Test NotificationType with NotificationUnknown
        """
        value = NotificationType.NotificationUnknown
        self.assertEqual(value.dump(), 'NotificationUnknown')
        self.assertEqual(value.name, 'NotificationUnknown')
        self.assertEqual(value.value, 24)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test NotificationType with FAIL
        """
        value = NotificationType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
