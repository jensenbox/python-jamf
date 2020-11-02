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


class AndroidDetails(object):
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
        'os_name': 'str',
        'manufacturer': 'str',
        'model': 'str',
        'internal_capacity_mb': 'int',
        'internal_available_mb': 'int',
        'internal_percent_used': 'int',
        'external_capacity_mb': 'int',
        'external_available_mb': 'int',
        'external_percent_used': 'int',
        'battery_level': 'int',
        'last_backup_timestamp': 'datetime',
        'api_version': 'int',
        'computer': 'AndroidDetailsComputer',
        'security': 'Security'
    }

    attribute_map = {
        'os_name': 'osName',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'internal_capacity_mb': 'internalCapacityMb',
        'internal_available_mb': 'internalAvailableMb',
        'internal_percent_used': 'internalPercentUsed',
        'external_capacity_mb': 'externalCapacityMb',
        'external_available_mb': 'externalAvailableMb',
        'external_percent_used': 'externalPercentUsed',
        'battery_level': 'batteryLevel',
        'last_backup_timestamp': 'lastBackupTimestamp',
        'api_version': 'apiVersion',
        'computer': 'computer',
        'security': 'security'
    }

    def __init__(self, os_name=None, manufacturer=None, model=None, internal_capacity_mb=None, internal_available_mb=None, internal_percent_used=None, external_capacity_mb=None, external_available_mb=None, external_percent_used=None, battery_level=None, last_backup_timestamp=None, api_version=None, computer=None, security=None, local_vars_configuration=None):  # noqa: E501
        """AndroidDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._os_name = None
        self._manufacturer = None
        self._model = None
        self._internal_capacity_mb = None
        self._internal_available_mb = None
        self._internal_percent_used = None
        self._external_capacity_mb = None
        self._external_available_mb = None
        self._external_percent_used = None
        self._battery_level = None
        self._last_backup_timestamp = None
        self._api_version = None
        self._computer = None
        self._security = None
        self.discriminator = None

        if os_name is not None:
            self.os_name = os_name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if internal_capacity_mb is not None:
            self.internal_capacity_mb = internal_capacity_mb
        if internal_available_mb is not None:
            self.internal_available_mb = internal_available_mb
        if internal_percent_used is not None:
            self.internal_percent_used = internal_percent_used
        if external_capacity_mb is not None:
            self.external_capacity_mb = external_capacity_mb
        if external_available_mb is not None:
            self.external_available_mb = external_available_mb
        if external_percent_used is not None:
            self.external_percent_used = external_percent_used
        if battery_level is not None:
            self.battery_level = battery_level
        if last_backup_timestamp is not None:
            self.last_backup_timestamp = last_backup_timestamp
        if api_version is not None:
            self.api_version = api_version
        if computer is not None:
            self.computer = computer
        if security is not None:
            self.security = security

    @property
    def os_name(self):
        """Gets the os_name of this AndroidDetails.  # noqa: E501


        :return: The os_name of this AndroidDetails.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this AndroidDetails.


        :param os_name: The os_name of this AndroidDetails.  # noqa: E501
        :type os_name: str
        """

        self._os_name = os_name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this AndroidDetails.  # noqa: E501


        :return: The manufacturer of this AndroidDetails.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this AndroidDetails.


        :param manufacturer: The manufacturer of this AndroidDetails.  # noqa: E501
        :type manufacturer: str
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this AndroidDetails.  # noqa: E501


        :return: The model of this AndroidDetails.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AndroidDetails.


        :param model: The model of this AndroidDetails.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def internal_capacity_mb(self):
        """Gets the internal_capacity_mb of this AndroidDetails.  # noqa: E501


        :return: The internal_capacity_mb of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._internal_capacity_mb

    @internal_capacity_mb.setter
    def internal_capacity_mb(self, internal_capacity_mb):
        """Sets the internal_capacity_mb of this AndroidDetails.


        :param internal_capacity_mb: The internal_capacity_mb of this AndroidDetails.  # noqa: E501
        :type internal_capacity_mb: int
        """

        self._internal_capacity_mb = internal_capacity_mb

    @property
    def internal_available_mb(self):
        """Gets the internal_available_mb of this AndroidDetails.  # noqa: E501


        :return: The internal_available_mb of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._internal_available_mb

    @internal_available_mb.setter
    def internal_available_mb(self, internal_available_mb):
        """Sets the internal_available_mb of this AndroidDetails.


        :param internal_available_mb: The internal_available_mb of this AndroidDetails.  # noqa: E501
        :type internal_available_mb: int
        """

        self._internal_available_mb = internal_available_mb

    @property
    def internal_percent_used(self):
        """Gets the internal_percent_used of this AndroidDetails.  # noqa: E501


        :return: The internal_percent_used of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._internal_percent_used

    @internal_percent_used.setter
    def internal_percent_used(self, internal_percent_used):
        """Sets the internal_percent_used of this AndroidDetails.


        :param internal_percent_used: The internal_percent_used of this AndroidDetails.  # noqa: E501
        :type internal_percent_used: int
        """

        self._internal_percent_used = internal_percent_used

    @property
    def external_capacity_mb(self):
        """Gets the external_capacity_mb of this AndroidDetails.  # noqa: E501


        :return: The external_capacity_mb of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._external_capacity_mb

    @external_capacity_mb.setter
    def external_capacity_mb(self, external_capacity_mb):
        """Sets the external_capacity_mb of this AndroidDetails.


        :param external_capacity_mb: The external_capacity_mb of this AndroidDetails.  # noqa: E501
        :type external_capacity_mb: int
        """

        self._external_capacity_mb = external_capacity_mb

    @property
    def external_available_mb(self):
        """Gets the external_available_mb of this AndroidDetails.  # noqa: E501


        :return: The external_available_mb of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._external_available_mb

    @external_available_mb.setter
    def external_available_mb(self, external_available_mb):
        """Sets the external_available_mb of this AndroidDetails.


        :param external_available_mb: The external_available_mb of this AndroidDetails.  # noqa: E501
        :type external_available_mb: int
        """

        self._external_available_mb = external_available_mb

    @property
    def external_percent_used(self):
        """Gets the external_percent_used of this AndroidDetails.  # noqa: E501


        :return: The external_percent_used of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._external_percent_used

    @external_percent_used.setter
    def external_percent_used(self, external_percent_used):
        """Sets the external_percent_used of this AndroidDetails.


        :param external_percent_used: The external_percent_used of this AndroidDetails.  # noqa: E501
        :type external_percent_used: int
        """

        self._external_percent_used = external_percent_used

    @property
    def battery_level(self):
        """Gets the battery_level of this AndroidDetails.  # noqa: E501


        :return: The battery_level of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._battery_level

    @battery_level.setter
    def battery_level(self, battery_level):
        """Sets the battery_level of this AndroidDetails.


        :param battery_level: The battery_level of this AndroidDetails.  # noqa: E501
        :type battery_level: int
        """

        self._battery_level = battery_level

    @property
    def last_backup_timestamp(self):
        """Gets the last_backup_timestamp of this AndroidDetails.  # noqa: E501


        :return: The last_backup_timestamp of this AndroidDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._last_backup_timestamp

    @last_backup_timestamp.setter
    def last_backup_timestamp(self, last_backup_timestamp):
        """Sets the last_backup_timestamp of this AndroidDetails.


        :param last_backup_timestamp: The last_backup_timestamp of this AndroidDetails.  # noqa: E501
        :type last_backup_timestamp: datetime
        """

        self._last_backup_timestamp = last_backup_timestamp

    @property
    def api_version(self):
        """Gets the api_version of this AndroidDetails.  # noqa: E501


        :return: The api_version of this AndroidDetails.  # noqa: E501
        :rtype: int
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this AndroidDetails.


        :param api_version: The api_version of this AndroidDetails.  # noqa: E501
        :type api_version: int
        """

        self._api_version = api_version

    @property
    def computer(self):
        """Gets the computer of this AndroidDetails.  # noqa: E501


        :return: The computer of this AndroidDetails.  # noqa: E501
        :rtype: AndroidDetailsComputer
        """
        return self._computer

    @computer.setter
    def computer(self, computer):
        """Sets the computer of this AndroidDetails.


        :param computer: The computer of this AndroidDetails.  # noqa: E501
        :type computer: AndroidDetailsComputer
        """

        self._computer = computer

    @property
    def security(self):
        """Gets the security of this AndroidDetails.  # noqa: E501


        :return: The security of this AndroidDetails.  # noqa: E501
        :rtype: Security
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this AndroidDetails.


        :param security: The security of this AndroidDetails.  # noqa: E501
        :type security: Security
        """

        self._security = security

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
        if not isinstance(other, AndroidDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AndroidDetails):
            return True

        return self.to_dict() != other.to_dict()
