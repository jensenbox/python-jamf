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


class ComputerPartition(object):
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
        'name': 'str',
        'size_megabytes': 'int',
        'available_megabytes': 'int',
        'partition_type': 'str',
        'percent_used': 'int',
        'file_vault2_state': 'ComputerPartitionFileVault2State',
        'file_vault2_progress_percent': 'int',
        'lvm_managed': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'size_megabytes': 'sizeMegabytes',
        'available_megabytes': 'availableMegabytes',
        'partition_type': 'partitionType',
        'percent_used': 'percentUsed',
        'file_vault2_state': 'fileVault2State',
        'file_vault2_progress_percent': 'fileVault2ProgressPercent',
        'lvm_managed': 'lvmManaged'
    }

    def __init__(self, name=None, size_megabytes=None, available_megabytes=None, partition_type=None, percent_used=None, file_vault2_state=None, file_vault2_progress_percent=None, lvm_managed=None, local_vars_configuration=None):  # noqa: E501
        """ComputerPartition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._size_megabytes = None
        self._available_megabytes = None
        self._partition_type = None
        self._percent_used = None
        self._file_vault2_state = None
        self._file_vault2_progress_percent = None
        self._lvm_managed = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size_megabytes is not None:
            self.size_megabytes = size_megabytes
        if available_megabytes is not None:
            self.available_megabytes = available_megabytes
        if partition_type is not None:
            self.partition_type = partition_type
        if percent_used is not None:
            self.percent_used = percent_used
        if file_vault2_state is not None:
            self.file_vault2_state = file_vault2_state
        self.file_vault2_progress_percent = file_vault2_progress_percent
        if lvm_managed is not None:
            self.lvm_managed = lvm_managed

    @property
    def name(self):
        """Gets the name of this ComputerPartition.  # noqa: E501


        :return: The name of this ComputerPartition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerPartition.


        :param name: The name of this ComputerPartition.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def size_megabytes(self):
        """Gets the size_megabytes of this ComputerPartition.  # noqa: E501

        Partition Size in MB.  # noqa: E501

        :return: The size_megabytes of this ComputerPartition.  # noqa: E501
        :rtype: int
        """
        return self._size_megabytes

    @size_megabytes.setter
    def size_megabytes(self, size_megabytes):
        """Sets the size_megabytes of this ComputerPartition.

        Partition Size in MB.  # noqa: E501

        :param size_megabytes: The size_megabytes of this ComputerPartition.  # noqa: E501
        :type size_megabytes: int
        """

        self._size_megabytes = size_megabytes

    @property
    def available_megabytes(self):
        """Gets the available_megabytes of this ComputerPartition.  # noqa: E501

        Available space in MB.  # noqa: E501

        :return: The available_megabytes of this ComputerPartition.  # noqa: E501
        :rtype: int
        """
        return self._available_megabytes

    @available_megabytes.setter
    def available_megabytes(self, available_megabytes):
        """Sets the available_megabytes of this ComputerPartition.

        Available space in MB.  # noqa: E501

        :param available_megabytes: The available_megabytes of this ComputerPartition.  # noqa: E501
        :type available_megabytes: int
        """

        self._available_megabytes = available_megabytes

    @property
    def partition_type(self):
        """Gets the partition_type of this ComputerPartition.  # noqa: E501


        :return: The partition_type of this ComputerPartition.  # noqa: E501
        :rtype: str
        """
        return self._partition_type

    @partition_type.setter
    def partition_type(self, partition_type):
        """Sets the partition_type of this ComputerPartition.


        :param partition_type: The partition_type of this ComputerPartition.  # noqa: E501
        :type partition_type: str
        """
        allowed_values = ["BOOT", "RECOVERY", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and partition_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `partition_type` ({0}), must be one of {1}"  # noqa: E501
                .format(partition_type, allowed_values)
            )

        self._partition_type = partition_type

    @property
    def percent_used(self):
        """Gets the percent_used of this ComputerPartition.  # noqa: E501

        Percentage of space used.  # noqa: E501

        :return: The percent_used of this ComputerPartition.  # noqa: E501
        :rtype: int
        """
        return self._percent_used

    @percent_used.setter
    def percent_used(self, percent_used):
        """Sets the percent_used of this ComputerPartition.

        Percentage of space used.  # noqa: E501

        :param percent_used: The percent_used of this ComputerPartition.  # noqa: E501
        :type percent_used: int
        """
        if (self.local_vars_configuration.client_side_validation and
                percent_used is not None and percent_used > 100):  # noqa: E501
            raise ValueError("Invalid value for `percent_used`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                percent_used is not None and percent_used < 0):  # noqa: E501
            raise ValueError("Invalid value for `percent_used`, must be a value greater than or equal to `0`")  # noqa: E501

        self._percent_used = percent_used

    @property
    def file_vault2_state(self):
        """Gets the file_vault2_state of this ComputerPartition.  # noqa: E501


        :return: The file_vault2_state of this ComputerPartition.  # noqa: E501
        :rtype: ComputerPartitionFileVault2State
        """
        return self._file_vault2_state

    @file_vault2_state.setter
    def file_vault2_state(self, file_vault2_state):
        """Sets the file_vault2_state of this ComputerPartition.


        :param file_vault2_state: The file_vault2_state of this ComputerPartition.  # noqa: E501
        :type file_vault2_state: ComputerPartitionFileVault2State
        """

        self._file_vault2_state = file_vault2_state

    @property
    def file_vault2_progress_percent(self):
        """Gets the file_vault2_progress_percent of this ComputerPartition.  # noqa: E501

        Percentage progress of current FileVault 2 operation.  # noqa: E501

        :return: The file_vault2_progress_percent of this ComputerPartition.  # noqa: E501
        :rtype: int
        """
        return self._file_vault2_progress_percent

    @file_vault2_progress_percent.setter
    def file_vault2_progress_percent(self, file_vault2_progress_percent):
        """Sets the file_vault2_progress_percent of this ComputerPartition.

        Percentage progress of current FileVault 2 operation.  # noqa: E501

        :param file_vault2_progress_percent: The file_vault2_progress_percent of this ComputerPartition.  # noqa: E501
        :type file_vault2_progress_percent: int
        """

        self._file_vault2_progress_percent = file_vault2_progress_percent

    @property
    def lvm_managed(self):
        """Gets the lvm_managed of this ComputerPartition.  # noqa: E501


        :return: The lvm_managed of this ComputerPartition.  # noqa: E501
        :rtype: bool
        """
        return self._lvm_managed

    @lvm_managed.setter
    def lvm_managed(self, lvm_managed):
        """Sets the lvm_managed of this ComputerPartition.


        :param lvm_managed: The lvm_managed of this ComputerPartition.  # noqa: E501
        :type lvm_managed: bool
        """

        self._lvm_managed = lvm_managed

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
        if not isinstance(other, ComputerPartition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerPartition):
            return True

        return self.to_dict() != other.to_dict()