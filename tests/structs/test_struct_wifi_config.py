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


class TestCase_WifiConfig(unittest.TestCase):
    def test_01_WifiConfig(self):
        """
        Test WifiConfig
        """
        kid = pykerio.types.KId('WLAN')
        secret = 'My password'
        ssidconfig = pykerio.structs.WifiSsidConfig({
            'id': kid,
            'enabled': True,
            'assignment': pykerio.enums.PortAssignmentType(
                name='PortAssignmentStandalone'),
            'ssid': 'My WiFi',
            'group': pykerio.enums.InterfaceGroupType(name='Internet'),
            'encryption': pykerio.enums.WifiEncryptionType(
                name='WifiEncryptionWpaPsk'),
            'wpaPassword': secret})
        ssidconfiglist = pykerio.lists.WifiSsidConfigList()
        ssidconfiglist.append(ssidconfig)

        country = pykerio.types.KId('IT')

        teststruct = pykerio.structs.WifiConfig({
            'country': country,
            'band': pykerio.enums.WifiBandType(name='WifiBandBG'),
            'band80211n': False,
            'channel': 11,
            'ssids': ssidconfiglist})
        self.assertEqual(len(teststruct.keys()), 5)
        self.assertEqual(len(teststruct.values()), 5)

        self.assertEqual(teststruct['country'], country)
        self.assertEqual(teststruct['ssids'], ssidconfiglist)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
