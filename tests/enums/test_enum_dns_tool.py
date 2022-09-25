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

from pykerio.enums import DnsTool


class TestCase_DnsTool(unittest.TestCase):
    def test_00_DnsToolNslookup(self):
        """
        Test DnsTool with DnsToolNslookup
        """
        value = DnsTool.DnsToolNslookup
        self.assertEqual(value.dump(), 'DnsToolNslookup')
        self.assertEqual(value.name, 'DnsToolNslookup')
        self.assertEqual(value.value, 0)

    def test_01_DnsToolDig(self):
        """
        Test DnsTool with DnsToolDig
        """
        value = DnsTool.DnsToolDig
        self.assertEqual(value.dump(), 'DnsToolDig')
        self.assertEqual(value.name, 'DnsToolDig')
        self.assertEqual(value.value, 1)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test DnsTool with FAIL
        """
        value = DnsTool.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
