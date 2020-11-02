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


class AssignRemoveProfileResponseSyncState(object):
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
        'id': 'int',
        'serial_number': 'str',
        'profile_uuid': 'str',
        'sync_status': 'str',
        'failure_count': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'serial_number': 'serialNumber',
        'profile_uuid': 'profileUUID',
        'sync_status': 'syncStatus',
        'failure_count': 'failureCount',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, serial_number=None, profile_uuid=None, sync_status=None, failure_count=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """AssignRemoveProfileResponseSyncState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._serial_number = None
        self._profile_uuid = None
        self._sync_status = None
        self._failure_count = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if serial_number is not None:
            self.serial_number = serial_number
        if profile_uuid is not None:
            self.profile_uuid = profile_uuid
        if sync_status is not None:
            self.sync_status = sync_status
        if failure_count is not None:
            self.failure_count = failure_count
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The id of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignRemoveProfileResponseSyncState.


        :param id: The id of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def serial_number(self):
        """Gets the serial_number of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The serial_number of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this AssignRemoveProfileResponseSyncState.


        :param serial_number: The serial_number of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def profile_uuid(self):
        """Gets the profile_uuid of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The profile_uuid of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: str
        """
        return self._profile_uuid

    @profile_uuid.setter
    def profile_uuid(self, profile_uuid):
        """Sets the profile_uuid of this AssignRemoveProfileResponseSyncState.


        :param profile_uuid: The profile_uuid of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type profile_uuid: str
        """

        self._profile_uuid = profile_uuid

    @property
    def sync_status(self):
        """Gets the sync_status of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The sync_status of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this AssignRemoveProfileResponseSyncState.


        :param sync_status: The sync_status of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type sync_status: str
        """

        self._sync_status = sync_status

    @property
    def failure_count(self):
        """Gets the failure_count of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The failure_count of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this AssignRemoveProfileResponseSyncState.


        :param failure_count: The failure_count of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type failure_count: int
        """

        self._failure_count = failure_count

    @property
    def timestamp(self):
        """Gets the timestamp of this AssignRemoveProfileResponseSyncState.  # noqa: E501


        :return: The timestamp of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AssignRemoveProfileResponseSyncState.


        :param timestamp: The timestamp of this AssignRemoveProfileResponseSyncState.  # noqa: E501
        :type timestamp: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, AssignRemoveProfileResponseSyncState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignRemoveProfileResponseSyncState):
            return True

        return self.to_dict() != other.to_dict()