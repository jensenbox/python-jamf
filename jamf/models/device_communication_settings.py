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


class DeviceCommunicationSettings(object):
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
        'auto_renew_mobile_device_mdm_profile_when_ca_renewed': 'bool',
        'auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring': 'bool',
        'auto_renew_computer_mdm_profile_when_ca_renewed': 'bool',
        'auto_renew_computer_mdm_profile_when_device_identity_cert_expiring': 'bool',
        'mdm_profile_mobile_device_expiration_limit_in_days': 'int',
        'mdm_profile_computer_expiration_limit_in_days': 'int'
    }

    attribute_map = {
        'auto_renew_mobile_device_mdm_profile_when_ca_renewed': 'autoRenewMobileDeviceMdmProfileWhenCaRenewed',
        'auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring': 'autoRenewMobileDeviceMdmProfileWhenDeviceIdentityCertExpiring',
        'auto_renew_computer_mdm_profile_when_ca_renewed': 'autoRenewComputerMdmProfileWhenCaRenewed',
        'auto_renew_computer_mdm_profile_when_device_identity_cert_expiring': 'autoRenewComputerMdmProfileWhenDeviceIdentityCertExpiring',
        'mdm_profile_mobile_device_expiration_limit_in_days': 'mdmProfileMobileDeviceExpirationLimitInDays',
        'mdm_profile_computer_expiration_limit_in_days': 'mdmProfileComputerExpirationLimitInDays'
    }

    def __init__(self, auto_renew_mobile_device_mdm_profile_when_ca_renewed=None, auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring=None, auto_renew_computer_mdm_profile_when_ca_renewed=None, auto_renew_computer_mdm_profile_when_device_identity_cert_expiring=None, mdm_profile_mobile_device_expiration_limit_in_days=None, mdm_profile_computer_expiration_limit_in_days=None, local_vars_configuration=None):  # noqa: E501
        """DeviceCommunicationSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_renew_mobile_device_mdm_profile_when_ca_renewed = None
        self._auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring = None
        self._auto_renew_computer_mdm_profile_when_ca_renewed = None
        self._auto_renew_computer_mdm_profile_when_device_identity_cert_expiring = None
        self._mdm_profile_mobile_device_expiration_limit_in_days = None
        self._mdm_profile_computer_expiration_limit_in_days = None
        self.discriminator = None

        if auto_renew_mobile_device_mdm_profile_when_ca_renewed is not None:
            self.auto_renew_mobile_device_mdm_profile_when_ca_renewed = auto_renew_mobile_device_mdm_profile_when_ca_renewed
        if auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring is not None:
            self.auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring = auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring
        if auto_renew_computer_mdm_profile_when_ca_renewed is not None:
            self.auto_renew_computer_mdm_profile_when_ca_renewed = auto_renew_computer_mdm_profile_when_ca_renewed
        if auto_renew_computer_mdm_profile_when_device_identity_cert_expiring is not None:
            self.auto_renew_computer_mdm_profile_when_device_identity_cert_expiring = auto_renew_computer_mdm_profile_when_device_identity_cert_expiring
        if mdm_profile_mobile_device_expiration_limit_in_days is not None:
            self.mdm_profile_mobile_device_expiration_limit_in_days = mdm_profile_mobile_device_expiration_limit_in_days
        if mdm_profile_computer_expiration_limit_in_days is not None:
            self.mdm_profile_computer_expiration_limit_in_days = mdm_profile_computer_expiration_limit_in_days

    @property
    def auto_renew_mobile_device_mdm_profile_when_ca_renewed(self):
        """Gets the auto_renew_mobile_device_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501


        :return: The auto_renew_mobile_device_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew_mobile_device_mdm_profile_when_ca_renewed

    @auto_renew_mobile_device_mdm_profile_when_ca_renewed.setter
    def auto_renew_mobile_device_mdm_profile_when_ca_renewed(self, auto_renew_mobile_device_mdm_profile_when_ca_renewed):
        """Sets the auto_renew_mobile_device_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.


        :param auto_renew_mobile_device_mdm_profile_when_ca_renewed: The auto_renew_mobile_device_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501
        :type auto_renew_mobile_device_mdm_profile_when_ca_renewed: bool
        """

        self._auto_renew_mobile_device_mdm_profile_when_ca_renewed = auto_renew_mobile_device_mdm_profile_when_ca_renewed

    @property
    def auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring(self):
        """Gets the auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501


        :return: The auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring

    @auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring.setter
    def auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring(self, auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring):
        """Sets the auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.


        :param auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring: The auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501
        :type auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring: bool
        """

        self._auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring = auto_renew_mobile_device_mdm_profile_when_device_identity_cert_expiring

    @property
    def auto_renew_computer_mdm_profile_when_ca_renewed(self):
        """Gets the auto_renew_computer_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501


        :return: The auto_renew_computer_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew_computer_mdm_profile_when_ca_renewed

    @auto_renew_computer_mdm_profile_when_ca_renewed.setter
    def auto_renew_computer_mdm_profile_when_ca_renewed(self, auto_renew_computer_mdm_profile_when_ca_renewed):
        """Sets the auto_renew_computer_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.


        :param auto_renew_computer_mdm_profile_when_ca_renewed: The auto_renew_computer_mdm_profile_when_ca_renewed of this DeviceCommunicationSettings.  # noqa: E501
        :type auto_renew_computer_mdm_profile_when_ca_renewed: bool
        """

        self._auto_renew_computer_mdm_profile_when_ca_renewed = auto_renew_computer_mdm_profile_when_ca_renewed

    @property
    def auto_renew_computer_mdm_profile_when_device_identity_cert_expiring(self):
        """Gets the auto_renew_computer_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501


        :return: The auto_renew_computer_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew_computer_mdm_profile_when_device_identity_cert_expiring

    @auto_renew_computer_mdm_profile_when_device_identity_cert_expiring.setter
    def auto_renew_computer_mdm_profile_when_device_identity_cert_expiring(self, auto_renew_computer_mdm_profile_when_device_identity_cert_expiring):
        """Sets the auto_renew_computer_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.


        :param auto_renew_computer_mdm_profile_when_device_identity_cert_expiring: The auto_renew_computer_mdm_profile_when_device_identity_cert_expiring of this DeviceCommunicationSettings.  # noqa: E501
        :type auto_renew_computer_mdm_profile_when_device_identity_cert_expiring: bool
        """

        self._auto_renew_computer_mdm_profile_when_device_identity_cert_expiring = auto_renew_computer_mdm_profile_when_device_identity_cert_expiring

    @property
    def mdm_profile_mobile_device_expiration_limit_in_days(self):
        """Gets the mdm_profile_mobile_device_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501


        :return: The mdm_profile_mobile_device_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: int
        """
        return self._mdm_profile_mobile_device_expiration_limit_in_days

    @mdm_profile_mobile_device_expiration_limit_in_days.setter
    def mdm_profile_mobile_device_expiration_limit_in_days(self, mdm_profile_mobile_device_expiration_limit_in_days):
        """Sets the mdm_profile_mobile_device_expiration_limit_in_days of this DeviceCommunicationSettings.


        :param mdm_profile_mobile_device_expiration_limit_in_days: The mdm_profile_mobile_device_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501
        :type mdm_profile_mobile_device_expiration_limit_in_days: int
        """

        self._mdm_profile_mobile_device_expiration_limit_in_days = mdm_profile_mobile_device_expiration_limit_in_days

    @property
    def mdm_profile_computer_expiration_limit_in_days(self):
        """Gets the mdm_profile_computer_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501


        :return: The mdm_profile_computer_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501
        :rtype: int
        """
        return self._mdm_profile_computer_expiration_limit_in_days

    @mdm_profile_computer_expiration_limit_in_days.setter
    def mdm_profile_computer_expiration_limit_in_days(self, mdm_profile_computer_expiration_limit_in_days):
        """Sets the mdm_profile_computer_expiration_limit_in_days of this DeviceCommunicationSettings.


        :param mdm_profile_computer_expiration_limit_in_days: The mdm_profile_computer_expiration_limit_in_days of this DeviceCommunicationSettings.  # noqa: E501
        :type mdm_profile_computer_expiration_limit_in_days: int
        """

        self._mdm_profile_computer_expiration_limit_in_days = mdm_profile_computer_expiration_limit_in_days

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
        if not isinstance(other, DeviceCommunicationSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceCommunicationSettings):
            return True

        return self.to_dict() != other.to_dict()
