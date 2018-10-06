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


class NotificationType(BaseEnumeration):
    VALUES = {'NotificationUpdate': 0,
              'NotificationDump': 1,
              'NotificationLowMemory': 2,
              'NotificationDomains': 3,
              'NotificationSubWillExpire': 4,
              'NotificationSubExpired': 5,
              'NotificationLicWillExpire': 6,
              'NotificationLicExpired': 7,
              'NotificationBackupLine': 8,
              'NotificationInterfaceSpeed': 9,
              'NotificationSmtp': 10,
              'NotificationLlbLine': 11,
              'NotificationLlb': 12,
              'NotificationConnectionOnDemand': 13,
              'NotificationConnectionFailover': 14,
              'NotificationConnectionBalancing': 15,
              'NotificationConnectionPersistent': 16,
              'NotificationCertificateError': 17,
              'NotificationCertificateWillExpire': 18,
              'NotificationCertificateExpired': 19,
              'NotificationCaWillExpire': 20,
              'NotificationCaExpired': 21,
              'NotificationBackupFailed': 22,
              'NotificationPacketDump': 23,
              'NotificationUnknown': 24
             }
