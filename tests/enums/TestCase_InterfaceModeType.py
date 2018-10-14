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


class TestCase_InterfaceModeType(unittest.TestCase):
    def test_00_InterfaceModeType_InterfaceModeManual(self):
        """
        Test InterfaceModeType with InterfaceModeManual
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeManual')
        self.assertEquals(value.dump(), 'InterfaceModeManual')
        self.assertEquals(value.get_name(), 'InterfaceModeManual')
        self.assertEquals(value.get_value(), 0)

    def test_01_InterfaceModeType_InterfaceModeAutomatic(self):
        """
        Test InterfaceModeType with InterfaceModeAutomatic
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeAutomatic')
        self.assertEquals(value.dump(), 'InterfaceModeAutomatic')
        self.assertEquals(value.get_name(), 'InterfaceModeAutomatic')
        self.assertEquals(value.get_value(), 1)

    def test_02_InterfaceModeType_InterfaceModeLinkLocal(self):
        """
        Test InterfaceModeType with InterfaceModeLinkLocal
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeLinkLocal')
        self.assertEquals(value.dump(), 'InterfaceModeLinkLocal')
        self.assertEquals(value.get_name(), 'InterfaceModeLinkLocal')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_InterfaceModeType_FAIL(self):
        """
        Test InterfaceModeType with FAIL
        """
        value = pykerio.enums.InterfaceModeType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
