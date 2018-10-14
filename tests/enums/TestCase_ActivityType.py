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


class TestCase_ActivityType(unittest.TestCase):
    def test_00_ActivityType_ActivityTypeWeb(self):
        """
        Test ActivityType with ActivityTypeWeb
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWeb')
        self.assertEquals(value.dump(), 'ActivityTypeWeb')
        self.assertEquals(value.get_name(), 'ActivityTypeWeb')
        self.assertEquals(value.get_value(), 0)

    def test_01_ActivityType_ActivityTypeWebSearch(self):
        """
        Test ActivityType with ActivityTypeWebSearch
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebSearch')
        self.assertEquals(value.dump(), 'ActivityTypeWebSearch')
        self.assertEquals(value.get_name(), 'ActivityTypeWebSearch')
        self.assertEquals(value.get_value(), 1)

    def test_02_ActivityType_ActivityTypeMail(self):
        """
        Test ActivityType with ActivityTypeMail
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMail')
        self.assertEquals(value.dump(), 'ActivityTypeMail')
        self.assertEquals(value.get_name(), 'ActivityTypeMail')
        self.assertEquals(value.get_value(), 2)

    def test_03_ActivityType_ActivityTypeDownload(self):
        """
        Test ActivityType with ActivityTypeDownload
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeDownload')
        self.assertEquals(value.dump(), 'ActivityTypeDownload')
        self.assertEquals(value.get_name(), 'ActivityTypeDownload')
        self.assertEquals(value.get_value(), 3)

    def test_04_ActivityType_ActivityTypeUpload(self):
        """
        Test ActivityType with ActivityTypeUpload
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeUpload')
        self.assertEquals(value.dump(), 'ActivityTypeUpload')
        self.assertEquals(value.get_name(), 'ActivityTypeUpload')
        self.assertEquals(value.get_value(), 4)

    def test_05_ActivityType_ActivityTypeMultimedia(self):
        """
        Test ActivityType with ActivityTypeMultimedia
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMultimedia')
        self.assertEquals(value.dump(), 'ActivityTypeMultimedia')
        self.assertEquals(value.get_name(), 'ActivityTypeMultimedia')
        self.assertEquals(value.get_value(), 5)

    def test_06_ActivityType_ActivityTypeP2p(self):
        """
        Test ActivityType with ActivityTypeP2p
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeP2p')
        self.assertEquals(value.dump(), 'ActivityTypeP2p')
        self.assertEquals(value.get_name(), 'ActivityTypeP2p')
        self.assertEquals(value.get_value(), 6)

    def test_07_ActivityType_ActivityTypeRemoteAccess(self):
        """
        Test ActivityType with ActivityTypeRemoteAccess
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeRemoteAccess')
        self.assertEquals(value.dump(), 'ActivityTypeRemoteAccess')
        self.assertEquals(value.get_name(), 'ActivityTypeRemoteAccess')
        self.assertEquals(value.get_value(), 7)

    def test_08_ActivityType_ActivityTypeVpn(self):
        """
        Test ActivityType with ActivityTypeVpn
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeVpn')
        self.assertEquals(value.dump(), 'ActivityTypeVpn')
        self.assertEquals(value.get_name(), 'ActivityTypeVpn')
        self.assertEquals(value.get_value(), 8)

    def test_09_ActivityType_ActivityTypeInstantMessaging(self):
        """
        Test ActivityType with ActivityTypeInstantMessaging
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeInstantMessaging')
        self.assertEquals(value.dump(), 'ActivityTypeInstantMessaging')
        self.assertEquals(value.get_name(), 'ActivityTypeInstantMessaging')
        self.assertEquals(value.get_value(), 9)

    def test_10_ActivityType_ActivityTypeHugeConnection(self):
        """
        Test ActivityType with ActivityTypeHugeConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeHugeConnection')
        self.assertEquals(value.dump(), 'ActivityTypeHugeConnection')
        self.assertEquals(value.get_name(), 'ActivityTypeHugeConnection')
        self.assertEquals(value.get_value(), 10)

    def test_11_ActivityType_ActivityTypeMailConnection(self):
        """
        Test ActivityType with ActivityTypeMailConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeMailConnection')
        self.assertEquals(value.dump(), 'ActivityTypeMailConnection')
        self.assertEquals(value.get_name(), 'ActivityTypeMailConnection')
        self.assertEquals(value.get_value(), 11)

    def test_12_ActivityType_ActivityTypeP2pAttempt(self):
        """
        Test ActivityType with ActivityTypeP2pAttempt
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeP2pAttempt')
        self.assertEquals(value.dump(), 'ActivityTypeP2pAttempt')
        self.assertEquals(value.get_name(), 'ActivityTypeP2pAttempt')
        self.assertEquals(value.get_value(), 12)

    def test_13_ActivityType_ActivityTypeWebConnection(self):
        """
        Test ActivityType with ActivityTypeWebConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebConnection')
        self.assertEquals(value.dump(), 'ActivityTypeWebConnection')
        self.assertEquals(value.get_name(), 'ActivityTypeWebConnection')
        self.assertEquals(value.get_value(), 13)

    def test_14_ActivityType_ActivityTypeHTTPConnection(self):
        """
        Test ActivityType with ActivityTypeHTTPConnection
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeHTTPConnection')
        self.assertEquals(value.dump(), 'ActivityTypeHTTPConnection')
        self.assertEquals(value.get_name(), 'ActivityTypeHTTPConnection')
        self.assertEquals(value.get_value(), 14)

    def test_15_ActivityType_ActivityTypeWebMultimedia(self):
        """
        Test ActivityType with ActivityTypeWebMultimedia
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeWebMultimedia')
        self.assertEquals(value.dump(), 'ActivityTypeWebMultimedia')
        self.assertEquals(value.get_name(), 'ActivityTypeWebMultimedia')
        self.assertEquals(value.get_value(), 15)

    def test_16_ActivityType_ActivityTypeSip(self):
        """
        Test ActivityType with ActivityTypeSip
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeSip')
        self.assertEquals(value.dump(), 'ActivityTypeSip')
        self.assertEquals(value.get_name(), 'ActivityTypeSip')
        self.assertEquals(value.get_value(), 16)

    def test_17_ActivityType_ActivityTypeSocialNetwork(self):
        """
        Test ActivityType with ActivityTypeSocialNetwork
        """
        value = pykerio.enums.ActivityType(name='ActivityTypeSocialNetwork')
        self.assertEquals(value.dump(), 'ActivityTypeSocialNetwork')
        self.assertEquals(value.get_name(), 'ActivityTypeSocialNetwork')
        self.assertEquals(value.get_value(), 17)

    @unittest.expectedFailure
    def test_99_ActivityType_FAIL(self):
        """
        Test ActivityType with FAIL
        """
        value = pykerio.enums.ActivityType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
