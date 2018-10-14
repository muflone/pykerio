##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio


class TestCase_UserStatisticType(unittest.TestCase):
    def test_00_UserStatisticType_UserStatisticAll(self):
        """
        Test UserStatisticType with UserStatisticAll
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticAll')
        self.assertEquals(value.dump(), 'UserStatisticAll')
        self.assertEquals(value.get_name(), 'UserStatisticAll')
        self.assertEquals(value.get_value(), 0)

    def test_01_UserStatisticType_UserStatisticUser(self):
        """
        Test UserStatisticType with UserStatisticUser
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticUser')
        self.assertEquals(value.dump(), 'UserStatisticUser')
        self.assertEquals(value.get_name(), 'UserStatisticUser')
        self.assertEquals(value.get_value(), 1)

    def test_02_UserStatisticType_UserStatisticOther(self):
        """
        Test UserStatisticType with UserStatisticOther
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticOther')
        self.assertEquals(value.dump(), 'UserStatisticOther')
        self.assertEquals(value.get_name(), 'UserStatisticOther')
        self.assertEquals(value.get_value(), 2)

    def test_03_UserStatisticType_UserStatisticGuest(self):
        """
        Test UserStatisticType with UserStatisticGuest
        """
        value = pykerio.enums.UserStatisticType(name='UserStatisticGuest')
        self.assertEquals(value.dump(), 'UserStatisticGuest')
        self.assertEquals(value.get_name(), 'UserStatisticGuest')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_UserStatisticType_FAIL(self):
        """
        Test UserStatisticType with FAIL
        """
        value = pykerio.enums.UserStatisticType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
