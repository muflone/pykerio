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

from pykerio.enums import ActivityType


class TestCase_ActivityType(unittest.TestCase):
    def test_00_ActivityTypeWeb(self):
        """
        Test ActivityType with ActivityTypeWeb
        """
        value = ActivityType.ActivityTypeWeb
        self.assertEqual(value.dump(), 'ActivityTypeWeb')
        self.assertEqual(value.name, 'ActivityTypeWeb')
        self.assertEqual(value.value, 0)

    def test_01_ActivityTypeWebSearch(self):
        """
        Test ActivityType with ActivityTypeWebSearch
        """
        value = ActivityType.ActivityTypeWebSearch
        self.assertEqual(value.dump(), 'ActivityTypeWebSearch')
        self.assertEqual(value.name, 'ActivityTypeWebSearch')
        self.assertEqual(value.value, 1)

    def test_02_ActivityTypeMail(self):
        """
        Test ActivityType with ActivityTypeMail
        """
        value = ActivityType.ActivityTypeMail
        self.assertEqual(value.dump(), 'ActivityTypeMail')
        self.assertEqual(value.name, 'ActivityTypeMail')
        self.assertEqual(value.value, 2)

    def test_03_ActivityTypeDownload(self):
        """
        Test ActivityType with ActivityTypeDownload
        """
        value = ActivityType.ActivityTypeDownload
        self.assertEqual(value.dump(), 'ActivityTypeDownload')
        self.assertEqual(value.name, 'ActivityTypeDownload')
        self.assertEqual(value.value, 3)

    def test_04_ActivityTypeUpload(self):
        """
        Test ActivityType with ActivityTypeUpload
        """
        value = ActivityType.ActivityTypeUpload
        self.assertEqual(value.dump(), 'ActivityTypeUpload')
        self.assertEqual(value.name, 'ActivityTypeUpload')
        self.assertEqual(value.value, 4)

    def test_05_ActivityTypeMultimedia(self):
        """
        Test ActivityType with ActivityTypeMultimedia
        """
        value = ActivityType.ActivityTypeMultimedia
        self.assertEqual(value.dump(), 'ActivityTypeMultimedia')
        self.assertEqual(value.name, 'ActivityTypeMultimedia')
        self.assertEqual(value.value, 5)

    def test_06_ActivityTypeP2p(self):
        """
        Test ActivityType with ActivityTypeP2p
        """
        value = ActivityType.ActivityTypeP2p
        self.assertEqual(value.dump(), 'ActivityTypeP2p')
        self.assertEqual(value.name, 'ActivityTypeP2p')
        self.assertEqual(value.value, 6)

    def test_07_ActivityTypeRemoteAccess(self):
        """
        Test ActivityType with ActivityTypeRemoteAccess
        """
        value = ActivityType.ActivityTypeRemoteAccess
        self.assertEqual(value.dump(), 'ActivityTypeRemoteAccess')
        self.assertEqual(value.name, 'ActivityTypeRemoteAccess')
        self.assertEqual(value.value, 7)

    def test_08_ActivityTypeVpn(self):
        """
        Test ActivityType with ActivityTypeVpn
        """
        value = ActivityType.ActivityTypeVpn
        self.assertEqual(value.dump(), 'ActivityTypeVpn')
        self.assertEqual(value.name, 'ActivityTypeVpn')
        self.assertEqual(value.value, 8)

    def test_09_ActivityTypeInstantMessaging(self):
        """
        Test ActivityType with ActivityTypeInstantMessaging
        """
        value = ActivityType.ActivityTypeInstantMessaging
        self.assertEqual(value.dump(), 'ActivityTypeInstantMessaging')
        self.assertEqual(value.name, 'ActivityTypeInstantMessaging')
        self.assertEqual(value.value, 9)

    def test_10_ActivityTypeHugeConnection(self):
        """
        Test ActivityType with ActivityTypeHugeConnection
        """
        value = ActivityType.ActivityTypeHugeConnection
        self.assertEqual(value.dump(), 'ActivityTypeHugeConnection')
        self.assertEqual(value.name, 'ActivityTypeHugeConnection')
        self.assertEqual(value.value, 10)

    def test_11_ActivityTypeMailConnection(self):
        """
        Test ActivityType with ActivityTypeMailConnection
        """
        value = ActivityType.ActivityTypeMailConnection
        self.assertEqual(value.dump(), 'ActivityTypeMailConnection')
        self.assertEqual(value.name, 'ActivityTypeMailConnection')
        self.assertEqual(value.value, 11)

    def test_12_ActivityTypeP2pAttempt(self):
        """
        Test ActivityType with ActivityTypeP2pAttempt
        """
        value = ActivityType.ActivityTypeP2pAttempt
        self.assertEqual(value.dump(), 'ActivityTypeP2pAttempt')
        self.assertEqual(value.name, 'ActivityTypeP2pAttempt')
        self.assertEqual(value.value, 12)

    def test_13_ActivityTypeWebConnection(self):
        """
        Test ActivityType with ActivityTypeWebConnection
        """
        value = ActivityType.ActivityTypeWebConnection
        self.assertEqual(value.dump(), 'ActivityTypeWebConnection')
        self.assertEqual(value.name, 'ActivityTypeWebConnection')
        self.assertEqual(value.value, 13)

    def test_14_ActivityTypeHTTPConnection(self):
        """
        Test ActivityType with ActivityTypeHTTPConnection
        """
        value = ActivityType.ActivityTypeHTTPConnection
        self.assertEqual(value.dump(), 'ActivityTypeHTTPConnection')
        self.assertEqual(value.name, 'ActivityTypeHTTPConnection')
        self.assertEqual(value.value, 14)

    def test_15_ActivityTypeWebMultimedia(self):
        """
        Test ActivityType with ActivityTypeWebMultimedia
        """
        value = ActivityType.ActivityTypeWebMultimedia
        self.assertEqual(value.dump(), 'ActivityTypeWebMultimedia')
        self.assertEqual(value.name, 'ActivityTypeWebMultimedia')
        self.assertEqual(value.value, 15)

    def test_16_ActivityTypeSip(self):
        """
        Test ActivityType with ActivityTypeSip
        """
        value = ActivityType.ActivityTypeSip
        self.assertEqual(value.dump(), 'ActivityTypeSip')
        self.assertEqual(value.name, 'ActivityTypeSip')
        self.assertEqual(value.value, 16)

    def test_17_ActivityTypeSocialNetwork(self):
        """
        Test ActivityType with ActivityTypeSocialNetwork
        """
        value = ActivityType.ActivityTypeSocialNetwork
        self.assertEqual(value.dump(), 'ActivityTypeSocialNetwork')
        self.assertEqual(value.name, 'ActivityTypeSocialNetwork')
        self.assertEqual(value.value, 17)
