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

import os
import ssl
import time
import unittest

import pykerio
from pykerio.enums import (InterfaceGroupType,
                           InterfaceType,
                           SpeedDuplexType)


class TestCase_Ports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Prepares session
        """
        # Ignore invalid certificates
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        # API object
        api = pykerio.PyKerioControl(
            server=os.environ.get('KERIO_SERVER', 'control-demo.kerio.com'),
            port=int(os.environ.get('KERIO_PORT', '4081')))
        # ApiApplication object
        application = pykerio.structs.ApiApplication({
            'name': cls.__name__,
            'vendor': pykerio.constants.APP_NAME,
            'version': pykerio.constants.APP_VERSION})

        # Session login
        cls.session = pykerio.interfaces.Session(api)
        cls.session.login(userName=os.environ.get('KERIO_USERNAME',
                                                  'admin-en'),
                          password=os.environ.get('KERIO_PASSWORD',
                                                  'kerio'),
                          application=application)

        # Ports
        cls.ports = pykerio.interfaces.Ports(api)
        # Interaces
        cls.interfaces = pykerio.interfaces.Interfaces(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        cls.session.logout()

    def test_01_get(self):
        """
        Test Ports get
        """
        ports_list = self.__class__.ports.get()
        self.assertNotEqual(len(ports_list), 0)
        for port in ports_list:
            self.assertEqual(type(port), pykerio.structs.PortConfig)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_02_set(self):
        """
        Test Ports set
        """
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=InterfaceType.Ethernet,
            interface_group=InterfaceGroupType.Guest)

        ports_list = self.__class__.ports.get()
        for port in ports_list:
            if port['id'] == ifaces[0]['ports'][0]:
                # Change Guests ports speed to FullDuplex 100 Mbits
                port['speedDuplex'] = SpeedDuplexType.SpeedDuplexFull100
        # Apply changes
        self.__class__.ports.set(ports_list, 10)
        time.sleep(3)
        # Restore full speed
        for port in ports_list:
            if port['id'] == ifaces[0]['ports'][0]:
                # Change Guests ports speed to automatic
                port['speedDuplex'] = SpeedDuplexType.SpeedDuplexAuto
        # Apply changes
        self.__class__.ports.set(ports_list, 10)
