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
from jamf.models.enrollment_customization_panel import EnrollmentCustomizationPanel  # noqa: E501
from jamf.rest import ApiException

class TestEnrollmentCustomizationPanel(unittest.TestCase):
    """EnrollmentCustomizationPanel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EnrollmentCustomizationPanel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.enrollment_customization_panel.EnrollmentCustomizationPanel()  # noqa: E501
        if include_optional :
            return EnrollmentCustomizationPanel(
                display_name = 'A Panel', 
                rank = 0
            )
        else :
            return EnrollmentCustomizationPanel(
                display_name = 'A Panel',
                rank = 0,
        )

    def testEnrollmentCustomizationPanel(self):
        """Test EnrollmentCustomizationPanel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
