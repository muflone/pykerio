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

import unittest

from pykerio.enums import Entity


class TestCase_Entity(unittest.TestCase):
    def test_00_EntityUser(self):
        """
        Test Entity with EntityUser
        """
        value = Entity.EntityUser
        self.assertEqual(value.dump(), 'EntityUser')
        self.assertEqual(value.name, 'EntityUser')
        self.assertEqual(value.value, 0)

    def test_01_EntityAlias(self):
        """
        Test Entity with EntityAlias
        """
        value = Entity.EntityAlias
        self.assertEqual(value.dump(), 'EntityAlias')
        self.assertEqual(value.name, 'EntityAlias')
        self.assertEqual(value.value, 1)

    def test_02_EntityGroup(self):
        """
        Test Entity with EntityGroup
        """
        value = Entity.EntityGroup
        self.assertEqual(value.dump(), 'EntityGroup')
        self.assertEqual(value.name, 'EntityGroup')
        self.assertEqual(value.value, 2)

    def test_03_EntityMailingList(self):
        """
        Test Entity with EntityMailingList
        """
        value = Entity.EntityMailingList
        self.assertEqual(value.dump(), 'EntityMailingList')
        self.assertEqual(value.name, 'EntityMailingList')
        self.assertEqual(value.value, 3)

    def test_04_EntityResource(self):
        """
        Test Entity with EntityResource
        """
        value = Entity.EntityResource
        self.assertEqual(value.dump(), 'EntityResource')
        self.assertEqual(value.name, 'EntityResource')
        self.assertEqual(value.value, 4)

    def test_05_EntityTimeRange(self):
        """
        Test Entity with EntityTimeRange
        """
        value = Entity.EntityTimeRange
        self.assertEqual(value.dump(), 'EntityTimeRange')
        self.assertEqual(value.name, 'EntityTimeRange')
        self.assertEqual(value.value, 5)

    def test_06_EntityTimeRangeGroup(self):
        """
        Test Entity with EntityTimeRangeGroup
        """
        value = Entity.EntityTimeRangeGroup
        self.assertEqual(value.dump(), 'EntityTimeRangeGroup')
        self.assertEqual(value.name, 'EntityTimeRangeGroup')
        self.assertEqual(value.value, 6)

    def test_07_EntityIpAddress(self):
        """
        Test Entity with EntityIpAddress
        """
        value = Entity.EntityIpAddress
        self.assertEqual(value.dump(), 'EntityIpAddress')
        self.assertEqual(value.name, 'EntityIpAddress')
        self.assertEqual(value.value, 7)

    def test_08_EntityIpAddressGroup(self):
        """
        Test Entity with EntityIpAddressGroup
        """
        value = Entity.EntityIpAddressGroup
        self.assertEqual(value.dump(), 'EntityIpAddressGroup')
        self.assertEqual(value.name, 'EntityIpAddressGroup')
        self.assertEqual(value.value, 8)

    def test_09_EntityService(self):
        """
        Test Entity with EntityService
        """
        value = Entity.EntityService
        self.assertEqual(value.dump(), 'EntityService')
        self.assertEqual(value.name, 'EntityService')
        self.assertEqual(value.value, 9)

    def test_10_EntityDomain(self):
        """
        Test Entity with EntityDomain
        """
        value = Entity.EntityDomain
        self.assertEqual(value.dump(), 'EntityDomain')
        self.assertEqual(value.name, 'EntityDomain')
        self.assertEqual(value.value, 10)
