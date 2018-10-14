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


class TestCase_InterfaceStatusType(unittest.TestCase):
    def test_00_InterfaceStatusType_Up(self):
        """
        Test InterfaceStatusType with Up
        """
        value = pykerio.enums.InterfaceStatusType(name='Up')
        self.assertEquals(value.dump(), 'Up')
        self.assertEquals(value.get_name(), 'Up')
        self.assertEquals(value.get_value(), 0)

    def test_01_InterfaceStatusType_Down(self):
        """
        Test InterfaceStatusType with Down
        """
        value = pykerio.enums.InterfaceStatusType(name='Down')
        self.assertEquals(value.dump(), 'Down')
        self.assertEquals(value.get_name(), 'Down')
        self.assertEquals(value.get_value(), 1)

    def test_02_InterfaceStatusType_Connecting(self):
        """
        Test InterfaceStatusType with Connecting
        """
        value = pykerio.enums.InterfaceStatusType(name='Connecting')
        self.assertEquals(value.dump(), 'Connecting')
        self.assertEquals(value.get_name(), 'Connecting')
        self.assertEquals(value.get_value(), 2)

    def test_03_InterfaceStatusType_Disconnecting(self):
        """
        Test InterfaceStatusType with Disconnecting
        """
        value = pykerio.enums.InterfaceStatusType(name='Disconnecting')
        self.assertEquals(value.dump(), 'Disconnecting')
        self.assertEquals(value.get_name(), 'Disconnecting')
        self.assertEquals(value.get_value(), 3)

    def test_04_InterfaceStatusType_CableDisconnected(self):
        """
        Test InterfaceStatusType with CableDisconnected
        """
        value = pykerio.enums.InterfaceStatusType(name='CableDisconnected')
        self.assertEquals(value.dump(), 'CableDisconnected')
        self.assertEquals(value.get_name(), 'CableDisconnected')
        self.assertEquals(value.get_value(), 4)

    def test_05_InterfaceStatusType_Error(self):
        """
        Test InterfaceStatusType with Error
        """
        value = pykerio.enums.InterfaceStatusType(name='Error')
        self.assertEquals(value.dump(), 'Error')
        self.assertEquals(value.get_name(), 'Error')
        self.assertEquals(value.get_value(), 5)

    def test_06_InterfaceStatusType_Backup(self):
        """
        Test InterfaceStatusType with Backup
        """
        value = pykerio.enums.InterfaceStatusType(name='Backup')
        self.assertEquals(value.dump(), 'Backup')
        self.assertEquals(value.get_name(), 'Backup')
        self.assertEquals(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_InterfaceStatusType_FAIL(self):
        """
        Test InterfaceStatusType with FAIL
        """
        value = pykerio.enums.InterfaceStatusType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
