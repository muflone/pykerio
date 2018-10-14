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


class TestCase_UserConditionType(unittest.TestCase):
    def test_00_UserConditionType_AnyUser(self):
        """
        Test UserConditionType with AnyUser
        """
        value = pykerio.enums.UserConditionType(name='AnyUser')
        self.assertEquals(value.dump(), 'AnyUser')
        self.assertEquals(value.get_name(), 'AnyUser')
        self.assertEquals(value.get_value(), 0)

    def test_01_UserConditionType_AuthenticatedUsers(self):
        """
        Test UserConditionType with AuthenticatedUsers
        """
        value = pykerio.enums.UserConditionType(name='AuthenticatedUsers')
        self.assertEquals(value.dump(), 'AuthenticatedUsers')
        self.assertEquals(value.get_name(), 'AuthenticatedUsers')
        self.assertEquals(value.get_value(), 1)

    def test_02_UserConditionType_UnrecognizedUsers(self):
        """
        Test UserConditionType with UnrecognizedUsers
        """
        value = pykerio.enums.UserConditionType(name='UnrecognizedUsers')
        self.assertEquals(value.dump(), 'UnrecognizedUsers')
        self.assertEquals(value.get_name(), 'UnrecognizedUsers')
        self.assertEquals(value.get_value(), 2)

    def test_03_UserConditionType_SelectedUsers(self):
        """
        Test UserConditionType with SelectedUsers
        """
        value = pykerio.enums.UserConditionType(name='SelectedUsers')
        self.assertEquals(value.dump(), 'SelectedUsers')
        self.assertEquals(value.get_name(), 'SelectedUsers')
        self.assertEquals(value.get_value(), 3)

    def test_04_UserConditionType_Nobody(self):
        """
        Test UserConditionType with Nobody
        """
        value = pykerio.enums.UserConditionType(name='Nobody')
        self.assertEquals(value.dump(), 'Nobody')
        self.assertEquals(value.get_name(), 'Nobody')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_UserConditionType_FAIL(self):
        """
        Test UserConditionType with FAIL
        """
        value = pykerio.enums.UserConditionType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
