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


class TestCase_InterfaceConditionType(unittest.TestCase):
    def test_00_InterfaceConditionType_InterfaceInternet(self):
        """
        Test InterfaceConditionType with InterfaceInternet
        """
        value = pykerio.enums.InterfaceConditionType(name='InterfaceInternet')
        self.assertEqual(value.dump(), 'InterfaceInternet')
        self.assertEqual(value.get_name(), 'InterfaceInternet')
        self.assertEqual(value.get_value(), 0)

    def test_01_InterfaceConditionType_InterfaceTrusted(self):
        """
        Test InterfaceConditionType with InterfaceTrusted
        """
        value = pykerio.enums.InterfaceConditionType(name='InterfaceTrusted')
        self.assertEqual(value.dump(), 'InterfaceTrusted')
        self.assertEqual(value.get_name(), 'InterfaceTrusted')
        self.assertEqual(value.get_value(), 1)

    def test_02_InterfaceConditionType_InterfaceGuest(self):
        """
        Test InterfaceConditionType with InterfaceGuest
        """
        value = pykerio.enums.InterfaceConditionType(name='InterfaceGuest')
        self.assertEqual(value.dump(), 'InterfaceGuest')
        self.assertEqual(value.get_name(), 'InterfaceGuest')
        self.assertEqual(value.get_value(), 2)

    def test_03_InterfaceConditionType_InterfaceSelected(self):
        """
        Test InterfaceConditionType with InterfaceSelected
        """
        value = pykerio.enums.InterfaceConditionType(name='InterfaceSelected')
        self.assertEqual(value.dump(), 'InterfaceSelected')
        self.assertEqual(value.get_name(), 'InterfaceSelected')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_InterfaceConditionType_FAIL(self):
        """
        Test InterfaceConditionType with FAIL
        """
        value = pykerio.enums.InterfaceConditionType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
