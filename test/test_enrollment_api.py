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
from openapi_client.api.enrollment_api import EnrollmentApi  # noqa: E501
from openapi_client.rest import ApiException


class TestEnrollmentApi(unittest.TestCase):
    """EnrollmentApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.enrollment_api.EnrollmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_enrollment_access_groups_get(self):
        """Test case for v1_enrollment_access_groups_get

        Retrieve the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_access_groups_group_key_delete(self):
        """Test case for v1_enrollment_access_groups_group_key_delete

        Delete an LDAP group's access to user initiated Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_access_groups_group_key_get(self):
        """Test case for v1_enrollment_access_groups_group_key_get

        Retrieve the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_access_groups_group_key_put(self):
        """Test case for v1_enrollment_access_groups_group_key_put

        Modify the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_filtered_language_codes_get(self):
        """Test case for v1_enrollment_filtered_language_codes_get

        Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_get(self):
        """Test case for v1_enrollment_get

        Get Enrollment object and Re-enrollment settings   # noqa: E501
        """
        pass

    def test_v1_enrollment_history_get(self):
        """Test case for v1_enrollment_history_get

        Get sorted and paged Enrollment history object   # noqa: E501
        """
        pass

    def test_v1_enrollment_history_post(self):
        """Test case for v1_enrollment_history_post

        Add Enrollment history object notes   # noqa: E501
        """
        pass

    def test_v1_enrollment_language_codes_get(self):
        """Test case for v1_enrollment_language_codes_get

        Retrieve the list of languages and corresponding ISO 639-1 Codes   # noqa: E501
        """
        pass

    def test_v1_enrollment_languages_get(self):
        """Test case for v1_enrollment_languages_get

        Get an array of the language codes that have Enrollment messaging   # noqa: E501
        """
        pass

    def test_v1_enrollment_languages_language_delete(self):
        """Test case for v1_enrollment_languages_language_delete

        Delete the Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v1_enrollment_languages_language_get(self):
        """Test case for v1_enrollment_languages_language_get

        Retrieve the Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v1_enrollment_languages_language_put(self):
        """Test case for v1_enrollment_languages_language_put

        Edit Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v1_enrollment_put(self):
        """Test case for v1_enrollment_put

        Update Enrollment object   # noqa: E501
        """
        pass

    def test_v2_enrollment_access_groups_get(self):
        """Test case for v2_enrollment_access_groups_get

        Retrieve the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v2_enrollment_access_groups_server_id_group_id_delete(self):
        """Test case for v2_enrollment_access_groups_server_id_group_id_delete

        Delete an LDAP group's access to user initiated Enrollment   # noqa: E501
        """
        pass

    def test_v2_enrollment_access_groups_server_id_group_id_get(self):
        """Test case for v2_enrollment_access_groups_server_id_group_id_get

        Retrieve the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v2_enrollment_access_groups_server_id_group_id_put(self):
        """Test case for v2_enrollment_access_groups_server_id_group_id_put

        Modify the configured LDAP groups configured for User-Initiated Enrollment   # noqa: E501
        """
        pass

    def test_v2_enrollment_filtered_language_codes_get(self):
        """Test case for v2_enrollment_filtered_language_codes_get

        Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment   # noqa: E501
        """
        pass

    def test_v2_enrollment_get(self):
        """Test case for v2_enrollment_get

        Get Enrollment object and Re-enrollment settings   # noqa: E501
        """
        pass

    def test_v2_enrollment_history_get(self):
        """Test case for v2_enrollment_history_get

        Get sorted and paged Enrollment history object   # noqa: E501
        """
        pass

    def test_v2_enrollment_history_post(self):
        """Test case for v2_enrollment_history_post

        Add Enrollment history object notes   # noqa: E501
        """
        pass

    def test_v2_enrollment_language_codes_get(self):
        """Test case for v2_enrollment_language_codes_get

        Retrieve the list of languages and corresponding ISO 639-1 Codes   # noqa: E501
        """
        pass

    def test_v2_enrollment_languages_get(self):
        """Test case for v2_enrollment_languages_get

        Get an array of the language codes that have Enrollment messaging   # noqa: E501
        """
        pass

    def test_v2_enrollment_languages_language_id_delete(self):
        """Test case for v2_enrollment_languages_language_id_delete

        Delete the Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v2_enrollment_languages_language_id_get(self):
        """Test case for v2_enrollment_languages_language_id_get

        Retrieve the Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v2_enrollment_languages_language_id_put(self):
        """Test case for v2_enrollment_languages_language_id_put

        Edit Enrollment messaging for a language   # noqa: E501
        """
        pass

    def test_v2_enrollment_put(self):
        """Test case for v2_enrollment_put

        Update Enrollment object   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
