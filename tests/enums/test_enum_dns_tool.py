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


class TestCase_DnsTool(unittest.TestCase):
    def test_00_DnsTool_DnsToolNslookup(self):
        """
        Test DnsTool with DnsToolNslookup
        """
        value = pykerio.enums.DnsTool(name='DnsToolNslookup')
        self.assertEqual(value.dump(), 'DnsToolNslookup')
        self.assertEqual(value.get_name(), 'DnsToolNslookup')
        self.assertEqual(value.get_value(), 0)

    def test_01_DnsTool_DnsToolDig(self):
        """
        Test DnsTool with DnsToolDig
        """
        value = pykerio.enums.DnsTool(name='DnsToolDig')
        self.assertEqual(value.dump(), 'DnsToolDig')
        self.assertEqual(value.get_name(), 'DnsToolDig')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_DnsTool_FAIL(self):
        """
        Test DnsTool with FAIL
        """
        value = pykerio.enums.DnsTool(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
