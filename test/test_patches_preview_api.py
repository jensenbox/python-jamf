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
from jamf.api.patches_preview_api import PatchesPreviewApi  # noqa: E501
from jamf.rest import ApiException


class TestPatchesPreviewApi(unittest.TestCase):
    """PatchesPreviewApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.patches_preview_api.PatchesPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_patch_disclaimer_agree_post(self):
        """Test case for patch_disclaimer_agree_post

        Accept Patch reporting disclaimer   # noqa: E501
        """
        pass

    def test_patch_obj_id_get(self):
        """Test case for patch_obj_id_get

        Return Active Patch Summary   # noqa: E501
        """
        pass

    def test_patch_obj_id_put(self):
        """Test case for patch_obj_id_put

        Update patch report   # noqa: E501
        """
        pass

    def test_patch_obj_id_versions_get(self):
        """Test case for patch_obj_id_versions_get

        Return patch versions   # noqa: E501
        """
        pass

    def test_patch_obj_policy_id_logs_eligible_retry_count_get(self):
        """Test case for patch_obj_policy_id_logs_eligible_retry_count_get

        Return the count of the Patch Policy Logs for the policy is that are eligible for a retry attempt   # noqa: E501
        """
        pass

    def test_patch_obj_policy_id_software_title_configuration_id_get(self):
        """Test case for patch_obj_policy_id_software_title_configuration_id_get

        Return the Software Title Configuration Id for the given patch   # noqa: E501
        """
        pass

    def test_patch_obj_software_title_configuration_id_get(self):
        """Test case for patch_obj_software_title_configuration_id_get

        Return the Software Title Configuration   # noqa: E501
        """
        pass

    def test_patch_obj_software_title_id_policies_get(self):
        """Test case for patch_obj_software_title_id_policies_get

        Return the Summaries of the Patch Policies for the software title   # noqa: E501
        """
        pass

    def test_patch_objs_policy_id_get(self):
        """Test case for patch_objs_policy_id_get

        Return Patch Policy Summary   # noqa: E501
        """
        pass

    def test_patch_on_dashboard_get(self):
        """Test case for patch_on_dashboard_get

        Return list of Patch ids on dashboard   # noqa: E501
        """
        pass

    def test_patch_retry_policy_post(self):
        """Test case for patch_retry_policy_post

        Retry policy   # noqa: E501
        """
        pass

    def test_patch_search_active_patch_history_post(self):
        """Test case for patch_search_active_patch_history_post

        Search the history for a Specific Active Patch   # noqa: E501
        """
        pass

    def test_patch_search_patch_policy_logs_post(self):
        """Test case for patch_search_patch_policy_logs_post

        Return Patch Policy Logs   # noqa: E501
        """
        pass

    def test_patch_svc_retry_policy_post(self):
        """Test case for patch_svc_retry_policy_post

        Retry policy   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
