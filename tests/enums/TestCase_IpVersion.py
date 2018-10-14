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


class TestCase_IpVersion(unittest.TestCase):
    def test_00_IpVersion_IpVersion4(self):
        """
        Test IpVersion with IpVersion4
        """
        value = pykerio.enums.IpVersion(name='IpVersion4')
        self.assertEquals(value.dump(), 'IpVersion4')
        self.assertEquals(value.get_name(), 'IpVersion4')
        self.assertEquals(value.get_value(), 0)

    def test_01_IpVersion_IpVersion6(self):
        """
        Test IpVersion with IpVersion6
        """
        value = pykerio.enums.IpVersion(name='IpVersion6')
        self.assertEquals(value.dump(), 'IpVersion6')
        self.assertEquals(value.get_name(), 'IpVersion6')
        self.assertEquals(value.get_value(), 1)

    def test_02_IpVersion_IpVersionAny(self):
        """
        Test IpVersion with IpVersionAny
        """
        value = pykerio.enums.IpVersion(name='IpVersionAny')
        self.assertEquals(value.dump(), 'IpVersionAny')
        self.assertEquals(value.get_name(), 'IpVersionAny')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_IpVersion_FAIL(self):
        """
        Test IpVersion with FAIL
        """
        value = pykerio.enums.IpVersion(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
