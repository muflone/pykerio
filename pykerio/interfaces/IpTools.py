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

from ..enums import ActiveTool
from ..enums import DnsTool
from ..enums import DnsType
from ..enums import IpVersion

from ..lists import StringList


class IpTools(object):
    def __init__(self, api: PyKerio):
        self.api = api

    def getStatus(self):
        response = self.api.request_rpc(
            method='IpTools.getStatus',
            params={})
        active_tool = ActiveTool(name=response.result['activeTool'])
        lines = StringList()
        lines.load(response.result['lines'])
        return (active_tool, lines)

    def stop(self):
        """
        Interrupt currently running tool.
        """
        response = self.api.request_rpc(
            method='IpTools.stop',
            params={})

    def ping(self, target: str, ipversion: IpVersion, infinite: bool,
             packetSize: int, allowFragmentation: bool):
        """
        Execute IpTool Ping
        """
        response = self.api.request_rpc(
            method='IpTools.ping',
            params={'target': target,
                    'ipv': ipversion,
                    'infinite': infinite,
                    'packetSize': packetSize,
                    'allowFragmentation': allowFragmentation})

    def traceRoute(self, target: str, ipversion: IpVersion,
                   resolveHostnames: bool):
        """
        Execute IpTool Traceroute
        """
        response = self.api.request_rpc(
            method='IpTools.traceRoute',
            params={'target': target,
                    'ipv': ipversion,
                    'resolveHostnames': resolveHostnames})

    def whois(self, target: str):
        """
        Execute IpTool Whois
        """
        response = self.api.request_rpc(
            method='IpTools.whois',
            params={'target': target})

    def dns(self, name: str, server: str, tool: DnsTool, dns_type: DnsType):
        """
        Execute IpTool DNS
        """
        response = self.api.request_rpc(
            method='IpTools.dns',
            params={'name': name,
                    'server': server,
                    'tool': tool,
                    'type': dns_type})

    def getDnsServers(self):
        """
        Get DNS servers
        """
        response = self.api.request_rpc(
            method='IpTools.getDnsServers',
            params={})
        results = StringList()
        results.load(response.result['servers'])
        return results
