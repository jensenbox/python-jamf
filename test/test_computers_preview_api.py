# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.computers_preview_api import ComputersPreviewApi  # noqa: E501
from openapi_client.rest import ApiException


class TestComputersPreviewApi(unittest.TestCase):
    """ComputersPreviewApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.computers_preview_api.ComputersPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_preview_computers_get(self):
        """Test case for preview_computers_get

        Return a list of Computers   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
