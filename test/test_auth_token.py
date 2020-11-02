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
from openapi_client.models.auth_token import AuthToken  # noqa: E501
from openapi_client.rest import ApiException

class TestAuthToken(unittest.TestCase):
    """AuthToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.auth_token.AuthToken()  # noqa: E501
        if include_optional :
            return AuthToken(
                token = 'eyJhbGciOiJIUzUxMiJ9.eyJhdXRoZW50aWNhdGVkLWFwcCI6IkdFTkVSSUMiLCJhdXRoZW50aWNhdGlvbi10eXBlIjoiSlNTIiwiZ3JvdXBzIjpbXSwic3ViamVjdC10eXBlIjoiSlNTX1VTRVJfSUQiLCJ0b2tlbi11dWlkIjoiNzc0YWY3MGYtYWQ0Yy00N2QzLTk2MzktZjEwMjBhMTIwYzExIiwibGRhcC1zZXJ2ZXItaWQiOi0xLCJzdWIiOiIxIiwiZXhwIjoxNTM5NjE5MzQ4fQ.0t7sgYyIyA7kTTmrM8tMGE7fnXcJ1ZzQODAJp0pzg92-cBMQS0Cv8S9oWjkJD7VJS-CHA1dOppr0G_2dCPOfng', 
                expires = 1539619348124
            )
        else :
            return AuthToken(
        )

    def testAuthToken(self):
        """Test AuthToken"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
