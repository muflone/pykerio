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


class TestCase_ByteUnits(unittest.TestCase):
    def test_00_Bytes(self):
        """
        Test ByteUnits with Bytes
        """
        value = pykerio.enums.ByteUnits(name='Bytes')
        self.assertEqual(value.dump(), 'Bytes')
        self.assertEqual(value.get_name(), 'Bytes')
        self.assertEqual(value.get_value(), 0)

    def test_01_KiloBytes(self):
        """
        Test ByteUnits with KiloBytes
        """
        value = pykerio.enums.ByteUnits(name='KiloBytes')
        self.assertEqual(value.dump(), 'KiloBytes')
        self.assertEqual(value.get_name(), 'KiloBytes')
        self.assertEqual(value.get_value(), 1)

    def test_02_MegaBytes(self):
        """
        Test ByteUnits with MegaBytes
        """
        value = pykerio.enums.ByteUnits(name='MegaBytes')
        self.assertEqual(value.dump(), 'MegaBytes')
        self.assertEqual(value.get_name(), 'MegaBytes')
        self.assertEqual(value.get_value(), 2)

    def test_03_GigaBytes(self):
        """
        Test ByteUnits with GigaBytes
        """
        value = pykerio.enums.ByteUnits(name='GigaBytes')
        self.assertEqual(value.dump(), 'GigaBytes')
        self.assertEqual(value.get_name(), 'GigaBytes')
        self.assertEqual(value.get_value(), 3)

    def test_04_TeraBytes(self):
        """
        Test ByteUnits with TeraBytes
        """
        value = pykerio.enums.ByteUnits(name='TeraBytes')
        self.assertEqual(value.dump(), 'TeraBytes')
        self.assertEqual(value.get_name(), 'TeraBytes')
        self.assertEqual(value.get_value(), 4)

    def test_05_PetaBytes(self):
        """
        Test ByteUnits with PetaBytes
        """
        value = pykerio.enums.ByteUnits(name='PetaBytes')
        self.assertEqual(value.dump(), 'PetaBytes')
        self.assertEqual(value.get_name(), 'PetaBytes')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ByteUnits with FAIL
        """
        value = pykerio.enums.ByteUnits(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
