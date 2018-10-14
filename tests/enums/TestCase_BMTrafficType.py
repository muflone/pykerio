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


class TestCase_BMTrafficType(unittest.TestCase):
    def test_00_BMTrafficType_BMTrafficEmail(self):
        """
        Test BMTrafficType with BMTrafficEmail
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficEmail')
        self.assertEquals(value.dump(), 'BMTrafficEmail')
        self.assertEquals(value.get_name(), 'BMTrafficEmail')
        self.assertEquals(value.get_value(), 0)

    def test_01_BMTrafficType_BMTrafficFtp(self):
        """
        Test BMTrafficType with BMTrafficFtp
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficFtp')
        self.assertEquals(value.dump(), 'BMTrafficFtp')
        self.assertEquals(value.get_name(), 'BMTrafficFtp')
        self.assertEquals(value.get_value(), 1)

    def test_02_BMTrafficType_BMTrafficInstantMessaging(self):
        """
        Test BMTrafficType with BMTrafficInstantMessaging
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficInstantMessaging')
        self.assertEquals(value.dump(), 'BMTrafficInstantMessaging')
        self.assertEquals(value.get_name(), 'BMTrafficInstantMessaging')
        self.assertEquals(value.get_value(), 2)

    def test_03_BMTrafficType_BMTrafficMultimedia(self):
        """
        Test BMTrafficType with BMTrafficMultimedia
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficMultimedia')
        self.assertEquals(value.dump(), 'BMTrafficMultimedia')
        self.assertEquals(value.get_name(), 'BMTrafficMultimedia')
        self.assertEquals(value.get_value(), 3)

    def test_04_BMTrafficType_BMTrafficP2p(self):
        """
        Test BMTrafficType with BMTrafficP2p
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficP2p')
        self.assertEquals(value.dump(), 'BMTrafficP2p')
        self.assertEquals(value.get_name(), 'BMTrafficP2p')
        self.assertEquals(value.get_value(), 4)

    def test_05_BMTrafficType_BMTrafficRemoteAccess(self):
        """
        Test BMTrafficType with BMTrafficRemoteAccess
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficRemoteAccess')
        self.assertEquals(value.dump(), 'BMTrafficRemoteAccess')
        self.assertEquals(value.get_name(), 'BMTrafficRemoteAccess')
        self.assertEquals(value.get_value(), 5)

    def test_06_BMTrafficType_BMTrafficSip(self):
        """
        Test BMTrafficType with BMTrafficSip
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficSip')
        self.assertEquals(value.dump(), 'BMTrafficSip')
        self.assertEquals(value.get_name(), 'BMTrafficSip')
        self.assertEquals(value.get_value(), 6)

    def test_07_BMTrafficType_BMTrafficVpn(self):
        """
        Test BMTrafficType with BMTrafficVpn
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficVpn')
        self.assertEquals(value.dump(), 'BMTrafficVpn')
        self.assertEquals(value.get_name(), 'BMTrafficVpn')
        self.assertEquals(value.get_value(), 7)

    def test_08_BMTrafficType_BMTrafficWeb(self):
        """
        Test BMTrafficType with BMTrafficWeb
        """
        value = pykerio.enums.BMTrafficType(name='BMTrafficWeb')
        self.assertEquals(value.dump(), 'BMTrafficWeb')
        self.assertEquals(value.get_name(), 'BMTrafficWeb')
        self.assertEquals(value.get_value(), 8)

    @unittest.expectedFailure
    def test_99_BMTrafficType_FAIL(self):
        """
        Test BMTrafficType with FAIL
        """
        value = pykerio.enums.BMTrafficType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
