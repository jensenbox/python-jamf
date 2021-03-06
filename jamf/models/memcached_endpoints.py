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


class MemcachedEndpoints(object):
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
        'host_name': 'str',
        'port': 'int',
        'enabled': 'bool',
        'jss_cache_configuration_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'host_name': 'hostName',
        'port': 'port',
        'enabled': 'enabled',
        'jss_cache_configuration_id': 'jssCacheConfigurationId'
    }

    def __init__(self, id=None, name=None, host_name=None, port=None, enabled=None, jss_cache_configuration_id=None, local_vars_configuration=None):  # noqa: E501
        """MemcachedEndpoints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._host_name = None
        self._port = None
        self._enabled = None
        self._jss_cache_configuration_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if host_name is not None:
            self.host_name = host_name
        if port is not None:
            self.port = port
        if enabled is not None:
            self.enabled = enabled
        if jss_cache_configuration_id is not None:
            self.jss_cache_configuration_id = jss_cache_configuration_id

    @property
    def id(self):
        """Gets the id of this MemcachedEndpoints.  # noqa: E501


        :return: The id of this MemcachedEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MemcachedEndpoints.


        :param id: The id of this MemcachedEndpoints.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MemcachedEndpoints.  # noqa: E501


        :return: The name of this MemcachedEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MemcachedEndpoints.


        :param name: The name of this MemcachedEndpoints.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def host_name(self):
        """Gets the host_name of this MemcachedEndpoints.  # noqa: E501


        :return: The host_name of this MemcachedEndpoints.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this MemcachedEndpoints.


        :param host_name: The host_name of this MemcachedEndpoints.  # noqa: E501
        :type host_name: str
        """

        self._host_name = host_name

    @property
    def port(self):
        """Gets the port of this MemcachedEndpoints.  # noqa: E501


        :return: The port of this MemcachedEndpoints.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MemcachedEndpoints.


        :param port: The port of this MemcachedEndpoints.  # noqa: E501
        :type port: int
        """

        self._port = port

    @property
    def enabled(self):
        """Gets the enabled of this MemcachedEndpoints.  # noqa: E501


        :return: The enabled of this MemcachedEndpoints.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MemcachedEndpoints.


        :param enabled: The enabled of this MemcachedEndpoints.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def jss_cache_configuration_id(self):
        """Gets the jss_cache_configuration_id of this MemcachedEndpoints.  # noqa: E501


        :return: The jss_cache_configuration_id of this MemcachedEndpoints.  # noqa: E501
        :rtype: int
        """
        return self._jss_cache_configuration_id

    @jss_cache_configuration_id.setter
    def jss_cache_configuration_id(self, jss_cache_configuration_id):
        """Sets the jss_cache_configuration_id of this MemcachedEndpoints.


        :param jss_cache_configuration_id: The jss_cache_configuration_id of this MemcachedEndpoints.  # noqa: E501
        :type jss_cache_configuration_id: int
        """

        self._jss_cache_configuration_id = jss_cache_configuration_id

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
        if not isinstance(other, MemcachedEndpoints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemcachedEndpoints):
            return True

        return self.to_dict() != other.to_dict()
