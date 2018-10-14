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


class TestCase_SearchStatus(unittest.TestCase):
    def test_00_SearchStatus_ResultFound(self):
        """
        Test SearchStatus with ResultFound
        """
        value = pykerio.enums.SearchStatus(name='ResultFound')
        self.assertEquals(value.dump(), 'ResultFound')
        self.assertEquals(value.get_name(), 'ResultFound')
        self.assertEquals(value.get_value(), 0)

    def test_01_SearchStatus_Searching(self):
        """
        Test SearchStatus with Searching
        """
        value = pykerio.enums.SearchStatus(name='Searching')
        self.assertEquals(value.dump(), 'Searching')
        self.assertEquals(value.get_name(), 'Searching')
        self.assertEquals(value.get_value(), 1)

    def test_02_SearchStatus_Cancelled(self):
        """
        Test SearchStatus with Cancelled
        """
        value = pykerio.enums.SearchStatus(name='Cancelled')
        self.assertEquals(value.dump(), 'Cancelled')
        self.assertEquals(value.get_name(), 'Cancelled')
        self.assertEquals(value.get_value(), 2)

    def test_03_SearchStatus_ResultNotFound(self):
        """
        Test SearchStatus with ResultNotFound
        """
        value = pykerio.enums.SearchStatus(name='ResultNotFound')
        self.assertEquals(value.dump(), 'ResultNotFound')
        self.assertEquals(value.get_name(), 'ResultNotFound')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_SearchStatus_FAIL(self):
        """
        Test SearchStatus with FAIL
        """
        value = pykerio.enums.SearchStatus(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
