#/usr/bin/env python
# -*- encoding: utf8 -*-
# author: MartianZ <fzyadmin@gmail.com>

from .base import BaseHandler

class NotFoundHandler(BaseHandler):
	def prepare(self):
		pass
		
	def get(self):
		self.write("")

handlers = [
	(r"/.*", NotFoundHandler),
	]