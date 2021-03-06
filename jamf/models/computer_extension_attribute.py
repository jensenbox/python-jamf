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


class ComputerExtensionAttribute(object):
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
        'definition_id': 'str',
        'name': 'str',
        'description': 'str',
        'enabled': 'bool',
        'multi_value': 'bool',
        'values': 'list[str]',
        'data_type': 'str',
        'options': 'list[str]',
        'input_type': 'str'
    }

    attribute_map = {
        'definition_id': 'definitionId',
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'multi_value': 'multiValue',
        'values': 'values',
        'data_type': 'dataType',
        'options': 'options',
        'input_type': 'inputType'
    }

    def __init__(self, definition_id=None, name=None, description=None, enabled=None, multi_value=None, values=None, data_type=None, options=None, input_type=None, local_vars_configuration=None):  # noqa: E501
        """ComputerExtensionAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._definition_id = None
        self._name = None
        self._description = None
        self._enabled = None
        self._multi_value = None
        self._values = None
        self._data_type = None
        self._options = None
        self._input_type = None
        self.discriminator = None

        if definition_id is not None:
            self.definition_id = definition_id
        if name is not None:
            self.name = name
        self.description = description
        if enabled is not None:
            self.enabled = enabled
        if multi_value is not None:
            self.multi_value = multi_value
        self.values = values
        self.data_type = data_type
        self.options = options
        self.input_type = input_type

    @property
    def definition_id(self):
        """Gets the definition_id of this ComputerExtensionAttribute.  # noqa: E501

        An identifier of extension attribute definition.  # noqa: E501

        :return: The definition_id of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._definition_id

    @definition_id.setter
    def definition_id(self, definition_id):
        """Sets the definition_id of this ComputerExtensionAttribute.

        An identifier of extension attribute definition.  # noqa: E501

        :param definition_id: The definition_id of this ComputerExtensionAttribute.  # noqa: E501
        :type definition_id: str
        """

        self._definition_id = definition_id

    @property
    def name(self):
        """Gets the name of this ComputerExtensionAttribute.  # noqa: E501

        A human-readable name by which attribute can be referred to.  # noqa: E501

        :return: The name of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerExtensionAttribute.

        A human-readable name by which attribute can be referred to.  # noqa: E501

        :param name: The name of this ComputerExtensionAttribute.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ComputerExtensionAttribute.  # noqa: E501

        An additional explanation of exact attribute meaning, possible values, etc.  # noqa: E501

        :return: The description of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComputerExtensionAttribute.

        An additional explanation of exact attribute meaning, possible values, etc.  # noqa: E501

        :param description: The description of this ComputerExtensionAttribute.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ComputerExtensionAttribute.  # noqa: E501


        :return: The enabled of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ComputerExtensionAttribute.


        :param enabled: The enabled of this ComputerExtensionAttribute.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def multi_value(self):
        """Gets the multi_value of this ComputerExtensionAttribute.  # noqa: E501


        :return: The multi_value of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._multi_value

    @multi_value.setter
    def multi_value(self, multi_value):
        """Sets the multi_value of this ComputerExtensionAttribute.


        :param multi_value: The multi_value of this ComputerExtensionAttribute.  # noqa: E501
        :type multi_value: bool
        """

        self._multi_value = multi_value

    @property
    def values(self):
        """Gets the values of this ComputerExtensionAttribute.  # noqa: E501

        A value of extension attribute, in some rare cases there may be multiple values present, hence the array.   # noqa: E501

        :return: The values of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ComputerExtensionAttribute.

        A value of extension attribute, in some rare cases there may be multiple values present, hence the array.   # noqa: E501

        :param values: The values of this ComputerExtensionAttribute.  # noqa: E501
        :type values: list[str]
        """

        self._values = values

    @property
    def data_type(self):
        """Gets the data_type of this ComputerExtensionAttribute.  # noqa: E501

        A data type of extension attribute.  # noqa: E501

        :return: The data_type of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ComputerExtensionAttribute.

        A data type of extension attribute.  # noqa: E501

        :param data_type: The data_type of this ComputerExtensionAttribute.  # noqa: E501
        :type data_type: str
        """
        allowed_values = [None,"STRING", "INTEGER", "DATE_TIME"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def options(self):
        """Gets the options of this ComputerExtensionAttribute.  # noqa: E501

        A closed list of possible values (applies to `popup` input type).   # noqa: E501

        :return: The options of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ComputerExtensionAttribute.

        A closed list of possible values (applies to `popup` input type).   # noqa: E501

        :param options: The options of this ComputerExtensionAttribute.  # noqa: E501
        :type options: list[str]
        """

        self._options = options

    @property
    def input_type(self):
        """Gets the input_type of this ComputerExtensionAttribute.  # noqa: E501

        The input method. `text` is most common and means simply free text, `popup` i a closed list of values from which one or many can be selected and `script` value is calculated and can never be set directly.   # noqa: E501

        :return: The input_type of this ComputerExtensionAttribute.  # noqa: E501
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this ComputerExtensionAttribute.

        The input method. `text` is most common and means simply free text, `popup` i a closed list of values from which one or many can be selected and `script` value is calculated and can never be set directly.   # noqa: E501

        :param input_type: The input_type of this ComputerExtensionAttribute.  # noqa: E501
        :type input_type: str
        """
        allowed_values = [None,"TEXT", "POPUP", "SCRIPT", "LDAP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and input_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `input_type` ({0}), must be one of {1}"  # noqa: E501
                .format(input_type, allowed_values)
            )

        self._input_type = input_type

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
        if not isinstance(other, ComputerExtensionAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerExtensionAttribute):
            return True

        return self.to_dict() != other.to_dict()
