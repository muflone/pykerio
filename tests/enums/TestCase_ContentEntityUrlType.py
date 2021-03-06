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


class TestCase_ContentEntityUrlType(unittest.TestCase):
    def test_00_ContentEntityUrlType_ContentEntityUrlWildcard(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlWildcard
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlWildcard')
        self.assertEquals(value.dump(), 'ContentEntityUrlWildcard')
        self.assertEquals(value.get_name(), 'ContentEntityUrlWildcard')
        self.assertEquals(value.get_value(), 0)

    def test_01_ContentEntityUrlType_ContentEntityUrlRegex(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlRegex
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlRegex')
        self.assertEquals(value.dump(), 'ContentEntityUrlRegex')
        self.assertEquals(value.get_name(), 'ContentEntityUrlRegex')
        self.assertEquals(value.get_value(), 1)

    def test_02_ContentEntityUrlType_ContentEntityUrlHostname(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlHostname
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlHostname')
        self.assertEquals(value.dump(), 'ContentEntityUrlHostname')
        self.assertEquals(value.get_name(), 'ContentEntityUrlHostname')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_ContentEntityUrlType_FAIL(self):
        """
        Test ContentEntityUrlType with FAIL
        """
        value = pykerio.enums.ContentEntityUrlType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
