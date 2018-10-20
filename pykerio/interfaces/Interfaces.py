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

from ..pykerio import PyKerio

from ..constants import UNLIMITED

from ..enums import CompareOperator
from ..enums import ConnectivityStatus
from ..enums import InterfaceGroupType
from ..enums import InterfaceType
from ..enums import LogicalOperator
from ..enums import SortDirection

from ..lists import CreateResultList
from ..lists import ErrorList
from ..lists import InterfaceList
from ..lists import IpCollisionList
from ..lists import KIdList
from ..lists import NotificationTypeList
from ..lists import SortOrderList
from ..lists import StringList
from ..lists import SubConditionList
from ..lists import WifiCountryList

from ..structs import ConnectivityConfig
from ..structs import Interface
from ..structs import IpsecPeerIdConfig
from ..structs import SearchQuery
from ..structs import SortOrder
from ..structs import SubCondition
from ..structs import WifiConfig

from ..types import KId


class Interfaces(object):
    def __init__(self, api: PyKerio):
        self.api = api

    def reset(self):
        """
        discard changes cached in manager
        """
        response = self.api.request_rpc(
            method='Interfaces.reset',
            params={})

    def get(self, query: SearchQuery, sortByGroup: bool):
        """
        Obtain list of interfaces
        note: when sorting is set to 'name' column, interfaces are first sorted
        by 'type' and then by 'name'.
        When sortByGroup is true and sorting is 'name', sorting order is
        'group', 'type', 'name'
        """
        response = self.api.request_rpc(
            method='Interfaces.get',
            params={'query': query.dump(),
                    'sortByGroup': sortByGroup})
        totalItems = response.result['totalItems']
        if query['fields']:
            # If a fields list was requested, return only the dictionary with
            # the requested fields
            results = response.result['list']
        else:
            results = InterfaceList()
            results.load(response.result['list'])
        return (results, totalItems)

    def set(self, ids: KIdList, details: Interface):
        """
        Update interface's details
        """
        response = self.api.request_rpc(
            method='Interfaces.set',
            params={'ids': ids.dump(),
                    'details': details.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def create(self, interfaces: InterfaceList):
        """
        Creates new interface
        (Only one interface can be created at a time)
        VPN Tunnel or RAS on Ape/Box
        """
        response = self.api.request_rpc(
            method='Interfaces.create',
            params={'list': interfaces.dump()})
        errors = ErrorList()
        errors.load(response.result['errors'])
        results = CreateResultList()
        results.load(response.result['result'])
        return (errors, results)

    def remove(self, ids: KIdList):
        """
        Delete Interface configuration - VPN Tunnel or RAS on Ape/Box
        """
        response = self.api.request_rpc(
            method='Interfaces.remove',
            params={'ids': ids.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def apply(self, revertTimeout: int):
        """
        write changes cached in manager to configuration
        """
        response = self.api.request_rpc(
            method='Interfaces.apply',
            params={'revertTimeout': revertTimeout})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def dial(self, kid: KId):
        """
        Dial interface. Works only for disconnected RAS.
        Action is taken immediatelly, without apply.
        """
        response = self.api.request_rpc(
            method='Interfaces.dial',
            params={'id': kid})

    def hangup(self, kid: KId):
        """
        Hangup interface. Works only for connected RAS.
        Action is taken immediatelly, without apply.
        """
        response = self.api.request_rpc(
            method='Interfaces.hangup',
            params={'id': kid})

    def checkIpCollision(self):
        """
        Checks collision of all interfaces IP + VPN Server network
        """
        response = self.api.request_rpc(
            method='Interfaces.checkIpCollision',
            params={})
        results = IpCollisionList()
        results.load(response.result['collisions'])
        return results

    def startConnectivityTest(self):
        """
        Initiates testing of connectivity
        """
        response = self.api.request_rpc(
            method='Interfaces.startConnectivityTest',
            params={})

    def cancelConnectivityTest(self):
        """
        Cancels testing of connectivity and sets status to ConnectivityError
        """
        response = self.api.request_rpc(
            method='Interfaces.cancelConnectivityTest',
            params={})

    def connectivityTestStatus(self):
        """
        Returns progress of connectivity test
        startTest() has to be called before call of this function,
        otherwise status is instantly ConnectivityError.
        """
        response = self.api.request_rpc(
            method='Interfaces.connectivityTestStatus',
            params={})
        results = ConnectivityStatus(response.result['status'])
        return results

    def getWarnings(self):
        """
        Checks Link Load Balancing warnings
        """
        response = self.api.request_rpc(
            method='Interfaces.getWarnings',
            params={})
        results = NotificationTypeList()
        results.load(response.result['warnings'])
        return results

    def getConnectivityConfig(self):
        """
        Returns Connectivity config values
        """
        response = self.api.request_rpc(
            method='Interfaces.getConnectivityConfig',
            params={})
        results = ConnectivityConfig(response.result['config'])
        return results

    def setConnectivityConfig(self, config: ConnectivityConfig):
        """
        Stores Connectivity config values
        """
        response = self.api.request_rpc(
            method='Interfaces.setConnectivityConfig',
            params={'config': config.dump()})

    def getIpsecPeerIdConfig(self):
        """
        Returns Country list with allowed channel configuration
        """
        response = self.api.request_rpc(
            method='Interfaces.getIpsecPeerIdConfig',
            params={})
        results = IpsecPeerIdConfig(response.result['config'])
        return results

    #FIXME: needs testing and a box with WiFi
    def getWifiCountries(self):
        """
        Returns Country list with allowed channel configuration
        """
        response = self.api.request_rpc(
            method='Interfaces.getWifiCountries',
            params={})
        results = WifiCountryList()
        results.load(response.result['countries'])
        return results

    #FIXME: needs testing and a box with WiFi
    def getWifiConfig(self):
        """
        Returns WiFi configuration
        """
        response = self.api.request_rpc(
            method='Interfaces.getWifiConfig',
            params={})
        results = WifiConfig(response.result['config'])
        return results

    #FIXME: needs testing and a box with WiFi
    def setWifiConfig(self, config: WifiConfig):
        """
        Sets WiFi configuration
        """
        response = self.api.request_rpc(
            method='Interfaces.setWifiConfig',
            params={'config': config.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def find(self, name: str, interface_type: InterfaceType,
             interface_group: InterfaceGroupType):
        """
        Find interfaces by name, type or group
        """
        results = InterfaceList()
        conditions = SubConditionList()
        if name:
            conditions.append(SubCondition({'fieldName': 'name',
                                            'comparator': CompareOperator('Eq'),
                                            'value': name}))
        if interface_type:
            conditions.append(SubCondition({'fieldName': 'type',
                                            'comparator': CompareOperator('Eq'),
                                            'value': interface_type.dump()}))
        if interface_group:
            conditions.append(SubCondition({'fieldName': 'group',
                                            'comparator': CompareOperator('Eq'),
                                            'value': interface_group.dump()}))

        order = SortOrder({'columnName': 'name',
                           'direction': SortDirection(name='Asc'),
                           'caseSensitive': False})
        orderbylist = SortOrderList()
        orderbylist.append(order)

        search_query = SearchQuery({
            'fields': StringList(),
            'conditions': conditions,
            'combining': LogicalOperator('And'),
            'start': 0,
            'limit': UNLIMITED,
            'orderBy': orderbylist})
        (ifaces, count) = self.get(query=search_query, sortByGroup=True)
        # Add results
        for iface in ifaces:
            results.append(Interface(iface))
        return results
