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


class TestCase_ReverseProxyRuleList(unittest.TestCase):
    def test_01_ReverseProxyRuleList(self):
        """
        Test ReverseProxyRuleList
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

        testlist = pykerio.lists.ReverseProxyRuleList()
        self.assertEqual(len(testlist), 0)

        testlist.append(teststruct)
        self.assertEqual(len(testlist), 1)
        self.assertEqual(testlist[-1], teststruct)

        testlist.clear()
        self.assertEqual(len(testlist), 0)
