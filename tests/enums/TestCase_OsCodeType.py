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


class TestCase_OsCodeType(unittest.TestCase):
    def test_00_OsCodeType_OsWindows(self):
        """
        Test OsCodeType with OsWindows
        """
        value = pykerio.enums.OsCodeType(name='OsWindows')
        self.assertEquals(value.dump(), 'OsWindows')
        self.assertEquals(value.get_name(), 'OsWindows')
        self.assertEquals(value.get_value(), 0)

    def test_01_OsCodeType_OsLinux(self):
        """
        Test OsCodeType with OsLinux
        """
        value = pykerio.enums.OsCodeType(name='OsLinux')
        self.assertEquals(value.dump(), 'OsLinux')
        self.assertEquals(value.get_name(), 'OsLinux')
        self.assertEquals(value.get_value(), 1)

    def test_02_OsCodeType_OsMacos(self):
        """
        Test OsCodeType with OsMacos
        """
        value = pykerio.enums.OsCodeType(name='OsMacos')
        self.assertEquals(value.dump(), 'OsMacos')
        self.assertEquals(value.get_name(), 'OsMacos')
        self.assertEquals(value.get_value(), 2)

    def test_03_OsCodeType_OsUnknown(self):
        """
        Test OsCodeType with OsUnknown
        """
        value = pykerio.enums.OsCodeType(name='OsUnknown')
        self.assertEquals(value.dump(), 'OsUnknown')
        self.assertEquals(value.get_name(), 'OsUnknown')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_OsCodeType_FAIL(self):
        """
        Test OsCodeType with FAIL
        """
        value = pykerio.enums.OsCodeType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
