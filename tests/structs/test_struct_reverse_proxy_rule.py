##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Kostiantyn Kostiuk <kostyanf14@live.com>
#   Copyright: 2018-2023 Fabio Castelli
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
from pykerio.enums import HttpsServerMode


class TestCase_ReverseProxyRule(unittest.TestCase):
    def test_01_ReverseProxyRule(self):
        """
        Test ReverseProxyRule
        """
        domain = 'domain.com'
        serverHttp = False
        httpsMode = HttpsServerMode.HttpsServerModeCustomCertificate
        customCertificateId = '66315de7-48b2-b844-81fa-c08f5e0f6144'
        customCertificateInvalid = False
        targetServer = '10.0.0.10'
        targetHttps = True
        antivirus = False
        enabled = True
        description = 'Reverse proxy HTTPS rule for domain.com'
        rule_id = '148'

        customCertificate = pykerio.structs.IdReference({
            'id': customCertificateId,
            'name': domain,
            'invalid': customCertificateInvalid
        })

        teststruct = pykerio.structs.ReverseProxyRule({
            'serverHostname': domain,
            'serverHttp': serverHttp,
            'httpsMode': httpsMode,
            'customCertificate': customCertificate,
            'targetServer': targetServer,
            'targetHttps': targetHttps,
            'antivirus': antivirus,
            'enabled': enabled,
            'description': description,
            'id': rule_id
        })
        self.assertEqual(len(teststruct.keys()), 10)
        self.assertEqual(len(teststruct.values()), 10)

        self.assertEqual(teststruct['serverHostname'], domain)
        self.assertEqual(teststruct['serverHttp'], serverHttp)
        self.assertEqual(teststruct['httpsMode'], httpsMode)
        self.assertEqual(teststruct['customCertificate'], customCertificate)
        self.assertEqual(teststruct['targetServer'], targetServer)
        self.assertEqual(teststruct['targetHttps'], targetHttps)
        self.assertEqual(teststruct['antivirus'], antivirus)
        self.assertEqual(teststruct['description'], description)
        self.assertEqual(teststruct['id'], rule_id)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
