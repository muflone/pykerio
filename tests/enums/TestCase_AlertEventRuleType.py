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


class TestCase_AlertEventRuleType(unittest.TestCase):
    def test_00_AlertEventRuleType_AlertTraffic(self):
        """
        Test AlertEventRuleType with AlertTraffic
        """
        value = pykerio.enums.AlertEventRuleType(name='AlertTraffic')
        self.assertEquals(value.dump(), 'AlertTraffic')
        self.assertEquals(value.get_name(), 'AlertTraffic')
        self.assertEquals(value.get_value(), 0)

    def test_01_AlertEventRuleType_AlertContent(self):
        """
        Test AlertEventRuleType with AlertContent
        """
        value = pykerio.enums.AlertEventRuleType(name='AlertContent')
        self.assertEquals(value.dump(), 'AlertContent')
        self.assertEquals(value.get_name(), 'AlertContent')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_AlertEventRuleType_FAIL(self):
        """
        Test AlertEventRuleType with FAIL
        """
        value = pykerio.enums.AlertEventRuleType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
