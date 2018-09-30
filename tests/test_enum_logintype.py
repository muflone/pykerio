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
        value = pykerio.enums.LoginType(value='LoginRegular')
        self.assertEquals(value.value, 'LoginRegular')
        self.assertEquals(value.dump(), 'LoginRegular')

    def test_02_LoginType_LoginAutomatic(self):
        """
        Test LoginType with LoginAutomatic
        """
        value = pykerio.enums.LoginType(value='LoginAutomatic')
        self.assertEquals(value.value, 'LoginAutomatic')
        self.assertEquals(value.dump(), 'LoginAutomatic')


    def test_03_LoginType_LoginReactivation(self):
        """
        Test LoginType with LoginReactivation
        """
        value = pykerio.enums.LoginType(value='LoginReactivation')
        self.assertEquals(value.value, 'LoginReactivation')
        self.assertEquals(value.dump(), 'LoginReactivation')

    @unittest.expectedFailure
    def test_99_LoginType_FAIL(self):
        """
        Test LoginType with FAIL
        """
        value = pykerio.enums.LoginType(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
