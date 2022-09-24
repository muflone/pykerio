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


class AuthMethodType(BaseEnumeration):
    WEB = 0
    SSL_WEB = 1
    NTLM = 2
    PROXY = 3
    AUTOMATIC = 4
    VPN_CLIENT = 5
    SSO = 6
    API = 7
    RADIUS = 8
    NONE = 9

    VALUES = {
        'AuthMethodWeb': WEB,
        'AuthMethodSslWeb': SSL_WEB,
        'AuthMethodNtlm': NTLM,
        'AuthMethodProxy': PROXY,
        'AuthMethodAutomatic': AUTOMATIC,
        'AuthMethodVpnClient': VPN_CLIENT,
        'AuthMethodSso': SSO,
        'AuthMethodApi': API,
        'AuthMethodRadius': RADIUS,
        'AuthMethodNone': NONE
    }
