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


class ComputerApplication(object):
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
        'path': 'str',
        'version': 'str',
        'mac_app_store': 'bool',
        'size_megabytes': 'int',
        'bundle_id': 'str',
        'update_available': 'bool',
        'external_version_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'version': 'version',
        'mac_app_store': 'macAppStore',
        'size_megabytes': 'sizeMegabytes',
        'bundle_id': 'bundleId',
        'update_available': 'updateAvailable',
        'external_version_id': 'externalVersionId'
    }

    def __init__(self, name=None, path=None, version=None, mac_app_store=None, size_megabytes=None, bundle_id=None, update_available=None, external_version_id=None, local_vars_configuration=None):  # noqa: E501
        """ComputerApplication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._path = None
        self._version = None
        self._mac_app_store = None
        self._size_megabytes = None
        self._bundle_id = None
        self._update_available = None
        self._external_version_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if version is not None:
            self.version = version
        if mac_app_store is not None:
            self.mac_app_store = mac_app_store
        if size_megabytes is not None:
            self.size_megabytes = size_megabytes
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if update_available is not None:
            self.update_available = update_available
        if external_version_id is not None:
            self.external_version_id = external_version_id

    @property
    def name(self):
        """Gets the name of this ComputerApplication.  # noqa: E501


        :return: The name of this ComputerApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerApplication.


        :param name: The name of this ComputerApplication.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ComputerApplication.  # noqa: E501


        :return: The path of this ComputerApplication.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComputerApplication.


        :param path: The path of this ComputerApplication.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def version(self):
        """Gets the version of this ComputerApplication.  # noqa: E501


        :return: The version of this ComputerApplication.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComputerApplication.


        :param version: The version of this ComputerApplication.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def mac_app_store(self):
        """Gets the mac_app_store of this ComputerApplication.  # noqa: E501


        :return: The mac_app_store of this ComputerApplication.  # noqa: E501
        :rtype: bool
        """
        return self._mac_app_store

    @mac_app_store.setter
    def mac_app_store(self, mac_app_store):
        """Sets the mac_app_store of this ComputerApplication.


        :param mac_app_store: The mac_app_store of this ComputerApplication.  # noqa: E501
        :type mac_app_store: bool
        """

        self._mac_app_store = mac_app_store

    @property
    def size_megabytes(self):
        """Gets the size_megabytes of this ComputerApplication.  # noqa: E501


        :return: The size_megabytes of this ComputerApplication.  # noqa: E501
        :rtype: int
        """
        return self._size_megabytes

    @size_megabytes.setter
    def size_megabytes(self, size_megabytes):
        """Sets the size_megabytes of this ComputerApplication.


        :param size_megabytes: The size_megabytes of this ComputerApplication.  # noqa: E501
        :type size_megabytes: int
        """

        self._size_megabytes = size_megabytes

    @property
    def bundle_id(self):
        """Gets the bundle_id of this ComputerApplication.  # noqa: E501


        :return: The bundle_id of this ComputerApplication.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this ComputerApplication.


        :param bundle_id: The bundle_id of this ComputerApplication.  # noqa: E501
        :type bundle_id: str
        """

        self._bundle_id = bundle_id

    @property
    def update_available(self):
        """Gets the update_available of this ComputerApplication.  # noqa: E501


        :return: The update_available of this ComputerApplication.  # noqa: E501
        :rtype: bool
        """
        return self._update_available

    @update_available.setter
    def update_available(self, update_available):
        """Sets the update_available of this ComputerApplication.


        :param update_available: The update_available of this ComputerApplication.  # noqa: E501
        :type update_available: bool
        """

        self._update_available = update_available

    @property
    def external_version_id(self):
        """Gets the external_version_id of this ComputerApplication.  # noqa: E501

        The app's external version ID. It can be used in the iTunes Search API to decide if the app needs to be updated  # noqa: E501

        :return: The external_version_id of this ComputerApplication.  # noqa: E501
        :rtype: str
        """
        return self._external_version_id

    @external_version_id.setter
    def external_version_id(self, external_version_id):
        """Sets the external_version_id of this ComputerApplication.

        The app's external version ID. It can be used in the iTunes Search API to decide if the app needs to be updated  # noqa: E501

        :param external_version_id: The external_version_id of this ComputerApplication.  # noqa: E501
        :type external_version_id: str
        """

        self._external_version_id = external_version_id

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
        if not isinstance(other, ComputerApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputerApplication):
            return True

        return self.to_dict() != other.to_dict()
