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

import unittest

import pykerio


class TestCase_ReverseProxyConfig(unittest.TestCase):
    def test_01_ReverseProxyConfig(self):
        """
        Test ReverseProxyConfig
        """

        enabled = True
        domain = 'domain.com'
        serverHttp = False
        httpsMode = pykerio.enums.HttpsServerMode(
            'HttpsServerModeCustomCertificate')
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

        rule = pykerio.structs.ReverseProxyRule({
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

        rulelist = pykerio.lists.ReverseProxyRuleList()
        rulelist.append(rule)

        teststruct = pykerio.structs.ReverseProxyConfig({
            'enabled': enabled,
            'defaultCertificate': customCertificate,
            'rules': rulelist
        })

        self.assertEquals(len(teststruct.keys()), 3)
        self.assertEquals(len(teststruct.values()), 3)

        self.assertEquals(teststruct['enabled'], enabled)
        self.assertEquals(teststruct['defaultCertificate'], customCertificate)
        self.assertEquals(teststruct['rules'], rulelist)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
