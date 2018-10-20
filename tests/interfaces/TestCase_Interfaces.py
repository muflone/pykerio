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


class TestCase_Interfaces(unittest.TestCase):
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

        # Interfaces
        cls.interfaces = pykerio.interfaces.Interfaces(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        # Disconnection may fail when set test fail for permissions issues
        try:
            cls.session.logout()
        except Exception:
            pass

    def test_01_get(self):
        """
        Test Interfaces get
        """
        fields = pykerio.lists.StringList()
        conditions = pykerio.lists.SubConditionList()

        order = pykerio.structs.SortOrder({
            'columnName': 'type',
            'direction': pykerio.enums.SortDirection(name='Asc'),
            'caseSensitive': False})
        orderbylist = pykerio.lists.SortOrderList()
        orderbylist.append(order)

        search_query = pykerio.structs.SearchQuery({
            'fields': fields,
            'conditions': conditions,
            'combining': pykerio.enums.LogicalOperator('And'),
            'start': 0,
            'limit': pykerio.constants.UNLIMITED,
            'orderBy': orderbylist})
        (ifaces, count) = self.__class__.interfaces.get(query=search_query,
                                                        sortByGroup=False)
        # Check for count = 0
        self.assertNotEquals(count, 0)
        # Check for number of interfaces different from count
        self.assertEquals(len(ifaces), count)
        # Check for results in InterfaceList form (only for empty fields list)
        self.assertEquals(type(ifaces), pykerio.lists.InterfaceList)
        print()
        for iface in ifaces:
            # Check the type for each interface
            self.assertEquals(type(iface), pykerio.structs.Interface)
            # print(iface['name'], iface['type'].dump())
            iface_type = iface['type'].dump()
            if iface_type == pykerio.enums.InterfaceType('Ethernet').dump():
                print('{ENABLED:2s}{TYPE:15s}{GROUP:15s}{LINK:20s}'
                      '{NAME:15s}{IP:20s}{SUBNET:20s}{GATEWAY:20s}{DNS:20s}'
                      '{MAC:20s}{SYSTEMNAME:20s}'.format(
                      ENABLED='E' if iface['enabled'] else 'D',
                      LINK=iface['linkStatus'].dump(),
                      NAME=iface['name'],
                      GATEWAY=iface['gateway'],
                      DNS=iface['dnsServers'],
                      IP=iface['ip'],
                      SUBNET=iface['subnetMask'],
                      MAC=iface['mac'],
                      SYSTEMNAME=iface['systemName'],
                      GROUP=iface['group'].dump(),
                      TYPE=iface['type'].dump()))
            elif iface_type == pykerio.enums.InterfaceType('VpnServer').dump():
                # Check for VpnServer config type
                self.assertEquals(type(iface['server']),
                                  pykerio.structs.VpnServerConfig)
                print('{ENABLED:2s}{TYPE:15s}{GROUP:15s}{LINK:20s}'
                      '{NAME:15s}{IP:20s}{SUBNET:20s}{GATEWAY:20s}{DNS:20s}'
                      ''.format(
                      ENABLED='E' if iface['enabled'] else 'D',
                      LINK=iface['linkStatus'].dump(),
                      NAME=iface['name'],
                      GATEWAY=iface['ip'],
                      DNS=iface['server']['primaryDns'],
                      IP=iface['server']['network'],
                      SUBNET=iface['server']['mask'],
                      GROUP=iface['group'].dump(),
                      TYPE=iface['type'].dump()))

    def test_02_get_with_fields(self):
        """
        Test Interfaces get with fields
        """
        fields = pykerio.lists.StringList(['name', 'type', 'group'])
        conditions = pykerio.lists.SubConditionList()
        conditions.append(pykerio.structs.SubCondition({
            'fieldName': 'type',
            'comparator': pykerio.enums.CompareOperator('Eq'),
            'value': 'Ethernet'}))

        order = pykerio.structs.SortOrder({
            'columnName': 'name',
            'direction': pykerio.enums.SortDirection(name='Asc'),
            'caseSensitive': False})
        orderbylist = pykerio.lists.SortOrderList()
        orderbylist.append(order)

        search_query = pykerio.structs.SearchQuery({
            'fields': fields,
            'conditions': conditions,
            'combining': pykerio.enums.LogicalOperator('And'),
            'start': 0,
            'limit': pykerio.constants.UNLIMITED,
            'orderBy': orderbylist})
        (ifaces, count) = self.__class__.interfaces.get(query=search_query,
                                                        sortByGroup=True)
        # Check for count = 0
        self.assertNotEquals(count, 0)
        # Check for number of interfaces different from count
        self.assertEquals(len(ifaces), count)
        # Check for results not in dictionary form (only for filled fields list)
        self.assertNotEquals(type(ifaces), dict)
        # Check for the number of fields in the first interface
        self.assertEquals(len(ifaces[0].items()), len(fields))

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_03_set(self):
        """
        Test Interfaces set
        """
        fields = pykerio.lists.StringList()
        conditions = pykerio.lists.SubConditionList()
        conditions.append(pykerio.structs.SubCondition({
            'fieldName': 'type',
            'comparator': pykerio.enums.CompareOperator('Eq'),
            'value': 'Ethernet'}))
        conditions.append(pykerio.structs.SubCondition({
            'fieldName': 'group',
            'comparator': pykerio.enums.CompareOperator('Eq'),
            'value': 'Trusted'}))

        order = pykerio.structs.SortOrder({
            'columnName': 'name',
            'direction': pykerio.enums.SortDirection(name='Asc'),
            'caseSensitive': False})
        orderbylist = pykerio.lists.SortOrderList()
        orderbylist.append(order)

        search_query = pykerio.structs.SearchQuery({
            'fields': fields,
            'conditions': conditions,
            'combining': pykerio.enums.LogicalOperator('And'),
            'start': 0,
            'limit': pykerio.constants.UNLIMITED,
            'orderBy': orderbylist})
        (ifaces, count) = self.__class__.interfaces.get(query=search_query,
                                                        sortByGroup=True)
        for iface in ifaces:
            kid = pykerio.types.KId(iface['id'])
            self.__class__.interfaces.set(pykerio.lists.KIdList(kid),
                                          iface)
        self.__class__.interfaces.reset()

    def test_04_reset(self):
        """
        Test Interfaces reset
        """
        self.__class__.interfaces.reset()

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_05_apply(self):
        """
        Test Interfaces apply
        """
        self.__class__.interfaces.apply(10)

    def test_06_find(self):
        """
        Test Interfaces find
        """
        filter_type = pykerio.enums.InterfaceType('Ethernet')
        filter_group = pykerio.enums.InterfaceGroupType('Trusted')
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=filter_type,
            interface_group=filter_group)
        for iface in ifaces:
            self.assertEquals(iface['type'].dump(), filter_type.dump())
            self.assertEquals(iface['group'].dump(), filter_group.dump())

        filter_type = pykerio.enums.InterfaceType('Ethernet')
        filter_group = None
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=filter_type,
            interface_group=filter_group)
        for iface in ifaces:
            self.assertEquals(iface['type'].dump(), filter_type.dump())

        filter_type = None
        filter_group = pykerio.enums.InterfaceGroupType('Trusted')
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=filter_type,
            interface_group=filter_group)
        for iface in ifaces:
            self.assertEquals(iface['group'].dump(), filter_group.dump())

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_07_create(self):
        """
        Test Interfaces create
        """
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=pykerio.enums.InterfaceType('VpnTunnel'),
            interface_group=None)
        if ifaces:
            # Create a new VPN tunnel based on the first found
            ifaces[0]['name'] = 'Tunnel %s' % self.__class__.__name__
            ifaces[0]['enabled'] = False
            ifaces[0]['tunnel']['remoteFingerprint'] = ':'.join(
                'f' * 16).replace('f', 'ff')
            interfaces_list = pykerio.lists.InterfaceList()
            interfaces_list.append(ifaces[0])
            (error_list, results_list) = self.__class__.interfaces.create(
                interfaces_list)
            self.assertEquals(len(error_list), 0)
            self.assertEquals(len(results_list), 1)
            # Apply changes
            self.__class__.interfaces.apply(10)
            self.__class__.session.apply()
        else:
            self.assertFalse(True)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_08_create_ras(self):
        """
        Test Interfaces create for Ras connection
        """
        ifaces = self.__class__.interfaces.find(
            name=None,
            interface_type=pykerio.enums.InterfaceType('Ras'),
            interface_group=None)
        if ifaces:
            # Create a new Ras connection based on the first found
            ifaces[0]['name'] = 'Ras %s' % self.__class__.__name__
            ifaces[0]['enabled'] = False
            interfaces_list = pykerio.lists.InterfaceList()
            interfaces_list.append(ifaces[0])
            (error_list, results_list) = self.__class__.interfaces.create(
                interfaces_list)
            self.assertEquals(len(error_list), 0)
            self.assertEquals(len(results_list), 1)
            # Apply changes
            self.__class__.interfaces.apply(10)
            self.__class__.session.apply()
        else:
            self.assertFalse(True)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_09_dial(self):
        """
        Test Interfaces dial
        """
        ifaces = self.__class__.interfaces.find(
            name='Ras %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('Ras'),
            interface_group=None)
        if ifaces:
            kid = ifaces[0]['id']
            # Dial
            self.__class__.interfaces.dial(kid)
        else:
            self.assertFalse(True)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_10_hangup(self):
        """
        Test Interfaces hangup
        """
        ifaces = self.__class__.interfaces.find(
            name='Ras %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('Ras'),
            interface_group=None)
        if ifaces:
            kid = ifaces[0]['id']
            # Dial
            self.__class__.interfaces.hangup(kid)
        else:
            self.assertFalse(True)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_11_remove(self):
        """
        Test Interfaces remove
        """
        interfaces_list = pykerio.lists.KIdList()
        # Remove the test VPN tunnel
        ifaces = self.__class__.interfaces.find(
            name='Tunnel %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('VpnTunnel'),
            interface_group=None)
        self.assertEquals(len(ifaces), 1)
        kid = pykerio.types.KId(ifaces[0]['id'])
        interfaces_list.append(kid)
        # Remove the test Ras connection
        ifaces = self.__class__.interfaces.find(
            name='Ras %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('Ras'),
            interface_group=None)
        self.assertEquals(len(ifaces), 1)
        kid = pykerio.types.KId(ifaces[0]['id'])
        interfaces_list.append(kid)

        self.assertEquals(len(interfaces_list), 2)
        error_list = self.__class__.interfaces.remove(interfaces_list)
        self.assertEquals(len(error_list), 0)
        # Apply changes
        self.__class__.interfaces.apply(10)
        self.__class__.session.apply()
        # Check for removed interface
        ifaces = self.__class__.interfaces.find(
            name='Tunnel %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('VpnTunnel'),
            interface_group=None)
        self.assertEquals(len(ifaces), 0)
        ifaces = self.__class__.interfaces.find(
            name='Ras %s' % self.__class__.__name__,
            interface_type=pykerio.enums.InterfaceType('Ras'),
            interface_group=None)
        self.assertEquals(len(ifaces), 0)

    def test_12_checkIpCollision(self):
        """
        Test Interfaces checkIpCollision
        """
        collisions = self.__class__.interfaces.checkIpCollision()
        self.assertEquals(len(collisions), 0)

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_13_startConnectivityTest(self):
        """
        Test Interfaces startConnectivityTest
        """
        self.__class__.interfaces.startConnectivityTest()

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_14_connectivityTestStatus(self):
        """
        Test Interfaces connectivityTestStatus
        """
        status = self.__class__.interfaces.connectivityTestStatus()
        self.assertEquals(status.dump(), pykerio.enums.ConnectivityStatus(
            name='ConnectivityOk').dump())

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_15_cancelConnectivityTest(self):
        """
        Test Interfaces cancelConnectivityTest
        """
        self.__class__.interfaces.cancelConnectivityTest()

    def test_16_getWarnings(self):
        """
        Test Interfaces getWarnings
        """
        warnings = self.__class__.interfaces.getWarnings()
        self.assertEquals(len(warnings), 0)

    def test_17_getConnectivityConfig(self):
        """
        Test Interfaces getConnectivityConfig
        """
        config = self.__class__.interfaces.getConnectivityConfig()

    @unittest.skipIf(os.environ.get('KERIO_READONLY', 'NO').upper() == 'YES',
                     'Insufficient rights')
    def test_18_setConnectivityConfig(self):
        """
        Test Interfaces setConnectivityConfig
        """
        config = self.__class__.interfaces.getConnectivityConfig()
        config['probeHosts']['enabled'] = not config['probeHosts']['enabled']
        self.__class__.interfaces.setConnectivityConfig(config=config)
        self.__class__.interfaces.apply(10)
        self.__class__.session.apply()
        # Revert previous status
        config['probeHosts']['enabled'] = not config['probeHosts']['enabled']
        self.__class__.interfaces.setConnectivityConfig(config=config)
        self.__class__.interfaces.apply(10)
        self.__class__.session.apply()

    def test_19_getIpsecPeerIdConfig(self):
        """
        Test Interfaces getIpsecPeerIdConfig
        """
        config = self.__class__.interfaces.getIpsecPeerIdConfig()

    @unittest.skipIf(os.environ.get('KERIO_HAS_WIFI', 'NO').upper() == 'NO',
                     'No WiFi module enabled')
    def test_20_getWifiCountries(self):
        """
        Test Interfaces getWifiCountries
        """
        results = self.__class__.interfaces.getWifiCountries()
        self.assertNotEqual(len(config.keys()), 0)

    @unittest.skipIf(os.environ.get('KERIO_HAS_WIFI', 'NO').upper() == 'NO',
                     'No WiFi module enabled')
    def test_21_getWifiConfig(self):
        """
        Test Interfaces getWifiConfig
        """
        config = self.__class__.interfaces.getWifiConfig()
        self.assertEquals(len(config.keys()), 5)

    @unittest.skipIf(os.environ.get('KERIO_HAS_WIFI', 'NO').upper() == 'NO',
                     'No WiFi module enabled')
    def test_22_setWifiConfig(self):
        """
        Test Interfaces setWifiConfig
        """
        config = self.__class__.interfaces.getWifiConfig()
        self.__class__.interfaces.getWifiConfig(config)
        self.__class__.interfaces.reset()
