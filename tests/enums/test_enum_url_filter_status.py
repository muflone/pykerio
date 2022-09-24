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


class TestCase_UrlFilterStatus(unittest.TestCase):
    def test_00_UrlFilterStatus_UrlFilterNotLicensed(self):
        """
        Test UrlFilterStatus with UrlFilterNotLicensed
        """
        value = pykerio.enums.UrlFilterStatus(name='UrlFilterNotLicensed')
        self.assertEqual(value.dump(), 'UrlFilterNotLicensed')
        self.assertEqual(value.get_name(), 'UrlFilterNotLicensed')
        self.assertEqual(value.get_value(), 0)

    def test_01_UrlFilterStatus_UrlFilterNotActivated(self):
        """
        Test UrlFilterStatus with UrlFilterNotActivated
        """
        value = pykerio.enums.UrlFilterStatus(name='UrlFilterNotActivated')
        self.assertEqual(value.dump(), 'UrlFilterNotActivated')
        self.assertEqual(value.get_name(), 'UrlFilterNotActivated')
        self.assertEqual(value.get_value(), 1)

    def test_02_UrlFilterStatus_UrlFilterActivating(self):
        """
        Test UrlFilterStatus with UrlFilterActivating
        """
        value = pykerio.enums.UrlFilterStatus(name='UrlFilterActivating')
        self.assertEqual(value.dump(), 'UrlFilterActivating')
        self.assertEqual(value.get_name(), 'UrlFilterActivating')
        self.assertEqual(value.get_value(), 2)

    def test_03_UrlFilterStatus_UrlFilterActivated(self):
        """
        Test UrlFilterStatus with UrlFilterActivated
        """
        value = pykerio.enums.UrlFilterStatus(name='UrlFilterActivated')
        self.assertEqual(value.dump(), 'UrlFilterActivated')
        self.assertEqual(value.get_name(), 'UrlFilterActivated')
        self.assertEqual(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_UrlFilterStatus_FAIL(self):
        """
        Test UrlFilterStatus with FAIL
        """
        value = pykerio.enums.UrlFilterStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)