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

from pykerio.enums import InterfaceStatusType


class TestCase_InterfaceStatusType(unittest.TestCase):
    def test_00_Up(self):
        """
        Test InterfaceStatusType with Up
        """
        value = InterfaceStatusType.Up
        self.assertEqual(value.dump(), 'Up')
        self.assertEqual(value.name, 'Up')
        self.assertEqual(value.value, 0)

    def test_01_Down(self):
        """
        Test InterfaceStatusType with Down
        """
        value = InterfaceStatusType.Down
        self.assertEqual(value.dump(), 'Down')
        self.assertEqual(value.name, 'Down')
        self.assertEqual(value.value, 1)

    def test_02_Connecting(self):
        """
        Test InterfaceStatusType with Connecting
        """
        value = InterfaceStatusType.Connecting
        self.assertEqual(value.dump(), 'Connecting')
        self.assertEqual(value.name, 'Connecting')
        self.assertEqual(value.value, 2)

    def test_03_Disconnecting(self):
        """
        Test InterfaceStatusType with Disconnecting
        """
        value = InterfaceStatusType.Disconnecting
        self.assertEqual(value.dump(), 'Disconnecting')
        self.assertEqual(value.name, 'Disconnecting')
        self.assertEqual(value.value, 3)

    def test_04_CableDisconnected(self):
        """
        Test InterfaceStatusType with CableDisconnected
        """
        value = InterfaceStatusType.CableDisconnected
        self.assertEqual(value.dump(), 'CableDisconnected')
        self.assertEqual(value.name, 'CableDisconnected')
        self.assertEqual(value.value, 4)

    def test_05_Error(self):
        """
        Test InterfaceStatusType with Error
        """
        value = InterfaceStatusType.Error
        self.assertEqual(value.dump(), 'Error')
        self.assertEqual(value.name, 'Error')
        self.assertEqual(value.value, 5)

    def test_06_Backup(self):
        """
        Test InterfaceStatusType with Backup
        """
        value = InterfaceStatusType.Backup
        self.assertEqual(value.dump(), 'Backup')
        self.assertEqual(value.name, 'Backup')
        self.assertEqual(value.value, 6)
