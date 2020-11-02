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


class GetEnrollmentCustomizationPanel(object):
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
        'display_name': 'str',
        'rank': 'int',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'rank': 'rank',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, display_name=None, rank=None, id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """GetEnrollmentCustomizationPanel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._rank = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.display_name = display_name
        self.rank = rank
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def display_name(self):
        """Gets the display_name of this GetEnrollmentCustomizationPanel.  # noqa: E501


        :return: The display_name of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetEnrollmentCustomizationPanel.


        :param display_name: The display_name of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def rank(self):
        """Gets the rank of this GetEnrollmentCustomizationPanel.  # noqa: E501


        :return: The rank of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this GetEnrollmentCustomizationPanel.


        :param rank: The rank of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :type rank: int
        """
        if self.local_vars_configuration.client_side_validation and rank is None:  # noqa: E501
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def id(self):
        """Gets the id of this GetEnrollmentCustomizationPanel.  # noqa: E501


        :return: The id of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetEnrollmentCustomizationPanel.


        :param id: The id of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GetEnrollmentCustomizationPanel.  # noqa: E501


        :return: The type of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetEnrollmentCustomizationPanel.


        :param type: The type of this GetEnrollmentCustomizationPanel.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, GetEnrollmentCustomizationPanel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetEnrollmentCustomizationPanel):
            return True

        return self.to_dict() != other.to_dict()
