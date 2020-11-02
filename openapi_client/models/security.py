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


class Security(object):
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
        'is_data_protected': 'bool',
        'is_block_level_encryption_capable': 'bool',
        'is_file_level_encryption_capable': 'bool',
        'is_passcode_present': 'bool',
        'is_passcode_compliant': 'bool',
        'is_passcode_compliant_with_profile': 'bool',
        'hardware_encryption': 'int',
        'is_activation_lock_enabled': 'bool',
        'is_jail_break_detected': 'bool'
    }

    attribute_map = {
        'is_data_protected': 'isDataProtected',
        'is_block_level_encryption_capable': 'isBlockLevelEncryptionCapable',
        'is_file_level_encryption_capable': 'isFileLevelEncryptionCapable',
        'is_passcode_present': 'isPasscodePresent',
        'is_passcode_compliant': 'isPasscodeCompliant',
        'is_passcode_compliant_with_profile': 'isPasscodeCompliantWithProfile',
        'hardware_encryption': 'hardwareEncryption',
        'is_activation_lock_enabled': 'isActivationLockEnabled',
        'is_jail_break_detected': 'isJailBreakDetected'
    }

    def __init__(self, is_data_protected=None, is_block_level_encryption_capable=None, is_file_level_encryption_capable=None, is_passcode_present=None, is_passcode_compliant=None, is_passcode_compliant_with_profile=None, hardware_encryption=None, is_activation_lock_enabled=None, is_jail_break_detected=None, local_vars_configuration=None):  # noqa: E501
        """Security - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_data_protected = None
        self._is_block_level_encryption_capable = None
        self._is_file_level_encryption_capable = None
        self._is_passcode_present = None
        self._is_passcode_compliant = None
        self._is_passcode_compliant_with_profile = None
        self._hardware_encryption = None
        self._is_activation_lock_enabled = None
        self._is_jail_break_detected = None
        self.discriminator = None

        if is_data_protected is not None:
            self.is_data_protected = is_data_protected
        if is_block_level_encryption_capable is not None:
            self.is_block_level_encryption_capable = is_block_level_encryption_capable
        if is_file_level_encryption_capable is not None:
            self.is_file_level_encryption_capable = is_file_level_encryption_capable
        if is_passcode_present is not None:
            self.is_passcode_present = is_passcode_present
        if is_passcode_compliant is not None:
            self.is_passcode_compliant = is_passcode_compliant
        if is_passcode_compliant_with_profile is not None:
            self.is_passcode_compliant_with_profile = is_passcode_compliant_with_profile
        if hardware_encryption is not None:
            self.hardware_encryption = hardware_encryption
        if is_activation_lock_enabled is not None:
            self.is_activation_lock_enabled = is_activation_lock_enabled
        if is_jail_break_detected is not None:
            self.is_jail_break_detected = is_jail_break_detected

    @property
    def is_data_protected(self):
        """Gets the is_data_protected of this Security.  # noqa: E501


        :return: The is_data_protected of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_data_protected

    @is_data_protected.setter
    def is_data_protected(self, is_data_protected):
        """Sets the is_data_protected of this Security.


        :param is_data_protected: The is_data_protected of this Security.  # noqa: E501
        :type is_data_protected: bool
        """

        self._is_data_protected = is_data_protected

    @property
    def is_block_level_encryption_capable(self):
        """Gets the is_block_level_encryption_capable of this Security.  # noqa: E501


        :return: The is_block_level_encryption_capable of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_block_level_encryption_capable

    @is_block_level_encryption_capable.setter
    def is_block_level_encryption_capable(self, is_block_level_encryption_capable):
        """Sets the is_block_level_encryption_capable of this Security.


        :param is_block_level_encryption_capable: The is_block_level_encryption_capable of this Security.  # noqa: E501
        :type is_block_level_encryption_capable: bool
        """

        self._is_block_level_encryption_capable = is_block_level_encryption_capable

    @property
    def is_file_level_encryption_capable(self):
        """Gets the is_file_level_encryption_capable of this Security.  # noqa: E501


        :return: The is_file_level_encryption_capable of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_file_level_encryption_capable

    @is_file_level_encryption_capable.setter
    def is_file_level_encryption_capable(self, is_file_level_encryption_capable):
        """Sets the is_file_level_encryption_capable of this Security.


        :param is_file_level_encryption_capable: The is_file_level_encryption_capable of this Security.  # noqa: E501
        :type is_file_level_encryption_capable: bool
        """

        self._is_file_level_encryption_capable = is_file_level_encryption_capable

    @property
    def is_passcode_present(self):
        """Gets the is_passcode_present of this Security.  # noqa: E501


        :return: The is_passcode_present of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_passcode_present

    @is_passcode_present.setter
    def is_passcode_present(self, is_passcode_present):
        """Sets the is_passcode_present of this Security.


        :param is_passcode_present: The is_passcode_present of this Security.  # noqa: E501
        :type is_passcode_present: bool
        """

        self._is_passcode_present = is_passcode_present

    @property
    def is_passcode_compliant(self):
        """Gets the is_passcode_compliant of this Security.  # noqa: E501


        :return: The is_passcode_compliant of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_passcode_compliant

    @is_passcode_compliant.setter
    def is_passcode_compliant(self, is_passcode_compliant):
        """Sets the is_passcode_compliant of this Security.


        :param is_passcode_compliant: The is_passcode_compliant of this Security.  # noqa: E501
        :type is_passcode_compliant: bool
        """

        self._is_passcode_compliant = is_passcode_compliant

    @property
    def is_passcode_compliant_with_profile(self):
        """Gets the is_passcode_compliant_with_profile of this Security.  # noqa: E501


        :return: The is_passcode_compliant_with_profile of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_passcode_compliant_with_profile

    @is_passcode_compliant_with_profile.setter
    def is_passcode_compliant_with_profile(self, is_passcode_compliant_with_profile):
        """Sets the is_passcode_compliant_with_profile of this Security.


        :param is_passcode_compliant_with_profile: The is_passcode_compliant_with_profile of this Security.  # noqa: E501
        :type is_passcode_compliant_with_profile: bool
        """

        self._is_passcode_compliant_with_profile = is_passcode_compliant_with_profile

    @property
    def hardware_encryption(self):
        """Gets the hardware_encryption of this Security.  # noqa: E501


        :return: The hardware_encryption of this Security.  # noqa: E501
        :rtype: int
        """
        return self._hardware_encryption

    @hardware_encryption.setter
    def hardware_encryption(self, hardware_encryption):
        """Sets the hardware_encryption of this Security.


        :param hardware_encryption: The hardware_encryption of this Security.  # noqa: E501
        :type hardware_encryption: int
        """

        self._hardware_encryption = hardware_encryption

    @property
    def is_activation_lock_enabled(self):
        """Gets the is_activation_lock_enabled of this Security.  # noqa: E501


        :return: The is_activation_lock_enabled of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_activation_lock_enabled

    @is_activation_lock_enabled.setter
    def is_activation_lock_enabled(self, is_activation_lock_enabled):
        """Sets the is_activation_lock_enabled of this Security.


        :param is_activation_lock_enabled: The is_activation_lock_enabled of this Security.  # noqa: E501
        :type is_activation_lock_enabled: bool
        """

        self._is_activation_lock_enabled = is_activation_lock_enabled

    @property
    def is_jail_break_detected(self):
        """Gets the is_jail_break_detected of this Security.  # noqa: E501


        :return: The is_jail_break_detected of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._is_jail_break_detected

    @is_jail_break_detected.setter
    def is_jail_break_detected(self, is_jail_break_detected):
        """Sets the is_jail_break_detected of this Security.


        :param is_jail_break_detected: The is_jail_break_detected of this Security.  # noqa: E501
        :type is_jail_break_detected: bool
        """

        self._is_jail_break_detected = is_jail_break_detected

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
        if not isinstance(other, Security):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Security):
            return True

        return self.to_dict() != other.to_dict()
