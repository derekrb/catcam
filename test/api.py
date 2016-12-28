from test import Test


class API(Test):

    def test_ping(self):
        r = self.app.get('/ping')
        self.assertEqual(200, r.status_code)
