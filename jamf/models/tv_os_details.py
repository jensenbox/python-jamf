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


class TvOsDetails(object):
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
        'model': 'str',
        'model_identifier': 'str',
        'model_number': 'str',
        'supervised': 'bool',
        'airplay_password': 'str',
        'device_id': 'str',
        'locales': 'str',
        'purchasing': 'PurchasingV2',
        'configuration_profiles': 'list[ConfigurationProfile]'
    }

    attribute_map = {
        'model': 'model',
        'model_identifier': 'modelIdentifier',
        'model_number': 'modelNumber',
        'supervised': 'supervised',
        'airplay_password': 'airplayPassword',
        'device_id': 'deviceId',
        'locales': 'locales',
        'purchasing': 'purchasing',
        'configuration_profiles': 'configurationProfiles'
    }

    def __init__(self, model=None, model_identifier=None, model_number=None, supervised=None, airplay_password=None, device_id=None, locales=None, purchasing=None, configuration_profiles=None, local_vars_configuration=None):  # noqa: E501
        """TvOsDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model = None
        self._model_identifier = None
        self._model_number = None
        self._supervised = None
        self._airplay_password = None
        self._device_id = None
        self._locales = None
        self._purchasing = None
        self._configuration_profiles = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if model_identifier is not None:
            self.model_identifier = model_identifier
        if model_number is not None:
            self.model_number = model_number
        if supervised is not None:
            self.supervised = supervised
        if airplay_password is not None:
            self.airplay_password = airplay_password
        if device_id is not None:
            self.device_id = device_id
        if locales is not None:
            self.locales = locales
        if purchasing is not None:
            self.purchasing = purchasing
        if configuration_profiles is not None:
            self.configuration_profiles = configuration_profiles

    @property
    def model(self):
        """Gets the model of this TvOsDetails.  # noqa: E501


        :return: The model of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TvOsDetails.


        :param model: The model of this TvOsDetails.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def model_identifier(self):
        """Gets the model_identifier of this TvOsDetails.  # noqa: E501


        :return: The model_identifier of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._model_identifier

    @model_identifier.setter
    def model_identifier(self, model_identifier):
        """Sets the model_identifier of this TvOsDetails.


        :param model_identifier: The model_identifier of this TvOsDetails.  # noqa: E501
        :type model_identifier: str
        """

        self._model_identifier = model_identifier

    @property
    def model_number(self):
        """Gets the model_number of this TvOsDetails.  # noqa: E501


        :return: The model_number of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this TvOsDetails.


        :param model_number: The model_number of this TvOsDetails.  # noqa: E501
        :type model_number: str
        """

        self._model_number = model_number

    @property
    def supervised(self):
        """Gets the supervised of this TvOsDetails.  # noqa: E501


        :return: The supervised of this TvOsDetails.  # noqa: E501
        :rtype: bool
        """
        return self._supervised

    @supervised.setter
    def supervised(self, supervised):
        """Sets the supervised of this TvOsDetails.


        :param supervised: The supervised of this TvOsDetails.  # noqa: E501
        :type supervised: bool
        """

        self._supervised = supervised

    @property
    def airplay_password(self):
        """Gets the airplay_password of this TvOsDetails.  # noqa: E501


        :return: The airplay_password of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._airplay_password

    @airplay_password.setter
    def airplay_password(self, airplay_password):
        """Sets the airplay_password of this TvOsDetails.


        :param airplay_password: The airplay_password of this TvOsDetails.  # noqa: E501
        :type airplay_password: str
        """

        self._airplay_password = airplay_password

    @property
    def device_id(self):
        """Gets the device_id of this TvOsDetails.  # noqa: E501


        :return: The device_id of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this TvOsDetails.


        :param device_id: The device_id of this TvOsDetails.  # noqa: E501
        :type device_id: str
        """

        self._device_id = device_id

    @property
    def locales(self):
        """Gets the locales of this TvOsDetails.  # noqa: E501


        :return: The locales of this TvOsDetails.  # noqa: E501
        :rtype: str
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this TvOsDetails.


        :param locales: The locales of this TvOsDetails.  # noqa: E501
        :type locales: str
        """

        self._locales = locales

    @property
    def purchasing(self):
        """Gets the purchasing of this TvOsDetails.  # noqa: E501


        :return: The purchasing of this TvOsDetails.  # noqa: E501
        :rtype: PurchasingV2
        """
        return self._purchasing

    @purchasing.setter
    def purchasing(self, purchasing):
        """Sets the purchasing of this TvOsDetails.


        :param purchasing: The purchasing of this TvOsDetails.  # noqa: E501
        :type purchasing: PurchasingV2
        """

        self._purchasing = purchasing

    @property
    def configuration_profiles(self):
        """Gets the configuration_profiles of this TvOsDetails.  # noqa: E501


        :return: The configuration_profiles of this TvOsDetails.  # noqa: E501
        :rtype: list[ConfigurationProfile]
        """
        return self._configuration_profiles

    @configuration_profiles.setter
    def configuration_profiles(self, configuration_profiles):
        """Sets the configuration_profiles of this TvOsDetails.


        :param configuration_profiles: The configuration_profiles of this TvOsDetails.  # noqa: E501
        :type configuration_profiles: list[ConfigurationProfile]
        """

        self._configuration_profiles = configuration_profiles

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
        if not isinstance(other, TvOsDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TvOsDetails):
            return True

        return self.to_dict() != other.to_dict()
