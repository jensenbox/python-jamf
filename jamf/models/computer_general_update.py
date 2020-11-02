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


class ComputerGeneralUpdate(object):
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
        'name': 'str',
        'last_ip_address': 'str',
        'barcode1': 'str',
        'barcode2': 'str',
        'asset_tag': 'str',
        'extension_attributes': 'list[ComputerExtensionAttribute]'
    }

    attribute_map = {
        'name': 'name',
        'last_ip_address': 'lastIpAddress',
        'barcode1': 'barcode1',
        'barcode2': 'barcode2',
        'asset_tag': 'assetTag',
        'extension_attributes': 'extensionAttributes'
    }

    def __init__(self, name=None, last_ip_address=None, barcode1=None, barcode2=None, asset_tag=None, extension_attributes=None, local_vars_configuration=None):  # noqa: E501
        """ComputerGeneralUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._last_ip_address = None
        self._barcode1 = None
        self._barcode2 = None
        self._asset_tag = None
        self._extension_attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if last_ip_address is not None:
            self.last_ip_address = last_ip_address
        if barcode1 is not None:
            self.barcode1 = barcode1
        if barcode2 is not None:
            self.barcode2 = barcode2
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if extension_attributes is not None:
            self.extension_attributes = extension_attributes

    @property
    def name(self):
        """Gets the name of this ComputerGeneralUpdate.  # noqa: E501


        :return: The name of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerGeneralUpdate.


        :param name: The name of this ComputerGeneralUpdate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def last_ip_address(self):
        """Gets the last_ip_address of this ComputerGeneralUpdate.  # noqa: E501


        :return: The last_ip_address of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: str
        """
        return self._last_ip_address

    @last_ip_address.setter
    def last_ip_address(self, last_ip_address):
        """Sets the last_ip_address of this ComputerGeneralUpdate.


        :param last_ip_address: The last_ip_address of this ComputerGeneralUpdate.  # noqa: E501
        :type last_ip_address: str
        """

        self._last_ip_address = last_ip_address

    @property
    def barcode1(self):
        """Gets the barcode1 of this ComputerGeneralUpdate.  # noqa: E501


        :return: The barcode1 of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: str
        """
        return self._barcode1

    @barcode1.setter
    def barcode1(self, barcode1):
        """Sets the barcode1 of this ComputerGeneralUpdate.


        :param barcode1: The barcode1 of this ComputerGeneralUpdate.  # noqa: E501
        :type barcode1: str
        """

        self._barcode1 = barcode1

    @property
    def barcode2(self):
        """Gets the barcode2 of this ComputerGeneralUpdate.  # noqa: E501


        :return: The barcode2 of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: str
        """
        return self._barcode2

    @barcode2.setter
    def barcode2(self, barcode2):
        """Sets the barcode2 of this ComputerGeneralUpdate.


        :param barcode2: The barcode2 of this ComputerGeneralUpdate.  # noqa: E501
        :type barcode2: str
        """

        self._barcode2 = barcode2

    @property
    def asset_tag(self):
        """Gets the asset_tag of this ComputerGeneralUpdate.  # noqa: E501


        :return: The asset_tag of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this ComputerGeneralUpdate.


        :param asset_tag: The asset_tag of this ComputerGeneralUpdate.  # noqa: E501
        :type asset_tag: str
        """

        self._asset_tag = asset_tag

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this ComputerGeneralUpdate.  # noqa: E501


        :return: The extension_attributes of this ComputerGeneralUpdate.  # noqa: E501
        :rtype: list[ComputerExtensionAttribute]
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this ComputerGeneralUpdate.


        :param extension_attributes: The extension_attributes of this ComputerGeneralUpdate.  # noqa: E501
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
        if not isinstance(other, ComputerGeneralUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerGeneralUpdate):
            return True

        return self.to_dict() != other.to_dict()
