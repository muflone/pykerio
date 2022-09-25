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

from pykerio.enums import UserConditionType


class TestCase_UserConditionType(unittest.TestCase):
    def test_00_AnyUser(self):
        """
        Test UserConditionType with AnyUser
        """
        value = UserConditionType.AnyUser
        self.assertEqual(value.dump(), 'AnyUser')
        self.assertEqual(value.name, 'AnyUser')
        self.assertEqual(value.value, 0)

    def test_01_AuthenticatedUsers(self):
        """
        Test UserConditionType with AuthenticatedUsers
        """
        value = UserConditionType.AuthenticatedUsers
        self.assertEqual(value.dump(), 'AuthenticatedUsers')
        self.assertEqual(value.name, 'AuthenticatedUsers')
        self.assertEqual(value.value, 1)

    def test_02_UnrecognizedUsers(self):
        """
        Test UserConditionType with UnrecognizedUsers
        """
        value = UserConditionType.UnrecognizedUsers
        self.assertEqual(value.dump(), 'UnrecognizedUsers')
        self.assertEqual(value.name, 'UnrecognizedUsers')
        self.assertEqual(value.value, 2)

    def test_03_SelectedUsers(self):
        """
        Test UserConditionType with SelectedUsers
        """
        value = UserConditionType.SelectedUsers
        self.assertEqual(value.dump(), 'SelectedUsers')
        self.assertEqual(value.name, 'SelectedUsers')
        self.assertEqual(value.value, 3)

    def test_04_Nobody(self):
        """
        Test UserConditionType with Nobody
        """
        value = UserConditionType.Nobody
        self.assertEqual(value.dump(), 'Nobody')
        self.assertEqual(value.name, 'Nobody')
        self.assertEqual(value.value, 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test UserConditionType with FAIL
        """
        value = UserConditionType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
