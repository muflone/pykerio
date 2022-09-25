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

from pykerio.enums import InterfaceModeType


class TestCase_InterfaceModeType(unittest.TestCase):
    def test_00_InterfaceModeManual(self):
        """
        Test InterfaceModeType with InterfaceModeManual
        """
        value = InterfaceModeType.InterfaceModeManual
        self.assertEqual(value.dump(), 'InterfaceModeManual')
        self.assertEqual(value.name, 'InterfaceModeManual')
        self.assertEqual(value.value, 0)

    def test_01_InterfaceModeAutomatic(self):
        """
        Test InterfaceModeType with InterfaceModeAutomatic
        """
        value = InterfaceModeType.InterfaceModeAutomatic
        self.assertEqual(value.dump(), 'InterfaceModeAutomatic')
        self.assertEqual(value.name, 'InterfaceModeAutomatic')
        self.assertEqual(value.value, 1)

    def test_02_InterfaceModeLinkLocal(self):
        """
        Test InterfaceModeType with InterfaceModeLinkLocal
        """
        value = InterfaceModeType.InterfaceModeLinkLocal
        self.assertEqual(value.dump(), 'InterfaceModeLinkLocal')
        self.assertEqual(value.name, 'InterfaceModeLinkLocal')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test InterfaceModeType with FAIL
        """
        value = InterfaceModeType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
