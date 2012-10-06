# -*- coding: utf-8 -*-


from urllib import urlencode
from urllib2 import urlopen, HTTPError
from json import loads

from logging import log

from module.common import APIExerciser

url = "http://localhost:8001/api/%s"

class TestBackends():

    def setUp(self):
        u = urlopen(url % "login", data=urlencode({"username": "TestUser", "password": "sometestpw"}))
        self.key = loads(u.read())
        assert self.key is not False

    def test_random(self):
        api = APIExerciser.APIExerciser(None, True, "TestUser", "sometestpw")

        assert api.api.login("crapp", "wrong pw") is False

        for i in range(0, 1000):
            api.testAPI()

    def call(self, name, post=None):
        if not post: post = {}
        post["session"] = self.key
        u = urlopen(url % name, data=urlencode(post))
        return loads(u.read())

    def test_wronglogin(self):
        u = urlopen(url % "login", data=urlencode({"username": "crap", "password": "wrongpw"}))
        assert loads(u.read()) is False

    def test_access(self):
        try:
            urlopen(url % "getServerVersion")
        except HTTPError, e:
            assert e.code == 403
        else:
            assert False

    def test_status(self):
        ret = self.call("statusServer")
        log(1, str(ret))
        assert "pause" in ret
        assert "queue" in ret

    def test_unknown_method(self):
        try:
            self.call("notExisting")
        except HTTPError, e:
            assert e.code == 404
        else:
            assert False