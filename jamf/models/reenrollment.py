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


class Reenrollment(object):
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
        'is_flush_policy_history_enabled': 'bool',
        'is_flush_location_information_enabled': 'bool',
        'is_flush_location_information_history_enabled': 'bool',
        'is_flush_extension_attributes_enabled': 'bool',
        'flush_mdm_queue': 'str'
    }

    attribute_map = {
        'is_flush_policy_history_enabled': 'isFlushPolicyHistoryEnabled',
        'is_flush_location_information_enabled': 'isFlushLocationInformationEnabled',
        'is_flush_location_information_history_enabled': 'isFlushLocationInformationHistoryEnabled',
        'is_flush_extension_attributes_enabled': 'isFlushExtensionAttributesEnabled',
        'flush_mdm_queue': 'flushMDMQueue'
    }

    def __init__(self, is_flush_policy_history_enabled=False, is_flush_location_information_enabled=False, is_flush_location_information_history_enabled=False, is_flush_extension_attributes_enabled=False, flush_mdm_queue=None, local_vars_configuration=None):  # noqa: E501
        """Reenrollment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_flush_policy_history_enabled = None
        self._is_flush_location_information_enabled = None
        self._is_flush_location_information_history_enabled = None
        self._is_flush_extension_attributes_enabled = None
        self._flush_mdm_queue = None
        self.discriminator = None

        if is_flush_policy_history_enabled is not None:
            self.is_flush_policy_history_enabled = is_flush_policy_history_enabled
        if is_flush_location_information_enabled is not None:
            self.is_flush_location_information_enabled = is_flush_location_information_enabled
        if is_flush_location_information_history_enabled is not None:
            self.is_flush_location_information_history_enabled = is_flush_location_information_history_enabled
        if is_flush_extension_attributes_enabled is not None:
            self.is_flush_extension_attributes_enabled = is_flush_extension_attributes_enabled
        self.flush_mdm_queue = flush_mdm_queue

    @property
    def is_flush_policy_history_enabled(self):
        """Gets the is_flush_policy_history_enabled of this Reenrollment.  # noqa: E501


        :return: The is_flush_policy_history_enabled of this Reenrollment.  # noqa: E501
        :rtype: bool
        """
        return self._is_flush_policy_history_enabled

    @is_flush_policy_history_enabled.setter
    def is_flush_policy_history_enabled(self, is_flush_policy_history_enabled):
        """Sets the is_flush_policy_history_enabled of this Reenrollment.


        :param is_flush_policy_history_enabled: The is_flush_policy_history_enabled of this Reenrollment.  # noqa: E501
        :type is_flush_policy_history_enabled: bool
        """

        self._is_flush_policy_history_enabled = is_flush_policy_history_enabled

    @property
    def is_flush_location_information_enabled(self):
        """Gets the is_flush_location_information_enabled of this Reenrollment.  # noqa: E501


        :return: The is_flush_location_information_enabled of this Reenrollment.  # noqa: E501
        :rtype: bool
        """
        return self._is_flush_location_information_enabled

    @is_flush_location_information_enabled.setter
    def is_flush_location_information_enabled(self, is_flush_location_information_enabled):
        """Sets the is_flush_location_information_enabled of this Reenrollment.


        :param is_flush_location_information_enabled: The is_flush_location_information_enabled of this Reenrollment.  # noqa: E501
        :type is_flush_location_information_enabled: bool
        """

        self._is_flush_location_information_enabled = is_flush_location_information_enabled

    @property
    def is_flush_location_information_history_enabled(self):
        """Gets the is_flush_location_information_history_enabled of this Reenrollment.  # noqa: E501


        :return: The is_flush_location_information_history_enabled of this Reenrollment.  # noqa: E501
        :rtype: bool
        """
        return self._is_flush_location_information_history_enabled

    @is_flush_location_information_history_enabled.setter
    def is_flush_location_information_history_enabled(self, is_flush_location_information_history_enabled):
        """Sets the is_flush_location_information_history_enabled of this Reenrollment.


        :param is_flush_location_information_history_enabled: The is_flush_location_information_history_enabled of this Reenrollment.  # noqa: E501
        :type is_flush_location_information_history_enabled: bool
        """

        self._is_flush_location_information_history_enabled = is_flush_location_information_history_enabled

    @property
    def is_flush_extension_attributes_enabled(self):
        """Gets the is_flush_extension_attributes_enabled of this Reenrollment.  # noqa: E501


        :return: The is_flush_extension_attributes_enabled of this Reenrollment.  # noqa: E501
        :rtype: bool
        """
        return self._is_flush_extension_attributes_enabled

    @is_flush_extension_attributes_enabled.setter
    def is_flush_extension_attributes_enabled(self, is_flush_extension_attributes_enabled):
        """Sets the is_flush_extension_attributes_enabled of this Reenrollment.


        :param is_flush_extension_attributes_enabled: The is_flush_extension_attributes_enabled of this Reenrollment.  # noqa: E501
        :type is_flush_extension_attributes_enabled: bool
        """

        self._is_flush_extension_attributes_enabled = is_flush_extension_attributes_enabled

    @property
    def flush_mdm_queue(self):
        """Gets the flush_mdm_queue of this Reenrollment.  # noqa: E501


        :return: The flush_mdm_queue of this Reenrollment.  # noqa: E501
        :rtype: str
        """
        return self._flush_mdm_queue

    @flush_mdm_queue.setter
    def flush_mdm_queue(self, flush_mdm_queue):
        """Sets the flush_mdm_queue of this Reenrollment.


        :param flush_mdm_queue: The flush_mdm_queue of this Reenrollment.  # noqa: E501
        :type flush_mdm_queue: str
        """
        if self.local_vars_configuration.client_side_validation and flush_mdm_queue is None:  # noqa: E501
            raise ValueError("Invalid value for `flush_mdm_queue`, must not be `None`")  # noqa: E501
        allowed_values = ["DELETE_NOTHING", "DELETE_ERRORS", "DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED", "DELETE_EVERYTHING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flush_mdm_queue not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `flush_mdm_queue` ({0}), must be one of {1}"  # noqa: E501
                .format(flush_mdm_queue, allowed_values)
            )

        self._flush_mdm_queue = flush_mdm_queue

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
        if not isinstance(other, Reenrollment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Reenrollment):
            return True

        return self.to_dict() != other.to_dict()