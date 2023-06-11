##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Just Me <just806me@gmail.com>
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

import os
import ssl
import unittest

import pykerio


class TestCase_ReverseProxy(unittest.TestCase):
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

        # ReverseProxy
        cls.reverse_proxy = pykerio.interfaces.ReverseProxy(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        cls.session.logout()

    def test_01_get(self):
        """
        Test ReverseProxy get
        """
        config = self.__class__.reverse_proxy.get()
        self.assertEqual(type(config), pykerio.structs.ReverseProxyConfig)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_02_set(self):
        """
        Test ReverseProxy set
        """
        config = self.__class__.reverse_proxy.get()
        # Toggling enabled flag
        config['enabled'] = not config['enabled']
        # Apply changes
        self.__class__.reverse_proxy.set(config)
