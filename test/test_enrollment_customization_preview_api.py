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
from openapi_client.api.enrollment_customization_preview_api import EnrollmentCustomizationPreviewApi  # noqa: E501
from openapi_client.rest import ApiException


class TestEnrollmentCustomizationPreviewApi(unittest.TestCase):
    """EnrollmentCustomizationPreviewApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.enrollment_customization_preview_api.EnrollmentCustomizationPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_enrollment_customization_id_all_get(self):
        """Test case for v1_enrollment_customization_id_all_get

        Get all Panels for single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_all_panel_id_delete(self):
        """Test case for v1_enrollment_customization_id_all_panel_id_delete

        Delete a single Panel from an Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_all_panel_id_get(self):
        """Test case for v1_enrollment_customization_id_all_panel_id_get

        Get a single Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_ldap_panel_id_delete(self):
        """Test case for v1_enrollment_customization_id_ldap_panel_id_delete

        Delete an LDAP single panel from an Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_ldap_panel_id_get(self):
        """Test case for v1_enrollment_customization_id_ldap_panel_id_get

        Get a single LDAP panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_ldap_panel_id_put(self):
        """Test case for v1_enrollment_customization_id_ldap_panel_id_put

        Update a single LDAP Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_ldap_post(self):
        """Test case for v1_enrollment_customization_id_ldap_post

        Create an LDAP Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_sso_panel_id_delete(self):
        """Test case for v1_enrollment_customization_id_sso_panel_id_delete

        Delete a single SSO Panel from an Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_sso_panel_id_get(self):
        """Test case for v1_enrollment_customization_id_sso_panel_id_get

        Get a single SSO Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_sso_panel_id_put(self):
        """Test case for v1_enrollment_customization_id_sso_panel_id_put

        Update a single SSO Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_sso_post(self):
        """Test case for v1_enrollment_customization_id_sso_post

        Create an SSO Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_text_panel_id_delete(self):
        """Test case for v1_enrollment_customization_id_text_panel_id_delete

        Delete a Text single Panel from an Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_text_panel_id_get(self):
        """Test case for v1_enrollment_customization_id_text_panel_id_get

        Get a single Text Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_text_panel_id_markdown_get(self):
        """Test case for v1_enrollment_customization_id_text_panel_id_markdown_get

        Get the markdown output of a single Text Panel for a single Enrollment   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_text_panel_id_put(self):
        """Test case for v1_enrollment_customization_id_text_panel_id_put

        Update a single Text Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_id_text_post(self):
        """Test case for v1_enrollment_customization_id_text_post

        Create a Text Panel for a single Enrollment Customization   # noqa: E501
        """
        pass

    def test_v1_enrollment_customization_parse_markdown_post(self):
        """Test case for v1_enrollment_customization_parse_markdown_post

        Parse the given string as markdown text and return Html output   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()