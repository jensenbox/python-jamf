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


class CloudLdapMappingsRequest(object):
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
        'user_mappings': 'UserMappings',
        'group_mappings': 'GroupMappings',
        'membership_mappings': 'MembershipMappings'
    }

    attribute_map = {
        'user_mappings': 'userMappings',
        'group_mappings': 'groupMappings',
        'membership_mappings': 'membershipMappings'
    }

    def __init__(self, user_mappings=None, group_mappings=None, membership_mappings=None, local_vars_configuration=None):  # noqa: E501
        """CloudLdapMappingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_mappings = None
        self._group_mappings = None
        self._membership_mappings = None
        self.discriminator = None

        self.user_mappings = user_mappings
        self.group_mappings = group_mappings
        self.membership_mappings = membership_mappings

    @property
    def user_mappings(self):
        """Gets the user_mappings of this CloudLdapMappingsRequest.  # noqa: E501


        :return: The user_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :rtype: UserMappings
        """
        return self._user_mappings

    @user_mappings.setter
    def user_mappings(self, user_mappings):
        """Sets the user_mappings of this CloudLdapMappingsRequest.


        :param user_mappings: The user_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :type user_mappings: UserMappings
        """
        if self.local_vars_configuration.client_side_validation and user_mappings is None:  # noqa: E501
            raise ValueError("Invalid value for `user_mappings`, must not be `None`")  # noqa: E501

        self._user_mappings = user_mappings

    @property
    def group_mappings(self):
        """Gets the group_mappings of this CloudLdapMappingsRequest.  # noqa: E501


        :return: The group_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :rtype: GroupMappings
        """
        return self._group_mappings

    @group_mappings.setter
    def group_mappings(self, group_mappings):
        """Sets the group_mappings of this CloudLdapMappingsRequest.


        :param group_mappings: The group_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :type group_mappings: GroupMappings
        """
        if self.local_vars_configuration.client_side_validation and group_mappings is None:  # noqa: E501
            raise ValueError("Invalid value for `group_mappings`, must not be `None`")  # noqa: E501

        self._group_mappings = group_mappings

    @property
    def membership_mappings(self):
        """Gets the membership_mappings of this CloudLdapMappingsRequest.  # noqa: E501


        :return: The membership_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :rtype: MembershipMappings
        """
        return self._membership_mappings

    @membership_mappings.setter
    def membership_mappings(self, membership_mappings):
        """Sets the membership_mappings of this CloudLdapMappingsRequest.


        :param membership_mappings: The membership_mappings of this CloudLdapMappingsRequest.  # noqa: E501
        :type membership_mappings: MembershipMappings
        """
        if self.local_vars_configuration.client_side_validation and membership_mappings is None:  # noqa: E501
            raise ValueError("Invalid value for `membership_mappings`, must not be `None`")  # noqa: E501

        self._membership_mappings = membership_mappings

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
        if not isinstance(other, CloudLdapMappingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLdapMappingsRequest):
            return True

        return self.to_dict() != other.to_dict()
