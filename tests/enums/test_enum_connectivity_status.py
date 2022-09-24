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


class TestCase_ConnectivityStatus(unittest.TestCase):
    def test_00_ConnectivityStatus_ConnectivityOk(self):
        """
        Test ConnectivityStatus with ConnectivityOk
        """
        value = pykerio.enums.ConnectivityStatus(name='ConnectivityOk')
        self.assertEqual(value.dump(), 'ConnectivityOk')
        self.assertEqual(value.get_name(), 'ConnectivityOk')
        self.assertEqual(value.get_value(), 0)

    def test_01_ConnectivityStatus_ConnectivityChecking(self):
        """
        Test ConnectivityStatus with ConnectivityChecking
        """
        value = pykerio.enums.ConnectivityStatus(name='ConnectivityChecking')
        self.assertEqual(value.dump(), 'ConnectivityChecking')
        self.assertEqual(value.get_name(), 'ConnectivityChecking')
        self.assertEqual(value.get_value(), 1)

    def test_02_ConnectivityStatus_ConnectivityError(self):
        """
        Test ConnectivityStatus with ConnectivityError
        """
        value = pykerio.enums.ConnectivityStatus(name='ConnectivityError')
        self.assertEqual(value.dump(), 'ConnectivityError')
        self.assertEqual(value.get_name(), 'ConnectivityError')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_ConnectivityStatus_FAIL(self):
        """
        Test ConnectivityStatus with FAIL
        """
        value = pykerio.enums.ConnectivityStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
