# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ComputerPrestageAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'is_install_profiles_during_setup': 'bool',
        'prestage_installed_profile_ids': 'list[int]',
        'custom_package_ids': 'list[int]',
        'custom_package_distribution_point_id': 'int'
    }

    attribute_map = {
        'is_install_profiles_during_setup': 'isInstallProfilesDuringSetup',
        'prestage_installed_profile_ids': 'prestageInstalledProfileIds',
        'custom_package_ids': 'customPackageIds',
        'custom_package_distribution_point_id': 'customPackageDistributionPointId'
    }

    def __init__(self, is_install_profiles_during_setup=None, prestage_installed_profile_ids=None, custom_package_ids=None, custom_package_distribution_point_id=None, local_vars_configuration=None):  # noqa: E501
        """ComputerPrestageAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_install_profiles_during_setup = None
        self._prestage_installed_profile_ids = None
        self._custom_package_ids = None
        self._custom_package_distribution_point_id = None
        self.discriminator = None

        self.is_install_profiles_during_setup = is_install_profiles_during_setup
        self.prestage_installed_profile_ids = prestage_installed_profile_ids
        self.custom_package_ids = custom_package_ids
        self.custom_package_distribution_point_id = custom_package_distribution_point_id

    @property
    def is_install_profiles_during_setup(self):
        """Gets the is_install_profiles_during_setup of this ComputerPrestageAllOf.  # noqa: E501


        :return: The is_install_profiles_during_setup of this ComputerPrestageAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_install_profiles_during_setup

    @is_install_profiles_during_setup.setter
    def is_install_profiles_during_setup(self, is_install_profiles_during_setup):
        """Sets the is_install_profiles_during_setup of this ComputerPrestageAllOf.


        :param is_install_profiles_during_setup: The is_install_profiles_during_setup of this ComputerPrestageAllOf.  # noqa: E501
        :type is_install_profiles_during_setup: bool
        """
        if self.local_vars_configuration.client_side_validation and is_install_profiles_during_setup is None:  # noqa: E501
            raise ValueError("Invalid value for `is_install_profiles_during_setup`, must not be `None`")  # noqa: E501

        self._is_install_profiles_during_setup = is_install_profiles_during_setup

    @property
    def prestage_installed_profile_ids(self):
        """Gets the prestage_installed_profile_ids of this ComputerPrestageAllOf.  # noqa: E501


        :return: The prestage_installed_profile_ids of this ComputerPrestageAllOf.  # noqa: E501
        :rtype: list[int]
        """
        return self._prestage_installed_profile_ids

    @prestage_installed_profile_ids.setter
    def prestage_installed_profile_ids(self, prestage_installed_profile_ids):
        """Sets the prestage_installed_profile_ids of this ComputerPrestageAllOf.


        :param prestage_installed_profile_ids: The prestage_installed_profile_ids of this ComputerPrestageAllOf.  # noqa: E501
        :type prestage_installed_profile_ids: list[int]
        """
        if self.local_vars_configuration.client_side_validation and prestage_installed_profile_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `prestage_installed_profile_ids`, must not be `None`")  # noqa: E501

        self._prestage_installed_profile_ids = prestage_installed_profile_ids

    @property
    def custom_package_ids(self):
        """Gets the custom_package_ids of this ComputerPrestageAllOf.  # noqa: E501


        :return: The custom_package_ids of this ComputerPrestageAllOf.  # noqa: E501
        :rtype: list[int]
        """
        return self._custom_package_ids

    @custom_package_ids.setter
    def custom_package_ids(self, custom_package_ids):
        """Sets the custom_package_ids of this ComputerPrestageAllOf.


        :param custom_package_ids: The custom_package_ids of this ComputerPrestageAllOf.  # noqa: E501
        :type custom_package_ids: list[int]
        """
        if self.local_vars_configuration.client_side_validation and custom_package_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_package_ids`, must not be `None`")  # noqa: E501

        self._custom_package_ids = custom_package_ids

    @property
    def custom_package_distribution_point_id(self):
        """Gets the custom_package_distribution_point_id of this ComputerPrestageAllOf.  # noqa: E501


        :return: The custom_package_distribution_point_id of this ComputerPrestageAllOf.  # noqa: E501
        :rtype: int
        """
        return self._custom_package_distribution_point_id

    @custom_package_distribution_point_id.setter
    def custom_package_distribution_point_id(self, custom_package_distribution_point_id):
        """Sets the custom_package_distribution_point_id of this ComputerPrestageAllOf.


        :param custom_package_distribution_point_id: The custom_package_distribution_point_id of this ComputerPrestageAllOf.  # noqa: E501
        :type custom_package_distribution_point_id: int
        """
        if self.local_vars_configuration.client_side_validation and custom_package_distribution_point_id is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_package_distribution_point_id`, must not be `None`")  # noqa: E501

        self._custom_package_distribution_point_id = custom_package_distribution_point_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComputerPrestageAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerPrestageAllOf):
            return True

        return self.to_dict() != other.to_dict()
