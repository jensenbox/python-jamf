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
from jamf.api.computer_prestages_api import ComputerPrestagesApi  # noqa: E501
from jamf.rest import ApiException


class TestComputerPrestagesApi(unittest.TestCase):
    """ComputerPrestagesApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.computer_prestages_api.ComputerPrestagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_computer_prestages_get(self):
        """Test case for v1_computer_prestages_get

        Search for sorted and paged Computer Prestages   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_delete(self):
        """Test case for v1_computer_prestages_id_delete

        Delete a Computer Prestage with the supplied id   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_get(self):
        """Test case for v1_computer_prestages_id_get

        Retrieve a Computer Prestage with the supplied id   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_put(self):
        """Test case for v1_computer_prestages_id_put

        Update a Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_scope_delete(self):
        """Test case for v1_computer_prestages_id_scope_delete

        Remove device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_scope_get(self):
        """Test case for v1_computer_prestages_id_scope_get

        Get device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_scope_post(self):
        """Test case for v1_computer_prestages_id_scope_post

        Add device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_id_scope_put(self):
        """Test case for v1_computer_prestages_id_scope_put

        Replace device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_post(self):
        """Test case for v1_computer_prestages_post

        Create a Computer Prestage   # noqa: E501
        """
        pass

    def test_v1_computer_prestages_scope_get(self):
        """Test case for v1_computer_prestages_scope_get

        Get all device Scope for all Computer Prestages   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_get(self):
        """Test case for v2_computer_prestages_get

        Get sorted and paged Computer Prestages   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_delete(self):
        """Test case for v2_computer_prestages_id_delete

        Delete a Computer Prestage with the supplied id   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_get(self):
        """Test case for v2_computer_prestages_id_get

        Retrieve a Computer Prestage with the supplied id   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_put(self):
        """Test case for v2_computer_prestages_id_put

        Update a Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_scope_delete_multiple_post(self):
        """Test case for v2_computer_prestages_id_scope_delete_multiple_post

        Remove device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_scope_get(self):
        """Test case for v2_computer_prestages_id_scope_get

        Get device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_scope_post(self):
        """Test case for v2_computer_prestages_id_scope_post

        Add device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_id_scope_put(self):
        """Test case for v2_computer_prestages_id_scope_put

        Replace device Scope for a specific Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_post(self):
        """Test case for v2_computer_prestages_post

        Create a Computer Prestage   # noqa: E501
        """
        pass

    def test_v2_computer_prestages_scope_get(self):
        """Test case for v2_computer_prestages_scope_get

        Get all device Scope for all Computer Prestages   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
