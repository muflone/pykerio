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


class TestCase_MppeType(unittest.TestCase):
    def test_00_MppeDisabled(self):
        """
        Test MppeType with MppeDisabled
        """
        value = pykerio.enums.MppeType(name='MppeDisabled')
        self.assertEqual(value.dump(), 'MppeDisabled')
        self.assertEqual(value.get_name(), 'MppeDisabled')
        self.assertEqual(value.get_value(), 0)

    def test_01_MppeEnabled(self):
        """
        Test MppeType with MppeEnabled
        """
        value = pykerio.enums.MppeType(name='MppeEnabled')
        self.assertEqual(value.dump(), 'MppeEnabled')
        self.assertEqual(value.get_name(), 'MppeEnabled')
        self.assertEqual(value.get_value(), 1)

    def test_02_Mppe128Enabled(self):
        """
        Test MppeType with Mppe128Enabled
        """
        value = pykerio.enums.MppeType(name='Mppe128Enabled')
        self.assertEqual(value.dump(), 'Mppe128Enabled')
        self.assertEqual(value.get_name(), 'Mppe128Enabled')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test MppeType with FAIL
        """
        value = pykerio.enums.MppeType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
