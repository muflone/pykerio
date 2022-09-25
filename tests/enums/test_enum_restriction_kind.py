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

from pykerio.enums import RestrictionKind


class TestCase_RestrictionKind(unittest.TestCase):
    def test_00_Regex(self):
        """
        Test RestrictionKind with Regex
        """
        value = RestrictionKind.Regex
        self.assertEqual(value.dump(), 'Regex')
        self.assertEqual(value.name, 'Regex')
        self.assertEqual(value.value, 0)

    def test_01_ByteLength(self):
        """
        Test RestrictionKind with ByteLength
        """
        value = RestrictionKind.ByteLength
        self.assertEqual(value.dump(), 'ByteLength')
        self.assertEqual(value.name, 'ByteLength')
        self.assertEqual(value.value, 1)

    def test_02_ForbiddenNameList(self):
        """
        Test RestrictionKind with ForbiddenNameList
        """
        value = RestrictionKind.ForbiddenNameList
        self.assertEqual(value.dump(), 'ForbiddenNameList')
        self.assertEqual(value.name, 'ForbiddenNameList')
        self.assertEqual(value.value, 2)

    def test_03_ForbiddenPrefixList(self):
        """
        Test RestrictionKind with ForbiddenPrefixList
        """
        value = RestrictionKind.ForbiddenPrefixList
        self.assertEqual(value.dump(), 'ForbiddenPrefixList')
        self.assertEqual(value.name, 'ForbiddenPrefixList')
        self.assertEqual(value.value, 3)

    def test_04_ForbiddenSuffixList(self):
        """
        Test RestrictionKind with ForbiddenSuffixList
        """
        value = RestrictionKind.ForbiddenSuffixList
        self.assertEqual(value.dump(), 'ForbiddenSuffixList')
        self.assertEqual(value.name, 'ForbiddenSuffixList')
        self.assertEqual(value.value, 4)

    def test_05_ForbiddenCharacterList(self):
        """
        Test RestrictionKind with ForbiddenCharacterList
        """
        value = RestrictionKind.ForbiddenCharacterList
        self.assertEqual(value.dump(), 'ForbiddenCharacterList')
        self.assertEqual(value.name, 'ForbiddenCharacterList')
        self.assertEqual(value.value, 5)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test RestrictionKind with FAIL
        """
        value = RestrictionKind.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
