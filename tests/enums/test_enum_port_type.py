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


class TestCase_PortType(unittest.TestCase):
    def test_00_PortType_PortEthernet(self):
        """
        Test PortType with PortEthernet
        """
        value = pykerio.enums.PortType(name='PortEthernet')
        self.assertEqual(value.dump(), 'PortEthernet')
        self.assertEqual(value.get_name(), 'PortEthernet')
        self.assertEqual(value.get_value(), 0)

    def test_01_PortType_PortWifi(self):
        """
        Test PortType with PortWifi
        """
        value = pykerio.enums.PortType(name='PortWifi')
        self.assertEqual(value.dump(), 'PortWifi')
        self.assertEqual(value.get_name(), 'PortWifi')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_PortType_FAIL(self):
        """
        Test PortType with FAIL
        """
        value = pykerio.enums.PortType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
