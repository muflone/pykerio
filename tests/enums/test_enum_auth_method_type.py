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


class TestCase_AuthMethodType(unittest.TestCase):
    def test_00_AuthMethodWeb(self):
        """
        Test AuthMethodType with AuthMethodWeb
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodWeb')
        self.assertEqual(value.dump(), 'AuthMethodWeb')
        self.assertEqual(value.get_name(), 'AuthMethodWeb')
        self.assertEqual(value.get_value(), 0)

    def test_01_AuthMethodSslWeb(self):
        """
        Test AuthMethodType with AuthMethodSslWeb
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodSslWeb')
        self.assertEqual(value.dump(), 'AuthMethodSslWeb')
        self.assertEqual(value.get_name(), 'AuthMethodSslWeb')
        self.assertEqual(value.get_value(), 1)

    def test_02_AuthMethodNtlm(self):
        """
        Test AuthMethodType with AuthMethodNtlm
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodNtlm')
        self.assertEqual(value.dump(), 'AuthMethodNtlm')
        self.assertEqual(value.get_name(), 'AuthMethodNtlm')
        self.assertEqual(value.get_value(), 2)

    def test_03_AuthMethodProxy(self):
        """
        Test AuthMethodType with AuthMethodProxy
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodProxy')
        self.assertEqual(value.dump(), 'AuthMethodProxy')
        self.assertEqual(value.get_name(), 'AuthMethodProxy')
        self.assertEqual(value.get_value(), 3)

    def test_04_AuthMethodAutomatic(self):
        """
        Test AuthMethodType with AuthMethodAutomatic
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodAutomatic')
        self.assertEqual(value.dump(), 'AuthMethodAutomatic')
        self.assertEqual(value.get_name(), 'AuthMethodAutomatic')
        self.assertEqual(value.get_value(), 4)

    def test_05_AuthMethodVpnClient(self):
        """
        Test AuthMethodType with AuthMethodVpnClient
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodVpnClient')
        self.assertEqual(value.dump(), 'AuthMethodVpnClient')
        self.assertEqual(value.get_name(), 'AuthMethodVpnClient')
        self.assertEqual(value.get_value(), 5)

    def test_06_AuthMethodSso(self):
        """
        Test AuthMethodType with AuthMethodSso
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodSso')
        self.assertEqual(value.dump(), 'AuthMethodSso')
        self.assertEqual(value.get_name(), 'AuthMethodSso')
        self.assertEqual(value.get_value(), 6)

    def test_07_AuthMethodApi(self):
        """
        Test AuthMethodType with AuthMethodApi
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodApi')
        self.assertEqual(value.dump(), 'AuthMethodApi')
        self.assertEqual(value.get_name(), 'AuthMethodApi')
        self.assertEqual(value.get_value(), 7)

    def test_08_AuthMethodRadius(self):
        """
        Test AuthMethodType with AuthMethodRadius
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodRadius')
        self.assertEqual(value.dump(), 'AuthMethodRadius')
        self.assertEqual(value.get_name(), 'AuthMethodRadius')
        self.assertEqual(value.get_value(), 8)

    def test_09_AuthMethodNone(self):
        """
        Test AuthMethodType with AuthMethodNone
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodNone')
        self.assertEqual(value.dump(), 'AuthMethodNone')
        self.assertEqual(value.get_name(), 'AuthMethodNone')
        self.assertEqual(value.get_value(), 9)

    @unittest.expectedFailure
    def test_99_FAIL(self):
        """
        Test AuthMethodType with FAIL
        """
        value = pykerio.enums.AuthMethodType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)
