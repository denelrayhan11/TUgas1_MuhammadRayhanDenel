from django.test import TestCase

class testurls(TestCase):
    def test_show_mywatchlisthtml_url(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEquals(response.status_code,200)

    def test_show_mywatchlistxml_url(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEquals(response.status_code,200)

    def test_show_mywatchlistjson_url(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEquals(response.status_code,200)

# Create your tests here.
