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
from ..json_serializable import JSONSerializable

from ..shared import LoginType
from ..shared import ClientTimestampList

from .ApiApplication import ApiApplication


class Session(JSONSerializable):
    def __init__(self, api: PyKerio):
        self.api = api

    def login(self, userName: str, password: str, application: ApiApplication):
        """
        Log in given user.

        Please note that with a session to one module you cannot use another
        one (eg. with admin session you cannot use webmail).
        """
        response = self.api.request_rpc(
            method='Session.login',
            params={'userName': userName,
                    'password': password,
                    'application': application.dump()
                   })
        self.api.token = response.result['token']

    def logout(self):
        """
        destroys session
        """
        response = self.api.request_rpc(
            method='Session.logout',
            params={})

    def getUserName(self):
        """
        Retrieves name os logged user
        """
        response = self.api.request_rpc(
            method='Session.getUserName',
            params={})
        return response.result['name']

    def getCsrfToken(self):
        """
        Retrieves an unique session ID intended to be used for CSRF protection
        in web forms.
        This ID is different from the session cookie but also remains the same
        during the session lifetime.
        """
        response = self.api.request_rpc(
            method='Session.getCsrfToken',
            params={})
        return response.result['token']

    def getLoginType(self):
        """
        Returns type of login, that has to be performed
        """
        response = self.api.request_rpc(
            method='Session.getLoginType',
            params={})
        return LoginType(response.result['type'])

    def reset(self):
        """
        reset all persistent objects (managers) in session
        """
        response = self.api.request_rpc(
            method='Session.reset',
            params={})

    def setSessionVariable(self, name: str, value: str):
        """
        Stores clients defined variable to configuration for logged user
        """
        response = self.api.request_rpc(
            method='Session.setSessionVariable',
            params={'name': name,
                    'value': value
                   })

    def getSessionVariable(self, name: str):
        """
        Returns clients defined variable stored in configuration for logged user
        """
        response = self.api.request_rpc(
            method='Session.getSessionVariable',
            params={'name': name})
        return response.result['value']

    def getConnectedInterface(self):
        """
        Returns id of interface through which is client connected to server
        """
        response = self.api.request_rpc(
            method='Session.getConnectedInterface',
            params={})
        return response.result['id']

    def getConfigTimestamp(self):
        """
        Reloads configuration and returns timestamp of current configuration
        """
        response = self.api.request_rpc(
            method='Session.getConfigTimestamp',
            params={})
        return ClientTimestampList(response.result['clientTimestampList'])

    # FIXME: needs testing
    def confirmConfig(self, clientTimestampList: ClientTimestampList):
        """
        Confirm the new configuration
        """
        response = self.api.request_rpc(
            method='Session.confirmConfig',
            params={'clientTimestampList': clientTimestampList})
        return response.result['confirmed']
