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
from jamf.api.sso_certificate_api import SsoCertificateApi  # noqa: E501
from jamf.rest import ApiException


class TestSsoCertificateApi(unittest.TestCase):
    """SsoCertificateApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.sso_certificate_api.SsoCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v2_sso_cert_delete(self):
        """Test case for v2_sso_cert_delete

        Delete the currently configured certificate used by SSO   # noqa: E501
        """
        pass

    def test_v2_sso_cert_download_get(self):
        """Test case for v2_sso_cert_download_get

        Download the certificate currently configured for use with Jamf Pro's SSO configuration   # noqa: E501
        """
        pass

    def test_v2_sso_cert_get(self):
        """Test case for v2_sso_cert_get

        Retrieve the certificate currently configured for use with SSO   # noqa: E501
        """
        pass

    def test_v2_sso_cert_parse_post(self):
        """Test case for v2_sso_cert_parse_post

        Parse the certificate to get details about certificate type and keys needed to upload certificate file   # noqa: E501
        """
        pass

    def test_v2_sso_cert_post(self):
        """Test case for v2_sso_cert_post

        Jamf Pro will generate a new certificate and use it to sign SSO   # noqa: E501
        """
        pass

    def test_v2_sso_cert_put(self):
        """Test case for v2_sso_cert_put

        Update the certificate used by Jamf Pro to sign SSO requests to the identify provider   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
