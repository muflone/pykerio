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

from pykerio.enums import UserStatisticType


class TestCase_UserStatisticType(unittest.TestCase):
    def test_00_UserStatisticAll(self):
        """
        Test UserStatisticType with UserStatisticAll
        """
        value = UserStatisticType.UserStatisticAll
        self.assertEqual(value.dump(), 'UserStatisticAll')
        self.assertEqual(value.name, 'UserStatisticAll')
        self.assertEqual(value.value, 0)

    def test_01_UserStatisticUser(self):
        """
        Test UserStatisticType with UserStatisticUser
        """
        value = UserStatisticType.UserStatisticUser
        self.assertEqual(value.dump(), 'UserStatisticUser')
        self.assertEqual(value.name, 'UserStatisticUser')
        self.assertEqual(value.value, 1)

    def test_02_UserStatisticOther(self):
        """
        Test UserStatisticType with UserStatisticOther
        """
        value = UserStatisticType.UserStatisticOther
        self.assertEqual(value.dump(), 'UserStatisticOther')
        self.assertEqual(value.name, 'UserStatisticOther')
        self.assertEqual(value.value, 2)

    def test_03_UserStatisticGuest(self):
        """
        Test UserStatisticType with UserStatisticGuest
        """
        value = UserStatisticType.UserStatisticGuest
        self.assertEqual(value.dump(), 'UserStatisticGuest')
        self.assertEqual(value.name, 'UserStatisticGuest')
        self.assertEqual(value.value, 3)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test UserStatisticType with FAIL
        """
        value = UserStatisticType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
