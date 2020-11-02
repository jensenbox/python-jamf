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


class PrestageScopeResponse(object):
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
        'prestage_id': 'int',
        'assignments': 'list[PrestageScopeAssignment]',
        'version_lock': 'int'
    }

    attribute_map = {
        'prestage_id': 'prestageId',
        'assignments': 'assignments',
        'version_lock': 'versionLock'
    }

    def __init__(self, prestage_id=None, assignments=None, version_lock=None, local_vars_configuration=None):  # noqa: E501
        """PrestageScopeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prestage_id = None
        self._assignments = None
        self._version_lock = None
        self.discriminator = None

        if prestage_id is not None:
            self.prestage_id = prestage_id
        if assignments is not None:
            self.assignments = assignments
        if version_lock is not None:
            self.version_lock = version_lock

    @property
    def prestage_id(self):
        """Gets the prestage_id of this PrestageScopeResponse.  # noqa: E501


        :return: The prestage_id of this PrestageScopeResponse.  # noqa: E501
        :rtype: int
        """
        return self._prestage_id

    @prestage_id.setter
    def prestage_id(self, prestage_id):
        """Sets the prestage_id of this PrestageScopeResponse.


        :param prestage_id: The prestage_id of this PrestageScopeResponse.  # noqa: E501
        :type prestage_id: int
        """

        self._prestage_id = prestage_id

    @property
    def assignments(self):
        """Gets the assignments of this PrestageScopeResponse.  # noqa: E501


        :return: The assignments of this PrestageScopeResponse.  # noqa: E501
        :rtype: list[PrestageScopeAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this PrestageScopeResponse.


        :param assignments: The assignments of this PrestageScopeResponse.  # noqa: E501
        :type assignments: list[PrestageScopeAssignment]
        """

        self._assignments = assignments

    @property
    def version_lock(self):
        """Gets the version_lock of this PrestageScopeResponse.  # noqa: E501


        :return: The version_lock of this PrestageScopeResponse.  # noqa: E501
        :rtype: int
        """
        return self._version_lock

    @version_lock.setter
    def version_lock(self, version_lock):
        """Sets the version_lock of this PrestageScopeResponse.


        :param version_lock: The version_lock of this PrestageScopeResponse.  # noqa: E501
        :type version_lock: int
        """

        self._version_lock = version_lock

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
        if not isinstance(other, PrestageScopeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrestageScopeResponse):
            return True

        return self.to_dict() != other.to_dict()