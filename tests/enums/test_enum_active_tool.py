##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import unittest

import pykerio


class TestCase_ActiveTool(unittest.TestCase):
    def test_00_ActiveToolNone(self):
        """
        Test ActiveTool with ActiveToolNone
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolNone')
        self.assertEqual(value.dump(), 'ActiveToolNone')
        self.assertEqual(value.get_name(), 'ActiveToolNone')
        self.assertEqual(value.get_value(), 0)

    def test_01_ActiveToolPing(self):
        """
        Test ActiveTool with ActiveToolPing
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolPing')
        self.assertEqual(value.dump(), 'ActiveToolPing')
        self.assertEqual(value.get_name(), 'ActiveToolPing')
        self.assertEqual(value.get_value(), 1)

    def test_02_ActiveToolTraceRoute(self):
        """
        Test ActiveTool with ActiveToolTraceRoute
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolTraceRoute')
        self.assertEqual(value.dump(), 'ActiveToolTraceRoute')
        self.assertEqual(value.get_name(), 'ActiveToolTraceRoute')
        self.assertEqual(value.get_value(), 2)

    def test_03_ActiveToolDns(self):
        """
        Test ActiveTool with ActiveToolDns
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolDns')
        self.assertEqual(value.dump(), 'ActiveToolDns')
        self.assertEqual(value.get_name(), 'ActiveToolDns')
        self.assertEqual(value.get_value(), 3)

    def test_04_ActiveToolWhois(self):
        """
        Test ActiveTool with ActiveToolWhois
        """
        value = pykerio.enums.ActiveTool(name='ActiveToolWhois')
        self.assertEqual(value.dump(), 'ActiveToolWhois')
        self.assertEqual(value.get_name(), 'ActiveToolWhois')
        self.assertEqual(value.get_value(), 4)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test ActiveTool with FAIL
        """
        value = pykerio.enums.ActiveTool(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
