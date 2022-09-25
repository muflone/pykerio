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

from pykerio.enums import DirectoryServiceType


class TestCase_DirectoryServiceType(unittest.TestCase):
    def test_00_WindowsActiveDirectory(self):
        """
        Test DirectoryServiceType with WindowsActiveDirectory
        """
        value = DirectoryServiceType.WindowsActiveDirectory
        self.assertEqual(value.dump(), 'WindowsActiveDirectory')
        self.assertEqual(value.name, 'WindowsActiveDirectory')
        self.assertEqual(value.value, 0)

    def test_01_AppleDirectoryKerberos(self):
        """
        Test DirectoryServiceType with AppleDirectoryKerberos
        """
        value = DirectoryServiceType.AppleDirectoryKerberos
        self.assertEqual(value.dump(), 'AppleDirectoryKerberos')
        self.assertEqual(value.name, 'AppleDirectoryKerberos')
        self.assertEqual(value.value, 1)

    def test_02_AppleDirectoryPassword(self):
        """
        Test DirectoryServiceType with AppleDirectoryPassword
        """
        value = DirectoryServiceType.AppleDirectoryPassword
        self.assertEqual(value.dump(), 'AppleDirectoryPassword')
        self.assertEqual(value.name, 'AppleDirectoryPassword')
        self.assertEqual(value.value, 2)
