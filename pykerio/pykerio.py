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

import http.cookiejar
import json
import urllib.request

from .json_serializable import JSONSerializable
from .rpc_response import RPCResponse


class PyKerio(object):
    def __init__(self, server: str, port: int):
        if type(self) == PyKerio:
            raise Exception('<PyKerio> must be subclassed by '
                            'PyKerio(Connect|Operator|Control).')
        self.server = server
        self.port = port
        self.token = None
        # Cookie storage is necessary for session handling
        cookies = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cookies))
        urllib.request.install_opener(opener)

    def request(self, method: str, params: dict):
        """
        Remotely calls given method with given params.
        :param: method string with fully qualified method name
        :param: params dict with parameters of remotely called method
        :param: token CSRF token is always required except login method.
                Use method 'Session.login' to obtain this token.
        """
        request = urllib.request.Request(
            url='https://%s:%d/admin/api/jsonrpc/' % (self.server, self.port)
        )
        request.add_header('Content-Type', 'application/json')
        # Add token if present
        if (self.token is not None):
            request.add_header('X-Token', self.token)
        data = json.dumps({'method': method,
                           'id': 1,
                           'jsonrpc': '2.0',
                           'params': dict((key, value.dump()
                                     if isinstance(value, JSONSerializable)
                                     else value)
                                     for (key, value) in params.items())
                          }).encode()
        httpResponse = urllib.request.urlopen(url=request,
                                              data=data)

        if (httpResponse.status == 200):
            body = httpResponse.read().decode()
            return json.loads(body)

    def request_rpc(self, method: str, params: dict):
        """
        Call a remote request returning a RPCResponse object.
        """
        response = self.request(method=method,
                                params=params)
        response_rpc = RPCResponse(response)
        if response_rpc.error:
            raise Exception(response_rpc.error['message'])
        return response_rpc
