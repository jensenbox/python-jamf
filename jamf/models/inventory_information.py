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

from jamf.configuration import Configuration


class InventoryInformation(object):
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
        'managed_computers': 'int',
        'unmanaged_computers': 'int',
        'managed_devices': 'int',
        'unmanaged_devices': 'int'
    }

    attribute_map = {
        'managed_computers': 'managedComputers',
        'unmanaged_computers': 'unmanagedComputers',
        'managed_devices': 'managedDevices',
        'unmanaged_devices': 'unmanagedDevices'
    }

    def __init__(self, managed_computers=None, unmanaged_computers=None, managed_devices=None, unmanaged_devices=None, local_vars_configuration=None):  # noqa: E501
        """InventoryInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._managed_computers = None
        self._unmanaged_computers = None
        self._managed_devices = None
        self._unmanaged_devices = None
        self.discriminator = None

        if managed_computers is not None:
            self.managed_computers = managed_computers
        if unmanaged_computers is not None:
            self.unmanaged_computers = unmanaged_computers
        if managed_devices is not None:
            self.managed_devices = managed_devices
        if unmanaged_devices is not None:
            self.unmanaged_devices = unmanaged_devices

    @property
    def managed_computers(self):
        """Gets the managed_computers of this InventoryInformation.  # noqa: E501

        Number of managed computers in inventory.  # noqa: E501

        :return: The managed_computers of this InventoryInformation.  # noqa: E501
        :rtype: int
        """
        return self._managed_computers

    @managed_computers.setter
    def managed_computers(self, managed_computers):
        """Sets the managed_computers of this InventoryInformation.

        Number of managed computers in inventory.  # noqa: E501

        :param managed_computers: The managed_computers of this InventoryInformation.  # noqa: E501
        :type managed_computers: int
        """
        if (self.local_vars_configuration.client_side_validation and
                managed_computers is not None and managed_computers < 0):  # noqa: E501
            raise ValueError("Invalid value for `managed_computers`, must be a value greater than or equal to `0`")  # noqa: E501

        self._managed_computers = managed_computers

    @property
    def unmanaged_computers(self):
        """Gets the unmanaged_computers of this InventoryInformation.  # noqa: E501

        Number of unmanaged computers in inventory.  # noqa: E501

        :return: The unmanaged_computers of this InventoryInformation.  # noqa: E501
        :rtype: int
        """
        return self._unmanaged_computers

    @unmanaged_computers.setter
    def unmanaged_computers(self, unmanaged_computers):
        """Sets the unmanaged_computers of this InventoryInformation.

        Number of unmanaged computers in inventory.  # noqa: E501

        :param unmanaged_computers: The unmanaged_computers of this InventoryInformation.  # noqa: E501
        :type unmanaged_computers: int
        """
        if (self.local_vars_configuration.client_side_validation and
                unmanaged_computers is not None and unmanaged_computers < 0):  # noqa: E501
            raise ValueError("Invalid value for `unmanaged_computers`, must be a value greater than or equal to `0`")  # noqa: E501

        self._unmanaged_computers = unmanaged_computers

    @property
    def managed_devices(self):
        """Gets the managed_devices of this InventoryInformation.  # noqa: E501

        Number of managed devices in inventory.  # noqa: E501

        :return: The managed_devices of this InventoryInformation.  # noqa: E501
        :rtype: int
        """
        return self._managed_devices

    @managed_devices.setter
    def managed_devices(self, managed_devices):
        """Sets the managed_devices of this InventoryInformation.

        Number of managed devices in inventory.  # noqa: E501

        :param managed_devices: The managed_devices of this InventoryInformation.  # noqa: E501
        :type managed_devices: int
        """
        if (self.local_vars_configuration.client_side_validation and
                managed_devices is not None and managed_devices < 0):  # noqa: E501
            raise ValueError("Invalid value for `managed_devices`, must be a value greater than or equal to `0`")  # noqa: E501

        self._managed_devices = managed_devices

    @property
    def unmanaged_devices(self):
        """Gets the unmanaged_devices of this InventoryInformation.  # noqa: E501

        Number of unmanaged devices in inventory.  # noqa: E501

        :return: The unmanaged_devices of this InventoryInformation.  # noqa: E501
        :rtype: int
        """
        return self._unmanaged_devices

    @unmanaged_devices.setter
    def unmanaged_devices(self, unmanaged_devices):
        """Sets the unmanaged_devices of this InventoryInformation.

        Number of unmanaged devices in inventory.  # noqa: E501

        :param unmanaged_devices: The unmanaged_devices of this InventoryInformation.  # noqa: E501
        :type unmanaged_devices: int
        """
        if (self.local_vars_configuration.client_side_validation and
                unmanaged_devices is not None and unmanaged_devices < 0):  # noqa: E501
            raise ValueError("Invalid value for `unmanaged_devices`, must be a value greater than or equal to `0`")  # noqa: E501

        self._unmanaged_devices = unmanaged_devices

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
        if not isinstance(other, InventoryInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryInformation):
            return True

        return self.to_dict() != other.to_dict()
