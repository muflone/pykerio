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


class TestCase_ByteUnits(unittest.TestCase):
    def test_00_ByteUnits_Bytes(self):
        """
        Test ByteUnits with Bytes
        """
        value = pykerio.enums.ByteUnits(name='Bytes')
        self.assertEquals(value.dump(), 'Bytes')
        self.assertEquals(value.get_name(), 'Bytes')
        self.assertEquals(value.get_value(), 0)

    def test_01_ByteUnits_KiloBytes(self):
        """
        Test ByteUnits with KiloBytes
        """
        value = pykerio.enums.ByteUnits(name='KiloBytes')
        self.assertEquals(value.dump(), 'KiloBytes')
        self.assertEquals(value.get_name(), 'KiloBytes')
        self.assertEquals(value.get_value(), 1)

    def test_02_ByteUnits_MegaBytes(self):
        """
        Test ByteUnits with MegaBytes
        """
        value = pykerio.enums.ByteUnits(name='MegaBytes')
        self.assertEquals(value.dump(), 'MegaBytes')
        self.assertEquals(value.get_name(), 'MegaBytes')
        self.assertEquals(value.get_value(), 2)

    def test_03_ByteUnits_GigaBytes(self):
        """
        Test ByteUnits with GigaBytes
        """
        value = pykerio.enums.ByteUnits(name='GigaBytes')
        self.assertEquals(value.dump(), 'GigaBytes')
        self.assertEquals(value.get_name(), 'GigaBytes')
        self.assertEquals(value.get_value(), 3)

    def test_04_ByteUnits_TeraBytes(self):
        """
        Test ByteUnits with TeraBytes
        """
        value = pykerio.enums.ByteUnits(name='TeraBytes')
        self.assertEquals(value.dump(), 'TeraBytes')
        self.assertEquals(value.get_name(), 'TeraBytes')
        self.assertEquals(value.get_value(), 4)

    def test_05_ByteUnits_PetaBytes(self):
        """
        Test ByteUnits with PetaBytes
        """
        value = pykerio.enums.ByteUnits(name='PetaBytes')
        self.assertEquals(value.dump(), 'PetaBytes')
        self.assertEquals(value.get_name(), 'PetaBytes')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_ByteUnits_FAIL(self):
        """
        Test ByteUnits with FAIL
        """
        value = pykerio.enums.ByteUnits(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
