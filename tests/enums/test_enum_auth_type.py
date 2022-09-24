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


class TestCase_AuthType(unittest.TestCase):
    def test_00_AuthType_Internal(self):
        """
        Test AuthType with Internal
        """
        value = pykerio.enums.AuthType(name='Internal')
        self.assertEqual(value.dump(), 'Internal')
        self.assertEqual(value.get_name(), 'Internal')
        self.assertEqual(value.get_value(), 0)

    def test_01_AuthType_KerberosNt(self):
        """
        Test AuthType with KerberosNt
        """
        value = pykerio.enums.AuthType(name='KerberosNt')
        self.assertEqual(value.dump(), 'KerberosNt')
        self.assertEqual(value.get_name(), 'KerberosNt')
        self.assertEqual(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_AuthType_FAIL(self):
        """
        Test AuthType with FAIL
        """
        value = pykerio.enums.AuthType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)