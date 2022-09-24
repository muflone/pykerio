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
        self.assertEqual(len(teststruct.keys()), 20)
        self.assertEqual(len(teststruct.values()), 20)

        self.assertEqual(teststruct['dead'], False)
        self.assertEqual(teststruct['credentials'], credentials)
        self.assertEqual(teststruct['timeout'], timeout)
        self.assertEqual(teststruct['connectTime'], connecttime)
        self.assertEqual(teststruct['noConnectTime'], noconnecttime)
        self.assertEqual(teststruct['rasType'], rastype)
        self.assertEqual(teststruct['mppe'], mppe)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
