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


class TestCase_UserFormatType(unittest.TestCase):
    def test_00_UserFormatType_UserFormatFL(self):
        """
        Test UserFormatType with UserFormatFL
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFL')
        self.assertEquals(value.dump(), 'UserFormatFL')
        self.assertEquals(value.get_name(), 'UserFormatFL')
        self.assertEquals(value.get_value(), 0)

    def test_01_UserFormatType_UserFormatFLU(self):
        """
        Test UserFormatType with UserFormatFLU
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFLU')
        self.assertEquals(value.dump(), 'UserFormatFLU')
        self.assertEquals(value.get_name(), 'UserFormatFLU')
        self.assertEquals(value.get_value(), 1)

    def test_02_UserFormatType_UserFormatFLD(self):
        """
        Test UserFormatType with UserFormatFLD
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFLD')
        self.assertEquals(value.dump(), 'UserFormatFLD')
        self.assertEquals(value.get_name(), 'UserFormatFLD')
        self.assertEquals(value.get_value(), 2)

    def test_03_UserFormatType_UserFormatLF(self):
        """
        Test UserFormatType with UserFormatLF
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLF')
        self.assertEquals(value.dump(), 'UserFormatLF')
        self.assertEquals(value.get_name(), 'UserFormatLF')
        self.assertEquals(value.get_value(), 3)

    def test_04_UserFormatType_UserFormatLFU(self):
        """
        Test UserFormatType with UserFormatLFU
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLFU')
        self.assertEquals(value.dump(), 'UserFormatLFU')
        self.assertEquals(value.get_name(), 'UserFormatLFU')
        self.assertEquals(value.get_value(), 4)

    def test_05_UserFormatType_UserFormatLFD(self):
        """
        Test UserFormatType with UserFormatLFD
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLFD')
        self.assertEquals(value.dump(), 'UserFormatLFD')
        self.assertEquals(value.get_name(), 'UserFormatLFD')
        self.assertEquals(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_UserFormatType_FAIL(self):
        """
        Test UserFormatType with FAIL
        """
        value = pykerio.enums.UserFormatType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
