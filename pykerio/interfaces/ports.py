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

from pykerio.lists.error_list import ErrorList
from pykerio.lists.port_config_list import PortConfigList
from pykerio.pykerio import PyKerio


class Ports(object):
    def __init__(self, api: PyKerio):
        self.api = api

    def get(self):
        """
        Returns list of system ports together with assignments
        """
        response = self.api.request_rpc(
            method='Ports.get',
            params={})
        results = PortConfigList()
        results.load(response.result['list'])
        return results

    def set(self, ports: PortConfigList, revertTimeout: int):
        """
        Stores configuration for system ports
        """
        response = self.api.request_rpc(
            method='Ports.set',
            params={'ports': ports.dump(),
                    'revertTimeout': revertTimeout})
        results = ErrorList()
        results.load(response.result['errors'])
        return results
