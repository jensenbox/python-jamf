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


class InventoryPreloadCsvValidationErrorCause(object):
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
        'code': 'str',
        'field': 'str',
        'description': 'str',
        'id': 'str',
        'value': 'str',
        'serial_number': 'str',
        'line': 'int',
        'field_size': 'int',
        'device_type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'field': 'field',
        'description': 'description',
        'id': 'id',
        'value': 'value',
        'serial_number': 'serialNumber',
        'line': 'line',
        'field_size': 'fieldSize',
        'device_type': 'deviceType'
    }

    def __init__(self, code=None, field=None, description=None, id=None, value=None, serial_number=None, line=None, field_size=None, device_type=None, local_vars_configuration=None):  # noqa: E501
        """InventoryPreloadCsvValidationErrorCause - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._field = None
        self._description = None
        self._id = None
        self._value = None
        self._serial_number = None
        self._line = None
        self._field_size = None
        self._device_type = None
        self.discriminator = None

        if code is not None:
            self.code = code
        self.field = field
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if serial_number is not None:
            self.serial_number = serial_number
        if line is not None:
            self.line = line
        if field_size is not None:
            self.field_size = field_size
        if device_type is not None:
            self.device_type = device_type

    @property
    def code(self):
        """Gets the code of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501

        Error-specific code that can be used to identify localization string, etc.  # noqa: E501

        :return: The code of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InventoryPreloadCsvValidationErrorCause.

        Error-specific code that can be used to identify localization string, etc.  # noqa: E501

        :param code: The code of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def field(self):
        """Gets the field of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501

        Name of the field that caused the error.  # noqa: E501

        :return: The field of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this InventoryPreloadCsvValidationErrorCause.

        Name of the field that caused the error.  # noqa: E501

        :param field: The field of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def description(self):
        """Gets the description of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501

        A general description of error for troubleshooting/debugging. Generally this text should not be displayed to a user; instead refer to errorCode and it's localized text  # noqa: E501

        :return: The description of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventoryPreloadCsvValidationErrorCause.

        A general description of error for troubleshooting/debugging. Generally this text should not be displayed to a user; instead refer to errorCode and it's localized text  # noqa: E501

        :param description: The description of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501

        id of object with error. Optional.  # noqa: E501

        :return: The id of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPreloadCsvValidationErrorCause.

        id of object with error. Optional.  # noqa: E501

        :param id: The id of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501


        :return: The value of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InventoryPreloadCsvValidationErrorCause.


        :param value: The value of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def serial_number(self):
        """Gets the serial_number of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501


        :return: The serial_number of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this InventoryPreloadCsvValidationErrorCause.


        :param serial_number: The serial_number of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def line(self):
        """Gets the line of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501


        :return: The line of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this InventoryPreloadCsvValidationErrorCause.


        :param line: The line of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type line: int
        """

        self._line = line

    @property
    def field_size(self):
        """Gets the field_size of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501


        :return: The field_size of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: int
        """
        return self._field_size

    @field_size.setter
    def field_size(self, field_size):
        """Sets the field_size of this InventoryPreloadCsvValidationErrorCause.


        :param field_size: The field_size of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type field_size: int
        """

        self._field_size = field_size

    @property
    def device_type(self):
        """Gets the device_type of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501


        :return: The device_type of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InventoryPreloadCsvValidationErrorCause.


        :param device_type: The device_type of this InventoryPreloadCsvValidationErrorCause.  # noqa: E501
        :type device_type: str
        """

        self._device_type = device_type

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
        if not isinstance(other, InventoryPreloadCsvValidationErrorCause):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryPreloadCsvValidationErrorCause):
            return True

        return self.to_dict() != other.to_dict()
