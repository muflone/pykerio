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

from .json_serializable import JSONSerializable

from .structs.ApiException import ApiException
from .structs.LocalizableMessageParameters import LocalizableMessageParameters

from .lists.StringList import StringList


class RPCResponse(JSONSerializable):
    def __init__(self, data: dict):
        self.jsonrpc = data['jsonrpc']
        self.id = data['id']
        if 'error' in data:
            errordata = data['error']['data']['messageParameters']
            messageparameters = LocalizableMessageParameters({
                'positionalParameters': StringList(
                    errordata['positionalParameters']),
                'plurality': errordata['plurality']})

            self.error = ApiException({
                'message': data['error']['message'],
                'code': data['error']['code'],
                'messageParameters': messageparameters})
        else:
            self.error = None
        self.result = data.get('result')

    def dump(self):
        """JSON serializable representation"""
        return {'jsonrpc': self.jsonrpc,
                'id': self.id,
                'error': self.error,
                'result': self.result
               }
