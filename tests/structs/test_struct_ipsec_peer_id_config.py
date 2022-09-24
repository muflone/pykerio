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


class TestCase_IpsecPeerIdConfig(unittest.TestCase):
    def test_01_IpsecPeerIdConfig(self):
        """
        Test IpsecPeerIdConfig
        """
        local_id = '192.168.10.0'
        secret = 'secretpassword'
        name = 'certificate1'
        certificate = pykerio.structs.IdReference({
            'id': pykerio.types.KId(name),
            'name': name,
            'invalid': False})
        certificatedn = pykerio.structs.CertificateDn({
            'certificate': certificate,
            'value': name})
        certificates = pykerio.lists.CertificateDnList()
        certificates.append(certificatedn)
        teststruct = pykerio.structs.IpsecPeerIdConfig({
            'defaultLocalIdValue': local_id,
            'defaultCipherIke': secret,
            'defaultCipherEsp': secret,
            'certificateDnValues': certificates})
        self.assertEqual(len(teststruct.keys()), 4)
        self.assertEqual(len(teststruct.values()), 4)

        self.assertEqual(teststruct['defaultLocalIdValue'], local_id)
        self.assertEqual(teststruct['defaultCipherIke'], secret)
        self.assertEqual(teststruct['defaultCipherEsp'], secret)
        self.assertEqual(teststruct['certificateDnValues'], certificates)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
