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


class TestCase_Ip6AddressMaskList(unittest.TestCase):
    def test_01_Ip6AddressMaskList(self):
        """
        Test Ip6AddressMaskList
        """
        testlist = pykerio.lists.Ip6AddressMaskList()
        self.assertEqual(len(testlist), 0)

        ip = pykerio.types.Ip6Address('fe80::a0c0:52ff:fe2f:7aad')
        length = 64
        teststruct = pykerio.structs.Ip6AddressMask({'ip': ip,
                                                    'prefixLength': length})
        testlist.append(teststruct)
        self.assertEqual(len(testlist), 1)

        self.assertEqual(testlist[-1], teststruct)

        testlist.clear()
        self.assertEqual(len(testlist), 0)
