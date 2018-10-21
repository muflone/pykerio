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

import os
import ssl
import unittest

import pykerio


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
        cls.session.login(userName=os.environ.get('KERIO_USERNAME', 'admin-en'),
                          password=os.environ.get('KERIO_PASSWORD', 'kerio'),
                          application=application)

        # Ports
        cls.ports = pykerio.interfaces.Ports(api)

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
        self.assertNotEquals(len(ports_list), 0)
        for port in ports_list:
            self.assertEquals(type(port), pykerio.structs.PortConfig)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_02_set(self):
        """
        Test Ports set
        """
        ports_list = self.__class__.ports.get()
        for port in ports_list:
            # Changing LAN ports speed to HalfDuplex 10 Mbit
            if port['assignment'].dump() == pykerio.enums.PortAssignmentType(
                    'PortAssignmentSwitch').dump():
                port['speedDuplex'] = pykerio.enums.SpeedDuplexType(
                    name='SpeedDuplexHalf10')
        # Apply changes
        self.__class__.ports.set(ports_list, 10)
