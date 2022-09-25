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

from pykerio.enums import InterfaceConditionType


class TestCase_InterfaceConditionType(unittest.TestCase):
    def test_00_InterfaceInternet(self):
        """
        Test InterfaceConditionType with InterfaceInternet
        """
        value = InterfaceConditionType.InterfaceInternet
        self.assertEqual(value.dump(), 'InterfaceInternet')
        self.assertEqual(value.name, 'InterfaceInternet')
        self.assertEqual(value.value, 0)

    def test_01_InterfaceTrusted(self):
        """
        Test InterfaceConditionType with InterfaceTrusted
        """
        value = InterfaceConditionType.InterfaceTrusted
        self.assertEqual(value.dump(), 'InterfaceTrusted')
        self.assertEqual(value.name, 'InterfaceTrusted')
        self.assertEqual(value.value, 1)

    def test_02_InterfaceGuest(self):
        """
        Test InterfaceConditionType with InterfaceGuest
        """
        value = InterfaceConditionType.InterfaceGuest
        self.assertEqual(value.dump(), 'InterfaceGuest')
        self.assertEqual(value.name, 'InterfaceGuest')
        self.assertEqual(value.value, 2)

    def test_03_InterfaceSelected(self):
        """
        Test InterfaceConditionType with InterfaceSelected
        """
        value = InterfaceConditionType.InterfaceSelected
        self.assertEqual(value.dump(), 'InterfaceSelected')
        self.assertEqual(value.name, 'InterfaceSelected')
        self.assertEqual(value.value, 3)
