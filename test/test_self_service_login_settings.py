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
from jamf.models.self_service_login_settings import SelfServiceLoginSettings  # noqa: E501
from jamf.rest import ApiException

class TestSelfServiceLoginSettings(unittest.TestCase):
    """SelfServiceLoginSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SelfServiceLoginSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.self_service_login_settings.SelfServiceLoginSettings()  # noqa: E501
        if include_optional :
            return SelfServiceLoginSettings(
                user_login_level = 'NotRequired', 
                is_allow_remember_me = True, 
                auth_type = 'Basic'
            )
        else :
            return SelfServiceLoginSettings(
                user_login_level = 'NotRequired',
                auth_type = 'Basic',
        )

    def testSelfServiceLoginSettings(self):
        """Test SelfServiceLoginSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
