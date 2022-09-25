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

from pykerio.enums import UrlEntryType


class TestCase_UrlEntryType(unittest.TestCase):
    def test_00_Url(self):
        """
        Test UrlEntryType with Url
        """
        value = UrlEntryType.Url
        self.assertEqual(value.dump(), 'Url')
        self.assertEqual(value.name, 'Url')
        self.assertEqual(value.value, 0)

    def test_01_UrlChildGroup(self):
        """
        Test UrlEntryType with UrlChildGroup
        """
        value = UrlEntryType.UrlChildGroup
        self.assertEqual(value.dump(), 'UrlChildGroup')
        self.assertEqual(value.name, 'UrlChildGroup')
        self.assertEqual(value.value, 1)
