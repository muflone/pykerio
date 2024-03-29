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


class TestCase_IpAddressList(unittest.TestCase):
    def test_01_IpAddressList(self):
        """
        Test IpAddressList
        """
        testlist = pykerio.lists.IpAddressList()
        self.assertEqual(len(testlist), 0)

        address = '192.168.1.1'
        ipaddress = pykerio.types.IpAddress(address)
        testlist.append(ipaddress)
        self.assertEqual(len(testlist), 1)

        self.assertEqual(testlist[-1], ipaddress)

        testlist.clear()
        self.assertEqual(len(testlist), 0)
