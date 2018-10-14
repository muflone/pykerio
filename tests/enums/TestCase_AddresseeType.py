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


class TestCase_AddresseeType(unittest.TestCase):
    def test_00_AddresseeType_AddresseeEmail(self):
        """
        Test AddresseeType with AddresseeEmail
        """
        value = pykerio.enums.AddresseeType(name='AddresseeEmail')
        self.assertEquals(value.dump(), 'AddresseeEmail')
        self.assertEquals(value.get_name(), 'AddresseeEmail')
        self.assertEquals(value.get_value(), 0)

    def test_01_AddresseeType_AddresseeUser(self):
        """
        Test AddresseeType with AddresseeUser
        """
        value = pykerio.enums.AddresseeType(name='AddresseeUser')
        self.assertEquals(value.dump(), 'AddresseeUser')
        self.assertEquals(value.get_name(), 'AddresseeUser')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_AddresseeType_FAIL(self):
        """
        Test AddresseeType with FAIL
        """
        value = pykerio.enums.AddresseeType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
