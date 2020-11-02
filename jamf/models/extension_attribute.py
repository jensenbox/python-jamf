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


class ExtensionAttribute(object):
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
        'id': 'int',
        'name': 'str',
        'type': 'str',
        'value': 'list[str]',
        'is_extension_attribute_collection_allowed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'is_extension_attribute_collection_allowed': 'isExtensionAttributeCollectionAllowed'
    }

    def __init__(self, id=None, name=None, type=None, value=None, is_extension_attribute_collection_allowed=None, local_vars_configuration=None):  # noqa: E501
        """ExtensionAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._value = None
        self._is_extension_attribute_collection_allowed = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if is_extension_attribute_collection_allowed is not None:
            self.is_extension_attribute_collection_allowed = is_extension_attribute_collection_allowed

    @property
    def id(self):
        """Gets the id of this ExtensionAttribute.  # noqa: E501


        :return: The id of this ExtensionAttribute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtensionAttribute.


        :param id: The id of this ExtensionAttribute.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExtensionAttribute.  # noqa: E501


        :return: The name of this ExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtensionAttribute.


        :param name: The name of this ExtensionAttribute.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ExtensionAttribute.  # noqa: E501


        :return: The type of this ExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExtensionAttribute.


        :param type: The type of this ExtensionAttribute.  # noqa: E501
        :type type: str
        """
        allowed_values = ["STRING", "INTEGER", "DATE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this ExtensionAttribute.  # noqa: E501


        :return: The value of this ExtensionAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExtensionAttribute.


        :param value: The value of this ExtensionAttribute.  # noqa: E501
        :type value: list[str]
        """

        self._value = value

    @property
    def is_extension_attribute_collection_allowed(self):
        """Gets the is_extension_attribute_collection_allowed of this ExtensionAttribute.  # noqa: E501


        :return: The is_extension_attribute_collection_allowed of this ExtensionAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._is_extension_attribute_collection_allowed

    @is_extension_attribute_collection_allowed.setter
    def is_extension_attribute_collection_allowed(self, is_extension_attribute_collection_allowed):
        """Sets the is_extension_attribute_collection_allowed of this ExtensionAttribute.


        :param is_extension_attribute_collection_allowed: The is_extension_attribute_collection_allowed of this ExtensionAttribute.  # noqa: E501
        :type is_extension_attribute_collection_allowed: bool
        """

        self._is_extension_attribute_collection_allowed = is_extension_attribute_collection_allowed

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
        if not isinstance(other, ExtensionAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionAttribute):
            return True

        return self.to_dict() != other.to_dict()
