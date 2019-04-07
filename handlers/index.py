#/usr/bin/env python
# -*- encoding: utf8 -*-
# author: MartianZ <fzyadmin@gmail.com>

from .base import BaseHandler
import os

class IndexHandler(BaseHandler):
	def get(self):
		articles = []
		file_list = []

		self.write("Hello, world")

handlers = [
	(r"/", IndexHandler),
	]