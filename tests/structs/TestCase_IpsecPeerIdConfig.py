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
        self.assertEquals(len(teststruct.keys()), 4)
        self.assertEquals(len(teststruct.values()), 4)

        self.assertEquals(teststruct['defaultLocalIdValue'], local_id)
        self.assertEquals(teststruct['defaultCipherIke'], secret)
        self.assertEquals(teststruct['defaultCipherEsp'], secret)
        self.assertEquals(teststruct['certificateDnValues'], certificates)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
