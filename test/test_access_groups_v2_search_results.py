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

import jamf
from jamf.models.access_groups_v2_search_results import AccessGroupsV2SearchResults  # noqa: E501
from jamf.rest import ApiException

class TestAccessGroupsV2SearchResults(unittest.TestCase):
    """AccessGroupsV2SearchResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccessGroupsV2SearchResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.access_groups_v2_search_results.AccessGroupsV2SearchResults()  # noqa: E501
        if include_optional :
            return AccessGroupsV2SearchResults(
                total_count = 10, 
                results = [
                    jamf.models.enrollment_access_group_v2.EnrollmentAccessGroupV2(
                        id = '1', 
                        ldap_server_id = '1', 
                        name = 'Grade School Pupils', 
                        site_id = '1', 
                        enterprise_enrollment_enabled = False, 
                        personal_enrollment_enabled = False, 
                        require_eula = False, )
                    ]
            )
        else :
            return AccessGroupsV2SearchResults(
        )

    def testAccessGroupsV2SearchResults(self):
        """Test AccessGroupsV2SearchResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
