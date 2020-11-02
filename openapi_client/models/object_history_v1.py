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


class ObjectHistoryV1(object):
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
        'id': 'str',
        'username': 'str',
        'date': 'str',
        'note': 'str',
        'details': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'date': 'date',
        'note': 'note',
        'details': 'details'
    }

    def __init__(self, id=None, username=None, date=None, note=None, details=None, local_vars_configuration=None):  # noqa: E501
        """ObjectHistoryV1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._date = None
        self._note = None
        self._details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if date is not None:
            self.date = date
        if note is not None:
            self.note = note
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this ObjectHistoryV1.  # noqa: E501


        :return: The id of this ObjectHistoryV1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectHistoryV1.


        :param id: The id of this ObjectHistoryV1.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this ObjectHistoryV1.  # noqa: E501


        :return: The username of this ObjectHistoryV1.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ObjectHistoryV1.


        :param username: The username of this ObjectHistoryV1.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def date(self):
        """Gets the date of this ObjectHistoryV1.  # noqa: E501


        :return: The date of this ObjectHistoryV1.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ObjectHistoryV1.


        :param date: The date of this ObjectHistoryV1.  # noqa: E501
        :type date: str
        """

        self._date = date

    @property
    def note(self):
        """Gets the note of this ObjectHistoryV1.  # noqa: E501


        :return: The note of this ObjectHistoryV1.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ObjectHistoryV1.


        :param note: The note of this ObjectHistoryV1.  # noqa: E501
        :type note: str
        """

        self._note = note

    @property
    def details(self):
        """Gets the details of this ObjectHistoryV1.  # noqa: E501


        :return: The details of this ObjectHistoryV1.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ObjectHistoryV1.


        :param details: The details of this ObjectHistoryV1.  # noqa: E501
        :type details: str
        """

        self._details = details

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
        if not isinstance(other, ObjectHistoryV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectHistoryV1):
            return True

        return self.to_dict() != other.to_dict()
