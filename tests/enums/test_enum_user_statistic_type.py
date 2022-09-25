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


class TestCase_UserStatisticType(unittest.TestCase):
    def test_00_UserStatisticAll(self):
        """
        Test UserStatisticType with UserStatisticAll
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticAll')
        self.assertEqual(value.dump(), 'UserStatisticAll')
        self.assertEqual(value.get_name(), 'UserStatisticAll')
        self.assertEqual(value.get_value(), 0)

    def test_01_UserStatisticUser(self):
        """
        Test UserStatisticType with UserStatisticUser
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticUser')
        self.assertEqual(value.dump(), 'UserStatisticUser')
        self.assertEqual(value.get_name(), 'UserStatisticUser')
        self.assertEqual(value.get_value(), 1)

    def test_02_UserStatisticOther(self):
        """
        Test UserStatisticType with UserStatisticOther
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticOther')
        self.assertEqual(value.dump(), 'UserStatisticOther')
        self.assertEqual(value.get_name(), 'UserStatisticOther')
        self.assertEqual(value.get_value(), 2)

    def test_03_UserStatisticGuest(self):
        """
        Test UserStatisticType with UserStatisticGuest
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticGuest')
        self.assertEqual(value.dump(), 'UserStatisticGuest')
        self.assertEqual(value.get_name(), 'UserStatisticGuest')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test UserStatisticType with FAIL
        """
        value = pykerio.enums.UserStatisticType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
