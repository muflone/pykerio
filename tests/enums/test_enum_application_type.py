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


class TestCase_ApplicationType(unittest.TestCase):
    def test_00_ApplicationType_ApplicationWebFilterCategory(self):
        """
        Test ApplicationType with ApplicationWebFilterCategory
        """
        value = pykerio.enums.ApplicationType(name='ApplicationWebFilterCategory')
        self.assertEqual(value.dump(), 'ApplicationWebFilterCategory')
        self.assertEqual(value.get_name(), 'ApplicationWebFilterCategory')
        self.assertEqual(value.get_value(), 0)

    def test_01_ApplicationType_ApplicationProtocol(self):
        """
        Test ApplicationType with ApplicationProtocol
        """
        value = pykerio.enums.ApplicationType(name='ApplicationProtocol')
        self.assertEqual(value.dump(), 'ApplicationProtocol')
        self.assertEqual(value.get_name(), 'ApplicationProtocol')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_ApplicationType_FAIL(self):
        """
        Test ApplicationType with FAIL
        """
        value = pykerio.enums.ApplicationType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
