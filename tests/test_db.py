# -*- coding: UTF-8 -*-

import unittest
from datetime import datetime

from args import ARGS

import oerplib


class TestDB(unittest.TestCase):

    def setUp(self):
        self.oerp = oerplib.OERP(ARGS.server)

    def test_db_list(self):
        res = self.oerp.db.list()
        self.assertIsInstance(res, list)

    def test_db_list_lang(self):
        res = self.oerp.db.list_lang()
        self.assertIsInstance(res, list)

    def test_db_dump(self):
        dump = self.oerp.db.dump(ARGS.super_admin_passwd, ARGS.database)
        self.assertIsNotNone(dump)

    def test_db_restore_new_database(self):
        dump = self.oerp.db.dump(ARGS.super_admin_passwd, ARGS.database)
        new_database = "%s_%s" % (ARGS.database, datetime.today())
        self.oerp.db.restore(ARGS.super_admin_passwd, new_database, dump)

    def test_db_restore_existing_database(self):
        dump = self.oerp.db.dump(ARGS.super_admin_passwd, ARGS.database)
        self.assertRaises(
                oerplib.error.Error,
                self.oerp.db.restore,
                ARGS.super_admin_passwd, ARGS.database, dump)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
