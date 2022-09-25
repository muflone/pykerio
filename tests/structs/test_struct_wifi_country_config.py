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
from pykerio.enums import WifiBandType


class TestCase_WifiCountryConfig(unittest.TestCase):
    def test_01_WifiCountryConfig(self):
        """
        Test WifiCountryConfig
        """
        kid = pykerio.types.KId('IT')

        channels = pykerio.lists.WifiChannelList()
        name = 'Channel 11'
        value = 11
        channel = pykerio.structs.WifiChannelInfo({'name': name,
                                                   'name80211n': name,
                                                   'value': value})
        channels.append(channel)

        channelsconfig = pykerio.structs.WifiModeChannelConfig({
            'band': WifiBandType.WifiBandBG,
            'channels': channels})
        channelslist = pykerio.lists.WifiModeChannelList()
        channelslist.append(channelsconfig)

        teststruct = pykerio.structs.WifiCountryConfig({
            'country': kid,
            'channels': channelslist})
        self.assertEqual(len(teststruct.keys()), 2)
        self.assertEqual(len(teststruct.values()), 2)

        self.assertEqual(teststruct['country'], kid)
        self.assertEqual(teststruct['channels'], channelslist)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
