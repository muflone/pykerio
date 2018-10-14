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


class TestCase_RuleAction(unittest.TestCase):
    def test_00_RuleAction_Allow(self):
        """
        Test RuleAction with Allow
        """
        value = pykerio.enums.RuleAction(name='Allow')
        self.assertEquals(value.dump(), 'Allow')
        self.assertEquals(value.get_name(), 'Allow')
        self.assertEquals(value.get_value(), 0)

    def test_01_RuleAction_Deny(self):
        """
        Test RuleAction with Deny
        """
        value = pykerio.enums.RuleAction(name='Deny')
        self.assertEquals(value.dump(), 'Deny')
        self.assertEquals(value.get_name(), 'Deny')
        self.assertEquals(value.get_value(), 1)

    def test_02_RuleAction_Drop(self):
        """
        Test RuleAction with Drop
        """
        value = pykerio.enums.RuleAction(name='Drop')
        self.assertEquals(value.dump(), 'Drop')
        self.assertEquals(value.get_name(), 'Drop')
        self.assertEquals(value.get_value(), 2)

    def test_03_RuleAction_NotSet(self):
        """
        Test RuleAction with NotSet
        """
        value = pykerio.enums.RuleAction(name='NotSet')
        self.assertEquals(value.dump(), 'NotSet')
        self.assertEquals(value.get_name(), 'NotSet')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_RuleAction_FAIL(self):
        """
        Test RuleAction with FAIL
        """
        value = pykerio.enums.RuleAction(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
