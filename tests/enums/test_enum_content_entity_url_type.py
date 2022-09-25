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

from pykerio.enums import ContentEntityUrlType


class TestCase_ContentEntityUrlType(unittest.TestCase):
    def test_00_ContentEntityUrlWildcard(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlWildcard
        """
        value = ContentEntityUrlType.ContentEntityUrlWildcard
        self.assertEqual(value.dump(), 'ContentEntityUrlWildcard')
        self.assertEqual(value.name, 'ContentEntityUrlWildcard')
        self.assertEqual(value.value, 0)

    def test_01_ContentEntityUrlRegex(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlRegex
        """
        value = ContentEntityUrlType.ContentEntityUrlRegex
        self.assertEqual(value.dump(), 'ContentEntityUrlRegex')
        self.assertEqual(value.name, 'ContentEntityUrlRegex')
        self.assertEqual(value.value, 1)

    def test_02_ContentEntityUrlHostname(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlHostname
        """
        value = ContentEntityUrlType.ContentEntityUrlHostname
        self.assertEqual(value.dump(), 'ContentEntityUrlHostname')
        self.assertEqual(value.name, 'ContentEntityUrlHostname')
        self.assertEqual(value.value, 2)
