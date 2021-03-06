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


class ComputerSecurity(object):
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
        'sip_status': 'str',
        'gatekeeper_status': 'str',
        'xprotect_version': 'str',
        'auto_login_disabled': 'bool',
        'remote_desktop_enabled': 'bool',
        'activation_lock_enabled': 'bool',
        'secure_boot_level': 'str',
        'external_boot_level': 'str',
        'bootstrap_token_allowed': 'bool'
    }

    attribute_map = {
        'sip_status': 'sipStatus',
        'gatekeeper_status': 'gatekeeperStatus',
        'xprotect_version': 'xprotectVersion',
        'auto_login_disabled': 'autoLoginDisabled',
        'remote_desktop_enabled': 'remoteDesktopEnabled',
        'activation_lock_enabled': 'activationLockEnabled',
        'secure_boot_level': 'secureBootLevel',
        'external_boot_level': 'externalBootLevel',
        'bootstrap_token_allowed': 'bootstrapTokenAllowed'
    }

    def __init__(self, sip_status=None, gatekeeper_status=None, xprotect_version=None, auto_login_disabled=None, remote_desktop_enabled=None, activation_lock_enabled=None, secure_boot_level=None, external_boot_level=None, bootstrap_token_allowed=None, local_vars_configuration=None):  # noqa: E501
        """ComputerSecurity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sip_status = None
        self._gatekeeper_status = None
        self._xprotect_version = None
        self._auto_login_disabled = None
        self._remote_desktop_enabled = None
        self._activation_lock_enabled = None
        self._secure_boot_level = None
        self._external_boot_level = None
        self._bootstrap_token_allowed = None
        self.discriminator = None

        if sip_status is not None:
            self.sip_status = sip_status
        if gatekeeper_status is not None:
            self.gatekeeper_status = gatekeeper_status
        if xprotect_version is not None:
            self.xprotect_version = xprotect_version
        if auto_login_disabled is not None:
            self.auto_login_disabled = auto_login_disabled
        if remote_desktop_enabled is not None:
            self.remote_desktop_enabled = remote_desktop_enabled
        if activation_lock_enabled is not None:
            self.activation_lock_enabled = activation_lock_enabled
        if secure_boot_level is not None:
            self.secure_boot_level = secure_boot_level
        if external_boot_level is not None:
            self.external_boot_level = external_boot_level
        if bootstrap_token_allowed is not None:
            self.bootstrap_token_allowed = bootstrap_token_allowed

    @property
    def sip_status(self):
        """Gets the sip_status of this ComputerSecurity.  # noqa: E501


        :return: The sip_status of this ComputerSecurity.  # noqa: E501
        :rtype: str
        """
        return self._sip_status

    @sip_status.setter
    def sip_status(self, sip_status):
        """Sets the sip_status of this ComputerSecurity.


        :param sip_status: The sip_status of this ComputerSecurity.  # noqa: E501
        :type sip_status: str
        """
        allowed_values = ["NOT_COLLECTED", "NOT_AVAILABLE", "DISABLED", "ENABLED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sip_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sip_status` ({0}), must be one of {1}"  # noqa: E501
                .format(sip_status, allowed_values)
            )

        self._sip_status = sip_status

    @property
    def gatekeeper_status(self):
        """Gets the gatekeeper_status of this ComputerSecurity.  # noqa: E501


        :return: The gatekeeper_status of this ComputerSecurity.  # noqa: E501
        :rtype: str
        """
        return self._gatekeeper_status

    @gatekeeper_status.setter
    def gatekeeper_status(self, gatekeeper_status):
        """Sets the gatekeeper_status of this ComputerSecurity.


        :param gatekeeper_status: The gatekeeper_status of this ComputerSecurity.  # noqa: E501
        :type gatekeeper_status: str
        """
        allowed_values = ["NOT_COLLECTED", "DISABLED", "APP_STORE_AND_IDENTIFIED_DEVELOPERS", "APP_STORE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and gatekeeper_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `gatekeeper_status` ({0}), must be one of {1}"  # noqa: E501
                .format(gatekeeper_status, allowed_values)
            )

        self._gatekeeper_status = gatekeeper_status

    @property
    def xprotect_version(self):
        """Gets the xprotect_version of this ComputerSecurity.  # noqa: E501


        :return: The xprotect_version of this ComputerSecurity.  # noqa: E501
        :rtype: str
        """
        return self._xprotect_version

    @xprotect_version.setter
    def xprotect_version(self, xprotect_version):
        """Sets the xprotect_version of this ComputerSecurity.


        :param xprotect_version: The xprotect_version of this ComputerSecurity.  # noqa: E501
        :type xprotect_version: str
        """

        self._xprotect_version = xprotect_version

    @property
    def auto_login_disabled(self):
        """Gets the auto_login_disabled of this ComputerSecurity.  # noqa: E501


        :return: The auto_login_disabled of this ComputerSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._auto_login_disabled

    @auto_login_disabled.setter
    def auto_login_disabled(self, auto_login_disabled):
        """Sets the auto_login_disabled of this ComputerSecurity.


        :param auto_login_disabled: The auto_login_disabled of this ComputerSecurity.  # noqa: E501
        :type auto_login_disabled: bool
        """

        self._auto_login_disabled = auto_login_disabled

    @property
    def remote_desktop_enabled(self):
        """Gets the remote_desktop_enabled of this ComputerSecurity.  # noqa: E501

        Collected for macOS 10.14.4 or later  # noqa: E501

        :return: The remote_desktop_enabled of this ComputerSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._remote_desktop_enabled

    @remote_desktop_enabled.setter
    def remote_desktop_enabled(self, remote_desktop_enabled):
        """Sets the remote_desktop_enabled of this ComputerSecurity.

        Collected for macOS 10.14.4 or later  # noqa: E501

        :param remote_desktop_enabled: The remote_desktop_enabled of this ComputerSecurity.  # noqa: E501
        :type remote_desktop_enabled: bool
        """

        self._remote_desktop_enabled = remote_desktop_enabled

    @property
    def activation_lock_enabled(self):
        """Gets the activation_lock_enabled of this ComputerSecurity.  # noqa: E501

        Collected for macOS 10.15.0 or later  # noqa: E501

        :return: The activation_lock_enabled of this ComputerSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._activation_lock_enabled

    @activation_lock_enabled.setter
    def activation_lock_enabled(self, activation_lock_enabled):
        """Sets the activation_lock_enabled of this ComputerSecurity.

        Collected for macOS 10.15.0 or later  # noqa: E501

        :param activation_lock_enabled: The activation_lock_enabled of this ComputerSecurity.  # noqa: E501
        :type activation_lock_enabled: bool
        """

        self._activation_lock_enabled = activation_lock_enabled

    @property
    def secure_boot_level(self):
        """Gets the secure_boot_level of this ComputerSecurity.  # noqa: E501

        Collected for macOS 10.15.0 or later  # noqa: E501

        :return: The secure_boot_level of this ComputerSecurity.  # noqa: E501
        :rtype: str
        """
        return self._secure_boot_level

    @secure_boot_level.setter
    def secure_boot_level(self, secure_boot_level):
        """Sets the secure_boot_level of this ComputerSecurity.

        Collected for macOS 10.15.0 or later  # noqa: E501

        :param secure_boot_level: The secure_boot_level of this ComputerSecurity.  # noqa: E501
        :type secure_boot_level: str
        """
        allowed_values = ["NO_SECURITY", "MEDIUM_SECURITY", "FULL_SECURITY", "NOT_SUPPORTED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and secure_boot_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `secure_boot_level` ({0}), must be one of {1}"  # noqa: E501
                .format(secure_boot_level, allowed_values)
            )

        self._secure_boot_level = secure_boot_level

    @property
    def external_boot_level(self):
        """Gets the external_boot_level of this ComputerSecurity.  # noqa: E501

        Collected for macOS 10.15.0 or later  # noqa: E501

        :return: The external_boot_level of this ComputerSecurity.  # noqa: E501
        :rtype: str
        """
        return self._external_boot_level

    @external_boot_level.setter
    def external_boot_level(self, external_boot_level):
        """Sets the external_boot_level of this ComputerSecurity.

        Collected for macOS 10.15.0 or later  # noqa: E501

        :param external_boot_level: The external_boot_level of this ComputerSecurity.  # noqa: E501
        :type external_boot_level: str
        """
        allowed_values = ["ALLOW_BOOTING_FROM_EXTERNAL_MEDIA", "DISALLOW_BOOTING_FROM_EXTERNAL_MEDIA", "NOT_SUPPORTED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and external_boot_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `external_boot_level` ({0}), must be one of {1}"  # noqa: E501
                .format(external_boot_level, allowed_values)
            )

        self._external_boot_level = external_boot_level

    @property
    def bootstrap_token_allowed(self):
        """Gets the bootstrap_token_allowed of this ComputerSecurity.  # noqa: E501

        Collected for macOS 11 or later  # noqa: E501

        :return: The bootstrap_token_allowed of this ComputerSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_token_allowed

    @bootstrap_token_allowed.setter
    def bootstrap_token_allowed(self, bootstrap_token_allowed):
        """Sets the bootstrap_token_allowed of this ComputerSecurity.

        Collected for macOS 11 or later  # noqa: E501

        :param bootstrap_token_allowed: The bootstrap_token_allowed of this ComputerSecurity.  # noqa: E501
        :type bootstrap_token_allowed: bool
        """

        self._bootstrap_token_allowed = bootstrap_token_allowed

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
        if not isinstance(other, ComputerSecurity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerSecurity):
            return True

        return self.to_dict() != other.to_dict()
