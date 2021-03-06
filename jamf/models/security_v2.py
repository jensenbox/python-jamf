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


class SecurityV2(object):
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
        'data_protected': 'bool',
        'block_level_encryption_capable': 'bool',
        'file_level_encryption_capable': 'bool',
        'passcode_present': 'bool',
        'passcode_compliant': 'bool',
        'passcode_compliant_with_profile': 'bool',
        'hardware_encryption': 'int',
        'activation_lock_enabled': 'bool',
        'jail_break_detected': 'bool'
    }

    attribute_map = {
        'data_protected': 'dataProtected',
        'block_level_encryption_capable': 'blockLevelEncryptionCapable',
        'file_level_encryption_capable': 'fileLevelEncryptionCapable',
        'passcode_present': 'passcodePresent',
        'passcode_compliant': 'passcodeCompliant',
        'passcode_compliant_with_profile': 'passcodeCompliantWithProfile',
        'hardware_encryption': 'hardwareEncryption',
        'activation_lock_enabled': 'activationLockEnabled',
        'jail_break_detected': 'jailBreakDetected'
    }

    def __init__(self, data_protected=None, block_level_encryption_capable=None, file_level_encryption_capable=None, passcode_present=None, passcode_compliant=None, passcode_compliant_with_profile=None, hardware_encryption=None, activation_lock_enabled=None, jail_break_detected=None, local_vars_configuration=None):  # noqa: E501
        """SecurityV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_protected = None
        self._block_level_encryption_capable = None
        self._file_level_encryption_capable = None
        self._passcode_present = None
        self._passcode_compliant = None
        self._passcode_compliant_with_profile = None
        self._hardware_encryption = None
        self._activation_lock_enabled = None
        self._jail_break_detected = None
        self.discriminator = None

        if data_protected is not None:
            self.data_protected = data_protected
        if block_level_encryption_capable is not None:
            self.block_level_encryption_capable = block_level_encryption_capable
        if file_level_encryption_capable is not None:
            self.file_level_encryption_capable = file_level_encryption_capable
        if passcode_present is not None:
            self.passcode_present = passcode_present
        if passcode_compliant is not None:
            self.passcode_compliant = passcode_compliant
        if passcode_compliant_with_profile is not None:
            self.passcode_compliant_with_profile = passcode_compliant_with_profile
        if hardware_encryption is not None:
            self.hardware_encryption = hardware_encryption
        if activation_lock_enabled is not None:
            self.activation_lock_enabled = activation_lock_enabled
        if jail_break_detected is not None:
            self.jail_break_detected = jail_break_detected

    @property
    def data_protected(self):
        """Gets the data_protected of this SecurityV2.  # noqa: E501


        :return: The data_protected of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._data_protected

    @data_protected.setter
    def data_protected(self, data_protected):
        """Sets the data_protected of this SecurityV2.


        :param data_protected: The data_protected of this SecurityV2.  # noqa: E501
        :type data_protected: bool
        """

        self._data_protected = data_protected

    @property
    def block_level_encryption_capable(self):
        """Gets the block_level_encryption_capable of this SecurityV2.  # noqa: E501


        :return: The block_level_encryption_capable of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._block_level_encryption_capable

    @block_level_encryption_capable.setter
    def block_level_encryption_capable(self, block_level_encryption_capable):
        """Sets the block_level_encryption_capable of this SecurityV2.


        :param block_level_encryption_capable: The block_level_encryption_capable of this SecurityV2.  # noqa: E501
        :type block_level_encryption_capable: bool
        """

        self._block_level_encryption_capable = block_level_encryption_capable

    @property
    def file_level_encryption_capable(self):
        """Gets the file_level_encryption_capable of this SecurityV2.  # noqa: E501


        :return: The file_level_encryption_capable of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._file_level_encryption_capable

    @file_level_encryption_capable.setter
    def file_level_encryption_capable(self, file_level_encryption_capable):
        """Sets the file_level_encryption_capable of this SecurityV2.


        :param file_level_encryption_capable: The file_level_encryption_capable of this SecurityV2.  # noqa: E501
        :type file_level_encryption_capable: bool
        """

        self._file_level_encryption_capable = file_level_encryption_capable

    @property
    def passcode_present(self):
        """Gets the passcode_present of this SecurityV2.  # noqa: E501


        :return: The passcode_present of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._passcode_present

    @passcode_present.setter
    def passcode_present(self, passcode_present):
        """Sets the passcode_present of this SecurityV2.


        :param passcode_present: The passcode_present of this SecurityV2.  # noqa: E501
        :type passcode_present: bool
        """

        self._passcode_present = passcode_present

    @property
    def passcode_compliant(self):
        """Gets the passcode_compliant of this SecurityV2.  # noqa: E501


        :return: The passcode_compliant of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._passcode_compliant

    @passcode_compliant.setter
    def passcode_compliant(self, passcode_compliant):
        """Sets the passcode_compliant of this SecurityV2.


        :param passcode_compliant: The passcode_compliant of this SecurityV2.  # noqa: E501
        :type passcode_compliant: bool
        """

        self._passcode_compliant = passcode_compliant

    @property
    def passcode_compliant_with_profile(self):
        """Gets the passcode_compliant_with_profile of this SecurityV2.  # noqa: E501


        :return: The passcode_compliant_with_profile of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._passcode_compliant_with_profile

    @passcode_compliant_with_profile.setter
    def passcode_compliant_with_profile(self, passcode_compliant_with_profile):
        """Sets the passcode_compliant_with_profile of this SecurityV2.


        :param passcode_compliant_with_profile: The passcode_compliant_with_profile of this SecurityV2.  # noqa: E501
        :type passcode_compliant_with_profile: bool
        """

        self._passcode_compliant_with_profile = passcode_compliant_with_profile

    @property
    def hardware_encryption(self):
        """Gets the hardware_encryption of this SecurityV2.  # noqa: E501


        :return: The hardware_encryption of this SecurityV2.  # noqa: E501
        :rtype: int
        """
        return self._hardware_encryption

    @hardware_encryption.setter
    def hardware_encryption(self, hardware_encryption):
        """Sets the hardware_encryption of this SecurityV2.


        :param hardware_encryption: The hardware_encryption of this SecurityV2.  # noqa: E501
        :type hardware_encryption: int
        """

        self._hardware_encryption = hardware_encryption

    @property
    def activation_lock_enabled(self):
        """Gets the activation_lock_enabled of this SecurityV2.  # noqa: E501


        :return: The activation_lock_enabled of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._activation_lock_enabled

    @activation_lock_enabled.setter
    def activation_lock_enabled(self, activation_lock_enabled):
        """Sets the activation_lock_enabled of this SecurityV2.


        :param activation_lock_enabled: The activation_lock_enabled of this SecurityV2.  # noqa: E501
        :type activation_lock_enabled: bool
        """

        self._activation_lock_enabled = activation_lock_enabled

    @property
    def jail_break_detected(self):
        """Gets the jail_break_detected of this SecurityV2.  # noqa: E501


        :return: The jail_break_detected of this SecurityV2.  # noqa: E501
        :rtype: bool
        """
        return self._jail_break_detected

    @jail_break_detected.setter
    def jail_break_detected(self, jail_break_detected):
        """Sets the jail_break_detected of this SecurityV2.


        :param jail_break_detected: The jail_break_detected of this SecurityV2.  # noqa: E501
        :type jail_break_detected: bool
        """

        self._jail_break_detected = jail_break_detected

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
        if not isinstance(other, SecurityV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityV2):
            return True

        return self.to_dict() != other.to_dict()
