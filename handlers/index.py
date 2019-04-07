#/usr/bin/env python
# -*- encoding: utf8 -*-
# author: MartianZ <fzyadmin@gmail.com>

from .base import BaseHandler
import tornado
import os

class IndexHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		articles = []
		file_list = []
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write("Hello, " + name)

handlers = [
	(r"/", IndexHandler),
	]