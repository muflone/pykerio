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
            'band': pykerio.enums.WifiBandType('WifiBandBG'),
            'channels': channels})
        channelslist = pykerio.lists.WifiModeChannelList()
        channelslist.append(channelsconfig)

        teststruct = pykerio.structs.WifiCountryConfig({
            'country': kid,
            'channels': channelslist})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['country'], kid)
        self.assertEquals(teststruct['channels'], channelslist)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
