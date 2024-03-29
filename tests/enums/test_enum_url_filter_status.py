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

from pykerio.enums import UrlFilterStatus


class TestCase_UrlFilterStatus(unittest.TestCase):
    def test_00_UrlFilterNotLicensed(self):
        """
        Test UrlFilterStatus with UrlFilterNotLicensed
        """
        value = UrlFilterStatus.UrlFilterNotLicensed
        self.assertEqual(value.dump(), 'UrlFilterNotLicensed')
        self.assertEqual(value.name, 'UrlFilterNotLicensed')
        self.assertEqual(value.value, 0)

    def test_01_UrlFilterNotActivated(self):
        """
        Test UrlFilterStatus with UrlFilterNotActivated
        """
        value = UrlFilterStatus.UrlFilterNotActivated
        self.assertEqual(value.dump(), 'UrlFilterNotActivated')
        self.assertEqual(value.name, 'UrlFilterNotActivated')
        self.assertEqual(value.value, 1)

    def test_02_UrlFilterActivating(self):
        """
        Test UrlFilterStatus with UrlFilterActivating
        """
        value = UrlFilterStatus.UrlFilterActivating
        self.assertEqual(value.dump(), 'UrlFilterActivating')
        self.assertEqual(value.name, 'UrlFilterActivating')
        self.assertEqual(value.value, 2)

    def test_03_UrlFilterActivated(self):
        """
        Test UrlFilterStatus with UrlFilterActivated
        """
        value = UrlFilterStatus.UrlFilterActivated
        self.assertEqual(value.dump(), 'UrlFilterActivated')
        self.assertEqual(value.name, 'UrlFilterActivated')
        self.assertEqual(value.value, 3)
