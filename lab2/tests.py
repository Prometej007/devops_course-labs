#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import unittest 
from app import *


class TestClass(unittest.TestCase):
    def setUp(self):
       	self.date_url='http://date.jsontest.com/'
       	self.ip_url='http://ip.jsontest.com/'
       	self.pm_time='23:23:23 PM'
       	self.am_time='09:09:09 AM'
       	self.wrong_time='123123123123'

    def test_date_work_successfully(self):
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        self.assertFalse(main())

    def test_no_date_in_response(self):
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
       	self.assertTrue(home_work(self.pm_time)==True)
       	self.assertTrue(home_work(self.am_time)==True)
       	self.assertTrue(home_work(self.wrong_time)==False)
