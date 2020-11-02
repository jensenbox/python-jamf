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


class CloudLdapServerRequest(object):
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
        'enabled': 'bool',
        'provider_name': 'str',
        'display_name': 'str',
        'server_url': 'str',
        'domain_name': 'str',
        'port': 'int',
        'keystore': 'CloudLdapKeystoreFile',
        'connection_timeout': 'int',
        'search_timeout': 'int',
        'use_wildcards': 'bool',
        'connection_type': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'provider_name': 'providerName',
        'display_name': 'displayName',
        'server_url': 'serverUrl',
        'domain_name': 'domainName',
        'port': 'port',
        'keystore': 'keystore',
        'connection_timeout': 'connectionTimeout',
        'search_timeout': 'searchTimeout',
        'use_wildcards': 'useWildcards',
        'connection_type': 'connectionType'
    }

    def __init__(self, enabled=None, provider_name=None, display_name=None, server_url=None, domain_name=None, port=None, keystore=None, connection_timeout=None, search_timeout=None, use_wildcards=None, connection_type=None, local_vars_configuration=None):  # noqa: E501
        """CloudLdapServerRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._provider_name = None
        self._display_name = None
        self._server_url = None
        self._domain_name = None
        self._port = None
        self._keystore = None
        self._connection_timeout = None
        self._search_timeout = None
        self._use_wildcards = None
        self._connection_type = None
        self.discriminator = None

        self.enabled = enabled
        self.provider_name = provider_name
        self.display_name = display_name
        self.server_url = server_url
        self.domain_name = domain_name
        self.port = port
        self.keystore = keystore
        self.connection_timeout = connection_timeout
        self.search_timeout = search_timeout
        self.use_wildcards = use_wildcards
        self.connection_type = connection_type

    @property
    def enabled(self):
        """Gets the enabled of this CloudLdapServerRequest.  # noqa: E501


        :return: The enabled of this CloudLdapServerRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudLdapServerRequest.


        :param enabled: The enabled of this CloudLdapServerRequest.  # noqa: E501
        :type enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def provider_name(self):
        """Gets the provider_name of this CloudLdapServerRequest.  # noqa: E501


        :return: The provider_name of this CloudLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this CloudLdapServerRequest.


        :param provider_name: The provider_name of this CloudLdapServerRequest.  # noqa: E501
        :type provider_name: str
        """
        if self.local_vars_configuration.client_side_validation and provider_name is None:  # noqa: E501
            raise ValueError("Invalid value for `provider_name`, must not be `None`")  # noqa: E501

        self._provider_name = provider_name

    @property
    def display_name(self):
        """Gets the display_name of this CloudLdapServerRequest.  # noqa: E501


        :return: The display_name of this CloudLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CloudLdapServerRequest.


        :param display_name: The display_name of this CloudLdapServerRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def server_url(self):
        """Gets the server_url of this CloudLdapServerRequest.  # noqa: E501


        :return: The server_url of this CloudLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this CloudLdapServerRequest.


        :param server_url: The server_url of this CloudLdapServerRequest.  # noqa: E501
        :type server_url: str
        """
        if self.local_vars_configuration.client_side_validation and server_url is None:  # noqa: E501
            raise ValueError("Invalid value for `server_url`, must not be `None`")  # noqa: E501

        self._server_url = server_url

    @property
    def domain_name(self):
        """Gets the domain_name of this CloudLdapServerRequest.  # noqa: E501


        :return: The domain_name of this CloudLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CloudLdapServerRequest.


        :param domain_name: The domain_name of this CloudLdapServerRequest.  # noqa: E501
        :type domain_name: str
        """
        if self.local_vars_configuration.client_side_validation and domain_name is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_name`, must not be `None`")  # noqa: E501

        self._domain_name = domain_name

    @property
    def port(self):
        """Gets the port of this CloudLdapServerRequest.  # noqa: E501


        :return: The port of this CloudLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CloudLdapServerRequest.


        :param port: The port of this CloudLdapServerRequest.  # noqa: E501
        :type port: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port < 1):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def keystore(self):
        """Gets the keystore of this CloudLdapServerRequest.  # noqa: E501


        :return: The keystore of this CloudLdapServerRequest.  # noqa: E501
        :rtype: CloudLdapKeystoreFile
        """
        return self._keystore

    @keystore.setter
    def keystore(self, keystore):
        """Sets the keystore of this CloudLdapServerRequest.


        :param keystore: The keystore of this CloudLdapServerRequest.  # noqa: E501
        :type keystore: CloudLdapKeystoreFile
        """
        if self.local_vars_configuration.client_side_validation and keystore is None:  # noqa: E501
            raise ValueError("Invalid value for `keystore`, must not be `None`")  # noqa: E501

        self._keystore = keystore

    @property
    def connection_timeout(self):
        """Gets the connection_timeout of this CloudLdapServerRequest.  # noqa: E501


        :return: The connection_timeout of this CloudLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection_timeout of this CloudLdapServerRequest.


        :param connection_timeout: The connection_timeout of this CloudLdapServerRequest.  # noqa: E501
        :type connection_timeout: int
        """
        if self.local_vars_configuration.client_side_validation and connection_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_timeout is not None and connection_timeout > 600):  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_timeout is not None and connection_timeout < 5):  # noqa: E501
            raise ValueError("Invalid value for `connection_timeout`, must be a value greater than or equal to `5`")  # noqa: E501

        self._connection_timeout = connection_timeout

    @property
    def search_timeout(self):
        """Gets the search_timeout of this CloudLdapServerRequest.  # noqa: E501


        :return: The search_timeout of this CloudLdapServerRequest.  # noqa: E501
        :rtype: int
        """
        return self._search_timeout

    @search_timeout.setter
    def search_timeout(self, search_timeout):
        """Sets the search_timeout of this CloudLdapServerRequest.


        :param search_timeout: The search_timeout of this CloudLdapServerRequest.  # noqa: E501
        :type search_timeout: int
        """
        if self.local_vars_configuration.client_side_validation and search_timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `search_timeout`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                search_timeout is not None and search_timeout > 600):  # noqa: E501
            raise ValueError("Invalid value for `search_timeout`, must be a value less than or equal to `600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                search_timeout is not None and search_timeout < 5):  # noqa: E501
            raise ValueError("Invalid value for `search_timeout`, must be a value greater than or equal to `5`")  # noqa: E501

        self._search_timeout = search_timeout

    @property
    def use_wildcards(self):
        """Gets the use_wildcards of this CloudLdapServerRequest.  # noqa: E501


        :return: The use_wildcards of this CloudLdapServerRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_wildcards

    @use_wildcards.setter
    def use_wildcards(self, use_wildcards):
        """Sets the use_wildcards of this CloudLdapServerRequest.


        :param use_wildcards: The use_wildcards of this CloudLdapServerRequest.  # noqa: E501
        :type use_wildcards: bool
        """
        if self.local_vars_configuration.client_side_validation and use_wildcards is None:  # noqa: E501
            raise ValueError("Invalid value for `use_wildcards`, must not be `None`")  # noqa: E501

        self._use_wildcards = use_wildcards

    @property
    def connection_type(self):
        """Gets the connection_type of this CloudLdapServerRequest.  # noqa: E501


        :return: The connection_type of this CloudLdapServerRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this CloudLdapServerRequest.


        :param connection_type: The connection_type of this CloudLdapServerRequest.  # noqa: E501
        :type connection_type: str
        """
        if self.local_vars_configuration.client_side_validation and connection_type is None:  # noqa: E501
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LDAPS", "START_TLS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and connection_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

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
        if not isinstance(other, CloudLdapServerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudLdapServerRequest):
            return True

        return self.to_dict() != other.to_dict()
