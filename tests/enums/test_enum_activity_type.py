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


class TestCase_ActivityType(unittest.TestCase):
    def test_00_ActivityTypeWeb(self):
        """
        Test ActivityType with ActivityTypeWeb
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWeb')
        self.assertEqual(value.dump(), 'ActivityTypeWeb')
        self.assertEqual(value.get_name(), 'ActivityTypeWeb')
        self.assertEqual(value.get_value(), 0)

    def test_01_ActivityTypeWebSearch(self):
        """
        Test ActivityType with ActivityTypeWebSearch
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebSearch')
        self.assertEqual(value.dump(), 'ActivityTypeWebSearch')
        self.assertEqual(value.get_name(), 'ActivityTypeWebSearch')
        self.assertEqual(value.get_value(), 1)

    def test_02_ActivityTypeMail(self):
        """
        Test ActivityType with ActivityTypeMail
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMail')
        self.assertEqual(value.dump(), 'ActivityTypeMail')
        self.assertEqual(value.get_name(), 'ActivityTypeMail')
        self.assertEqual(value.get_value(), 2)

    def test_03_ActivityTypeDownload(self):
        """
        Test ActivityType with ActivityTypeDownload
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeDownload')
        self.assertEqual(value.dump(), 'ActivityTypeDownload')
        self.assertEqual(value.get_name(), 'ActivityTypeDownload')
        self.assertEqual(value.get_value(), 3)

    def test_04_ActivityTypeUpload(self):
        """
        Test ActivityType with ActivityTypeUpload
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeUpload')
        self.assertEqual(value.dump(), 'ActivityTypeUpload')
        self.assertEqual(value.get_name(), 'ActivityTypeUpload')
        self.assertEqual(value.get_value(), 4)

    def test_05_ActivityTypeMultimedia(self):
        """
        Test ActivityType with ActivityTypeMultimedia
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMultimedia')
        self.assertEqual(value.dump(), 'ActivityTypeMultimedia')
        self.assertEqual(value.get_name(), 'ActivityTypeMultimedia')
        self.assertEqual(value.get_value(), 5)

    def test_06_ActivityTypeP2p(self):
        """
        Test ActivityType with ActivityTypeP2p
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeP2p')
        self.assertEqual(value.dump(), 'ActivityTypeP2p')
        self.assertEqual(value.get_name(), 'ActivityTypeP2p')
        self.assertEqual(value.get_value(), 6)

    def test_07_ActivityTypeRemoteAccess(self):
        """
        Test ActivityType with ActivityTypeRemoteAccess
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeRemoteAccess')
        self.assertEqual(value.dump(), 'ActivityTypeRemoteAccess')
        self.assertEqual(value.get_name(), 'ActivityTypeRemoteAccess')
        self.assertEqual(value.get_value(), 7)

    def test_08_ActivityTypeVpn(self):
        """
        Test ActivityType with ActivityTypeVpn
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeVpn')
        self.assertEqual(value.dump(), 'ActivityTypeVpn')
        self.assertEqual(value.get_name(), 'ActivityTypeVpn')
        self.assertEqual(value.get_value(), 8)

    def test_09_ActivityTypeInstantMessaging(self):
        """
        Test ActivityType with ActivityTypeInstantMessaging
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeInstantMessaging')
        self.assertEqual(value.dump(), 'ActivityTypeInstantMessaging')
        self.assertEqual(value.get_name(), 'ActivityTypeInstantMessaging')
        self.assertEqual(value.get_value(), 9)

    def test_10_ActivityTypeHugeConnection(self):
        """
        Test ActivityType with ActivityTypeHugeConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeHugeConnection')
        self.assertEqual(value.dump(), 'ActivityTypeHugeConnection')
        self.assertEqual(value.get_name(), 'ActivityTypeHugeConnection')
        self.assertEqual(value.get_value(), 10)

    def test_11_ActivityTypeMailConnection(self):
        """
        Test ActivityType with ActivityTypeMailConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMailConnection')
        self.assertEqual(value.dump(), 'ActivityTypeMailConnection')
        self.assertEqual(value.get_name(), 'ActivityTypeMailConnection')
        self.assertEqual(value.get_value(), 11)

    def test_12_ActivityTypeP2pAttempt(self):
        """
        Test ActivityType with ActivityTypeP2pAttempt
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeP2pAttempt')
        self.assertEqual(value.dump(), 'ActivityTypeP2pAttempt')
        self.assertEqual(value.get_name(), 'ActivityTypeP2pAttempt')
        self.assertEqual(value.get_value(), 12)

    def test_13_ActivityTypeWebConnection(self):
        """
        Test ActivityType with ActivityTypeWebConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebConnection')
        self.assertEqual(value.dump(), 'ActivityTypeWebConnection')
        self.assertEqual(value.get_name(), 'ActivityTypeWebConnection')
        self.assertEqual(value.get_value(), 13)

    def test_14_ActivityTypeHTTPConnection(self):
        """
        Test ActivityType with ActivityTypeHTTPConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeHTTPConnection')
        self.assertEqual(value.dump(), 'ActivityTypeHTTPConnection')
        self.assertEqual(value.get_name(), 'ActivityTypeHTTPConnection')
        self.assertEqual(value.get_value(), 14)

    def test_15_ActivityTypeWebMultimedia(self):
        """
        Test ActivityType with ActivityTypeWebMultimedia
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebMultimedia')
        self.assertEqual(value.dump(), 'ActivityTypeWebMultimedia')
        self.assertEqual(value.get_name(), 'ActivityTypeWebMultimedia')
        self.assertEqual(value.get_value(), 15)

    def test_16_ActivityTypeSip(self):
        """
        Test ActivityType with ActivityTypeSip
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeSip')
        self.assertEqual(value.dump(), 'ActivityTypeSip')
        self.assertEqual(value.get_name(), 'ActivityTypeSip')
        self.assertEqual(value.get_value(), 16)

    def test_17_ActivityTypeSocialNetwork(self):
        """
        Test ActivityType with ActivityTypeSocialNetwork
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeSocialNetwork')
        self.assertEqual(value.dump(), 'ActivityTypeSocialNetwork')
        self.assertEqual(value.get_name(), 'ActivityTypeSocialNetwork')
        self.assertEqual(value.get_value(), 17)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ActivityType with FAIL
        """
        value = pykerio.enums.ActivityType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
