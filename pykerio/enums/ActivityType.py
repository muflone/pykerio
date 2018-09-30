##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
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

from . import BaseEnumeration


class ActivityType(BaseEnumeration):
    VALUES = {'ActivityTypeWeb': 0,
              'ActivityTypeWebSearch': 1,
              'ActivityTypeMail': 2,
              'ActivityTypeDownload': 3,
              'ActivityTypeUpload': 4,
              'ActivityTypeMultimedia': 5,
              'ActivityTypeP2p': 6,
              'ActivityTypeRemoteAccess': 7,
              'ActivityTypeVpn': 8,
              'ActivityTypeInstantMessaging': 9,
              'ActivityTypeHugeConnection': 10,
              'ActivityTypeMailConnection': 11,
              'ActivityTypeP2pAttempt': 12,
              'ActivityTypeWebConnection': 13,
              'ActivityTypeHTTPConnection': 14,
              'ActivityTypeWebMultimedia': 15,
              'ActivityTypeSip': 16,
              'ActivityTypeSocialNetwork': 17
             }
