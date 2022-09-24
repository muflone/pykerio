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


class TestCase_RestrictionKind(unittest.TestCase):
    def test_00_RestrictionKind_Regex(self):
        """
        Test RestrictionKind with Regex
        """
        value = pykerio.enums.RestrictionKind(name='Regex')
        self.assertEqual(value.dump(), 'Regex')
        self.assertEqual(value.get_name(), 'Regex')
        self.assertEqual(value.get_value(), 0)

    def test_01_RestrictionKind_ByteLength(self):
        """
        Test RestrictionKind with ByteLength
        """
        value = pykerio.enums.RestrictionKind(name='ByteLength')
        self.assertEqual(value.dump(), 'ByteLength')
        self.assertEqual(value.get_name(), 'ByteLength')
        self.assertEqual(value.get_value(), 1)

    def test_02_RestrictionKind_ForbiddenNameList(self):
        """
        Test RestrictionKind with ForbiddenNameList
        """
        value = pykerio.enums.RestrictionKind(name='ForbiddenNameList')
        self.assertEqual(value.dump(), 'ForbiddenNameList')
        self.assertEqual(value.get_name(), 'ForbiddenNameList')
        self.assertEqual(value.get_value(), 2)

    def test_03_RestrictionKind_ForbiddenPrefixList(self):
        """
        Test RestrictionKind with ForbiddenPrefixList
        """
        value = pykerio.enums.RestrictionKind(name='ForbiddenPrefixList')
        self.assertEqual(value.dump(), 'ForbiddenPrefixList')
        self.assertEqual(value.get_name(), 'ForbiddenPrefixList')
        self.assertEqual(value.get_value(), 3)

    def test_04_RestrictionKind_ForbiddenSuffixList(self):
        """
        Test RestrictionKind with ForbiddenSuffixList
        """
        value = pykerio.enums.RestrictionKind(name='ForbiddenSuffixList')
        self.assertEqual(value.dump(), 'ForbiddenSuffixList')
        self.assertEqual(value.get_name(), 'ForbiddenSuffixList')
        self.assertEqual(value.get_value(), 4)

    def test_05_RestrictionKind_ForbiddenCharacterList(self):
        """
        Test RestrictionKind with ForbiddenCharacterList
        """
        value = pykerio.enums.RestrictionKind(name='ForbiddenCharacterList')
        self.assertEqual(value.dump(), 'ForbiddenCharacterList')
        self.assertEqual(value.get_name(), 'ForbiddenCharacterList')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_RestrictionKind_FAIL(self):
        """
        Test RestrictionKind with FAIL
        """
        value = pykerio.enums.RestrictionKind(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
