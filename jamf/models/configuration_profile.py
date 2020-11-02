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


class ConfigurationProfile(object):
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
        'version': 'str',
        'uuid': 'str',
        'identifier': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'version': 'version',
        'uuid': 'uuid',
        'identifier': 'identifier'
    }

    def __init__(self, display_name=None, version=None, uuid=None, identifier=None, local_vars_configuration=None):  # noqa: E501
        """ConfigurationProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._version = None
        self._uuid = None
        self._identifier = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version
        if uuid is not None:
            self.uuid = uuid
        if identifier is not None:
            self.identifier = identifier

    @property
    def display_name(self):
        """Gets the display_name of this ConfigurationProfile.  # noqa: E501


        :return: The display_name of this ConfigurationProfile.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ConfigurationProfile.


        :param display_name: The display_name of this ConfigurationProfile.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this ConfigurationProfile.  # noqa: E501


        :return: The version of this ConfigurationProfile.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ConfigurationProfile.


        :param version: The version of this ConfigurationProfile.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def uuid(self):
        """Gets the uuid of this ConfigurationProfile.  # noqa: E501


        :return: The uuid of this ConfigurationProfile.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ConfigurationProfile.


        :param uuid: The uuid of this ConfigurationProfile.  # noqa: E501
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def identifier(self):
        """Gets the identifier of this ConfigurationProfile.  # noqa: E501


        :return: The identifier of this ConfigurationProfile.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ConfigurationProfile.


        :param identifier: The identifier of this ConfigurationProfile.  # noqa: E501
        :type identifier: str
        """

        self._identifier = identifier

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
        if not isinstance(other, ConfigurationProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationProfile):
            return True

        return self.to_dict() != other.to_dict()
