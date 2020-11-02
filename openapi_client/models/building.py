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


class Building(object):
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
        'id': 'str',
        'name': 'str',
        'street_address1': 'str',
        'street_address2': 'str',
        'city': 'str',
        'state_province': 'str',
        'zip_postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'street_address1': 'streetAddress1',
        'street_address2': 'streetAddress2',
        'city': 'city',
        'state_province': 'stateProvince',
        'zip_postal_code': 'zipPostalCode',
        'country': 'country'
    }

    def __init__(self, id=None, name=None, street_address1=None, street_address2=None, city=None, state_province=None, zip_postal_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """Building - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._street_address1 = None
        self._street_address2 = None
        self._city = None
        self._state_province = None
        self._zip_postal_code = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if street_address1 is not None:
            self.street_address1 = street_address1
        if street_address2 is not None:
            self.street_address2 = street_address2
        if city is not None:
            self.city = city
        if state_province is not None:
            self.state_province = state_province
        if zip_postal_code is not None:
            self.zip_postal_code = zip_postal_code
        if country is not None:
            self.country = country

    @property
    def id(self):
        """Gets the id of this Building.  # noqa: E501


        :return: The id of this Building.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Building.


        :param id: The id of this Building.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Building.  # noqa: E501


        :return: The name of this Building.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Building.


        :param name: The name of this Building.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def street_address1(self):
        """Gets the street_address1 of this Building.  # noqa: E501


        :return: The street_address1 of this Building.  # noqa: E501
        :rtype: str
        """
        return self._street_address1

    @street_address1.setter
    def street_address1(self, street_address1):
        """Sets the street_address1 of this Building.


        :param street_address1: The street_address1 of this Building.  # noqa: E501
        :type street_address1: str
        """

        self._street_address1 = street_address1

    @property
    def street_address2(self):
        """Gets the street_address2 of this Building.  # noqa: E501


        :return: The street_address2 of this Building.  # noqa: E501
        :rtype: str
        """
        return self._street_address2

    @street_address2.setter
    def street_address2(self, street_address2):
        """Sets the street_address2 of this Building.


        :param street_address2: The street_address2 of this Building.  # noqa: E501
        :type street_address2: str
        """

        self._street_address2 = street_address2

    @property
    def city(self):
        """Gets the city of this Building.  # noqa: E501


        :return: The city of this Building.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Building.


        :param city: The city of this Building.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def state_province(self):
        """Gets the state_province of this Building.  # noqa: E501


        :return: The state_province of this Building.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this Building.


        :param state_province: The state_province of this Building.  # noqa: E501
        :type state_province: str
        """

        self._state_province = state_province

    @property
    def zip_postal_code(self):
        """Gets the zip_postal_code of this Building.  # noqa: E501


        :return: The zip_postal_code of this Building.  # noqa: E501
        :rtype: str
        """
        return self._zip_postal_code

    @zip_postal_code.setter
    def zip_postal_code(self, zip_postal_code):
        """Sets the zip_postal_code of this Building.


        :param zip_postal_code: The zip_postal_code of this Building.  # noqa: E501
        :type zip_postal_code: str
        """

        self._zip_postal_code = zip_postal_code

    @property
    def country(self):
        """Gets the country of this Building.  # noqa: E501


        :return: The country of this Building.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Building.


        :param country: The country of this Building.  # noqa: E501
        :type country: str
        """

        self._country = country

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
        if not isinstance(other, Building):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Building):
            return True

        return self.to_dict() != other.to_dict()
