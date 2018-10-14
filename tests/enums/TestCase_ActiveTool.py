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


class TestCase_ActiveTool(unittest.TestCase):
    def test_00_ActiveTool_ActiveToolNone(self):
        """
        Test ActiveTool with ActiveToolNone
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolNone')
        self.assertEquals(value.dump(), 'ActiveToolNone')
        self.assertEquals(value.get_name(), 'ActiveToolNone')
        self.assertEquals(value.get_value(), 0)

    def test_01_ActiveTool_ActiveToolPing(self):
        """
        Test ActiveTool with ActiveToolPing
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolPing')
        self.assertEquals(value.dump(), 'ActiveToolPing')
        self.assertEquals(value.get_name(), 'ActiveToolPing')
        self.assertEquals(value.get_value(), 1)

    def test_02_ActiveTool_ActiveToolTraceRoute(self):
        """
        Test ActiveTool with ActiveToolTraceRoute
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolTraceRoute')
        self.assertEquals(value.dump(), 'ActiveToolTraceRoute')
        self.assertEquals(value.get_name(), 'ActiveToolTraceRoute')
        self.assertEquals(value.get_value(), 2)

    def test_03_ActiveTool_ActiveToolDns(self):
        """
        Test ActiveTool with ActiveToolDns
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolDns')
        self.assertEquals(value.dump(), 'ActiveToolDns')
        self.assertEquals(value.get_name(), 'ActiveToolDns')
        self.assertEquals(value.get_value(), 3)

    def test_04_ActiveTool_ActiveToolWhois(self):
        """
        Test ActiveTool with ActiveToolWhois
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolWhois')
        self.assertEquals(value.dump(), 'ActiveToolWhois')
        self.assertEquals(value.get_name(), 'ActiveToolWhois')
        self.assertEquals(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_ActiveTool_FAIL(self):
        """
        Test ActiveTool with FAIL
        """
        value = pykerio.enums.ActiveTool(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
