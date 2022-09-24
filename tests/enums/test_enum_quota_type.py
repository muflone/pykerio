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


class TestCase_QuotaType(unittest.TestCase):
    def test_00_QuotaType_QuotaBoth(self):
        """
        Test QuotaType with QuotaBoth
        """
        value = pykerio.enums.QuotaType(name='QuotaBoth')
        self.assertEqual(value.dump(), 'QuotaBoth')
        self.assertEqual(value.get_name(), 'QuotaBoth')
        self.assertEqual(value.get_value(), 0)

    def test_01_QuotaType_QuotaDownload(self):
        """
        Test QuotaType with QuotaDownload
        """
        value = pykerio.enums.QuotaType(name='QuotaDownload')
        self.assertEqual(value.dump(), 'QuotaDownload')
        self.assertEqual(value.get_name(), 'QuotaDownload')
        self.assertEqual(value.get_value(), 1)

    def test_02_QuotaType_QuotaUpload(self):
        """
        Test QuotaType with QuotaUpload
        """
        value = pykerio.enums.QuotaType(name='QuotaUpload')
        self.assertEqual(value.dump(), 'QuotaUpload')
        self.assertEqual(value.get_name(), 'QuotaUpload')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_QuotaType_FAIL(self):
        """
        Test QuotaType with FAIL
        """
        value = pykerio.enums.QuotaType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
