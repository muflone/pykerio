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


class TestCase_NotificationType(unittest.TestCase):
    def test_00_NotificationUpdate(self):
        """
        Test NotificationType with NotificationUpdate
        """
        value = pykerio.enums.NotificationType(name='NotificationUpdate')
        self.assertEqual(value.dump(), 'NotificationUpdate')
        self.assertEqual(value.get_name(), 'NotificationUpdate')
        self.assertEqual(value.get_value(), 0)

    def test_01_NotificationDump(self):
        """
        Test NotificationType with NotificationDump
        """
        value = pykerio.enums.NotificationType(name='NotificationDump')
        self.assertEqual(value.dump(), 'NotificationDump')
        self.assertEqual(value.get_name(), 'NotificationDump')
        self.assertEqual(value.get_value(), 1)

    def test_02_NotificationLowMemory(self):
        """
        Test NotificationType with NotificationLowMemory
        """
        value = pykerio.enums.NotificationType(name='NotificationLowMemory')
        self.assertEqual(value.dump(), 'NotificationLowMemory')
        self.assertEqual(value.get_name(), 'NotificationLowMemory')
        self.assertEqual(value.get_value(), 2)

    def test_03_NotificationDomains(self):
        """
        Test NotificationType with NotificationDomains
        """
        value = pykerio.enums.NotificationType(name='NotificationDomains')
        self.assertEqual(value.dump(), 'NotificationDomains')
        self.assertEqual(value.get_name(), 'NotificationDomains')
        self.assertEqual(value.get_value(), 3)

    def test_04_NotificationSubWillExpire(self):
        """
        Test NotificationType with NotificationSubWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationSubWillExpire')
        self.assertEqual(value.dump(), 'NotificationSubWillExpire')
        self.assertEqual(value.get_name(), 'NotificationSubWillExpire')
        self.assertEqual(value.get_value(), 4)

    def test_05_NotificationSubExpired(self):
        """
        Test NotificationType with NotificationSubExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationSubExpired')
        self.assertEqual(value.dump(), 'NotificationSubExpired')
        self.assertEqual(value.get_name(), 'NotificationSubExpired')
        self.assertEqual(value.get_value(), 5)

    def test_06_NotificationLicWillExpire(self):
        """
        Test NotificationType with NotificationLicWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationLicWillExpire')
        self.assertEqual(value.dump(), 'NotificationLicWillExpire')
        self.assertEqual(value.get_name(), 'NotificationLicWillExpire')
        self.assertEqual(value.get_value(), 6)

    def test_07_NotificationLicExpired(self):
        """
        Test NotificationType with NotificationLicExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationLicExpired')
        self.assertEqual(value.dump(), 'NotificationLicExpired')
        self.assertEqual(value.get_name(), 'NotificationLicExpired')
        self.assertEqual(value.get_value(), 7)

    def test_08_NotificationBackupLine(self):
        """
        Test NotificationType with NotificationBackupLine
        """
        value = pykerio.enums.NotificationType(name='NotificationBackupLine')
        self.assertEqual(value.dump(), 'NotificationBackupLine')
        self.assertEqual(value.get_name(), 'NotificationBackupLine')
        self.assertEqual(value.get_value(), 8)

    def test_09_NotificationInterfaceSpeed(self):
        """
        Test NotificationType with NotificationInterfaceSpeed
        """
        value = pykerio.enums.NotificationType(name='NotificationInterfaceSpeed')
        self.assertEqual(value.dump(), 'NotificationInterfaceSpeed')
        self.assertEqual(value.get_name(), 'NotificationInterfaceSpeed')
        self.assertEqual(value.get_value(), 9)

    def test_10_NotificationSmtp(self):
        """
        Test NotificationType with NotificationSmtp
        """
        value = pykerio.enums.NotificationType(name='NotificationSmtp')
        self.assertEqual(value.dump(), 'NotificationSmtp')
        self.assertEqual(value.get_name(), 'NotificationSmtp')
        self.assertEqual(value.get_value(), 10)

    def test_11_NotificationLlbLine(self):
        """
        Test NotificationType with NotificationLlbLine
        """
        value = pykerio.enums.NotificationType(name='NotificationLlbLine')
        self.assertEqual(value.dump(), 'NotificationLlbLine')
        self.assertEqual(value.get_name(), 'NotificationLlbLine')
        self.assertEqual(value.get_value(), 11)

    def test_12_NotificationLlb(self):
        """
        Test NotificationType with NotificationLlb
        """
        value = pykerio.enums.NotificationType(name='NotificationLlb')
        self.assertEqual(value.dump(), 'NotificationLlb')
        self.assertEqual(value.get_name(), 'NotificationLlb')
        self.assertEqual(value.get_value(), 12)

    def test_13_NotificationConnectionOnDemand(self):
        """
        Test NotificationType with NotificationConnectionOnDemand
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionOnDemand')
        self.assertEqual(value.dump(), 'NotificationConnectionOnDemand')
        self.assertEqual(value.get_name(), 'NotificationConnectionOnDemand')
        self.assertEqual(value.get_value(), 13)

    def test_14_NotificationConnectionFailover(self):
        """
        Test NotificationType with NotificationConnectionFailover
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionFailover')
        self.assertEqual(value.dump(), 'NotificationConnectionFailover')
        self.assertEqual(value.get_name(), 'NotificationConnectionFailover')
        self.assertEqual(value.get_value(), 14)

    def test_15_NotificationConnectionBalancing(self):
        """
        Test NotificationType with NotificationConnectionBalancing
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionBalancing')
        self.assertEqual(value.dump(), 'NotificationConnectionBalancing')
        self.assertEqual(value.get_name(), 'NotificationConnectionBalancing')
        self.assertEqual(value.get_value(), 15)

    def test_16_NotificationConnectionPersistent(self):
        """
        Test NotificationType with NotificationConnectionPersistent
        """
        value = pykerio.enums.NotificationType(name='NotificationConnectionPersistent')
        self.assertEqual(value.dump(), 'NotificationConnectionPersistent')
        self.assertEqual(value.get_name(), 'NotificationConnectionPersistent')
        self.assertEqual(value.get_value(), 16)

    def test_17_NotificationCertificateError(self):
        """
        Test NotificationType with NotificationCertificateError
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateError')
        self.assertEqual(value.dump(), 'NotificationCertificateError')
        self.assertEqual(value.get_name(), 'NotificationCertificateError')
        self.assertEqual(value.get_value(), 17)

    def test_18_NotificationCertificateWillExpire(self):
        """
        Test NotificationType with NotificationCertificateWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateWillExpire')
        self.assertEqual(value.dump(), 'NotificationCertificateWillExpire')
        self.assertEqual(value.get_name(), 'NotificationCertificateWillExpire')
        self.assertEqual(value.get_value(), 18)

    def test_19_NotificationCertificateExpired(self):
        """
        Test NotificationType with NotificationCertificateExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationCertificateExpired')
        self.assertEqual(value.dump(), 'NotificationCertificateExpired')
        self.assertEqual(value.get_name(), 'NotificationCertificateExpired')
        self.assertEqual(value.get_value(), 19)

    def test_20_NotificationCaWillExpire(self):
        """
        Test NotificationType with NotificationCaWillExpire
        """
        value = pykerio.enums.NotificationType(name='NotificationCaWillExpire')
        self.assertEqual(value.dump(), 'NotificationCaWillExpire')
        self.assertEqual(value.get_name(), 'NotificationCaWillExpire')
        self.assertEqual(value.get_value(), 20)

    def test_21_NotificationCaExpired(self):
        """
        Test NotificationType with NotificationCaExpired
        """
        value = pykerio.enums.NotificationType(name='NotificationCaExpired')
        self.assertEqual(value.dump(), 'NotificationCaExpired')
        self.assertEqual(value.get_name(), 'NotificationCaExpired')
        self.assertEqual(value.get_value(), 21)

    def test_22_NotificationBackupFailed(self):
        """
        Test NotificationType with NotificationBackupFailed
        """
        value = pykerio.enums.NotificationType(name='NotificationBackupFailed')
        self.assertEqual(value.dump(), 'NotificationBackupFailed')
        self.assertEqual(value.get_name(), 'NotificationBackupFailed')
        self.assertEqual(value.get_value(), 22)

    def test_23_NotificationPacketDump(self):
        """
        Test NotificationType with NotificationPacketDump
        """
        value = pykerio.enums.NotificationType(name='NotificationPacketDump')
        self.assertEqual(value.dump(), 'NotificationPacketDump')
        self.assertEqual(value.get_name(), 'NotificationPacketDump')
        self.assertEqual(value.get_value(), 23)

    def test_24_NotificationUnknown(self):
        """
        Test NotificationType with NotificationUnknown
        """
        value = pykerio.enums.NotificationType(name='NotificationUnknown')
        self.assertEqual(value.dump(), 'NotificationUnknown')
        self.assertEqual(value.get_name(), 'NotificationUnknown')
        self.assertEqual(value.get_value(), 24)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test NotificationType with FAIL
        """
        value = pykerio.enums.NotificationType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
