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


class NotificationType(BaseEnumeration):
    UPDATE = 0
    DUMP = 1
    LOW_MEMORY = 2
    DOMAINS = 3
    SUB_WILL_EXPIRE = 4
    SUB_EXPIRED = 5
    LIC_WILL_EXPIRE = 6
    LIC_EXPIRED = 7
    BACKUP_LINE = 8
    INTERFACE_SPEED = 9
    SMTP = 10
    LLB_LINE = 11
    LLB = 12
    CONNECTION_ON_DEMAND = 13
    CONNECTION_FAILOVER = 14
    CONNECTION_BALANCING = 15
    CONNECTION_PERSISTENT = 16
    CERTIFICATE_ERROR = 17
    CERTIFICATE_WILL_EXPIRE = 18
    CERTIFICATE_EXPIRED = 19
    CA_WILL_EXPIRE = 20
    CA_EXPIRED = 21
    BACKUP_FAILED = 22
    PACKET_DUMP = 23
    UNKNOWN = 24

    VALUES = {
        'NotificationUpdate': UPDATE,
        'NotificationDump': DUMP,
        'NotificationLowMemory': LOW_MEMORY,
        'NotificationDomains': DOMAINS,
        'NotificationSubWillExpire': SUB_WILL_EXPIRE,
        'NotificationSubExpired': SUB_EXPIRED,
        'NotificationLicWillExpire': LIC_WILL_EXPIRE,
        'NotificationLicExpired': LIC_EXPIRED,
        'NotificationBackupLine': BACKUP_LINE,
        'NotificationInterfaceSpeed': INTERFACE_SPEED,
        'NotificationSmtp': SMTP,
        'NotificationLlbLine': LLB_LINE,
        'NotificationLlb': LLB,
        'NotificationConnectionOnDemand': CONNECTION_ON_DEMAND,
        'NotificationConnectionFailover': CONNECTION_FAILOVER,
        'NotificationConnectionBalancing': CONNECTION_BALANCING,
        'NotificationConnectionPersistent': CONNECTION_PERSISTENT,
        'NotificationCertificateError': CERTIFICATE_ERROR,
        'NotificationCertificateWillExpire': CERTIFICATE_WILL_EXPIRE,
        'NotificationCertificateExpired': CERTIFICATE_EXPIRED,
        'NotificationCaWillExpire': CA_WILL_EXPIRE,
        'NotificationCaExpired': CA_EXPIRED,
        'NotificationBackupFailed': BACKUP_FAILED,
        'NotificationPacketDump': PACKET_DUMP,
        'NotificationUnknown': UNKNOWN
    }
