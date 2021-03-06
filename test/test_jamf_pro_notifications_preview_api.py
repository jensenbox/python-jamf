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
from jamf.api.jamf_pro_notifications_preview_api import JamfProNotificationsPreviewApi  # noqa: E501
from jamf.rest import ApiException


class TestJamfProNotificationsPreviewApi(unittest.TestCase):
    """JamfProNotificationsPreviewApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.jamf_pro_notifications_preview_api.JamfProNotificationsPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notifications_alerts_get(self):
        """Test case for notifications_alerts_get

        Get Notifications for user and site   # noqa: E501
        """
        pass

    def test_notifications_alerts_id_delete(self):
        """Test case for notifications_alerts_id_delete

        DEPRECATED - USE \"alerts/{type}/{id}\" INSTEAD. Deletes only Patch Management notifications.   # noqa: E501
        """
        pass

    def test_notifications_alerts_type_id_delete(self):
        """Test case for notifications_alerts_type_id_delete

        Delete Notifications   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
