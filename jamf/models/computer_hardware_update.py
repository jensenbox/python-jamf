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


class ComputerHardwareUpdate(object):
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
        'network_adapter_type': 'str',
        'mac_address': 'str',
        'alt_network_adapter_type': 'str',
        'alt_mac_address': 'str',
        'extension_attributes': 'list[ComputerExtensionAttribute]'
    }

    attribute_map = {
        'network_adapter_type': 'networkAdapterType',
        'mac_address': 'macAddress',
        'alt_network_adapter_type': 'altNetworkAdapterType',
        'alt_mac_address': 'altMacAddress',
        'extension_attributes': 'extensionAttributes'
    }

    def __init__(self, network_adapter_type=None, mac_address=None, alt_network_adapter_type=None, alt_mac_address=None, extension_attributes=None, local_vars_configuration=None):  # noqa: E501
        """ComputerHardwareUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network_adapter_type = None
        self._mac_address = None
        self._alt_network_adapter_type = None
        self._alt_mac_address = None
        self._extension_attributes = None
        self.discriminator = None

        if network_adapter_type is not None:
            self.network_adapter_type = network_adapter_type
        if mac_address is not None:
            self.mac_address = mac_address
        if alt_network_adapter_type is not None:
            self.alt_network_adapter_type = alt_network_adapter_type
        if alt_mac_address is not None:
            self.alt_mac_address = alt_mac_address
        if extension_attributes is not None:
            self.extension_attributes = extension_attributes

    @property
    def network_adapter_type(self):
        """Gets the network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501


        :return: The network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._network_adapter_type

    @network_adapter_type.setter
    def network_adapter_type(self, network_adapter_type):
        """Sets the network_adapter_type of this ComputerHardwareUpdate.


        :param network_adapter_type: The network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501
        :type network_adapter_type: str
        """

        self._network_adapter_type = network_adapter_type

    @property
    def mac_address(self):
        """Gets the mac_address of this ComputerHardwareUpdate.  # noqa: E501


        :return: The mac_address of this ComputerHardwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this ComputerHardwareUpdate.


        :param mac_address: The mac_address of this ComputerHardwareUpdate.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def alt_network_adapter_type(self):
        """Gets the alt_network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501


        :return: The alt_network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._alt_network_adapter_type

    @alt_network_adapter_type.setter
    def alt_network_adapter_type(self, alt_network_adapter_type):
        """Sets the alt_network_adapter_type of this ComputerHardwareUpdate.


        :param alt_network_adapter_type: The alt_network_adapter_type of this ComputerHardwareUpdate.  # noqa: E501
        :type alt_network_adapter_type: str
        """

        self._alt_network_adapter_type = alt_network_adapter_type

    @property
    def alt_mac_address(self):
        """Gets the alt_mac_address of this ComputerHardwareUpdate.  # noqa: E501


        :return: The alt_mac_address of this ComputerHardwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._alt_mac_address

    @alt_mac_address.setter
    def alt_mac_address(self, alt_mac_address):
        """Sets the alt_mac_address of this ComputerHardwareUpdate.


        :param alt_mac_address: The alt_mac_address of this ComputerHardwareUpdate.  # noqa: E501
        :type alt_mac_address: str
        """

        self._alt_mac_address = alt_mac_address

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this ComputerHardwareUpdate.  # noqa: E501


        :return: The extension_attributes of this ComputerHardwareUpdate.  # noqa: E501
        :rtype: list[ComputerExtensionAttribute]
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this ComputerHardwareUpdate.


        :param extension_attributes: The extension_attributes of this ComputerHardwareUpdate.  # noqa: E501
        :type extension_attributes: list[ComputerExtensionAttribute]
        """

        self._extension_attributes = extension_attributes

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
        if not isinstance(other, ComputerHardwareUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerHardwareUpdate):
            return True

        return self.to_dict() != other.to_dict()
