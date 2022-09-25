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

from pykerio.enums import AuthMethodType


class TestCase_AuthMethodType(unittest.TestCase):
    def test_00_AuthMethodWeb(self):
        """
        Test AuthMethodType with AuthMethodWeb
        """
        value = AuthMethodType.AuthMethodWeb
        self.assertEqual(value.dump(), 'AuthMethodWeb')
        self.assertEqual(value.name, 'AuthMethodWeb')
        self.assertEqual(value.value, 0)

    def test_01_AuthMethodSslWeb(self):
        """
        Test AuthMethodType with AuthMethodSslWeb
        """
        value = AuthMethodType.AuthMethodSslWeb
        self.assertEqual(value.dump(), 'AuthMethodSslWeb')
        self.assertEqual(value.name, 'AuthMethodSslWeb')
        self.assertEqual(value.value, 1)

    def test_02_AuthMethodNtlm(self):
        """
        Test AuthMethodType with AuthMethodNtlm
        """
        value = AuthMethodType.AuthMethodNtlm
        self.assertEqual(value.dump(), 'AuthMethodNtlm')
        self.assertEqual(value.name, 'AuthMethodNtlm')
        self.assertEqual(value.value, 2)

    def test_03_AuthMethodProxy(self):
        """
        Test AuthMethodType with AuthMethodProxy
        """
        value = AuthMethodType.AuthMethodProxy
        self.assertEqual(value.dump(), 'AuthMethodProxy')
        self.assertEqual(value.name, 'AuthMethodProxy')
        self.assertEqual(value.value, 3)

    def test_04_AuthMethodAutomatic(self):
        """
        Test AuthMethodType with AuthMethodAutomatic
        """
        value = AuthMethodType.AuthMethodAutomatic
        self.assertEqual(value.dump(), 'AuthMethodAutomatic')
        self.assertEqual(value.name, 'AuthMethodAutomatic')
        self.assertEqual(value.value, 4)

    def test_05_AuthMethodVpnClient(self):
        """
        Test AuthMethodType with AuthMethodVpnClient
        """
        value = AuthMethodType.AuthMethodVpnClient
        self.assertEqual(value.dump(), 'AuthMethodVpnClient')
        self.assertEqual(value.name, 'AuthMethodVpnClient')
        self.assertEqual(value.value, 5)

    def test_06_AuthMethodSso(self):
        """
        Test AuthMethodType with AuthMethodSso
        """
        value = AuthMethodType.AuthMethodSso
        self.assertEqual(value.dump(), 'AuthMethodSso')
        self.assertEqual(value.name, 'AuthMethodSso')
        self.assertEqual(value.value, 6)

    def test_07_AuthMethodApi(self):
        """
        Test AuthMethodType with AuthMethodApi
        """
        value = AuthMethodType.AuthMethodApi
        self.assertEqual(value.dump(), 'AuthMethodApi')
        self.assertEqual(value.name, 'AuthMethodApi')
        self.assertEqual(value.value, 7)

    def test_08_AuthMethodRadius(self):
        """
        Test AuthMethodType with AuthMethodRadius
        """
        value = AuthMethodType.AuthMethodRadius
        self.assertEqual(value.dump(), 'AuthMethodRadius')
        self.assertEqual(value.name, 'AuthMethodRadius')
        self.assertEqual(value.value, 8)

    def test_09_AuthMethodNone(self):
        """
        Test AuthMethodType with AuthMethodNone
        """
        value = AuthMethodType.AuthMethodNone
        self.assertEqual(value.dump(), 'AuthMethodNone')
        self.assertEqual(value.name, 'AuthMethodNone')
        self.assertEqual(value.value, 9)
