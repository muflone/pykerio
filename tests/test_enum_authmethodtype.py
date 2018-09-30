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


class TestCase_AuthMethodType(unittest.TestCase):
    def test_01_AuthMethodType_AuthMethodWeb(self):
        """
        Test AuthMethodType with AuthMethodWeb
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodWeb')
        self.assertEquals(value.value, 'AuthMethodWeb')
        self.assertEquals(value.dump(), 'AuthMethodWeb')

    def test_02_AuthMethodType_AuthMethodSslWeb(self):
        """
        Test AuthMethodType with AuthMethodSslWeb
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodSslWeb')
        self.assertEquals(value.value, 'AuthMethodSslWeb')
        self.assertEquals(value.dump(), 'AuthMethodSslWeb')

    def test_03_AuthMethodType_AuthMethodNtlm(self):
        """
        Test AuthMethodType with AuthMethodNtlm
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodNtlm')
        self.assertEquals(value.value, 'AuthMethodNtlm')
        self.assertEquals(value.dump(), 'AuthMethodNtlm')

    def test_04_AuthMethodType_AuthMethodProxy(self):
        """
        Test AuthMethodType with AuthMethodProxy
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodProxy')
        self.assertEquals(value.value, 'AuthMethodProxy')
        self.assertEquals(value.dump(), 'AuthMethodProxy')

    def test_05_AuthMethodType_AuthMethodAutomatic(self):
        """
        Test AuthMethodType with AuthMethodAutomatic
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodAutomatic')
        self.assertEquals(value.value, 'AuthMethodAutomatic')
        self.assertEquals(value.dump(), 'AuthMethodAutomatic')

    def test_06_AuthMethodType_AuthMethodVpnClient(self):
        """
        Test AuthMethodType with AuthMethodVpnClient
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodVpnClient')
        self.assertEquals(value.value, 'AuthMethodVpnClient')
        self.assertEquals(value.dump(), 'AuthMethodVpnClient')

    def test_07_AuthMethodType_AuthMethodSso(self):
        """
        Test AuthMethodType with AuthMethodSso
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodSso')
        self.assertEquals(value.value, 'AuthMethodSso')
        self.assertEquals(value.dump(), 'AuthMethodSso')

    def test_08_AuthMethodType_AuthMethodApi(self):
        """
        Test AuthMethodType with AuthMethodApi
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodApi')
        self.assertEquals(value.value, 'AuthMethodApi')
        self.assertEquals(value.dump(), 'AuthMethodApi')

    def test_09_AuthMethodType_AuthMethodRadius(self):
        """
        Test AuthMethodType with AuthMethodRadius
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodRadius')
        self.assertEquals(value.value, 'AuthMethodRadius')
        self.assertEquals(value.dump(), 'AuthMethodRadius')

    def test_10_AuthMethodType_AuthMethodNone(self):
        """
        Test AuthMethodType with AuthMethodNone
        """
        value = pykerio.enums.AuthMethodType(value='AuthMethodNone')
        self.assertEquals(value.value, 'AuthMethodNone')
        self.assertEquals(value.dump(), 'AuthMethodNone')

    @unittest.expectedFailure
    def test_99_AuthMethodType_FAIL(self):
        """
        Test AuthMethodType with FAIL
        """
        value = pykerio.enums.AuthMethodType(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
