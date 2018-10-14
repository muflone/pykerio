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


class TestCase_SeverityUnit(unittest.TestCase):
    def test_00_SeverityUnit_SeverityEmergency(self):
        """
        Test SeverityUnit with SeverityEmergency
        """
        value = pykerio.enums.SeverityUnit(name='SeverityEmergency')
        self.assertEquals(value.dump(), 'SeverityEmergency')
        self.assertEquals(value.get_name(), 'SeverityEmergency')
        self.assertEquals(value.get_value(), 0)

    def test_01_SeverityUnit_SeverityAlert(self):
        """
        Test SeverityUnit with SeverityAlert
        """
        value = pykerio.enums.SeverityUnit(name='SeverityAlert')
        self.assertEquals(value.dump(), 'SeverityAlert')
        self.assertEquals(value.get_name(), 'SeverityAlert')
        self.assertEquals(value.get_value(), 1)

    def test_02_SeverityUnit_SeverityCritical(self):
        """
        Test SeverityUnit with SeverityCritical
        """
        value = pykerio.enums.SeverityUnit(name='SeverityCritical')
        self.assertEquals(value.dump(), 'SeverityCritical')
        self.assertEquals(value.get_name(), 'SeverityCritical')
        self.assertEquals(value.get_value(), 2)

    def test_03_SeverityUnit_SeverityError(self):
        """
        Test SeverityUnit with SeverityError
        """
        value = pykerio.enums.SeverityUnit(name='SeverityError')
        self.assertEquals(value.dump(), 'SeverityError')
        self.assertEquals(value.get_name(), 'SeverityError')
        self.assertEquals(value.get_value(), 3)

    def test_04_SeverityUnit_SeverityWarning(self):
        """
        Test SeverityUnit with SeverityWarning
        """
        value = pykerio.enums.SeverityUnit(name='SeverityWarning')
        self.assertEquals(value.dump(), 'SeverityWarning')
        self.assertEquals(value.get_name(), 'SeverityWarning')
        self.assertEquals(value.get_value(), 4)

    def test_05_SeverityUnit_SeverityNotice(self):
        """
        Test SeverityUnit with SeverityNotice
        """
        value = pykerio.enums.SeverityUnit(name='SeverityNotice')
        self.assertEquals(value.dump(), 'SeverityNotice')
        self.assertEquals(value.get_name(), 'SeverityNotice')
        self.assertEquals(value.get_value(), 5)

    def test_06_SeverityUnit_SeverityInformational(self):
        """
        Test SeverityUnit with SeverityInformational
        """
        value = pykerio.enums.SeverityUnit(name='SeverityInformational')
        self.assertEquals(value.dump(), 'SeverityInformational')
        self.assertEquals(value.get_name(), 'SeverityInformational')
        self.assertEquals(value.get_value(), 6)

    def test_07_SeverityUnit_SeverityDebug(self):
        """
        Test SeverityUnit with SeverityDebug
        """
        value = pykerio.enums.SeverityUnit(name='SeverityDebug')
        self.assertEquals(value.dump(), 'SeverityDebug')
        self.assertEquals(value.get_name(), 'SeverityDebug')
        self.assertEquals(value.get_value(), 7)

    @unittest.expectedFailure
    def test_99_SeverityUnit_FAIL(self):
        """
        Test SeverityUnit with FAIL
        """
        value = pykerio.enums.SeverityUnit(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
