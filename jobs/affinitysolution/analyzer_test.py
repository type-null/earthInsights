"""
test analyzer

"""

import json
import unittest
import pandas as pd
import analyzer


class TestMyModule(unittest.TestCase):

    def setUp(self):
        return

    def test_process(self):
        # read homework sheet
        df = pd.read_excel('data.xlsx', sheet_name='Transaction Description')

        # test for each row
        for i in range(len(df)):
            # result = analyzer.process(df["Input"][i])
            expected_result = json.loads(df["Output"][i])
            # self.assertEqual(result, expected_result)
