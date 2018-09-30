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

import pykerio.enums


class TestCase_ConnectionDirection(unittest.TestCase):
    def test_01_ConnectionDirection_ConnectionDirectionInbound(self):
        """
        Test ConnectionDirection with ConnectionDirectionInbound
        """
        value = pykerio.enums.ConnectionDirection(value='ConnectionDirectionInbound')
        self.assertEquals(value.value, 'ConnectionDirectionInbound')
        self.assertEquals(value.dump(), 'ConnectionDirectionInbound')

    def test_02_ConnectionDirection_ConnectionDirectionOutbound(self):
        """
        Test ConnectionDirection with ConnectionDirectionOutbound
        """
        value = pykerio.enums.ConnectionDirection(value='ConnectionDirectionOutbound')
        self.assertEquals(value.value, 'ConnectionDirectionOutbound')
        self.assertEquals(value.dump(), 'ConnectionDirectionOutbound')


    def test_03_ConnectionDirection_ConnectionDirectionLocal(self):
        """
        Test ConnectionDirection with ConnectionDirectionLocal
        """
        value = pykerio.enums.ConnectionDirection(value='ConnectionDirectionLocal')
        self.assertEquals(value.value, 'ConnectionDirectionLocal')
        self.assertEquals(value.dump(), 'ConnectionDirectionLocal')

    @unittest.expectedFailure
    def test_99_ConnectionDirection_FAIL(self):
        """
        Test ConnectionDirection with FAIL
        """
        value = pykerio.enums.ConnectionDirection(value='FAIL')
        self.assertEquals(value.value, 'FAIL')
        self.assertEquals(value.dump(), 'FAIL')
