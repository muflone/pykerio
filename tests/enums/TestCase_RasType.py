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


class TestCase_RasType(unittest.TestCase):
    def test_00_RasType_PPPoE(self):
        """
        Test RasType with PPPoE
        """
        value = pykerio.enums.RasType(name='PPPoE')
        self.assertEquals(value.dump(), 'PPPoE')
        self.assertEquals(value.get_name(), 'PPPoE')
        self.assertEquals(value.get_value(), 0)

    def test_01_RasType_PPTP(self):
        """
        Test RasType with PPTP
        """
        value = pykerio.enums.RasType(name='PPTP')
        self.assertEquals(value.dump(), 'PPTP')
        self.assertEquals(value.get_name(), 'PPTP')
        self.assertEquals(value.get_value(), 1)

    def test_02_RasType_L2TP(self):
        """
        Test RasType with L2TP
        """
        value = pykerio.enums.RasType(name='L2TP')
        self.assertEquals(value.dump(), 'L2TP')
        self.assertEquals(value.get_name(), 'L2TP')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_RasType_FAIL(self):
        """
        Test RasType with FAIL
        """
        value = pykerio.enums.RasType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
