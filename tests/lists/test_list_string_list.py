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


class TestCase_StringList(unittest.TestCase):
    def test_01_StringList(self):
        """
        Test StringList
        """
        testlist = pykerio.lists.StringList()
        self.assertEqual(len(testlist), 0)

        testlist.append('abc')
        testlist.append('def')

        self.assertEqual(len(testlist), 2)
        self.assertEqual(testlist[-1], 'def')

        testlist.clear()
        self.assertEqual(len(testlist), 0)
