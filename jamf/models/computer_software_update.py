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


class ComputerSoftwareUpdate(object):
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
        'version': 'str',
        'package_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'package_name': 'packageName'
    }

    def __init__(self, name=None, version=None, package_name=None, local_vars_configuration=None):  # noqa: E501
        """ComputerSoftwareUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._version = None
        self._package_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if package_name is not None:
            self.package_name = package_name

    @property
    def name(self):
        """Gets the name of this ComputerSoftwareUpdate.  # noqa: E501


        :return: The name of this ComputerSoftwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerSoftwareUpdate.


        :param name: The name of this ComputerSoftwareUpdate.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this ComputerSoftwareUpdate.  # noqa: E501


        :return: The version of this ComputerSoftwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComputerSoftwareUpdate.


        :param version: The version of this ComputerSoftwareUpdate.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def package_name(self):
        """Gets the package_name of this ComputerSoftwareUpdate.  # noqa: E501


        :return: The package_name of this ComputerSoftwareUpdate.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ComputerSoftwareUpdate.


        :param package_name: The package_name of this ComputerSoftwareUpdate.  # noqa: E501
        :type package_name: str
        """

        self._package_name = package_name

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
        if not isinstance(other, ComputerSoftwareUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerSoftwareUpdate):
            return True

        return self.to_dict() != other.to_dict()
