##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio


class TestCase_QuotaType(unittest.TestCase):
    def test_00_QuotaType_QuotaBoth(self):
        """
        Test QuotaType with QuotaBoth
        """
        value = pykerio.enums.QuotaType(name='QuotaBoth')
        self.assertEquals(value.dump(), 'QuotaBoth')
        self.assertEquals(value.get_name(), 'QuotaBoth')
        self.assertEquals(value.get_value(), 0)

    def test_01_QuotaType_QuotaDownload(self):
        """
        Test QuotaType with QuotaDownload
        """
        value = pykerio.enums.QuotaType(name='QuotaDownload')
        self.assertEquals(value.dump(), 'QuotaDownload')
        self.assertEquals(value.get_name(), 'QuotaDownload')
        self.assertEquals(value.get_value(), 1)

    def test_02_QuotaType_QuotaUpload(self):
        """
        Test QuotaType with QuotaUpload
        """
        value = pykerio.enums.QuotaType(name='QuotaUpload')
        self.assertEquals(value.dump(), 'QuotaUpload')
        self.assertEquals(value.get_name(), 'QuotaUpload')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_QuotaType_FAIL(self):
        """
        Test QuotaType with FAIL
        """
        value = pykerio.enums.QuotaType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
