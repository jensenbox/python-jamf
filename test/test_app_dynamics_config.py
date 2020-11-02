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
from openapi_client.models.app_dynamics_config import AppDynamicsConfig  # noqa: E501
from openapi_client.rest import ApiException

class TestAppDynamicsConfig(unittest.TestCase):
    """AppDynamicsConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppDynamicsConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.app_dynamics_config.AppDynamicsConfig()  # noqa: E501
        if include_optional :
            return AppDynamicsConfig(
                enable_eum = True, 
                app_key = 'AAA-BBB-CCC', 
                adrum_ext_url_http = 'http://adrum.example.com', 
                adrum_ext_url_https = 'https://adrum.example.com', 
                adrum_script_http = 'http://adrum.example.com/adrum/adrum.js', 
                adrum_script_https = 'https://adrum.example.com/adrum/adrum.js', 
                beacon_url_http = 'http://beacon.example.com', 
                beacon_url_https = 'https://beacon.example.com'
            )
        else :
            return AppDynamicsConfig(
                enable_eum = True,
                app_key = 'AAA-BBB-CCC',
                adrum_ext_url_http = 'http://adrum.example.com',
                adrum_ext_url_https = 'https://adrum.example.com',
                adrum_script_http = 'http://adrum.example.com/adrum/adrum.js',
                adrum_script_https = 'https://adrum.example.com/adrum/adrum.js',
                beacon_url_http = 'http://beacon.example.com',
                beacon_url_https = 'https://beacon.example.com',
        )

    def testAppDynamicsConfig(self):
        """Test AppDynamicsConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
