#/usr/bin/env python
# -*- encoding: utf8 -*-
# author: MartianZ <fzyadmin@gmail.com>

from .base import BaseHandler
import os

class LoginHandler(BaseHandler):
	def get(self):
		self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

	def post(self):
		print "X"
		self.set_secure_cookie("user", self.get_argument("name"))
		self.redirect("/")

handlers = [
	(r"/login", LoginHandler),
	]