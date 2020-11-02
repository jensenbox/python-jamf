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


class Recipient(object):
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
        'real_name': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'real_name': 'realName',
        'email': 'email'
    }

    def __init__(self, id=None, real_name=None, email=None, local_vars_configuration=None):  # noqa: E501
        """Recipient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._real_name = None
        self._email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if real_name is not None:
            self.real_name = real_name
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this Recipient.  # noqa: E501


        :return: The id of this Recipient.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Recipient.


        :param id: The id of this Recipient.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def real_name(self):
        """Gets the real_name of this Recipient.  # noqa: E501


        :return: The real_name of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this Recipient.


        :param real_name: The real_name of this Recipient.  # noqa: E501
        :type real_name: str
        """

        self._real_name = real_name

    @property
    def email(self):
        """Gets the email of this Recipient.  # noqa: E501


        :return: The email of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Recipient.


        :param email: The email of this Recipient.  # noqa: E501
        :type email: str
        """

        self._email = email

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
        if not isinstance(other, Recipient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Recipient):
            return True

        return self.to_dict() != other.to_dict()