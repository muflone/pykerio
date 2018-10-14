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


class TestCase_AuthMethodType(unittest.TestCase):
    def test_00_AuthMethodType_AuthMethodWeb(self):
        """
        Test AuthMethodType with AuthMethodWeb
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodWeb')
        self.assertEquals(value.dump(), 'AuthMethodWeb')
        self.assertEquals(value.get_name(), 'AuthMethodWeb')
        self.assertEquals(value.get_value(), 0)

    def test_01_AuthMethodType_AuthMethodSslWeb(self):
        """
        Test AuthMethodType with AuthMethodSslWeb
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodSslWeb')
        self.assertEquals(value.dump(), 'AuthMethodSslWeb')
        self.assertEquals(value.get_name(), 'AuthMethodSslWeb')
        self.assertEquals(value.get_value(), 1)

    def test_02_AuthMethodType_AuthMethodNtlm(self):
        """
        Test AuthMethodType with AuthMethodNtlm
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodNtlm')
        self.assertEquals(value.dump(), 'AuthMethodNtlm')
        self.assertEquals(value.get_name(), 'AuthMethodNtlm')
        self.assertEquals(value.get_value(), 2)

    def test_03_AuthMethodType_AuthMethodProxy(self):
        """
        Test AuthMethodType with AuthMethodProxy
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodProxy')
        self.assertEquals(value.dump(), 'AuthMethodProxy')
        self.assertEquals(value.get_name(), 'AuthMethodProxy')
        self.assertEquals(value.get_value(), 3)

    def test_04_AuthMethodType_AuthMethodAutomatic(self):
        """
        Test AuthMethodType with AuthMethodAutomatic
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodAutomatic')
        self.assertEquals(value.dump(), 'AuthMethodAutomatic')
        self.assertEquals(value.get_name(), 'AuthMethodAutomatic')
        self.assertEquals(value.get_value(), 4)

    def test_05_AuthMethodType_AuthMethodVpnClient(self):
        """
        Test AuthMethodType with AuthMethodVpnClient
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodVpnClient')
        self.assertEquals(value.dump(), 'AuthMethodVpnClient')
        self.assertEquals(value.get_name(), 'AuthMethodVpnClient')
        self.assertEquals(value.get_value(), 5)

    def test_06_AuthMethodType_AuthMethodSso(self):
        """
        Test AuthMethodType with AuthMethodSso
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodSso')
        self.assertEquals(value.dump(), 'AuthMethodSso')
        self.assertEquals(value.get_name(), 'AuthMethodSso')
        self.assertEquals(value.get_value(), 6)

    def test_07_AuthMethodType_AuthMethodApi(self):
        """
        Test AuthMethodType with AuthMethodApi
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodApi')
        self.assertEquals(value.dump(), 'AuthMethodApi')
        self.assertEquals(value.get_name(), 'AuthMethodApi')
        self.assertEquals(value.get_value(), 7)

    def test_08_AuthMethodType_AuthMethodRadius(self):
        """
        Test AuthMethodType with AuthMethodRadius
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodRadius')
        self.assertEquals(value.dump(), 'AuthMethodRadius')
        self.assertEquals(value.get_name(), 'AuthMethodRadius')
        self.assertEquals(value.get_value(), 8)

    def test_09_AuthMethodType_AuthMethodNone(self):
        """
        Test AuthMethodType with AuthMethodNone
        """
        value = pykerio.enums.AuthMethodType(name='AuthMethodNone')
        self.assertEquals(value.dump(), 'AuthMethodNone')
        self.assertEquals(value.get_name(), 'AuthMethodNone')
        self.assertEquals(value.get_value(), 9)

    @unittest.expectedFailure
    def test_99_AuthMethodType_FAIL(self):
        """
        Test AuthMethodType with FAIL
        """
        value = pykerio.enums.AuthMethodType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
