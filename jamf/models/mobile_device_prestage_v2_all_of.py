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


class MobileDevicePrestageV2AllOf(object):
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
        'allow_pairing': 'bool',
        'multi_user': 'bool',
        'supervised': 'bool',
        'maximum_shared_accounts': 'int',
        'configure_device_before_setup_assistant': 'bool',
        'names': 'MobileDevicePrestageNamesV2',
        'send_timezone': 'bool',
        'timezone': 'str'
    }

    attribute_map = {
        'allow_pairing': 'allowPairing',
        'multi_user': 'multiUser',
        'supervised': 'supervised',
        'maximum_shared_accounts': 'maximumSharedAccounts',
        'configure_device_before_setup_assistant': 'configureDeviceBeforeSetupAssistant',
        'names': 'names',
        'send_timezone': 'sendTimezone',
        'timezone': 'timezone'
    }

    def __init__(self, allow_pairing=None, multi_user=None, supervised=None, maximum_shared_accounts=None, configure_device_before_setup_assistant=None, names=None, send_timezone=None, timezone=None, local_vars_configuration=None):  # noqa: E501
        """MobileDevicePrestageV2AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allow_pairing = None
        self._multi_user = None
        self._supervised = None
        self._maximum_shared_accounts = None
        self._configure_device_before_setup_assistant = None
        self._names = None
        self._send_timezone = None
        self._timezone = None
        self.discriminator = None

        self.allow_pairing = allow_pairing
        self.multi_user = multi_user
        self.supervised = supervised
        self.maximum_shared_accounts = maximum_shared_accounts
        self.configure_device_before_setup_assistant = configure_device_before_setup_assistant
        if names is not None:
            self.names = names
        self.send_timezone = send_timezone
        self.timezone = timezone

    @property
    def allow_pairing(self):
        """Gets the allow_pairing of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The allow_pairing of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pairing

    @allow_pairing.setter
    def allow_pairing(self, allow_pairing):
        """Sets the allow_pairing of this MobileDevicePrestageV2AllOf.


        :param allow_pairing: The allow_pairing of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type allow_pairing: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_pairing is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_pairing`, must not be `None`")  # noqa: E501

        self._allow_pairing = allow_pairing

    @property
    def multi_user(self):
        """Gets the multi_user of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The multi_user of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._multi_user

    @multi_user.setter
    def multi_user(self, multi_user):
        """Sets the multi_user of this MobileDevicePrestageV2AllOf.


        :param multi_user: The multi_user of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type multi_user: bool
        """
        if self.local_vars_configuration.client_side_validation and multi_user is None:  # noqa: E501
            raise ValueError("Invalid value for `multi_user`, must not be `None`")  # noqa: E501

        self._multi_user = multi_user

    @property
    def supervised(self):
        """Gets the supervised of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The supervised of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._supervised

    @supervised.setter
    def supervised(self, supervised):
        """Sets the supervised of this MobileDevicePrestageV2AllOf.


        :param supervised: The supervised of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type supervised: bool
        """
        if self.local_vars_configuration.client_side_validation and supervised is None:  # noqa: E501
            raise ValueError("Invalid value for `supervised`, must not be `None`")  # noqa: E501

        self._supervised = supervised

    @property
    def maximum_shared_accounts(self):
        """Gets the maximum_shared_accounts of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The maximum_shared_accounts of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: int
        """
        return self._maximum_shared_accounts

    @maximum_shared_accounts.setter
    def maximum_shared_accounts(self, maximum_shared_accounts):
        """Sets the maximum_shared_accounts of this MobileDevicePrestageV2AllOf.


        :param maximum_shared_accounts: The maximum_shared_accounts of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type maximum_shared_accounts: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_shared_accounts is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_shared_accounts`, must not be `None`")  # noqa: E501

        self._maximum_shared_accounts = maximum_shared_accounts

    @property
    def configure_device_before_setup_assistant(self):
        """Gets the configure_device_before_setup_assistant of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The configure_device_before_setup_assistant of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._configure_device_before_setup_assistant

    @configure_device_before_setup_assistant.setter
    def configure_device_before_setup_assistant(self, configure_device_before_setup_assistant):
        """Sets the configure_device_before_setup_assistant of this MobileDevicePrestageV2AllOf.


        :param configure_device_before_setup_assistant: The configure_device_before_setup_assistant of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type configure_device_before_setup_assistant: bool
        """
        if self.local_vars_configuration.client_side_validation and configure_device_before_setup_assistant is None:  # noqa: E501
            raise ValueError("Invalid value for `configure_device_before_setup_assistant`, must not be `None`")  # noqa: E501

        self._configure_device_before_setup_assistant = configure_device_before_setup_assistant

    @property
    def names(self):
        """Gets the names of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The names of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: MobileDevicePrestageNamesV2
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this MobileDevicePrestageV2AllOf.


        :param names: The names of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type names: MobileDevicePrestageNamesV2
        """

        self._names = names

    @property
    def send_timezone(self):
        """Gets the send_timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The send_timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._send_timezone

    @send_timezone.setter
    def send_timezone(self, send_timezone):
        """Sets the send_timezone of this MobileDevicePrestageV2AllOf.


        :param send_timezone: The send_timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type send_timezone: bool
        """
        if self.local_vars_configuration.client_side_validation and send_timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `send_timezone`, must not be `None`")  # noqa: E501

        self._send_timezone = send_timezone

    @property
    def timezone(self):
        """Gets the timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501


        :return: The timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this MobileDevicePrestageV2AllOf.


        :param timezone: The timezone of this MobileDevicePrestageV2AllOf.  # noqa: E501
        :type timezone: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

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
        if not isinstance(other, MobileDevicePrestageV2AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileDevicePrestageV2AllOf):
            return True

        return self.to_dict() != other.to_dict()
