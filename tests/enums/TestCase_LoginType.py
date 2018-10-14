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


class TestCase_LoginType(unittest.TestCase):
    def test_00_LoginType_LoginRegular(self):
        """
        Test LoginType with LoginRegular
        """
        value = pykerio.enums.LoginType(name='LoginRegular')
        self.assertEquals(value.dump(), 'LoginRegular')
        self.assertEquals(value.get_name(), 'LoginRegular')
        self.assertEquals(value.get_value(), 0)

    def test_01_LoginType_LoginAutomatic(self):
        """
        Test LoginType with LoginAutomatic
        """
        value = pykerio.enums.LoginType(name='LoginAutomatic')
        self.assertEquals(value.dump(), 'LoginAutomatic')
        self.assertEquals(value.get_name(), 'LoginAutomatic')
        self.assertEquals(value.get_value(), 1)

    def test_02_LoginType_LoginReactivation(self):
        """
        Test LoginType with LoginReactivation
        """
        value = pykerio.enums.LoginType(name='LoginReactivation')
        self.assertEquals(value.dump(), 'LoginReactivation')
        self.assertEquals(value.get_name(), 'LoginReactivation')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_LoginType_FAIL(self):
        """
        Test LoginType with FAIL
        """
        value = pykerio.enums.LoginType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
