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


class TestCase_InterfaceGroupType(unittest.TestCase):
    def test_00_InterfaceGroupType_Other(self):
        """
        Test InterfaceGroupType with Other
        """
        value = pykerio.enums.InterfaceGroupType(name='Other')
        self.assertEquals(value.dump(), 'Other')
        self.assertEquals(value.get_name(), 'Other')
        self.assertEquals(value.get_value(), 0)

    def test_01_InterfaceGroupType_Guest(self):
        """
        Test InterfaceGroupType with Guest
        """
        value = pykerio.enums.InterfaceGroupType(name='Guest')
        self.assertEquals(value.dump(), 'Guest')
        self.assertEquals(value.get_name(), 'Guest')
        self.assertEquals(value.get_value(), 1)

    def test_02_InterfaceGroupType_Vpn(self):
        """
        Test InterfaceGroupType with Vpn
        """
        value = pykerio.enums.InterfaceGroupType(name='Vpn')
        self.assertEquals(value.dump(), 'Vpn')
        self.assertEquals(value.get_name(), 'Vpn')
        self.assertEquals(value.get_value(), 2)

    def test_03_InterfaceGroupType_Trusted(self):
        """
        Test InterfaceGroupType with Trusted
        """
        value = pykerio.enums.InterfaceGroupType(name='Trusted')
        self.assertEquals(value.dump(), 'Trusted')
        self.assertEquals(value.get_name(), 'Trusted')
        self.assertEquals(value.get_value(), 3)

    def test_04_InterfaceGroupType_Internet(self):
        """
        Test InterfaceGroupType with Internet
        """
        value = pykerio.enums.InterfaceGroupType(name='Internet')
        self.assertEquals(value.dump(), 'Internet')
        self.assertEquals(value.get_name(), 'Internet')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_InterfaceGroupType_FAIL(self):
        """
        Test InterfaceGroupType with FAIL
        """
        value = pykerio.enums.InterfaceGroupType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
