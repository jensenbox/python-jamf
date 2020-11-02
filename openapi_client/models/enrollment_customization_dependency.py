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


class EnrollmentCustomizationDependency(object):
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
        'human_readable_name': 'str',
        'hyperlink': 'str'
    }

    attribute_map = {
        'name': 'name',
        'human_readable_name': 'humanReadableName',
        'hyperlink': 'hyperlink'
    }

    def __init__(self, name=None, human_readable_name=None, hyperlink=None, local_vars_configuration=None):  # noqa: E501
        """EnrollmentCustomizationDependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._human_readable_name = None
        self._hyperlink = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if human_readable_name is not None:
            self.human_readable_name = human_readable_name
        if hyperlink is not None:
            self.hyperlink = hyperlink

    @property
    def name(self):
        """Gets the name of this EnrollmentCustomizationDependency.  # noqa: E501


        :return: The name of this EnrollmentCustomizationDependency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnrollmentCustomizationDependency.


        :param name: The name of this EnrollmentCustomizationDependency.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def human_readable_name(self):
        """Gets the human_readable_name of this EnrollmentCustomizationDependency.  # noqa: E501


        :return: The human_readable_name of this EnrollmentCustomizationDependency.  # noqa: E501
        :rtype: str
        """
        return self._human_readable_name

    @human_readable_name.setter
    def human_readable_name(self, human_readable_name):
        """Sets the human_readable_name of this EnrollmentCustomizationDependency.


        :param human_readable_name: The human_readable_name of this EnrollmentCustomizationDependency.  # noqa: E501
        :type human_readable_name: str
        """

        self._human_readable_name = human_readable_name

    @property
    def hyperlink(self):
        """Gets the hyperlink of this EnrollmentCustomizationDependency.  # noqa: E501


        :return: The hyperlink of this EnrollmentCustomizationDependency.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink

    @hyperlink.setter
    def hyperlink(self, hyperlink):
        """Sets the hyperlink of this EnrollmentCustomizationDependency.


        :param hyperlink: The hyperlink of this EnrollmentCustomizationDependency.  # noqa: E501
        :type hyperlink: str
        """

        self._hyperlink = hyperlink

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
        if not isinstance(other, EnrollmentCustomizationDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrollmentCustomizationDependency):
            return True

        return self.to_dict() != other.to_dict()