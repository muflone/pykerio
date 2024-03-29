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

from pykerio.enums import MppeType


class TestCase_MppeType(unittest.TestCase):
    def test_00_MppeDisabled(self):
        """
        Test MppeType with MppeDisabled
        """
        value = MppeType.MppeDisabled
        self.assertEqual(value.dump(), 'MppeDisabled')
        self.assertEqual(value.name, 'MppeDisabled')
        self.assertEqual(value.value, 0)

    def test_01_MppeEnabled(self):
        """
        Test MppeType with MppeEnabled
        """
        value = MppeType.MppeEnabled
        self.assertEqual(value.dump(), 'MppeEnabled')
        self.assertEqual(value.name, 'MppeEnabled')
        self.assertEqual(value.value, 1)

    def test_02_Mppe128Enabled(self):
        """
        Test MppeType with Mppe128Enabled
        """
        value = MppeType.Mppe128Enabled
        self.assertEqual(value.dump(), 'Mppe128Enabled')
        self.assertEqual(value.name, 'Mppe128Enabled')
        self.assertEqual(value.value, 2)
