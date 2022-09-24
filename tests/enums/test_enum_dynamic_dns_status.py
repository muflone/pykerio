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


class TestCase_DynamicDnsStatus(unittest.TestCase):
    def test_00_DynamicDnsStatus_DynamicDnsOk(self):
        """
        Test DynamicDnsStatus with DynamicDnsOk
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsOk')
        self.assertEqual(value.dump(), 'DynamicDnsOk')
        self.assertEqual(value.get_name(), 'DynamicDnsOk')
        self.assertEqual(value.get_value(), 0)

    def test_01_DynamicDnsStatus_DynamicDnsError(self):
        """
        Test DynamicDnsStatus with DynamicDnsError
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsError')
        self.assertEqual(value.dump(), 'DynamicDnsError')
        self.assertEqual(value.get_name(), 'DynamicDnsError')
        self.assertEqual(value.get_value(), 1)

    def test_02_DynamicDnsStatus_DynamicDnsUpdate(self):
        """
        Test DynamicDnsStatus with DynamicDnsUpdate
        """
        value = pykerio.enums.DynamicDnsStatus(name='DynamicDnsUpdate')
        self.assertEqual(value.dump(), 'DynamicDnsUpdate')
        self.assertEqual(value.get_name(), 'DynamicDnsUpdate')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_DynamicDnsStatus_FAIL(self):
        """
        Test DynamicDnsStatus with FAIL
        """
        value = pykerio.enums.DynamicDnsStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
