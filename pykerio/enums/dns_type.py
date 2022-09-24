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

from .base_enumeration import BaseEnumeration


class DnsType(BaseEnumeration):
    ANY = 0
    A = 1
    AAAA = 2
    CNAME = 3
    MX = 4
    NS = 5
    PTR = 6
    SOA = 7
    SPF = 8
    SRV = 9
    TXT = 10

    VALUES = {
        'DnsTypeAny': ANY,
        'DnsTypeA': A,
        'DnsTypeAAAA': AAAA,
        'DnsTypeCname': CNAME,
        'DnsTypeMx': MX,
        'DnsTypeNs': NS,
        'DnsTypePtr': PTR,
        'DnsTypeSoa': SOA,
        'DnsTypeSpf': SPF,
        'DnsTypeSrv': SRV,
        'DnsTypeTxt': TXT
    }
