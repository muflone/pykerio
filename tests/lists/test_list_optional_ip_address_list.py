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


class TestCase_OptionalIpAddressList(unittest.TestCase):
    def test_01_OptionalIpAddressList(self):
        """
        Test OptionalIpAddressList
        """
        testlist = pykerio.lists.OptionalIpAddressList()
        self.assertEqual(len(testlist), 0)

        enabled = True
        value = '127.0.0.1'
        teststruct = pykerio.structs.OptionalIpAddress({'enabled': enabled,
                                                        'value': value})
        testlist.append(teststruct)
        self.assertEqual(len(testlist), 1)

        self.assertEqual(testlist[-1], teststruct)

        testlist.clear()
        self.assertEqual(len(testlist), 0)
