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
from jamf.models.get_enrollment_customization_panel_text import GetEnrollmentCustomizationPanelText  # noqa: E501
from jamf.rest import ApiException

class TestGetEnrollmentCustomizationPanelText(unittest.TestCase):
    """GetEnrollmentCustomizationPanelText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEnrollmentCustomizationPanelText
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.get_enrollment_customization_panel_text.GetEnrollmentCustomizationPanelText()  # noqa: E501
        if include_optional :
            return GetEnrollmentCustomizationPanelText(
                display_name = 'A Panel', 
                rank = 0, 
                body = 'Welcome!', 
                subtext = 'World!', 
                title = 'My text panel', 
                back_button_text = 'Back', 
                continue_button_text = 'Continue', 
                id = 2, 
                type = 'text'
            )
        else :
            return GetEnrollmentCustomizationPanelText(
                display_name = 'A Panel',
                rank = 0,
                body = 'Welcome!',
                title = 'My text panel',
                back_button_text = 'Back',
                continue_button_text = 'Continue',
        )

    def testGetEnrollmentCustomizationPanelText(self):
        """Test GetEnrollmentCustomizationPanelText"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
