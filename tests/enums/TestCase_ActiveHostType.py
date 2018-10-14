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


class TestCase_ActiveHostType(unittest.TestCase):
    def test_00_ActiveHostType_ActiveHostFirevall(self):
        """
        Test ActiveHostType with ActiveHostFirevall
        """
        value = pykerio.enums.ActiveHostType(name='ActiveHostFirevall')
        self.assertEquals(value.dump(), 'ActiveHostFirevall')
        self.assertEquals(value.get_name(), 'ActiveHostFirevall')
        self.assertEquals(value.get_value(), 0)

    def test_01_ActiveHostType_ActiveHostVpnClient(self):
        """
        Test ActiveHostType with ActiveHostVpnClient
        """
        value = pykerio.enums.ActiveHostType(name='ActiveHostVpnClient')
        self.assertEquals(value.dump(), 'ActiveHostVpnClient')
        self.assertEquals(value.get_name(), 'ActiveHostVpnClient')
        self.assertEquals(value.get_value(), 1)

    def test_02_ActiveHostType_ActiveHostHost(self):
        """
        Test ActiveHostType with ActiveHostHost
        """
        value = pykerio.enums.ActiveHostType(name='ActiveHostHost')
        self.assertEquals(value.dump(), 'ActiveHostHost')
        self.assertEquals(value.get_name(), 'ActiveHostHost')
        self.assertEquals(value.get_value(), 2)

    def test_03_ActiveHostType_ActiveHostGuest(self):
        """
        Test ActiveHostType with ActiveHostGuest
        """
        value = pykerio.enums.ActiveHostType(name='ActiveHostGuest')
        self.assertEquals(value.dump(), 'ActiveHostGuest')
        self.assertEquals(value.get_name(), 'ActiveHostGuest')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_ActiveHostType_FAIL(self):
        """
        Test ActiveHostType with FAIL
        """
        value = pykerio.enums.ActiveHostType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
