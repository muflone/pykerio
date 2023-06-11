##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
#   Copyright: 2018-2023 Fabio Castelli
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


class TestCase_CertificateType(unittest.TestCase):
    def test_00_CertificateType_ActiveCertificate(self):
        """
        Test CertificateType with ActiveCertificate
        """
        value = pykerio.enums.CertificateType.ActiveCertificate
        self.assertEqual(value.dump(), 'ActiveCertificate')
        self.assertEqual(value.name, 'ActiveCertificate')
        self.assertEqual(value.value, 0)

    def test_01_CertificateType_InactiveCertificate(self):
        """
        Test CertificateType with InactiveCertificate
        """
        value = pykerio.enums.CertificateType.InactiveCertificate
        self.assertEqual(value.dump(), 'InactiveCertificate')
        self.assertEqual(value.name, 'InactiveCertificate')
        self.assertEqual(value.value, 1)

    def test_02_CertificateType_CertificateRequest(self):
        """
        Test CertificateType with CertificateRequest
        """
        value = pykerio.enums.CertificateType.CertificateRequest
        self.assertEqual(value.dump(), 'CertificateRequest')
        self.assertEqual(value.name, 'CertificateRequest')
        self.assertEqual(value.value, 2)

    def test_03_CertificateType_Authority(self):
        """
        Test CertificateType with Authority
        """
        value = pykerio.enums.CertificateType.Authority
        self.assertEqual(value.dump(), 'Authority')
        self.assertEqual(value.name, 'Authority')
        self.assertEqual(value.value, 3)

    def test_04_CertificateType_LocalAuthority(self):
        """
        Test CertificateType with LocalAuthority
        """
        value = pykerio.enums.CertificateType.LocalAuthority
        self.assertEqual(value.dump(), 'LocalAuthority')
        self.assertEqual(value.name, 'LocalAuthority')
        self.assertEqual(value.value, 4)

    def test_05_CertificateType_BuiltInAuthority(self):
        """
        Test CertificateType with BuiltInAuthority
        """
        value = pykerio.enums.CertificateType.BuiltInAuthority
        self.assertEqual(value.dump(), 'BuiltInAuthority')
        self.assertEqual(value.name, 'BuiltInAuthority')
        self.assertEqual(value.value, 5)

    def test_06_CertificateType_ServerCertificate(self):
        """
        Test CertificateType with ServerCertificate
        """
        value = pykerio.enums.CertificateType.ServerCertificate
        self.assertEqual(value.dump(), 'ServerCertificate')
        self.assertEqual(value.name, 'ServerCertificate')
        self.assertEqual(value.value, 6)
