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


class ComputerAttachment(object):
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
        'name': 'str',
        'file_type': 'str',
        'size_bytes': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'file_type': 'fileType',
        'size_bytes': 'sizeBytes'
    }

    def __init__(self, id=None, name=None, file_type=None, size_bytes=None, local_vars_configuration=None):  # noqa: E501
        """ComputerAttachment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._file_type = None
        self._size_bytes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if file_type is not None:
            self.file_type = file_type
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def id(self):
        """Gets the id of this ComputerAttachment.  # noqa: E501


        :return: The id of this ComputerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComputerAttachment.


        :param id: The id of this ComputerAttachment.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ComputerAttachment.  # noqa: E501


        :return: The name of this ComputerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerAttachment.


        :param name: The name of this ComputerAttachment.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def file_type(self):
        """Gets the file_type of this ComputerAttachment.  # noqa: E501


        :return: The file_type of this ComputerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ComputerAttachment.


        :param file_type: The file_type of this ComputerAttachment.  # noqa: E501
        :type file_type: str
        """

        self._file_type = file_type

    @property
    def size_bytes(self):
        """Gets the size_bytes of this ComputerAttachment.  # noqa: E501

        File size in bytes  # noqa: E501

        :return: The size_bytes of this ComputerAttachment.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this ComputerAttachment.

        File size in bytes  # noqa: E501

        :param size_bytes: The size_bytes of this ComputerAttachment.  # noqa: E501
        :type size_bytes: int
        """

        self._size_bytes = size_bytes

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
        if not isinstance(other, ComputerAttachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerAttachment):
            return True

        return self.to_dict() != other.to_dict()
