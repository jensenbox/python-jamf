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


class CloudLdapConfigurationRequest(object):
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
        'server': 'CloudLdapServerRequest',
        'mappings': 'CloudLdapMappingsRequest'
    }

    attribute_map = {
        'server': 'server',
        'mappings': 'mappings'
    }

    def __init__(self, server=None, mappings=None, local_vars_configuration=None):  # noqa: E501
        """CloudLdapConfigurationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._server = None
        self._mappings = None
        self.discriminator = None

        self.server = server
        if mappings is not None:
            self.mappings = mappings

    @property
    def server(self):
        """Gets the server of this CloudLdapConfigurationRequest.  # noqa: E501


        :return: The server of this CloudLdapConfigurationRequest.  # noqa: E501
        :rtype: CloudLdapServerRequest
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this CloudLdapConfigurationRequest.


        :param server: The server of this CloudLdapConfigurationRequest.  # noqa: E501
        :type server: CloudLdapServerRequest
        """
        if self.local_vars_configuration.client_side_validation and server is None:  # noqa: E501
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

    @property
    def mappings(self):
        """Gets the mappings of this CloudLdapConfigurationRequest.  # noqa: E501


        :return: The mappings of this CloudLdapConfigurationRequest.  # noqa: E501
        :rtype: CloudLdapMappingsRequest
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this CloudLdapConfigurationRequest.


        :param mappings: The mappings of this CloudLdapConfigurationRequest.  # noqa: E501
        :type mappings: CloudLdapMappingsRequest
        """

        self._mappings = mappings

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
        if not isinstance(other, CloudLdapConfigurationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLdapConfigurationRequest):
            return True

        return self.to_dict() != other.to_dict()
