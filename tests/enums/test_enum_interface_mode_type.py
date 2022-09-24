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


class TestCase_InterfaceModeType(unittest.TestCase):
    def test_00_InterfaceModeType_InterfaceModeManual(self):
        """
        Test InterfaceModeType with InterfaceModeManual
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeManual')
        self.assertEqual(value.dump(), 'InterfaceModeManual')
        self.assertEqual(value.get_name(), 'InterfaceModeManual')
        self.assertEqual(value.get_value(), 0)

    def test_01_InterfaceModeType_InterfaceModeAutomatic(self):
        """
        Test InterfaceModeType with InterfaceModeAutomatic
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeAutomatic')
        self.assertEqual(value.dump(), 'InterfaceModeAutomatic')
        self.assertEqual(value.get_name(), 'InterfaceModeAutomatic')
        self.assertEqual(value.get_value(), 1)

    def test_02_InterfaceModeType_InterfaceModeLinkLocal(self):
        """
        Test InterfaceModeType with InterfaceModeLinkLocal
        """
        value = pykerio.enums.InterfaceModeType(name='InterfaceModeLinkLocal')
        self.assertEqual(value.dump(), 'InterfaceModeLinkLocal')
        self.assertEqual(value.get_name(), 'InterfaceModeLinkLocal')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_InterfaceModeType_FAIL(self):
        """
        Test InterfaceModeType with FAIL
        """
        value = pykerio.enums.InterfaceModeType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
