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


class TestCase_CheckVersionType(unittest.TestCase):
    def test_00_CheckVersionType_CheckVersionConfig(self):
        """
        Test CheckVersionType with CheckVersionConfig
        """
        value = pykerio.enums.CheckVersionType(name='CheckVersionConfig')
        self.assertEqual(value.dump(), 'CheckVersionConfig')
        self.assertEqual(value.get_name(), 'CheckVersionConfig')
        self.assertEqual(value.get_value(), 0)

    def test_01_CheckVersionType_CheckVersionBeta(self):
        """
        Test CheckVersionType with CheckVersionBeta
        """
        value = pykerio.enums.CheckVersionType(name='CheckVersionBeta')
        self.assertEqual(value.dump(), 'CheckVersionBeta')
        self.assertEqual(value.get_name(), 'CheckVersionBeta')
        self.assertEqual(value.get_value(), 1)

    def test_02_CheckVersionType_CheckVersionFinal(self):
        """
        Test CheckVersionType with CheckVersionFinal
        """
        value = pykerio.enums.CheckVersionType(name='CheckVersionFinal')
        self.assertEqual(value.dump(), 'CheckVersionFinal')
        self.assertEqual(value.get_name(), 'CheckVersionFinal')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_CheckVersionType_FAIL(self):
        """
        Test CheckVersionType with FAIL
        """
        value = pykerio.enums.CheckVersionType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)