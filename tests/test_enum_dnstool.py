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


class TestCase_DnsTool(unittest.TestCase):
    def test_01_DnsTool_DnsToolNslookup(self):
        """
        Test DnsTool with DnsToolNslookup
        """
        value = pykerio.enums.DnsTool(value='DnsToolNslookup')
        self.assertEquals(value.value, 'DnsToolNslookup')
        self.assertEquals(value.dump(), 'DnsToolNslookup')

    def test_02_DnsTool_DnsToolDig(self):
        """
        Test DnsTool with DnsToolDig
        """
        value = pykerio.enums.DnsTool(value='DnsToolDig')
        self.assertEquals(value.value, 'DnsToolDig')
        self.assertEquals(value.dump(), 'DnsToolDig')

    @unittest.expectedFailure
    def test_99_DnsTool_FAIL(self):
        """
        Test DnsTool with FAIL
        """
        value = pykerio.enums.DnsTool(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
