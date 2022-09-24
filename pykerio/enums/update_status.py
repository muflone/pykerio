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


class UpdateStatus(BaseEnumeration):
    OK = 0
    CHECKING = 1
    CHECK_FAILED = 2
    DOWNLOAD_OK = 3
    DOWNLOADING = 4
    DOWNLOAD_FAILED = 5
    UPGRADING = 6
    UPGRADE_FAILED = 7

    VALUES = {
        'UpdateStatusOk': OK,
        'UpdateStatusChecking': CHECKING,
        'UpdateStatusCheckFailed': CHECK_FAILED,
        'UpdateStatusDownloadOk': DOWNLOAD_OK,
        'UpdateStatusDownloading': DOWNLOADING,
        'UpdateStatusDownloadFailed': DOWNLOAD_FAILED,
        'UpdateStatusUpgrading': UPGRADING,
        'UpdateStatusUpgradeFailed': UPGRADE_FAILED
    }
