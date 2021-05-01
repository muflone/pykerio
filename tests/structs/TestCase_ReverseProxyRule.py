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


class TestCase_ReverseProxyRule(unittest.TestCase):
    def test_01_ReverseProxyRule(self):
        """
        Test ReverseProxyRule
        """

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

        teststruct = pykerio.structs.ReverseProxyRule(
            {
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

        self.assertEquals(len(teststruct.keys()), 10)
        self.assertEquals(len(teststruct.values()), 10)

        self.assertEquals(teststruct['serverHostname'], domain)
        self.assertEquals(teststruct['serverHttp'], serverHttp)
        self.assertEquals(teststruct['httpsMode'], httpsMode)
        self.assertEquals(teststruct['customCertificate'], customCertificate)
        self.assertEquals(teststruct['targetServer'], targetServer)
        self.assertEquals(teststruct['targetHttps'], targetHttps)
        self.assertEquals(teststruct['antivirus'], antivirus)
        self.assertEquals(teststruct['description'], description)
        self.assertEquals(teststruct['id'], rule_id)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
