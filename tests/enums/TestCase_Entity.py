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


class TestCase_Entity(unittest.TestCase):
    def test_00_Entity_EntityUser(self):
        """
        Test Entity with EntityUser
        """
        value = pykerio.enums.Entity(name='EntityUser')
        self.assertEquals(value.dump(), 'EntityUser')
        self.assertEquals(value.get_name(), 'EntityUser')
        self.assertEquals(value.get_value(), 0)

    def test_01_Entity_EntityAlias(self):
        """
        Test Entity with EntityAlias
        """
        value = pykerio.enums.Entity(name='EntityAlias')
        self.assertEquals(value.dump(), 'EntityAlias')
        self.assertEquals(value.get_name(), 'EntityAlias')
        self.assertEquals(value.get_value(), 1)

    def test_02_Entity_EntityGroup(self):
        """
        Test Entity with EntityGroup
        """
        value = pykerio.enums.Entity(name='EntityGroup')
        self.assertEquals(value.dump(), 'EntityGroup')
        self.assertEquals(value.get_name(), 'EntityGroup')
        self.assertEquals(value.get_value(), 2)

    def test_03_Entity_EntityMailingList(self):
        """
        Test Entity with EntityMailingList
        """
        value = pykerio.enums.Entity(name='EntityMailingList')
        self.assertEquals(value.dump(), 'EntityMailingList')
        self.assertEquals(value.get_name(), 'EntityMailingList')
        self.assertEquals(value.get_value(), 3)

    def test_04_Entity_EntityResource(self):
        """
        Test Entity with EntityResource
        """
        value = pykerio.enums.Entity(name='EntityResource')
        self.assertEquals(value.dump(), 'EntityResource')
        self.assertEquals(value.get_name(), 'EntityResource')
        self.assertEquals(value.get_value(), 4)

    def test_05_Entity_EntityTimeRange(self):
        """
        Test Entity with EntityTimeRange
        """
        value = pykerio.enums.Entity(name='EntityTimeRange')
        self.assertEquals(value.dump(), 'EntityTimeRange')
        self.assertEquals(value.get_name(), 'EntityTimeRange')
        self.assertEquals(value.get_value(), 5)

    def test_06_Entity_EntityTimeRangeGroup(self):
        """
        Test Entity with EntityTimeRangeGroup
        """
        value = pykerio.enums.Entity(name='EntityTimeRangeGroup')
        self.assertEquals(value.dump(), 'EntityTimeRangeGroup')
        self.assertEquals(value.get_name(), 'EntityTimeRangeGroup')
        self.assertEquals(value.get_value(), 6)

    def test_07_Entity_EntityIpAddress(self):
        """
        Test Entity with EntityIpAddress
        """
        value = pykerio.enums.Entity(name='EntityIpAddress')
        self.assertEquals(value.dump(), 'EntityIpAddress')
        self.assertEquals(value.get_name(), 'EntityIpAddress')
        self.assertEquals(value.get_value(), 7)

    def test_08_Entity_EntityIpAddressGroup(self):
        """
        Test Entity with EntityIpAddressGroup
        """
        value = pykerio.enums.Entity(name='EntityIpAddressGroup')
        self.assertEquals(value.dump(), 'EntityIpAddressGroup')
        self.assertEquals(value.get_name(), 'EntityIpAddressGroup')
        self.assertEquals(value.get_value(), 8)

    def test_09_Entity_EntityService(self):
        """
        Test Entity with EntityService
        """
        value = pykerio.enums.Entity(name='EntityService')
        self.assertEquals(value.dump(), 'EntityService')
        self.assertEquals(value.get_name(), 'EntityService')
        self.assertEquals(value.get_value(), 9)

    def test_10_Entity_EntityDomain(self):
        """
        Test Entity with EntityDomain
        """
        value = pykerio.enums.Entity(name='EntityDomain')
        self.assertEquals(value.dump(), 'EntityDomain')
        self.assertEquals(value.get_name(), 'EntityDomain')
        self.assertEquals(value.get_value(), 10)

    @unittest.expectedFailure
    def test_99_Entity_FAIL(self):
        """
        Test Entity with FAIL
        """
        value = pykerio.enums.Entity(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
