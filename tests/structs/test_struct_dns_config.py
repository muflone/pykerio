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


class TestCase_DnsConfig(unittest.TestCase):
    def test_01_DnsConfig(self):
        """
        Test DnsConfig
        """
        forwarder = pykerio.structs.DnsForwarder({'enabled': True,
                                                  'domain': 'muflone.com',
                                                  'forwarders': '8.8.8.8'})
        customForwarders = pykerio.lists.DnsForwarderList()
        customForwarders.append(forwarder)
        useDomainController = pykerio.structs.OptionalString({
            'enabled': True,
            'value': 'muflone.com'})

        teststruct = pykerio.structs.DnsConfig({
            'forwarderEnabled': True,
            'cacheEnabled': True,
            'customForwardingEnabled': True,
            'customForwarders': customForwarders,
            'useDomainControler': useDomainController,
            'hostsEnabled': True,
            'dhcpLookupEnabled': True,
            'domainName': 'muflone.com'})
        self.assertEqual(len(teststruct.keys()), 8)
        self.assertEqual(len(teststruct.values()), 8)

        self.assertEqual(teststruct['customForwarders'], customForwarders)
        self.assertEqual(teststruct['useDomainControler'], useDomainController)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
