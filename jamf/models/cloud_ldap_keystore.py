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


class CloudLdapKeystore(object):
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
        'type': 'str',
        'expiration_date': 'datetime',
        'subject': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'expiration_date': 'expirationDate',
        'subject': 'subject',
        'file_name': 'fileName'
    }

    def __init__(self, type=None, expiration_date=None, subject=None, file_name=None, local_vars_configuration=None):  # noqa: E501
        """CloudLdapKeystore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._expiration_date = None
        self._subject = None
        self._file_name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if subject is not None:
            self.subject = subject
        if file_name is not None:
            self.file_name = file_name

    @property
    def type(self):
        """Gets the type of this CloudLdapKeystore.  # noqa: E501


        :return: The type of this CloudLdapKeystore.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudLdapKeystore.


        :param type: The type of this CloudLdapKeystore.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def expiration_date(self):
        """Gets the expiration_date of this CloudLdapKeystore.  # noqa: E501


        :return: The expiration_date of this CloudLdapKeystore.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this CloudLdapKeystore.


        :param expiration_date: The expiration_date of this CloudLdapKeystore.  # noqa: E501
        :type expiration_date: datetime
        """

        self._expiration_date = expiration_date

    @property
    def subject(self):
        """Gets the subject of this CloudLdapKeystore.  # noqa: E501


        :return: The subject of this CloudLdapKeystore.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CloudLdapKeystore.


        :param subject: The subject of this CloudLdapKeystore.  # noqa: E501
        :type subject: str
        """

        self._subject = subject

    @property
    def file_name(self):
        """Gets the file_name of this CloudLdapKeystore.  # noqa: E501


        :return: The file_name of this CloudLdapKeystore.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CloudLdapKeystore.


        :param file_name: The file_name of this CloudLdapKeystore.  # noqa: E501
        :type file_name: str
        """

        self._file_name = file_name

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
        if not isinstance(other, CloudLdapKeystore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLdapKeystore):
            return True

        return self.to_dict() != other.to_dict()
