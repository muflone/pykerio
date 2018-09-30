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

import pykerio.enums


class TestCase_ActiveTool(unittest.TestCase):
    def test_01_ActiveTool_ActiveToolNone(self):
        """
        Test ActiveTool with ActiveToolNone
        """
        value = pykerio.enums.ActiveTool(value='ActiveToolNone')
        self.assertEquals(value.value, 'ActiveToolNone')
        self.assertEquals(value.dump(), 'ActiveToolNone')

    def test_02_ActiveTool_ActiveToolPing(self):
        """
        Test ActiveTool with ActiveToolPing
        """
        value = pykerio.enums.ActiveTool(value='ActiveToolPing')
        self.assertEquals(value.value, 'ActiveToolPing')
        self.assertEquals(value.dump(), 'ActiveToolPing')

    def test_03_ActiveTool_ActiveToolTraceRoute(self):
        """
        Test ActiveTool with ActiveToolTraceRoute
        """
        value = pykerio.enums.ActiveTool(value='ActiveToolTraceRoute')
        self.assertEquals(value.value, 'ActiveToolTraceRoute')
        self.assertEquals(value.dump(), 'ActiveToolTraceRoute')

    def test_04_ActiveTool_ActiveToolDns(self):
        """
        Test ActiveTool with ActiveToolDns
        """
        value = pykerio.enums.ActiveTool(value='ActiveToolDns')
        self.assertEquals(value.value, 'ActiveToolDns')
        self.assertEquals(value.dump(), 'ActiveToolDns')

    def test_05_ActiveTool_ActiveToolWhois(self):
        """
        Test ActiveTool with ActiveToolWhois
        """
        value = pykerio.enums.ActiveTool(value='ActiveToolWhois')
        self.assertEquals(value.value, 'ActiveToolWhois ')
        self.assertEquals(value.dump(), 'ActiveToolWhois ')

    @unittest.expectedFailure
    def test_99_ActiveTool_FAIL(self):
        """
        Test ActiveTool with FAIL
        """
        value = pykerio.enums.ActiveTool(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
