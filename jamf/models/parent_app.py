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


class ParentApp(object):
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
        'timezone_id': 'str',
        'restricted_times': 'dict(str, TimeFrame)',
        'device_group_id': 'int',
        'is_enabled': 'bool',
        'allow_templates': 'bool'
    }

    attribute_map = {
        'timezone_id': 'timezoneId',
        'restricted_times': 'restrictedTimes',
        'device_group_id': 'deviceGroupId',
        'is_enabled': 'isEnabled',
        'allow_templates': 'allowTemplates'
    }

    def __init__(self, timezone_id=None, restricted_times=None, device_group_id=None, is_enabled=None, allow_templates=None, local_vars_configuration=None):  # noqa: E501
        """ParentApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timezone_id = None
        self._restricted_times = None
        self._device_group_id = None
        self._is_enabled = None
        self._allow_templates = None
        self.discriminator = None

        self.timezone_id = timezone_id
        self.restricted_times = restricted_times
        self.device_group_id = device_group_id
        self.is_enabled = is_enabled
        if allow_templates is not None:
            self.allow_templates = allow_templates

    @property
    def timezone_id(self):
        """Gets the timezone_id of this ParentApp.  # noqa: E501


        :return: The timezone_id of this ParentApp.  # noqa: E501
        :rtype: str
        """
        return self._timezone_id

    @timezone_id.setter
    def timezone_id(self, timezone_id):
        """Sets the timezone_id of this ParentApp.


        :param timezone_id: The timezone_id of this ParentApp.  # noqa: E501
        :type timezone_id: str
        """
        if self.local_vars_configuration.client_side_validation and timezone_id is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone_id`, must not be `None`")  # noqa: E501

        self._timezone_id = timezone_id

    @property
    def restricted_times(self):
        """Gets the restricted_times of this ParentApp.  # noqa: E501


        :return: The restricted_times of this ParentApp.  # noqa: E501
        :rtype: dict(str, TimeFrame)
        """
        return self._restricted_times

    @restricted_times.setter
    def restricted_times(self, restricted_times):
        """Sets the restricted_times of this ParentApp.


        :param restricted_times: The restricted_times of this ParentApp.  # noqa: E501
        :type restricted_times: dict(str, TimeFrame)
        """
        if self.local_vars_configuration.client_side_validation and restricted_times is None:  # noqa: E501
            raise ValueError("Invalid value for `restricted_times`, must not be `None`")  # noqa: E501

        self._restricted_times = restricted_times

    @property
    def device_group_id(self):
        """Gets the device_group_id of this ParentApp.  # noqa: E501


        :return: The device_group_id of this ParentApp.  # noqa: E501
        :rtype: int
        """
        return self._device_group_id

    @device_group_id.setter
    def device_group_id(self, device_group_id):
        """Sets the device_group_id of this ParentApp.


        :param device_group_id: The device_group_id of this ParentApp.  # noqa: E501
        :type device_group_id: int
        """
        if self.local_vars_configuration.client_side_validation and device_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_group_id`, must not be `None`")  # noqa: E501

        self._device_group_id = device_group_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this ParentApp.  # noqa: E501


        :return: The is_enabled of this ParentApp.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this ParentApp.


        :param is_enabled: The is_enabled of this ParentApp.  # noqa: E501
        :type is_enabled: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def allow_templates(self):
        """Gets the allow_templates of this ParentApp.  # noqa: E501


        :return: The allow_templates of this ParentApp.  # noqa: E501
        :rtype: bool
        """
        return self._allow_templates

    @allow_templates.setter
    def allow_templates(self, allow_templates):
        """Sets the allow_templates of this ParentApp.


        :param allow_templates: The allow_templates of this ParentApp.  # noqa: E501
        :type allow_templates: bool
        """

        self._allow_templates = allow_templates

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
        if not isinstance(other, ParentApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParentApp):
            return True

        return self.to_dict() != other.to_dict()