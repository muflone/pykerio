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

from pykerio.enums import WifiEncryptionType


class TestCase_WifiEncryptionType(unittest.TestCase):
    def test_00_WifiEncryptionDisabled(self):
        """
        Test WifiEncryptionType with WifiEncryptionDisabled
        """
        value = WifiEncryptionType.WifiEncryptionDisabled
        self.assertEqual(value.dump(), 'WifiEncryptionDisabled')
        self.assertEqual(value.name, 'WifiEncryptionDisabled')
        self.assertEqual(value.value, 0)

    def test_01_WifiEncryptionWpaPsk(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpaPsk
        """
        value = WifiEncryptionType.WifiEncryptionWpaPsk
        self.assertEqual(value.dump(), 'WifiEncryptionWpaPsk')
        self.assertEqual(value.name, 'WifiEncryptionWpaPsk')
        self.assertEqual(value.value, 1)

    def test_02_WifiEncryptionWpaEnt(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpaEnt
        """
        value = WifiEncryptionType.WifiEncryptionWpaEnt
        self.assertEqual(value.dump(), 'WifiEncryptionWpaEnt')
        self.assertEqual(value.name, 'WifiEncryptionWpaEnt')
        self.assertEqual(value.value, 2)

    def test_03_WifiEncryptionWpa2Psk(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpa2Psk
        """
        value = WifiEncryptionType.WifiEncryptionWpa2Psk
        self.assertEqual(value.dump(), 'WifiEncryptionWpa2Psk')
        self.assertEqual(value.name, 'WifiEncryptionWpa2Psk')
        self.assertEqual(value.value, 3)

    def test_04_WifiEncryptionWpa2Ent(self):
        """
        Test WifiEncryptionType with WifiEncryptionWpa2Ent
        """
        value = WifiEncryptionType.WifiEncryptionWpa2Ent
        self.assertEqual(value.dump(), 'WifiEncryptionWpa2Ent')
        self.assertEqual(value.name, 'WifiEncryptionWpa2Ent')
        self.assertEqual(value.value, 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test WifiEncryptionType with FAIL
        """
        value = WifiEncryptionType.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
