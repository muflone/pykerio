##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
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


class TestCase_CertificateType(unittest.TestCase):
    def test_00_CertificateType_ActiveCertificate(self):
        """
        Test CertificateType with ActiveCertificate
        """
        value = pykerio.enums.CertificateType(name='ActiveCertificate')
        self.assertEquals(value.dump(), 'ActiveCertificate')
        self.assertEquals(value.get_name(), 'ActiveCertificate')
        self.assertEquals(value.get_value(), 0)

    def test_01_CertificateType_InactiveCertificate(self):
        """
        Test CertificateType with InactiveCertificate
        """
        value = pykerio.enums.CertificateType(name='InactiveCertificate')
        self.assertEquals(value.dump(), 'InactiveCertificate')
        self.assertEquals(value.get_name(), 'InactiveCertificate')
        self.assertEquals(value.get_value(), 1)

    def test_02_CertificateType_CertificateRequest(self):
        """
        Test CertificateType with CertificateRequest
        """
        value = pykerio.enums.CertificateType(name='CertificateRequest')
        self.assertEquals(value.dump(), 'CertificateRequest')
        self.assertEquals(value.get_name(), 'CertificateRequest')
        self.assertEquals(value.get_value(), 2)

    def test_03_CertificateType_Authority(self):
        """
        Test CertificateType with Authority
        """
        value = pykerio.enums.CertificateType(name='Authority')
        self.assertEquals(value.dump(), 'Authority')
        self.assertEquals(value.get_name(), 'Authority')
        self.assertEquals(value.get_value(), 3)

    def test_04_CertificateType_LocalAuthority(self):
        """
        Test CertificateType with LocalAuthority
        """
        value = pykerio.enums.CertificateType(name='LocalAuthority')
        self.assertEquals(value.dump(), 'LocalAuthority')
        self.assertEquals(value.get_name(), 'LocalAuthority')
        self.assertEquals(value.get_value(), 4)

    def test_05_CertificateType_BuiltInAuthority(self):
        """
        Test CertificateType with BuiltInAuthority
        """
        value = pykerio.enums.CertificateType(name='BuiltInAuthority')
        self.assertEquals(value.dump(), 'BuiltInAuthority')
        self.assertEquals(value.get_name(), 'BuiltInAuthority')
        self.assertEquals(value.get_value(), 5)

    def test_06_CertificateType_ServerCertificate(self):
        """
        Test CertificateType with ServerCertificate
        """
        value = pykerio.enums.CertificateType(name='ServerCertificate')
        self.assertEquals(value.dump(), 'ServerCertificate')
        self.assertEquals(value.get_name(), 'ServerCertificate')
        self.assertEquals(value.get_value(), 6)

    @unittest.expectedFailure
    def test_99_CertificateType_FAIL(self):
        """
        Test CertificateType with FAIL
        """
        value = pykerio.enums.CertificateType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
