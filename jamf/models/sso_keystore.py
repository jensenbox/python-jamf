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


class SsoKeystore(object):
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
        'keys': 'list[CertificateKey]',
        'key': 'str',
        'password': 'str',
        'type': 'str',
        'keystore_setup_type': 'str'
    }

    attribute_map = {
        'keys': 'keys',
        'key': 'key',
        'password': 'password',
        'type': 'type',
        'keystore_setup_type': 'keystoreSetupType'
    }

    def __init__(self, keys=None, key=' ', password=None, type=None, keystore_setup_type=None, local_vars_configuration=None):  # noqa: E501
        """SsoKeystore - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keys = None
        self._key = None
        self._password = None
        self._type = None
        self._keystore_setup_type = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        self.key = key
        self.password = password
        self.type = type
        if keystore_setup_type is not None:
            self.keystore_setup_type = keystore_setup_type

    @property
    def keys(self):
        """Gets the keys of this SsoKeystore.  # noqa: E501


        :return: The keys of this SsoKeystore.  # noqa: E501
        :rtype: list[CertificateKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this SsoKeystore.


        :param keys: The keys of this SsoKeystore.  # noqa: E501
        :type keys: list[CertificateKey]
        """

        self._keys = keys

    @property
    def key(self):
        """Gets the key of this SsoKeystore.  # noqa: E501


        :return: The key of this SsoKeystore.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SsoKeystore.


        :param key: The key of this SsoKeystore.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def password(self):
        """Gets the password of this SsoKeystore.  # noqa: E501


        :return: The password of this SsoKeystore.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SsoKeystore.


        :param password: The password of this SsoKeystore.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def type(self):
        """Gets the type of this SsoKeystore.  # noqa: E501


        :return: The type of this SsoKeystore.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SsoKeystore.


        :param type: The type of this SsoKeystore.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["PKCS12", "JKS", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def keystore_setup_type(self):
        """Gets the keystore_setup_type of this SsoKeystore.  # noqa: E501


        :return: The keystore_setup_type of this SsoKeystore.  # noqa: E501
        :rtype: str
        """
        return self._keystore_setup_type

    @keystore_setup_type.setter
    def keystore_setup_type(self, keystore_setup_type):
        """Sets the keystore_setup_type of this SsoKeystore.


        :param keystore_setup_type: The keystore_setup_type of this SsoKeystore.  # noqa: E501
        :type keystore_setup_type: str
        """
        allowed_values = ["NONE", "UPLOADED", "GENERATED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and keystore_setup_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `keystore_setup_type` ({0}), must be one of {1}"  # noqa: E501
                .format(keystore_setup_type, allowed_values)
            )

        self._keystore_setup_type = keystore_setup_type

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
        if not isinstance(other, SsoKeystore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SsoKeystore):
            return True

        return self.to_dict() != other.to_dict()
