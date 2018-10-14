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


class TestCase_WarningType(unittest.TestCase):
    def test_00_WarningType_WarnBetaVersion(self):
        """
        Test WarningType with WarnBetaVersion
        """
        value = pykerio.enums.WarningType(name='WarnBetaVersion')
        self.assertEquals(value.dump(), 'WarnBetaVersion')
        self.assertEquals(value.get_name(), 'WarnBetaVersion')
        self.assertEquals(value.get_value(), 0)

    def test_01_WarningType_WarnUpdateFailed(self):
        """
        Test WarningType with WarnUpdateFailed
        """
        value = pykerio.enums.WarningType(name='WarnUpdateFailed')
        self.assertEquals(value.dump(), 'WarnUpdateFailed')
        self.assertEquals(value.get_name(), 'WarnUpdateFailed')
        self.assertEquals(value.get_value(), 1)

    def test_02_WarningType_WarnConfigurationReverted(self):
        """
        Test WarningType with WarnConfigurationReverted
        """
        value = pykerio.enums.WarningType(name='WarnConfigurationReverted')
        self.assertEquals(value.dump(), 'WarnConfigurationReverted')
        self.assertEquals(value.get_name(), 'WarnConfigurationReverted')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_WarningType_FAIL(self):
        """
        Test WarningType with FAIL
        """
        value = pykerio.enums.WarningType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
