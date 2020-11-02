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


class ClientCheckIn(object):
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
        'check_in_frequency': 'int',
        'is_create_hooks': 'bool',
        'is_hook_log': 'bool',
        'is_hook_policies': 'bool',
        'is_hook_hide_restore': 'bool',
        'is_hook_mcx': 'bool',
        'is_background_hooks': 'bool',
        'is_hook_display_status': 'bool',
        'is_create_startup_script': 'bool',
        'is_startup_log': 'bool',
        'is_startup_policies': 'bool',
        'is_startup_ssh': 'bool',
        'is_startup_mcx': 'bool',
        'is_enable_local_configuration_profiles': 'bool'
    }

    attribute_map = {
        'check_in_frequency': 'checkInFrequency',
        'is_create_hooks': 'isCreateHooks',
        'is_hook_log': 'isHookLog',
        'is_hook_policies': 'isHookPolicies',
        'is_hook_hide_restore': 'isHookHideRestore',
        'is_hook_mcx': 'isHookMCX',
        'is_background_hooks': 'isBackgroundHooks',
        'is_hook_display_status': 'isHookDisplayStatus',
        'is_create_startup_script': 'isCreateStartupScript',
        'is_startup_log': 'isStartupLog',
        'is_startup_policies': 'isStartupPolicies',
        'is_startup_ssh': 'isStartupSSH',
        'is_startup_mcx': 'isStartupMCX',
        'is_enable_local_configuration_profiles': 'isEnableLocalConfigurationProfiles'
    }

    def __init__(self, check_in_frequency=15, is_create_hooks=False, is_hook_log=False, is_hook_policies=False, is_hook_hide_restore=False, is_hook_mcx=False, is_background_hooks=False, is_hook_display_status=False, is_create_startup_script=False, is_startup_log=False, is_startup_policies=False, is_startup_ssh=False, is_startup_mcx=False, is_enable_local_configuration_profiles=False, local_vars_configuration=None):  # noqa: E501
        """ClientCheckIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_in_frequency = None
        self._is_create_hooks = None
        self._is_hook_log = None
        self._is_hook_policies = None
        self._is_hook_hide_restore = None
        self._is_hook_mcx = None
        self._is_background_hooks = None
        self._is_hook_display_status = None
        self._is_create_startup_script = None
        self._is_startup_log = None
        self._is_startup_policies = None
        self._is_startup_ssh = None
        self._is_startup_mcx = None
        self._is_enable_local_configuration_profiles = None
        self.discriminator = None

        if check_in_frequency is not None:
            self.check_in_frequency = check_in_frequency
        if is_create_hooks is not None:
            self.is_create_hooks = is_create_hooks
        if is_hook_log is not None:
            self.is_hook_log = is_hook_log
        if is_hook_policies is not None:
            self.is_hook_policies = is_hook_policies
        if is_hook_hide_restore is not None:
            self.is_hook_hide_restore = is_hook_hide_restore
        if is_hook_mcx is not None:
            self.is_hook_mcx = is_hook_mcx
        if is_background_hooks is not None:
            self.is_background_hooks = is_background_hooks
        if is_hook_display_status is not None:
            self.is_hook_display_status = is_hook_display_status
        if is_create_startup_script is not None:
            self.is_create_startup_script = is_create_startup_script
        if is_startup_log is not None:
            self.is_startup_log = is_startup_log
        if is_startup_policies is not None:
            self.is_startup_policies = is_startup_policies
        if is_startup_ssh is not None:
            self.is_startup_ssh = is_startup_ssh
        if is_startup_mcx is not None:
            self.is_startup_mcx = is_startup_mcx
        if is_enable_local_configuration_profiles is not None:
            self.is_enable_local_configuration_profiles = is_enable_local_configuration_profiles

    @property
    def check_in_frequency(self):
        """Gets the check_in_frequency of this ClientCheckIn.  # noqa: E501


        :return: The check_in_frequency of this ClientCheckIn.  # noqa: E501
        :rtype: int
        """
        return self._check_in_frequency

    @check_in_frequency.setter
    def check_in_frequency(self, check_in_frequency):
        """Sets the check_in_frequency of this ClientCheckIn.


        :param check_in_frequency: The check_in_frequency of this ClientCheckIn.  # noqa: E501
        :type check_in_frequency: int
        """

        self._check_in_frequency = check_in_frequency

    @property
    def is_create_hooks(self):
        """Gets the is_create_hooks of this ClientCheckIn.  # noqa: E501


        :return: The is_create_hooks of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_create_hooks

    @is_create_hooks.setter
    def is_create_hooks(self, is_create_hooks):
        """Sets the is_create_hooks of this ClientCheckIn.


        :param is_create_hooks: The is_create_hooks of this ClientCheckIn.  # noqa: E501
        :type is_create_hooks: bool
        """

        self._is_create_hooks = is_create_hooks

    @property
    def is_hook_log(self):
        """Gets the is_hook_log of this ClientCheckIn.  # noqa: E501


        :return: The is_hook_log of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_hook_log

    @is_hook_log.setter
    def is_hook_log(self, is_hook_log):
        """Sets the is_hook_log of this ClientCheckIn.


        :param is_hook_log: The is_hook_log of this ClientCheckIn.  # noqa: E501
        :type is_hook_log: bool
        """

        self._is_hook_log = is_hook_log

    @property
    def is_hook_policies(self):
        """Gets the is_hook_policies of this ClientCheckIn.  # noqa: E501


        :return: The is_hook_policies of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_hook_policies

    @is_hook_policies.setter
    def is_hook_policies(self, is_hook_policies):
        """Sets the is_hook_policies of this ClientCheckIn.


        :param is_hook_policies: The is_hook_policies of this ClientCheckIn.  # noqa: E501
        :type is_hook_policies: bool
        """

        self._is_hook_policies = is_hook_policies

    @property
    def is_hook_hide_restore(self):
        """Gets the is_hook_hide_restore of this ClientCheckIn.  # noqa: E501


        :return: The is_hook_hide_restore of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_hook_hide_restore

    @is_hook_hide_restore.setter
    def is_hook_hide_restore(self, is_hook_hide_restore):
        """Sets the is_hook_hide_restore of this ClientCheckIn.


        :param is_hook_hide_restore: The is_hook_hide_restore of this ClientCheckIn.  # noqa: E501
        :type is_hook_hide_restore: bool
        """

        self._is_hook_hide_restore = is_hook_hide_restore

    @property
    def is_hook_mcx(self):
        """Gets the is_hook_mcx of this ClientCheckIn.  # noqa: E501


        :return: The is_hook_mcx of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_hook_mcx

    @is_hook_mcx.setter
    def is_hook_mcx(self, is_hook_mcx):
        """Sets the is_hook_mcx of this ClientCheckIn.


        :param is_hook_mcx: The is_hook_mcx of this ClientCheckIn.  # noqa: E501
        :type is_hook_mcx: bool
        """

        self._is_hook_mcx = is_hook_mcx

    @property
    def is_background_hooks(self):
        """Gets the is_background_hooks of this ClientCheckIn.  # noqa: E501


        :return: The is_background_hooks of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_background_hooks

    @is_background_hooks.setter
    def is_background_hooks(self, is_background_hooks):
        """Sets the is_background_hooks of this ClientCheckIn.


        :param is_background_hooks: The is_background_hooks of this ClientCheckIn.  # noqa: E501
        :type is_background_hooks: bool
        """

        self._is_background_hooks = is_background_hooks

    @property
    def is_hook_display_status(self):
        """Gets the is_hook_display_status of this ClientCheckIn.  # noqa: E501


        :return: The is_hook_display_status of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_hook_display_status

    @is_hook_display_status.setter
    def is_hook_display_status(self, is_hook_display_status):
        """Sets the is_hook_display_status of this ClientCheckIn.


        :param is_hook_display_status: The is_hook_display_status of this ClientCheckIn.  # noqa: E501
        :type is_hook_display_status: bool
        """

        self._is_hook_display_status = is_hook_display_status

    @property
    def is_create_startup_script(self):
        """Gets the is_create_startup_script of this ClientCheckIn.  # noqa: E501


        :return: The is_create_startup_script of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_create_startup_script

    @is_create_startup_script.setter
    def is_create_startup_script(self, is_create_startup_script):
        """Sets the is_create_startup_script of this ClientCheckIn.


        :param is_create_startup_script: The is_create_startup_script of this ClientCheckIn.  # noqa: E501
        :type is_create_startup_script: bool
        """

        self._is_create_startup_script = is_create_startup_script

    @property
    def is_startup_log(self):
        """Gets the is_startup_log of this ClientCheckIn.  # noqa: E501


        :return: The is_startup_log of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_startup_log

    @is_startup_log.setter
    def is_startup_log(self, is_startup_log):
        """Sets the is_startup_log of this ClientCheckIn.


        :param is_startup_log: The is_startup_log of this ClientCheckIn.  # noqa: E501
        :type is_startup_log: bool
        """

        self._is_startup_log = is_startup_log

    @property
    def is_startup_policies(self):
        """Gets the is_startup_policies of this ClientCheckIn.  # noqa: E501


        :return: The is_startup_policies of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_startup_policies

    @is_startup_policies.setter
    def is_startup_policies(self, is_startup_policies):
        """Sets the is_startup_policies of this ClientCheckIn.


        :param is_startup_policies: The is_startup_policies of this ClientCheckIn.  # noqa: E501
        :type is_startup_policies: bool
        """

        self._is_startup_policies = is_startup_policies

    @property
    def is_startup_ssh(self):
        """Gets the is_startup_ssh of this ClientCheckIn.  # noqa: E501


        :return: The is_startup_ssh of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_startup_ssh

    @is_startup_ssh.setter
    def is_startup_ssh(self, is_startup_ssh):
        """Sets the is_startup_ssh of this ClientCheckIn.


        :param is_startup_ssh: The is_startup_ssh of this ClientCheckIn.  # noqa: E501
        :type is_startup_ssh: bool
        """

        self._is_startup_ssh = is_startup_ssh

    @property
    def is_startup_mcx(self):
        """Gets the is_startup_mcx of this ClientCheckIn.  # noqa: E501


        :return: The is_startup_mcx of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_startup_mcx

    @is_startup_mcx.setter
    def is_startup_mcx(self, is_startup_mcx):
        """Sets the is_startup_mcx of this ClientCheckIn.


        :param is_startup_mcx: The is_startup_mcx of this ClientCheckIn.  # noqa: E501
        :type is_startup_mcx: bool
        """

        self._is_startup_mcx = is_startup_mcx

    @property
    def is_enable_local_configuration_profiles(self):
        """Gets the is_enable_local_configuration_profiles of this ClientCheckIn.  # noqa: E501


        :return: The is_enable_local_configuration_profiles of this ClientCheckIn.  # noqa: E501
        :rtype: bool
        """
        return self._is_enable_local_configuration_profiles

    @is_enable_local_configuration_profiles.setter
    def is_enable_local_configuration_profiles(self, is_enable_local_configuration_profiles):
        """Sets the is_enable_local_configuration_profiles of this ClientCheckIn.


        :param is_enable_local_configuration_profiles: The is_enable_local_configuration_profiles of this ClientCheckIn.  # noqa: E501
        :type is_enable_local_configuration_profiles: bool
        """

        self._is_enable_local_configuration_profiles = is_enable_local_configuration_profiles

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
        if not isinstance(other, ClientCheckIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientCheckIn):
            return True

        return self.to_dict() != other.to_dict()