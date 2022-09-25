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

from pykerio.enums import ConnectivityStatus


class TestCase_ConnectivityStatus(unittest.TestCase):
    def test_00_ConnectivityOk(self):
        """
        Test ConnectivityStatus with ConnectivityOk
        """
        value = ConnectivityStatus.ConnectivityOk
        self.assertEqual(value.dump(), 'ConnectivityOk')
        self.assertEqual(value.name, 'ConnectivityOk')
        self.assertEqual(value.value, 0)

    def test_01_ConnectivityChecking(self):
        """
        Test ConnectivityStatus with ConnectivityChecking
        """
        value = ConnectivityStatus.ConnectivityChecking
        self.assertEqual(value.dump(), 'ConnectivityChecking')
        self.assertEqual(value.name, 'ConnectivityChecking')
        self.assertEqual(value.value, 1)

    def test_02_ConnectivityError(self):
        """
        Test ConnectivityStatus with ConnectivityError
        """
        value = ConnectivityStatus.ConnectivityError
        self.assertEqual(value.dump(), 'ConnectivityError')
        self.assertEqual(value.name, 'ConnectivityError')
        self.assertEqual(value.value, 2)
