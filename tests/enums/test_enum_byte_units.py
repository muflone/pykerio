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

from pykerio.enums import ByteUnits


class TestCase_ByteUnits(unittest.TestCase):
    def test_00_Bytes(self):
        """
        Test ByteUnits with Bytes
        """
        value = ByteUnits.Bytes
        self.assertEqual(value.dump(), 'Bytes')
        self.assertEqual(value.name, 'Bytes')
        self.assertEqual(value.value, 0)

    def test_01_KiloBytes(self):
        """
        Test ByteUnits with KiloBytes
        """
        value = ByteUnits.KiloBytes
        self.assertEqual(value.dump(), 'KiloBytes')
        self.assertEqual(value.name, 'KiloBytes')
        self.assertEqual(value.value, 1)

    def test_02_MegaBytes(self):
        """
        Test ByteUnits with MegaBytes
        """
        value = ByteUnits.MegaBytes
        self.assertEqual(value.dump(), 'MegaBytes')
        self.assertEqual(value.name, 'MegaBytes')
        self.assertEqual(value.value, 2)

    def test_03_GigaBytes(self):
        """
        Test ByteUnits with GigaBytes
        """
        value = ByteUnits.GigaBytes
        self.assertEqual(value.dump(), 'GigaBytes')
        self.assertEqual(value.name, 'GigaBytes')
        self.assertEqual(value.value, 3)

    def test_04_TeraBytes(self):
        """
        Test ByteUnits with TeraBytes
        """
        value = ByteUnits.TeraBytes
        self.assertEqual(value.dump(), 'TeraBytes')
        self.assertEqual(value.name, 'TeraBytes')
        self.assertEqual(value.value, 4)

    def test_05_PetaBytes(self):
        """
        Test ByteUnits with PetaBytes
        """
        value = ByteUnits.PetaBytes
        self.assertEqual(value.dump(), 'PetaBytes')
        self.assertEqual(value.name, 'PetaBytes')
        self.assertEqual(value.value, 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ByteUnits with FAIL
        """
        value = ByteUnits.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
