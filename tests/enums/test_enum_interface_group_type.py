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


class TestCase_InterfaceGroupType(unittest.TestCase):
    def test_00_Other(self):
        """
        Test InterfaceGroupType with Other
        """
        value = pykerio.enums.InterfaceGroupType(name='Other')
        self.assertEqual(value.dump(), 'Other')
        self.assertEqual(value.get_name(), 'Other')
        self.assertEqual(value.get_value(), 0)

    def test_01_Guest(self):
        """
        Test InterfaceGroupType with Guest
        """
        value = pykerio.enums.InterfaceGroupType(name='Guest')
        self.assertEqual(value.dump(), 'Guest')
        self.assertEqual(value.get_name(), 'Guest')
        self.assertEqual(value.get_value(), 1)

    def test_02_Vpn(self):
        """
        Test InterfaceGroupType with Vpn
        """
        value = pykerio.enums.InterfaceGroupType(name='Vpn')
        self.assertEqual(value.dump(), 'Vpn')
        self.assertEqual(value.get_name(), 'Vpn')
        self.assertEqual(value.get_value(), 2)

    def test_03_Trusted(self):
        """
        Test InterfaceGroupType with Trusted
        """
        value = pykerio.enums.InterfaceGroupType(name='Trusted')
        self.assertEqual(value.dump(), 'Trusted')
        self.assertEqual(value.get_name(), 'Trusted')
        self.assertEqual(value.get_value(), 3)

    def test_04_Internet(self):
        """
        Test InterfaceGroupType with Internet
        """
        value = pykerio.enums.InterfaceGroupType(name='Internet')
        self.assertEqual(value.dump(), 'Internet')
        self.assertEqual(value.get_name(), 'Internet')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test InterfaceGroupType with FAIL
        """
        value = pykerio.enums.InterfaceGroupType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
