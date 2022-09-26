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
import unittest

import pykerio


class TestCase_HardwareInfo(unittest.TestCase):
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

        # HardwareInfo
        cls.dns = pykerio.interfaces.Dns(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        cls.session.logout()

    def test_01_get(self):
        """
        Test Dns get
        """
        config = self.__class__.dns.get()
        self.assertTrue(isinstance(config, pykerio.structs.DnsConfig))

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_02_set(self):
        """
        Test Dns set
        """
        config = self.__class__.dns.get()
        # Disable cache and reset status
        config['cacheEnabled'] = not config['cacheEnabled']
        self.__class__.dns.set(config)
        config['cacheEnabled'] = not config['cacheEnabled']
        results = self.__class__.dns.set(config)
        self.assertEqual(len(results), 0)

    def test_03_getHosts(self):
        """
        Test Dns getHosts
        """
        results = self.__class__.dns.getHosts()
        for host in results:
            self.assertTrue(isinstance(host, pykerio.structs.DnsHost))

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_04_setHosts(self):
        """
        Test Dns setHosts
        """
        hosts = self.__class__.dns.getHosts()
        new_host = pykerio.structs.DnsHost({
            'enabled': True,
            'id': pykerio.types.KId(''),
            'ip': pykerio.types.IpAddress('8.8.8.8'),
            'hosts': 'dns.google.com',
            'description': 'Google public DNS'})
        hosts.append(new_host)
        results = self.__class__.dns.setHosts(hosts)
        self.assertEqual(len(results), 0)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_05_clearCache(self):
        """
        Test Dns clearCache
        """
        self.__class__.dns.clearCache()
