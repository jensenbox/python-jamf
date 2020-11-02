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


class MobileDeviceSearchParams(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'is_load_to_end': 'bool',
        'order_by': 'list[OrderBy]',
        'udid': 'str',
        'mac_address': 'str',
        'name': 'str',
        'serial_number': 'str',
        'os_type': 'str',
        'is_managed': 'bool',
        'excluded_ids': 'list[int]'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'is_load_to_end': 'isLoadToEnd',
        'order_by': 'orderBy',
        'udid': 'udid',
        'mac_address': 'macAddress',
        'name': 'name',
        'serial_number': 'serialNumber',
        'os_type': 'osType',
        'is_managed': 'isManaged',
        'excluded_ids': 'excludedIds'
    }

    def __init__(self, page_number=None, page_size=None, is_load_to_end=None, order_by=None, udid=None, mac_address=None, name=None, serial_number=None, os_type=None, is_managed=None, excluded_ids=None, local_vars_configuration=None):  # noqa: E501
        """MobileDeviceSearchParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page_number = None
        self._page_size = None
        self._is_load_to_end = None
        self._order_by = None
        self._udid = None
        self._mac_address = None
        self._name = None
        self._serial_number = None
        self._os_type = None
        self._is_managed = None
        self._excluded_ids = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if is_load_to_end is not None:
            self.is_load_to_end = is_load_to_end
        if order_by is not None:
            self.order_by = order_by
        if udid is not None:
            self.udid = udid
        if mac_address is not None:
            self.mac_address = mac_address
        if name is not None:
            self.name = name
        if serial_number is not None:
            self.serial_number = serial_number
        if os_type is not None:
            self.os_type = os_type
        if is_managed is not None:
            self.is_managed = is_managed
        if excluded_ids is not None:
            self.excluded_ids = excluded_ids

    @property
    def page_number(self):
        """Gets the page_number of this MobileDeviceSearchParams.  # noqa: E501


        :return: The page_number of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this MobileDeviceSearchParams.


        :param page_number: The page_number of this MobileDeviceSearchParams.  # noqa: E501
        :type page_number: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this MobileDeviceSearchParams.  # noqa: E501


        :return: The page_size of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this MobileDeviceSearchParams.


        :param page_size: The page_size of this MobileDeviceSearchParams.  # noqa: E501
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def is_load_to_end(self):
        """Gets the is_load_to_end of this MobileDeviceSearchParams.  # noqa: E501


        :return: The is_load_to_end of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_load_to_end

    @is_load_to_end.setter
    def is_load_to_end(self, is_load_to_end):
        """Sets the is_load_to_end of this MobileDeviceSearchParams.


        :param is_load_to_end: The is_load_to_end of this MobileDeviceSearchParams.  # noqa: E501
        :type is_load_to_end: bool
        """

        self._is_load_to_end = is_load_to_end

    @property
    def order_by(self):
        """Gets the order_by of this MobileDeviceSearchParams.  # noqa: E501


        :return: The order_by of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: list[OrderBy]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this MobileDeviceSearchParams.


        :param order_by: The order_by of this MobileDeviceSearchParams.  # noqa: E501
        :type order_by: list[OrderBy]
        """

        self._order_by = order_by

    @property
    def udid(self):
        """Gets the udid of this MobileDeviceSearchParams.  # noqa: E501


        :return: The udid of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this MobileDeviceSearchParams.


        :param udid: The udid of this MobileDeviceSearchParams.  # noqa: E501
        :type udid: str
        """

        self._udid = udid

    @property
    def mac_address(self):
        """Gets the mac_address of this MobileDeviceSearchParams.  # noqa: E501


        :return: The mac_address of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this MobileDeviceSearchParams.


        :param mac_address: The mac_address of this MobileDeviceSearchParams.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this MobileDeviceSearchParams.  # noqa: E501


        :return: The name of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MobileDeviceSearchParams.


        :param name: The name of this MobileDeviceSearchParams.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def serial_number(self):
        """Gets the serial_number of this MobileDeviceSearchParams.  # noqa: E501


        :return: The serial_number of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this MobileDeviceSearchParams.


        :param serial_number: The serial_number of this MobileDeviceSearchParams.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def os_type(self):
        """Gets the os_type of this MobileDeviceSearchParams.  # noqa: E501


        :return: The os_type of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this MobileDeviceSearchParams.


        :param os_type: The os_type of this MobileDeviceSearchParams.  # noqa: E501
        :type os_type: str
        """

        self._os_type = os_type

    @property
    def is_managed(self):
        """Gets the is_managed of this MobileDeviceSearchParams.  # noqa: E501


        :return: The is_managed of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this MobileDeviceSearchParams.


        :param is_managed: The is_managed of this MobileDeviceSearchParams.  # noqa: E501
        :type is_managed: bool
        """

        self._is_managed = is_managed

    @property
    def excluded_ids(self):
        """Gets the excluded_ids of this MobileDeviceSearchParams.  # noqa: E501


        :return: The excluded_ids of this MobileDeviceSearchParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_ids

    @excluded_ids.setter
    def excluded_ids(self, excluded_ids):
        """Sets the excluded_ids of this MobileDeviceSearchParams.


        :param excluded_ids: The excluded_ids of this MobileDeviceSearchParams.  # noqa: E501
        :type excluded_ids: list[int]
        """

        self._excluded_ids = excluded_ids

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
        if not isinstance(other, MobileDeviceSearchParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MobileDeviceSearchParams):
            return True

        return self.to_dict() != other.to_dict()