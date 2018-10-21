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

from ..lists import ErrorList
from ..lists import PortConfigList

from ..structs import PortConfig


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
