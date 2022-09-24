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


class TestCase_WifiEncryptionType(unittest.TestCase):
    def test_00_WifiEncryptionType_WifiEncryptionDisabled(self):
        """
        Test WifiEncryptionType with WifiEncryptionDisabled
        """
        value = pykerio.enums.WifiEncryptionType(name='WifiEncryptionDisabled')
        self.assertEqual(value.dump(), 'WifiEncryptionDisabled')
        self.assertEqual(value.get_name(), 'WifiEncryptionDisabled')
        self.assertEqual(value.get_value(), 0)

    def test_01_WifiEncryptionType_WifiEncryptionWpaPsk(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpaPsk
        """
        value = pykerio.enums.WifiEncryptionType(name='WifiEncryptionWpaPsk')
        self.assertEqual(value.dump(), 'WifiEncryptionWpaPsk')
        self.assertEqual(value.get_name(), 'WifiEncryptionWpaPsk')
        self.assertEqual(value.get_value(), 1)

    def test_02_WifiEncryptionType_WifiEncryptionWpaEnt(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpaEnt
        """
        value = pykerio.enums.WifiEncryptionType(name='WifiEncryptionWpaEnt')
        self.assertEqual(value.dump(), 'WifiEncryptionWpaEnt')
        self.assertEqual(value.get_name(), 'WifiEncryptionWpaEnt')
        self.assertEqual(value.get_value(), 2)

    def test_03_WifiEncryptionType_WifiEncryptionWpa2Psk(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpa2Psk
        """
        value = pykerio.enums.WifiEncryptionType(name='WifiEncryptionWpa2Psk')
        self.assertEqual(value.dump(), 'WifiEncryptionWpa2Psk')
        self.assertEqual(value.get_name(), 'WifiEncryptionWpa2Psk')
        self.assertEqual(value.get_value(), 3)

    def test_04_WifiEncryptionType_WifiEncryptionWpa2Ent(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpa2Ent
        """
        value = pykerio.enums.WifiEncryptionType(name='WifiEncryptionWpa2Ent')
        self.assertEqual(value.dump(), 'WifiEncryptionWpa2Ent')
        self.assertEqual(value.get_name(), 'WifiEncryptionWpa2Ent')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_WifiEncryptionType_FAIL(self):
        """
        Test WifiEncryptionType with FAIL
        """
        value = pykerio.enums.WifiEncryptionType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
