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


class TestCase_DynamicDnsStatus(unittest.TestCase):
    def test_00_DynamicDnsStatus_DynamicDnsOk(self):
        """
        Test DynamicDnsStatus with DynamicDnsOk
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsOk')
        self.assertEquals(value.dump(), 'DynamicDnsOk')
        self.assertEquals(value.get_name(), 'DynamicDnsOk')
        self.assertEquals(value.get_value(), 0)

    def test_01_DynamicDnsStatus_DynamicDnsError(self):
        """
        Test DynamicDnsStatus with DynamicDnsError
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsError')
        self.assertEquals(value.dump(), 'DynamicDnsError')
        self.assertEquals(value.get_name(), 'DynamicDnsError')
        self.assertEquals(value.get_value(), 1)

    def test_02_DynamicDnsStatus_DynamicDnsUpdate(self):
        """
        Test DynamicDnsStatus with DynamicDnsUpdate
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsUpdate')
        self.assertEquals(value.dump(), 'DynamicDnsUpdate')
        self.assertEquals(value.get_name(), 'DynamicDnsUpdate')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_DynamicDnsStatus_FAIL(self):
        """
        Test DynamicDnsStatus with FAIL
        """
        value = pykerio.enums.DynamicDnsStatus(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
