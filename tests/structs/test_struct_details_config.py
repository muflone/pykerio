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


class TestCase_DetailsConfig(unittest.TestCase):
    def test_01_DetailsConfig(self):
        """
        Test DetailsConfig
        """
        positional_parameters = pykerio.lists.StringList()
        positional_parameters.append('User1')
        positional_parameters.append('Foo')

        message = 'Would you want to delete the user %1 (%2)?'
        localizablemessage = pykerio.structs.LocalizableMessage({
            'message': message,
            'positionalParameters': positional_parameters,
            'plurality': 1})
        teststruct = pykerio.structs.DetailsConfig({
            'localizable': False,
            'fixedMessage': message,
            'localizableMessage': localizablemessage})
        self.assertEqual(len(teststruct.keys()), 3)
        self.assertEqual(len(teststruct.values()), 3)

        self.assertEqual(teststruct['localizable'], False)
        self.assertEqual(teststruct['fixedMessage'], message)
        self.assertEqual(teststruct['localizableMessage'], localizablemessage)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
