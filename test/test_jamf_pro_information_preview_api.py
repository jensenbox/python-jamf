# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import jamf
from jamf.api.jamf_pro_information_preview_api import JamfProInformationPreviewApi  # noqa: E501
from jamf.rest import ApiException


class TestJamfProInformationPreviewApi(unittest.TestCase):
    """JamfProInformationPreviewApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.jamf_pro_information_preview_api.JamfProInformationPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_jamf_pro_information_get(self):
        """Test case for v1_jamf_pro_information_get

        Get basic information about the Jamf Pro Server   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
