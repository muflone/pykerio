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


class TestCase_DnsHost(unittest.TestCase):
    def test_01_DnsHost(self):
        """
        Test DnsHost
        """
        kid = pykerio.types.KId('10')
        ip = pykerio.types.IpAddress('8.8.8.8')
        hosts = 'dns.google.com'
        teststruct = pykerio.structs.DnsHost({
            'enabled': True,
            'id': kid,
            'ip': ip,
            'hosts': hosts,
            'description': 'Google public DNS'})
        self.assertEquals(len(teststruct.keys()), 5)
        self.assertEquals(len(teststruct.values()), 5)

        self.assertEquals(teststruct['id'], kid)
        self.assertEquals(teststruct['ip'], ip)
        self.assertEquals(teststruct['hosts'], hosts)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
