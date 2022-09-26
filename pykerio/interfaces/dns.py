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

from pykerio.lists.dns_host_list import DnsHostList
from pykerio.lists.error_list import ErrorList
from pykerio.pykerio import PyKerio
from pykerio.structs.dns_config import DnsConfig


class Dns(object):
    def __init__(self, api: PyKerio):
        self.api = api

    def get(self):
        """
        Returns DNS configuration
        """
        response = self.api.request_rpc(
            method='Dns.get',
            params={})
        results = DnsConfig(response.result['config'])
        return results

    def getHosts(self):
        """
        Returns DNS ip/hosts mapping
        """
        response = self.api.request_rpc(
            method='Dns.getHosts',
            params={})
        results = DnsHostList()
        results.load(response.result['hosts'])
        return results

    def set(self, config: DnsConfig):
        """
        Stores DNS configuration
        """
        response = self.api.request_rpc(
            method='Dns.set',
            params={'config': config.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def setHosts(self, hosts: DnsHostList):
        """
        Stores DNS ip/hosts mapping
        """
        response = self.api.request_rpc(
            method='Dns.setHosts',
            params={'hosts': hosts.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results

    def importHosts(self, fileId: str, clean: bool):
        """
        Imports DNS hosts records from file (hosts format)
        """
        self.api.request_rpc(method='Dns.importHosts',
                             params={'fileId': fileId,
                                     'clean': clean})

    def clearCache(self):
        """
        Flushes DNS cache
        """
        self.api.request_rpc(method='Dns.clearCache',
                             params={})
