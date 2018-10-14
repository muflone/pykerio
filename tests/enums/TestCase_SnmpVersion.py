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


class TestCase_SnmpVersion(unittest.TestCase):
    def test_00_SnmpVersion_SnmpV2c(self):
        """
        Test SnmpVersion with SnmpV2c
        """
        value = pykerio.enums.SnmpVersion(name='SnmpV2c')
        self.assertEquals(value.dump(), 'SnmpV2c')
        self.assertEquals(value.get_name(), 'SnmpV2c')
        self.assertEquals(value.get_value(), 0)

    def test_01_SnmpVersion_SnmpV3(self):
        """
        Test SnmpVersion with SnmpV3
        """
        value = pykerio.enums.SnmpVersion(name='SnmpV3')
        self.assertEquals(value.dump(), 'SnmpV3')
        self.assertEquals(value.get_name(), 'SnmpV3')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_SnmpVersion_FAIL(self):
        """
        Test SnmpVersion with FAIL
        """
        value = pykerio.enums.SnmpVersion(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
