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

import unittest

import pykerio


class TestCase_NotificationSeverity(unittest.TestCase):
    def test_00_NotificationSeverity_NotificationWarning(self):
        """
        Test NotificationSeverity with NotificationWarning
        """
        value = pykerio.enums.NotificationSeverity(name='NotificationWarning')
        self.assertEquals(value.dump(), 'NotificationWarning')
        self.assertEquals(value.get_name(), 'NotificationWarning')
        self.assertEquals(value.get_value(), 0)

    def test_01_NotificationSeverity_NotificationError(self):
        """
        Test NotificationSeverity with NotificationError
        """
        value = pykerio.enums.NotificationSeverity(name='NotificationError')
        self.assertEquals(value.dump(), 'NotificationError')
        self.assertEquals(value.get_name(), 'NotificationError')
        self.assertEquals(value.get_value(), 1)

    @unittest.expectedFailure
    def test_99_NotificationSeverity_FAIL(self):
        """
        Test NotificationSeverity with FAIL
        """
        value = pykerio.enums.NotificationSeverity(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
