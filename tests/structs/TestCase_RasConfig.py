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

import unittest

import pykerio


class TestCase_RasConfig(unittest.TestCase):
    def test_01_RasConfig(self):
        """
        Test RasConfig
        """
        credentials = pykerio.structs.CredentialsConfig({
            'userName': pykerio.constants.APP_AUTHOR,
            'password': 'something',
            'passwordChanged': False})
        timeout = pykerio.structs.OptionalLong({'enabled': True,
                                                'value': 123})
        enabled = True
        kid = pykerio.types.KId('Object name')
        name = 'Object name'
        connecttime = pykerio.structs.OptionalEntity({
            'enabled': True,
            'id': pykerio.types.KId('Work hours'),
            'name': 'Work hours'})
        noconnecttime = pykerio.structs.OptionalEntity({
            'enabled': False,
            'id': pykerio.types.KId(''),
            'name': ''})
        rastype = pykerio.enums.RasType(name='PPPoE')
        mppe = pykerio.enums.MppeType(name='MppeEnabled')
        teststruct = pykerio.structs.RasConfig({'dead': False,
                                                'entryName': 'RAS Work',
                                                'useOwnCredentials': True,
                                                'credentials': credentials,
                                                'timeout': timeout,
                                                'connectTime': connecttime,
                                                'noConnectTime': noconnecttime,
                                                'bdScriptEnabled': True,
                                                'adScriptEnabled': True,
                                                'bhScriptEnabled': True,
                                                'ahScriptEnabled': True,
                                                'rasType': rastype,
                                                'pppoeIfaceId': '1',
                                                'server': 'server1',
                                                'papEnabled': False,
                                                'chapEnabled': False,
                                                'mschapEnabled': False,
                                                'mschapv2Enabled': False,
                                                'mppe': mppe,
                                                'mppeStateful': True})
        self.assertEquals(len(teststruct.keys()), 20)
        self.assertEquals(len(teststruct.values()), 20)

        self.assertEquals(teststruct['dead'], False)
        self.assertEquals(teststruct['credentials'], credentials)
        self.assertEquals(teststruct['timeout'], timeout)
        self.assertEquals(teststruct['connectTime'], connecttime)
        self.assertEquals(teststruct['noConnectTime'], noconnecttime)
        self.assertEquals(teststruct['rasType'], rastype)
        self.assertEquals(teststruct['mppe'], mppe)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
