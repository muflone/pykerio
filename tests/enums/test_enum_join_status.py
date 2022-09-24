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


class TestCase_JoinStatus(unittest.TestCase):
    def test_00_JoinStatus_JoinStatusConnected(self):
        """
        Test JoinStatus with JoinStatusConnected
        """
        value = pykerio.enums.JoinStatus(name='JoinStatusConnected')
        self.assertEqual(value.dump(), 'JoinStatusConnected')
        self.assertEqual(value.get_name(), 'JoinStatusConnected')
        self.assertEqual(value.get_value(), 0)

    def test_01_JoinStatus_JoinStatusDisconnected(self):
        """
        Test JoinStatus with JoinStatusDisconnected
        """
        value = pykerio.enums.JoinStatus(name='JoinStatusDisconnected')
        self.assertEqual(value.dump(), 'JoinStatusDisconnected')
        self.assertEqual(value.get_name(), 'JoinStatusDisconnected')
        self.assertEqual(value.get_value(), 1)

    def test_02_JoinStatus_JoinStatusError(self):
        """
        Test JoinStatus with JoinStatusError
        """
        value = pykerio.enums.JoinStatus(name='JoinStatusError')
        self.assertEqual(value.dump(), 'JoinStatusError')
        self.assertEqual(value.get_name(), 'JoinStatusError')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_JoinStatus_FAIL(self):
        """
        Test JoinStatus with FAIL
        """
        value = pykerio.enums.JoinStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)