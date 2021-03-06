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


class CloudLdapKeystoreFile(object):
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
        'password': 'str',
        'file_bytes': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'password': 'password',
        'file_bytes': 'fileBytes',
        'file_name': 'fileName'
    }

    def __init__(self, password=None, file_bytes=None, file_name=None, local_vars_configuration=None):  # noqa: E501
        """CloudLdapKeystoreFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password = None
        self._file_bytes = None
        self._file_name = None
        self.discriminator = None

        self.password = password
        self.file_bytes = file_bytes
        self.file_name = file_name

    @property
    def password(self):
        """Gets the password of this CloudLdapKeystoreFile.  # noqa: E501


        :return: The password of this CloudLdapKeystoreFile.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CloudLdapKeystoreFile.


        :param password: The password of this CloudLdapKeystoreFile.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def file_bytes(self):
        """Gets the file_bytes of this CloudLdapKeystoreFile.  # noqa: E501


        :return: The file_bytes of this CloudLdapKeystoreFile.  # noqa: E501
        :rtype: str
        """
        return self._file_bytes

    @file_bytes.setter
    def file_bytes(self, file_bytes):
        """Sets the file_bytes of this CloudLdapKeystoreFile.


        :param file_bytes: The file_bytes of this CloudLdapKeystoreFile.  # noqa: E501
        :type file_bytes: str
        """
        if self.local_vars_configuration.client_side_validation and file_bytes is None:  # noqa: E501
            raise ValueError("Invalid value for `file_bytes`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                file_bytes is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', file_bytes)):  # noqa: E501
            raise ValueError(r"Invalid value for `file_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._file_bytes = file_bytes

    @property
    def file_name(self):
        """Gets the file_name of this CloudLdapKeystoreFile.  # noqa: E501


        :return: The file_name of this CloudLdapKeystoreFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CloudLdapKeystoreFile.


        :param file_name: The file_name of this CloudLdapKeystoreFile.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, CloudLdapKeystoreFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLdapKeystoreFile):
            return True

        return self.to_dict() != other.to_dict()
