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


class TestCase_NtpUpdatePhase(unittest.TestCase):
    def test_00_NtpUpdatePhase_NtpUpdateDisabled(self):
        """
        Test NtpUpdatePhase with NtpUpdateDisabled
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateDisabled')
        self.assertEquals(value.dump(), 'NtpUpdateDisabled')
        self.assertEquals(value.get_name(), 'NtpUpdateDisabled')
        self.assertEquals(value.get_value(), 0)

    def test_01_NtpUpdatePhase_NtpUpdateOk(self):
        """
        Test NtpUpdatePhase with NtpUpdateOk
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateOk')
        self.assertEquals(value.dump(), 'NtpUpdateOk')
        self.assertEquals(value.get_name(), 'NtpUpdateOk')
        self.assertEquals(value.get_value(), 1)

    def test_02_NtpUpdatePhase_NtpUpdateError(self):
        """
        Test NtpUpdatePhase with NtpUpdateError
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateError')
        self.assertEquals(value.dump(), 'NtpUpdateError')
        self.assertEquals(value.get_name(), 'NtpUpdateError')
        self.assertEquals(value.get_value(), 2)

    def test_03_NtpUpdatePhase_NtpUpdateProgress(self):
        """
        Test NtpUpdatePhase with NtpUpdateProgress
        """
        value = pykerio.enums.NtpUpdatePhase(name='NtpUpdateProgress')
        self.assertEquals(value.dump(), 'NtpUpdateProgress')
        self.assertEquals(value.get_name(), 'NtpUpdateProgress')
        self.assertEquals(value.get_value(), 3)

    @unittest.expectedFailure
    def test_99_NtpUpdatePhase_FAIL(self):
        """
        Test NtpUpdatePhase with FAIL
        """
        value = pykerio.enums.NtpUpdatePhase(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
