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

from pykerio.enums import DynamicDnsStatus


class TestCase_DynamicDnsStatus(unittest.TestCase):
    def test_00_DynamicDnsOk(self):
        """
        Test DynamicDnsStatus with DynamicDnsOk
        """
        value = DynamicDnsStatus.DynamicDnsOk
        self.assertEqual(value.dump(), 'DynamicDnsOk')
        self.assertEqual(value.name, 'DynamicDnsOk')
        self.assertEqual(value.value, 0)

    def test_01_DynamicDnsError(self):
        """
        Test DynamicDnsStatus with DynamicDnsError
        """
        value = DynamicDnsStatus.DynamicDnsError
        self.assertEqual(value.dump(), 'DynamicDnsError')
        self.assertEqual(value.name, 'DynamicDnsError')
        self.assertEqual(value.value, 1)

    def test_02_DynamicDnsUpdate(self):
        """
        Test DynamicDnsStatus with DynamicDnsUpdate
        """
        value = DynamicDnsStatus.DynamicDnsUpdate
        self.assertEqual(value.dump(), 'DynamicDnsUpdate')
        self.assertEqual(value.name, 'DynamicDnsUpdate')
        self.assertEqual(value.value, 2)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test DynamicDnsStatus with FAIL
        """
        value = DynamicDnsStatus.FAIL
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.name, 'FAIL')
        self.assertEqual(value.value, 99)
