import pandas as pd
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .util import executeChallenge

class BaseViewTest(APITestCase):
    client = APIClient()

class TestCalculation(BaseViewTest):

    def test_results(self):

        _id = 0
        _img = "000002b66c9c498e.jpg"
        _x1 = 536
        _y1 = 685
        _x2 = 950
        _y2 = 1005

        _result = executeChallenge(_img,_x1,_y1,_x2,_y2)

        dsDesafio = pd.read_csv("../challenge/test.csv")
        expected = dsDesafio.iloc[0]["result"]        

        self.assertEqual(_result, expected)

