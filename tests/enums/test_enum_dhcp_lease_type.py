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


class TestCase_DhcpLeaseType(unittest.TestCase):
    def test_00_DhcpTypeReservation(self):
        """
        Test DhcpLeaseType with DhcpTypeReservation
        """
        value = pykerio.enums.DhcpLeaseType(name='DhcpTypeReservation')
        self.assertEqual(value.dump(), 'DhcpTypeReservation')
        self.assertEqual(value.get_name(), 'DhcpTypeReservation')
        self.assertEqual(value.get_value(), 0)

    def test_01_DhcpTypeLease(self):
        """
        Test DhcpLeaseType with DhcpTypeLease
        """
        value = pykerio.enums.DhcpLeaseType(name='DhcpTypeLease')
        self.assertEqual(value.dump(), 'DhcpTypeLease')
        self.assertEqual(value.get_name(), 'DhcpTypeLease')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test DhcpLeaseType with FAIL
        """
        value = pykerio.enums.DhcpLeaseType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
