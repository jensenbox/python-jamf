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
from jamf.models.script import Script  # noqa: E501
from jamf.rest import ApiException

class TestScript(unittest.TestCase):
    """Script unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Script
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.script.Script()  # noqa: E501
        if include_optional :
            return Script(
                id = '1', 
                name = 'Install Developer Utils Script', 
                info = 'Installs utilities for developers', 
                notes = 'Should be able to be re-run without problem.', 
                priority = 'AFTER', 
                category_id = '1', 
                category_name = 'Developer Tools', 
                parameter4 = '1', 
                parameter5 = '2', 
                parameter6 = '3', 
                parameter7 = '4', 
                parameter8 = '5', 
                parameter9 = '6', 
                parameter10 = '7', 
                parameter11 = '8', 
                os_requirements = '10.10.x', 
                script_contents = 'echo "Trivial script."'
            )
        else :
            return Script(
        )

    def testScript(self):
        """Test Script"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
