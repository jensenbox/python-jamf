# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.advanced_search_criteria_choices import AdvancedSearchCriteriaChoices  # noqa: E501
from openapi_client.rest import ApiException

class TestAdvancedSearchCriteriaChoices(unittest.TestCase):
    """AdvancedSearchCriteriaChoices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdvancedSearchCriteriaChoices
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.advanced_search_criteria_choices.AdvancedSearchCriteriaChoices()  # noqa: E501
        if include_optional :
            return AdvancedSearchCriteriaChoices(
                choices = ["Option 1","Option 2"]
            )
        else :
            return AdvancedSearchCriteriaChoices(
        )

    def testAdvancedSearchCriteriaChoices(self):
        """Test AdvancedSearchCriteriaChoices"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
