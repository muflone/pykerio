##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
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

from ..structs import ReverseProxyConfig


class ReverseProxy(object):
    def __init__(self, api: PyKerio):
        self.api = api

    def get(self):
        """
        Returns configuration for reverse proxy
        """
        response = self.api.request_rpc(
            method='ReverseProxy.get',
            params={})
        results = ReverseProxyConfig(response.result['config'])
        return results

    def set(self, config: ReverseProxyConfig):
        """
        Stores configuration for reverse proxy
        """
        response = self.api.request_rpc(
            method='ReverseProxy.set',
            params={'config': config.dump()})
        results = ErrorList()
        results.load(response.result['errors'])
        return results
