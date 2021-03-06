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


class Network(object):
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
        'cellular_technology': 'str',
        'is_voice_roaming_enabled': 'bool',
        'imei': 'str',
        'iccid': 'str',
        'meid': 'str',
        'carrier_settings_version': 'str',
        'current_carrier_network': 'str',
        'current_mobile_country_code': 'str',
        'current_mobile_network_code': 'str',
        'home_carrier_network': 'str',
        'home_mobile_country_code': 'str',
        'home_mobile_network_code': 'str',
        'is_data_roaming_enabled': 'bool',
        'is_roaming': 'bool',
        'is_personal_hotspot_enabled': 'bool',
        'phone_number': 'str'
    }

    attribute_map = {
        'cellular_technology': 'cellularTechnology',
        'is_voice_roaming_enabled': 'isVoiceRoamingEnabled',
        'imei': 'imei',
        'iccid': 'iccid',
        'meid': 'meid',
        'carrier_settings_version': 'carrierSettingsVersion',
        'current_carrier_network': 'currentCarrierNetwork',
        'current_mobile_country_code': 'currentMobileCountryCode',
        'current_mobile_network_code': 'currentMobileNetworkCode',
        'home_carrier_network': 'homeCarrierNetwork',
        'home_mobile_country_code': 'homeMobileCountryCode',
        'home_mobile_network_code': 'homeMobileNetworkCode',
        'is_data_roaming_enabled': 'isDataRoamingEnabled',
        'is_roaming': 'isRoaming',
        'is_personal_hotspot_enabled': 'isPersonalHotspotEnabled',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, cellular_technology=None, is_voice_roaming_enabled=None, imei=None, iccid=None, meid=None, carrier_settings_version=None, current_carrier_network=None, current_mobile_country_code=None, current_mobile_network_code=None, home_carrier_network=None, home_mobile_country_code=None, home_mobile_network_code=None, is_data_roaming_enabled=None, is_roaming=None, is_personal_hotspot_enabled=None, phone_number=None, local_vars_configuration=None):  # noqa: E501
        """Network - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cellular_technology = None
        self._is_voice_roaming_enabled = None
        self._imei = None
        self._iccid = None
        self._meid = None
        self._carrier_settings_version = None
        self._current_carrier_network = None
        self._current_mobile_country_code = None
        self._current_mobile_network_code = None
        self._home_carrier_network = None
        self._home_mobile_country_code = None
        self._home_mobile_network_code = None
        self._is_data_roaming_enabled = None
        self._is_roaming = None
        self._is_personal_hotspot_enabled = None
        self._phone_number = None
        self.discriminator = None

        if cellular_technology is not None:
            self.cellular_technology = cellular_technology
        if is_voice_roaming_enabled is not None:
            self.is_voice_roaming_enabled = is_voice_roaming_enabled
        if imei is not None:
            self.imei = imei
        if iccid is not None:
            self.iccid = iccid
        if meid is not None:
            self.meid = meid
        if carrier_settings_version is not None:
            self.carrier_settings_version = carrier_settings_version
        if current_carrier_network is not None:
            self.current_carrier_network = current_carrier_network
        if current_mobile_country_code is not None:
            self.current_mobile_country_code = current_mobile_country_code
        if current_mobile_network_code is not None:
            self.current_mobile_network_code = current_mobile_network_code
        if home_carrier_network is not None:
            self.home_carrier_network = home_carrier_network
        if home_mobile_country_code is not None:
            self.home_mobile_country_code = home_mobile_country_code
        if home_mobile_network_code is not None:
            self.home_mobile_network_code = home_mobile_network_code
        if is_data_roaming_enabled is not None:
            self.is_data_roaming_enabled = is_data_roaming_enabled
        if is_roaming is not None:
            self.is_roaming = is_roaming
        if is_personal_hotspot_enabled is not None:
            self.is_personal_hotspot_enabled = is_personal_hotspot_enabled
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def cellular_technology(self):
        """Gets the cellular_technology of this Network.  # noqa: E501


        :return: The cellular_technology of this Network.  # noqa: E501
        :rtype: str
        """
        return self._cellular_technology

    @cellular_technology.setter
    def cellular_technology(self, cellular_technology):
        """Sets the cellular_technology of this Network.


        :param cellular_technology: The cellular_technology of this Network.  # noqa: E501
        :type cellular_technology: str
        """

        self._cellular_technology = cellular_technology

    @property
    def is_voice_roaming_enabled(self):
        """Gets the is_voice_roaming_enabled of this Network.  # noqa: E501


        :return: The is_voice_roaming_enabled of this Network.  # noqa: E501
        :rtype: bool
        """
        return self._is_voice_roaming_enabled

    @is_voice_roaming_enabled.setter
    def is_voice_roaming_enabled(self, is_voice_roaming_enabled):
        """Sets the is_voice_roaming_enabled of this Network.


        :param is_voice_roaming_enabled: The is_voice_roaming_enabled of this Network.  # noqa: E501
        :type is_voice_roaming_enabled: bool
        """

        self._is_voice_roaming_enabled = is_voice_roaming_enabled

    @property
    def imei(self):
        """Gets the imei of this Network.  # noqa: E501


        :return: The imei of this Network.  # noqa: E501
        :rtype: str
        """
        return self._imei

    @imei.setter
    def imei(self, imei):
        """Sets the imei of this Network.


        :param imei: The imei of this Network.  # noqa: E501
        :type imei: str
        """

        self._imei = imei

    @property
    def iccid(self):
        """Gets the iccid of this Network.  # noqa: E501


        :return: The iccid of this Network.  # noqa: E501
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this Network.


        :param iccid: The iccid of this Network.  # noqa: E501
        :type iccid: str
        """

        self._iccid = iccid

    @property
    def meid(self):
        """Gets the meid of this Network.  # noqa: E501


        :return: The meid of this Network.  # noqa: E501
        :rtype: str
        """
        return self._meid

    @meid.setter
    def meid(self, meid):
        """Sets the meid of this Network.


        :param meid: The meid of this Network.  # noqa: E501
        :type meid: str
        """

        self._meid = meid

    @property
    def carrier_settings_version(self):
        """Gets the carrier_settings_version of this Network.  # noqa: E501


        :return: The carrier_settings_version of this Network.  # noqa: E501
        :rtype: str
        """
        return self._carrier_settings_version

    @carrier_settings_version.setter
    def carrier_settings_version(self, carrier_settings_version):
        """Sets the carrier_settings_version of this Network.


        :param carrier_settings_version: The carrier_settings_version of this Network.  # noqa: E501
        :type carrier_settings_version: str
        """

        self._carrier_settings_version = carrier_settings_version

    @property
    def current_carrier_network(self):
        """Gets the current_carrier_network of this Network.  # noqa: E501


        :return: The current_carrier_network of this Network.  # noqa: E501
        :rtype: str
        """
        return self._current_carrier_network

    @current_carrier_network.setter
    def current_carrier_network(self, current_carrier_network):
        """Sets the current_carrier_network of this Network.


        :param current_carrier_network: The current_carrier_network of this Network.  # noqa: E501
        :type current_carrier_network: str
        """

        self._current_carrier_network = current_carrier_network

    @property
    def current_mobile_country_code(self):
        """Gets the current_mobile_country_code of this Network.  # noqa: E501


        :return: The current_mobile_country_code of this Network.  # noqa: E501
        :rtype: str
        """
        return self._current_mobile_country_code

    @current_mobile_country_code.setter
    def current_mobile_country_code(self, current_mobile_country_code):
        """Sets the current_mobile_country_code of this Network.


        :param current_mobile_country_code: The current_mobile_country_code of this Network.  # noqa: E501
        :type current_mobile_country_code: str
        """

        self._current_mobile_country_code = current_mobile_country_code

    @property
    def current_mobile_network_code(self):
        """Gets the current_mobile_network_code of this Network.  # noqa: E501


        :return: The current_mobile_network_code of this Network.  # noqa: E501
        :rtype: str
        """
        return self._current_mobile_network_code

    @current_mobile_network_code.setter
    def current_mobile_network_code(self, current_mobile_network_code):
        """Sets the current_mobile_network_code of this Network.


        :param current_mobile_network_code: The current_mobile_network_code of this Network.  # noqa: E501
        :type current_mobile_network_code: str
        """

        self._current_mobile_network_code = current_mobile_network_code

    @property
    def home_carrier_network(self):
        """Gets the home_carrier_network of this Network.  # noqa: E501


        :return: The home_carrier_network of this Network.  # noqa: E501
        :rtype: str
        """
        return self._home_carrier_network

    @home_carrier_network.setter
    def home_carrier_network(self, home_carrier_network):
        """Sets the home_carrier_network of this Network.


        :param home_carrier_network: The home_carrier_network of this Network.  # noqa: E501
        :type home_carrier_network: str
        """

        self._home_carrier_network = home_carrier_network

    @property
    def home_mobile_country_code(self):
        """Gets the home_mobile_country_code of this Network.  # noqa: E501


        :return: The home_mobile_country_code of this Network.  # noqa: E501
        :rtype: str
        """
        return self._home_mobile_country_code

    @home_mobile_country_code.setter
    def home_mobile_country_code(self, home_mobile_country_code):
        """Sets the home_mobile_country_code of this Network.


        :param home_mobile_country_code: The home_mobile_country_code of this Network.  # noqa: E501
        :type home_mobile_country_code: str
        """

        self._home_mobile_country_code = home_mobile_country_code

    @property
    def home_mobile_network_code(self):
        """Gets the home_mobile_network_code of this Network.  # noqa: E501


        :return: The home_mobile_network_code of this Network.  # noqa: E501
        :rtype: str
        """
        return self._home_mobile_network_code

    @home_mobile_network_code.setter
    def home_mobile_network_code(self, home_mobile_network_code):
        """Sets the home_mobile_network_code of this Network.


        :param home_mobile_network_code: The home_mobile_network_code of this Network.  # noqa: E501
        :type home_mobile_network_code: str
        """

        self._home_mobile_network_code = home_mobile_network_code

    @property
    def is_data_roaming_enabled(self):
        """Gets the is_data_roaming_enabled of this Network.  # noqa: E501


        :return: The is_data_roaming_enabled of this Network.  # noqa: E501
        :rtype: bool
        """
        return self._is_data_roaming_enabled

    @is_data_roaming_enabled.setter
    def is_data_roaming_enabled(self, is_data_roaming_enabled):
        """Sets the is_data_roaming_enabled of this Network.


        :param is_data_roaming_enabled: The is_data_roaming_enabled of this Network.  # noqa: E501
        :type is_data_roaming_enabled: bool
        """

        self._is_data_roaming_enabled = is_data_roaming_enabled

    @property
    def is_roaming(self):
        """Gets the is_roaming of this Network.  # noqa: E501


        :return: The is_roaming of this Network.  # noqa: E501
        :rtype: bool
        """
        return self._is_roaming

    @is_roaming.setter
    def is_roaming(self, is_roaming):
        """Sets the is_roaming of this Network.


        :param is_roaming: The is_roaming of this Network.  # noqa: E501
        :type is_roaming: bool
        """

        self._is_roaming = is_roaming

    @property
    def is_personal_hotspot_enabled(self):
        """Gets the is_personal_hotspot_enabled of this Network.  # noqa: E501


        :return: The is_personal_hotspot_enabled of this Network.  # noqa: E501
        :rtype: bool
        """
        return self._is_personal_hotspot_enabled

    @is_personal_hotspot_enabled.setter
    def is_personal_hotspot_enabled(self, is_personal_hotspot_enabled):
        """Sets the is_personal_hotspot_enabled of this Network.


        :param is_personal_hotspot_enabled: The is_personal_hotspot_enabled of this Network.  # noqa: E501
        :type is_personal_hotspot_enabled: bool
        """

        self._is_personal_hotspot_enabled = is_personal_hotspot_enabled

    @property
    def phone_number(self):
        """Gets the phone_number of this Network.  # noqa: E501


        :return: The phone_number of this Network.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Network.


        :param phone_number: The phone_number of this Network.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, Network):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Network):
            return True

        return self.to_dict() != other.to_dict()
