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


class ComputerMdmCapability(object):
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
        'capable': 'bool',
        'capable_users': 'list[str]'
    }

    attribute_map = {
        'capable': 'capable',
        'capable_users': 'capableUsers'
    }

    def __init__(self, capable=None, capable_users=None, local_vars_configuration=None):  # noqa: E501
        """ComputerMdmCapability - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capable = None
        self._capable_users = None
        self.discriminator = None

        if capable is not None:
            self.capable = capable
        if capable_users is not None:
            self.capable_users = capable_users

    @property
    def capable(self):
        """Gets the capable of this ComputerMdmCapability.  # noqa: E501


        :return: The capable of this ComputerMdmCapability.  # noqa: E501
        :rtype: bool
        """
        return self._capable

    @capable.setter
    def capable(self, capable):
        """Sets the capable of this ComputerMdmCapability.


        :param capable: The capable of this ComputerMdmCapability.  # noqa: E501
        :type capable: bool
        """

        self._capable = capable

    @property
    def capable_users(self):
        """Gets the capable_users of this ComputerMdmCapability.  # noqa: E501


        :return: The capable_users of this ComputerMdmCapability.  # noqa: E501
        :rtype: list[str]
        """
        return self._capable_users

    @capable_users.setter
    def capable_users(self, capable_users):
        """Sets the capable_users of this ComputerMdmCapability.


        :param capable_users: The capable_users of this ComputerMdmCapability.  # noqa: E501
        :type capable_users: list[str]
        """

        self._capable_users = capable_users

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
        if not isinstance(other, ComputerMdmCapability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerMdmCapability):
            return True

        return self.to_dict() != other.to_dict()
