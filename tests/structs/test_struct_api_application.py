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

import pykerio


class TestCase_ApiApplication(unittest.TestCase):
    def test_01_ApiApplication(self):
        """
        Test ApiApplication
        """
        teststruct = pykerio.structs.ApiApplication({
            'name': pykerio.constants.APP_NAME,
            'vendor': pykerio.constants.APP_AUTHOR,
            'version': pykerio.constants.APP_VERSION})
        self.assertEqual(len(teststruct.keys()), 3)
        self.assertEqual(len(teststruct.values()), 3)

        self.assertEqual(teststruct['name'], pykerio.constants.APP_NAME)
        self.assertEqual(teststruct['vendor'], pykerio.constants.APP_AUTHOR)
        self.assertEqual(teststruct['version'], pykerio.constants.APP_VERSION)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
