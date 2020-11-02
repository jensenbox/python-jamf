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


class IosDetailsApplications(object):
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
        'identifier': 'str',
        'name': 'str',
        'version': 'str',
        'short_version': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'version': 'version',
        'short_version': 'shortVersion'
    }

    def __init__(self, identifier=None, name=None, version=None, short_version=None, local_vars_configuration=None):  # noqa: E501
        """IosDetailsApplications - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._identifier = None
        self._name = None
        self._version = None
        self._short_version = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if short_version is not None:
            self.short_version = short_version

    @property
    def identifier(self):
        """Gets the identifier of this IosDetailsApplications.  # noqa: E501


        :return: The identifier of this IosDetailsApplications.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this IosDetailsApplications.


        :param identifier: The identifier of this IosDetailsApplications.  # noqa: E501
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this IosDetailsApplications.  # noqa: E501


        :return: The name of this IosDetailsApplications.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IosDetailsApplications.


        :param name: The name of this IosDetailsApplications.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this IosDetailsApplications.  # noqa: E501


        :return: The version of this IosDetailsApplications.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IosDetailsApplications.


        :param version: The version of this IosDetailsApplications.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def short_version(self):
        """Gets the short_version of this IosDetailsApplications.  # noqa: E501


        :return: The short_version of this IosDetailsApplications.  # noqa: E501
        :rtype: str
        """
        return self._short_version

    @short_version.setter
    def short_version(self, short_version):
        """Sets the short_version of this IosDetailsApplications.


        :param short_version: The short_version of this IosDetailsApplications.  # noqa: E501
        :type short_version: str
        """

        self._short_version = short_version

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
        if not isinstance(other, IosDetailsApplications):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IosDetailsApplications):
            return True

        return self.to_dict() != other.to_dict()