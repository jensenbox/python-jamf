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


class IosDetailsEbooks(object):
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
        'author': 'str',
        'title': 'str',
        'version': 'str'
    }

    attribute_map = {
        'author': 'author',
        'title': 'title',
        'version': 'version'
    }

    def __init__(self, author=None, title=None, version=None, local_vars_configuration=None):  # noqa: E501
        """IosDetailsEbooks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._title = None
        self._version = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version

    @property
    def author(self):
        """Gets the author of this IosDetailsEbooks.  # noqa: E501


        :return: The author of this IosDetailsEbooks.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this IosDetailsEbooks.


        :param author: The author of this IosDetailsEbooks.  # noqa: E501
        :type author: str
        """

        self._author = author

    @property
    def title(self):
        """Gets the title of this IosDetailsEbooks.  # noqa: E501


        :return: The title of this IosDetailsEbooks.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IosDetailsEbooks.


        :param title: The title of this IosDetailsEbooks.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this IosDetailsEbooks.  # noqa: E501


        :return: The version of this IosDetailsEbooks.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IosDetailsEbooks.


        :param version: The version of this IosDetailsEbooks.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, IosDetailsEbooks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IosDetailsEbooks):
            return True

        return self.to_dict() != other.to_dict()
