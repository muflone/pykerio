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

from . import BaseEnumeration


class ActivityType(BaseEnumeration):
    WEB = 0
    WEB_SEARCH = 1
    MAIL = 2
    DOWNLOAD = 3
    UPLOAD = 4
    MULTIMEDIA = 5
    P2P = 6
    REMOTE_ACCESS = 7
    VPN = 8
    INSTANT_MESSAGING = 9
    HUGE_CONNECTION = 10
    MAIL_CONNECTION = 11
    P2P_ATTEMPT = 12
    WEB_CONNECTION = 13
    HTTP_CONNECTION = 14
    WEB_MULTIMEDIA = 15
    SIP = 16
    SOCIAL_NETWORK = 17

    VALUES = {
        'ActivityTypeWeb': WEB,
        'ActivityTypeWebSearch': WEB_SEARCH,
        'ActivityTypeMail': MAIL,
        'ActivityTypeDownload': DOWNLOAD,
        'ActivityTypeUpload': UPLOAD,
        'ActivityTypeMultimedia': MULTIMEDIA,
        'ActivityTypeP2p': P2P,
        'ActivityTypeRemoteAccess': REMOTE_ACCESS,
        'ActivityTypeVpn': VPN,
        'ActivityTypeInstantMessaging': INSTANT_MESSAGING,
        'ActivityTypeHugeConnection': HUGE_CONNECTION,
        'ActivityTypeMailConnection': MAIL_CONNECTION,
        'ActivityTypeP2pAttempt': P2P_ATTEMPT,
        'ActivityTypeWebConnection': WEB_CONNECTION,
        'ActivityTypeHTTPConnection': HTTP_CONNECTION,
        'ActivityTypeWebMultimedia': WEB_MULTIMEDIA,
        'ActivityTypeSip': SIP,
        'ActivityTypeSocialNetwork': SOCIAL_NETWORK
    }
