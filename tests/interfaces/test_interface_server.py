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

import os
import ssl
import unittest

import pykerio
from pykerio.enums import ServerOs


class TestCase_Server(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Prepares session
        """
        # Ignore invalid certificates
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        # API object
        api = pykerio.PyKerioControl(
            server=os.environ.get('KERIO_SERVER', 'control-demo.kerio.com'),
            port=int(os.environ.get('KERIO_PORT', '4081')))
        # ApiApplication object
        application = pykerio.structs.ApiApplication({
            'name': cls.__name__,
            'vendor': pykerio.constants.APP_NAME,
            'version': pykerio.constants.APP_VERSION})

        # Session login
        cls.session = pykerio.interfaces.Session(api)
        cls.session.login(userName=os.environ.get('KERIO_USERNAME',
                                                  'admin-en'),
                          password=os.environ.get('KERIO_PASSWORD',
                                                  'kerio'),
                          application=application)

        # Server
        cls.server = pykerio.interfaces.Server(api)

    @classmethod
    def tearDownClass(cls):
        """
        Closes session
        """
        cls.session.logout()

    def test_01_getOs(self):
        """
        Test Server getOs
        """
        server_os = self.__class__.server.getOs()
        self.assertEqual(server_os.dump(), ServerOs.Linux.name)

    def test_02_getRestrictionList(self):
        """
        Test Server getRestrictionList
        """
        restrictions_list = self.__class__.server.getRestrictionList()
        self.assertNotEqual(len(restrictions_list), 0)
        for restriction in restrictions_list:
            self.assertEqual(type(restriction), pykerio.structs.Restriction)
