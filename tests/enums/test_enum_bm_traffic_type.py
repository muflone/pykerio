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

from pykerio.enums import BMTrafficType


class TestCase_BMTrafficType(unittest.TestCase):
    def test_00_BMTrafficEmail(self):
        """
        Test BMTrafficType with BMTrafficEmail
        """
        value = BMTrafficType.BMTrafficEmail
        self.assertEqual(value.dump(), 'BMTrafficEmail')
        self.assertEqual(value.name, 'BMTrafficEmail')
        self.assertEqual(value.value, 0)

    def test_01_BMTrafficFtp(self):
        """
        Test BMTrafficType with BMTrafficFtp
        """
        value = BMTrafficType.BMTrafficFtp
        self.assertEqual(value.dump(), 'BMTrafficFtp')
        self.assertEqual(value.name, 'BMTrafficFtp')
        self.assertEqual(value.value, 1)

    def test_02_BMTrafficInstantMessaging(self):
        """
        Test BMTrafficType with BMTrafficInstantMessaging
        """
        value = BMTrafficType.BMTrafficInstantMessaging
        self.assertEqual(value.dump(), 'BMTrafficInstantMessaging')
        self.assertEqual(value.name, 'BMTrafficInstantMessaging')
        self.assertEqual(value.value, 2)

    def test_03_BMTrafficMultimedia(self):
        """
        Test BMTrafficType with BMTrafficMultimedia
        """
        value = BMTrafficType.BMTrafficMultimedia
        self.assertEqual(value.dump(), 'BMTrafficMultimedia')
        self.assertEqual(value.name, 'BMTrafficMultimedia')
        self.assertEqual(value.value, 3)

    def test_04_BMTrafficP2p(self):
        """
        Test BMTrafficType with BMTrafficP2p
        """
        value = BMTrafficType.BMTrafficP2p
        self.assertEqual(value.dump(), 'BMTrafficP2p')
        self.assertEqual(value.name, 'BMTrafficP2p')
        self.assertEqual(value.value, 4)

    def test_05_BMTrafficRemoteAccess(self):
        """
        Test BMTrafficType with BMTrafficRemoteAccess
        """
        value = BMTrafficType.BMTrafficRemoteAccess
        self.assertEqual(value.dump(), 'BMTrafficRemoteAccess')
        self.assertEqual(value.name, 'BMTrafficRemoteAccess')
        self.assertEqual(value.value, 5)

    def test_06_BMTrafficSip(self):
        """
        Test BMTrafficType with BMTrafficSip
        """
        value = BMTrafficType.BMTrafficSip
        self.assertEqual(value.dump(), 'BMTrafficSip')
        self.assertEqual(value.name, 'BMTrafficSip')
        self.assertEqual(value.value, 6)

    def test_07_BMTrafficVpn(self):
        """
        Test BMTrafficType with BMTrafficVpn
        """
        value = BMTrafficType.BMTrafficVpn
        self.assertEqual(value.dump(), 'BMTrafficVpn')
        self.assertEqual(value.name, 'BMTrafficVpn')
        self.assertEqual(value.value, 7)

    def test_08_BMTrafficWeb(self):
        """
        Test BMTrafficType with BMTrafficWeb
        """
        value = BMTrafficType.BMTrafficWeb
        self.assertEqual(value.dump(), 'BMTrafficWeb')
        self.assertEqual(value.name, 'BMTrafficWeb')
        self.assertEqual(value.value, 8)
