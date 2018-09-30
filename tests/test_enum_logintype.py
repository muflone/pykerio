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

import pykerio.enums


class TestCase_LoginType(unittest.TestCase):
    def test_01_LoginType_LoginRegular(self):
        """
        Test LoginType with LoginRegular
        """
        login_type = pykerio.enums.LoginType(value='LoginRegular')
        self.assertEquals(login_type.value, 'LoginRegular')
        self.assertEquals(login_type.dump(), 'LoginRegular')

    def test_02_LoginType_LoginAutomatic(self):
        """
        Test LoginType with LoginAutomatic
        """
        login_type = pykerio.enums.LoginType(value='LoginAutomatic')
        self.assertEquals(login_type.value, 'LoginAutomatic')
        self.assertEquals(login_type.dump(), 'LoginAutomatic')


    def test_03_LoginType_LoginReactivation(self):
        """
        Test LoginType with LoginReactivation
        """
        login_type = pykerio.enums.LoginType(value='LoginReactivation')
        self.assertEquals(login_type.value, 'LoginReactivation')
        self.assertEquals(login_type.dump(), 'LoginReactivation')

    @unittest.expectedFailure
    def test_99_LoginType_FAIL(self):
        """
        Test LoginType with FAIL
        """
        login_type = pykerio.enums.LoginType(value='FAIL')
        self.assertEquals(login_type.value, 'FAIL')
        self.assertEquals(login_type.dump(), 'FAIL')
