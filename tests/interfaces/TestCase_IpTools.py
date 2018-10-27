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
import time
import unittest

import pykerio


class TestCase_IpTools(unittest.TestCase):
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

        # HardwareInfo
        cls.iptools = pykerio.interfaces.IpTools(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        cls.session.logout()

    def test_01_ping(self):
        """
        Test IpTools ping
        """
        self.__class__.iptools.ping(target='kerio.com',
                                    ipversion=pykerio.enums.IpVersion(
                                        name='IpVersion4'),
                                    infinite=True,
                                    packetSize=pykerio.constants.DEFAULT_PING_SIZE,
                                    allowFragmentation=False)
        time.sleep(3)
        active_tool, lines = self.__class__.iptools.getStatus()
        self.assertEquals(active_tool.dump(), pykerio.enums.ActiveTool(
            name='ActiveToolPing').dump())
        for line in lines:
            print(line)
        self.__class__.iptools.stop()

    def test_02_traceRoute(self):
        """
        Test IpTools traceRoute
        """
        self.__class__.iptools.traceRoute(target='kerio.com',
                                          ipversion=pykerio.enums.IpVersion(
                                              name='IpVersion4'),
                                          resolveHostnames=True)
        time.sleep(3)
        active_tool, lines = self.__class__.iptools.getStatus()
        for line in lines:
            print(line)
        self.__class__.iptools.stop()

    def test_03_whois(self):
        """
        Test IpTools whois
        """
        self.__class__.iptools.whois(target='kerio.com')
        time.sleep(3)
        active_tool, lines = self.__class__.iptools.getStatus()
        for line in lines:
            print(line)
        self.__class__.iptools.stop()

    def test_04_dns(self):
        """
        Test IpTools dns (using nslookup)
        """
        self.__class__.iptools.dns(name='kerio.com',
                                   server='8.8.8.8',
                                   tool=pykerio.enums.DnsTool(
                                       name='DnsToolNslookup'),
                                   dns_type=pykerio.enums.DnsType('DnsTypeAny'))
        time.sleep(3)
        active_tool, lines = self.__class__.iptools.getStatus()
        for line in lines:
            print(line)
        self.__class__.iptools.stop()

    def test_05_dns(self):
        """
        Test IpTools dns (using dig)
        """
        self.__class__.iptools.dns(name='kerio.com',
                                   server='8.8.8.8',
                                   tool=pykerio.enums.DnsTool(
                                       name='DnsToolDig'),
                                   dns_type=pykerio.enums.DnsType('DnsTypeAny'))
        time.sleep(3)
        active_tool, lines = self.__class__.iptools.getStatus()
        for line in lines:
            print(line)
        self.__class__.iptools.stop()

    def test_06_getDnsServers(self):
        """
        Test IpTools getDnsServers
        """
        servers = self.__class__.iptools.getDnsServers()
        self.assertNotEqual(len(servers), 0)

    def test_07_getStatus(self):
        """
        Test IpTools getStatus
        """
        active_tool, lines = self.__class__.iptools.getStatus()
        self.assertTrue(isinstance(active_tool, pykerio.enums.ActiveTool))

    def test_08_stop(self):
        """
        Test IpTools stop
        """
        self.__class__.iptools.stop()
