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


class TestCase_ServerOs(unittest.TestCase):
    def test_00_ServerOs_Windows(self):
        """
        Test ServerOs with Windows
        """
        value = pykerio.enums.ServerOs(name='Windows')
        self.assertEqual(value.dump(), 'Windows')
        self.assertEqual(value.get_name(), 'Windows')
        self.assertEqual(value.get_value(), 0)

    def test_01_ServerOs_Linux(self):
        """
        Test ServerOs with Linux
        """
        value = pykerio.enums.ServerOs(name='Linux')
        self.assertEqual(value.dump(), 'Linux')
        self.assertEqual(value.get_name(), 'Linux')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_ServerOs_FAIL(self):
        """
        Test ServerOs with FAIL
        """
        value = pykerio.enums.ServerOs(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
