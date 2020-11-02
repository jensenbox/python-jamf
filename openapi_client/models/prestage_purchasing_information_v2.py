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


class PrestagePurchasingInformationV2(object):
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
        'leased': 'bool',
        'purchased': 'bool',
        'apple_care_id': 'str',
        'po_number': 'str',
        'vendor': 'str',
        'purchase_price': 'str',
        'life_expectancy': 'int',
        'purchasing_account': 'str',
        'purchasing_contact': 'str',
        'lease_date': 'str',
        'po_date': 'str',
        'warranty_date': 'str',
        'version_lock': 'int'
    }

    attribute_map = {
        'id': 'id',
        'leased': 'leased',
        'purchased': 'purchased',
        'apple_care_id': 'appleCareId',
        'po_number': 'poNumber',
        'vendor': 'vendor',
        'purchase_price': 'purchasePrice',
        'life_expectancy': 'lifeExpectancy',
        'purchasing_account': 'purchasingAccount',
        'purchasing_contact': 'purchasingContact',
        'lease_date': 'leaseDate',
        'po_date': 'poDate',
        'warranty_date': 'warrantyDate',
        'version_lock': 'versionLock'
    }

    def __init__(self, id=None, leased=None, purchased=None, apple_care_id=None, po_number=None, vendor=None, purchase_price=None, life_expectancy=None, purchasing_account=None, purchasing_contact=None, lease_date=None, po_date=None, warranty_date=None, version_lock=None, local_vars_configuration=None):  # noqa: E501
        """PrestagePurchasingInformationV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._leased = None
        self._purchased = None
        self._apple_care_id = None
        self._po_number = None
        self._vendor = None
        self._purchase_price = None
        self._life_expectancy = None
        self._purchasing_account = None
        self._purchasing_contact = None
        self._lease_date = None
        self._po_date = None
        self._warranty_date = None
        self._version_lock = None
        self.discriminator = None

        self.id = id
        self.leased = leased
        self.purchased = purchased
        self.apple_care_id = apple_care_id
        self.po_number = po_number
        self.vendor = vendor
        self.purchase_price = purchase_price
        self.life_expectancy = life_expectancy
        self.purchasing_account = purchasing_account
        self.purchasing_contact = purchasing_contact
        self.lease_date = lease_date
        self.po_date = po_date
        self.warranty_date = warranty_date
        self.version_lock = version_lock

    @property
    def id(self):
        """Gets the id of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The id of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrestagePurchasingInformationV2.


        :param id: The id of this PrestagePurchasingInformationV2.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def leased(self):
        """Gets the leased of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The leased of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: bool
        """
        return self._leased

    @leased.setter
    def leased(self, leased):
        """Sets the leased of this PrestagePurchasingInformationV2.


        :param leased: The leased of this PrestagePurchasingInformationV2.  # noqa: E501
        :type leased: bool
        """
        if self.local_vars_configuration.client_side_validation and leased is None:  # noqa: E501
            raise ValueError("Invalid value for `leased`, must not be `None`")  # noqa: E501

        self._leased = leased

    @property
    def purchased(self):
        """Gets the purchased of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The purchased of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: bool
        """
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        """Sets the purchased of this PrestagePurchasingInformationV2.


        :param purchased: The purchased of this PrestagePurchasingInformationV2.  # noqa: E501
        :type purchased: bool
        """
        if self.local_vars_configuration.client_side_validation and purchased is None:  # noqa: E501
            raise ValueError("Invalid value for `purchased`, must not be `None`")  # noqa: E501

        self._purchased = purchased

    @property
    def apple_care_id(self):
        """Gets the apple_care_id of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The apple_care_id of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._apple_care_id

    @apple_care_id.setter
    def apple_care_id(self, apple_care_id):
        """Sets the apple_care_id of this PrestagePurchasingInformationV2.


        :param apple_care_id: The apple_care_id of this PrestagePurchasingInformationV2.  # noqa: E501
        :type apple_care_id: str
        """
        if self.local_vars_configuration.client_side_validation and apple_care_id is None:  # noqa: E501
            raise ValueError("Invalid value for `apple_care_id`, must not be `None`")  # noqa: E501

        self._apple_care_id = apple_care_id

    @property
    def po_number(self):
        """Gets the po_number of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The po_number of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this PrestagePurchasingInformationV2.


        :param po_number: The po_number of this PrestagePurchasingInformationV2.  # noqa: E501
        :type po_number: str
        """
        if self.local_vars_configuration.client_side_validation and po_number is None:  # noqa: E501
            raise ValueError("Invalid value for `po_number`, must not be `None`")  # noqa: E501

        self._po_number = po_number

    @property
    def vendor(self):
        """Gets the vendor of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The vendor of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this PrestagePurchasingInformationV2.


        :param vendor: The vendor of this PrestagePurchasingInformationV2.  # noqa: E501
        :type vendor: str
        """
        if self.local_vars_configuration.client_side_validation and vendor is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor`, must not be `None`")  # noqa: E501

        self._vendor = vendor

    @property
    def purchase_price(self):
        """Gets the purchase_price of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The purchase_price of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this PrestagePurchasingInformationV2.


        :param purchase_price: The purchase_price of this PrestagePurchasingInformationV2.  # noqa: E501
        :type purchase_price: str
        """
        if self.local_vars_configuration.client_side_validation and purchase_price is None:  # noqa: E501
            raise ValueError("Invalid value for `purchase_price`, must not be `None`")  # noqa: E501

        self._purchase_price = purchase_price

    @property
    def life_expectancy(self):
        """Gets the life_expectancy of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The life_expectancy of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: int
        """
        return self._life_expectancy

    @life_expectancy.setter
    def life_expectancy(self, life_expectancy):
        """Sets the life_expectancy of this PrestagePurchasingInformationV2.


        :param life_expectancy: The life_expectancy of this PrestagePurchasingInformationV2.  # noqa: E501
        :type life_expectancy: int
        """
        if self.local_vars_configuration.client_side_validation and life_expectancy is None:  # noqa: E501
            raise ValueError("Invalid value for `life_expectancy`, must not be `None`")  # noqa: E501

        self._life_expectancy = life_expectancy

    @property
    def purchasing_account(self):
        """Gets the purchasing_account of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The purchasing_account of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_account

    @purchasing_account.setter
    def purchasing_account(self, purchasing_account):
        """Sets the purchasing_account of this PrestagePurchasingInformationV2.


        :param purchasing_account: The purchasing_account of this PrestagePurchasingInformationV2.  # noqa: E501
        :type purchasing_account: str
        """
        if self.local_vars_configuration.client_side_validation and purchasing_account is None:  # noqa: E501
            raise ValueError("Invalid value for `purchasing_account`, must not be `None`")  # noqa: E501

        self._purchasing_account = purchasing_account

    @property
    def purchasing_contact(self):
        """Gets the purchasing_contact of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The purchasing_contact of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_contact

    @purchasing_contact.setter
    def purchasing_contact(self, purchasing_contact):
        """Sets the purchasing_contact of this PrestagePurchasingInformationV2.


        :param purchasing_contact: The purchasing_contact of this PrestagePurchasingInformationV2.  # noqa: E501
        :type purchasing_contact: str
        """
        if self.local_vars_configuration.client_side_validation and purchasing_contact is None:  # noqa: E501
            raise ValueError("Invalid value for `purchasing_contact`, must not be `None`")  # noqa: E501

        self._purchasing_contact = purchasing_contact

    @property
    def lease_date(self):
        """Gets the lease_date of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The lease_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._lease_date

    @lease_date.setter
    def lease_date(self, lease_date):
        """Sets the lease_date of this PrestagePurchasingInformationV2.


        :param lease_date: The lease_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :type lease_date: str
        """
        if self.local_vars_configuration.client_side_validation and lease_date is None:  # noqa: E501
            raise ValueError("Invalid value for `lease_date`, must not be `None`")  # noqa: E501

        self._lease_date = lease_date

    @property
    def po_date(self):
        """Gets the po_date of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The po_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._po_date

    @po_date.setter
    def po_date(self, po_date):
        """Sets the po_date of this PrestagePurchasingInformationV2.


        :param po_date: The po_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :type po_date: str
        """
        if self.local_vars_configuration.client_side_validation and po_date is None:  # noqa: E501
            raise ValueError("Invalid value for `po_date`, must not be `None`")  # noqa: E501

        self._po_date = po_date

    @property
    def warranty_date(self):
        """Gets the warranty_date of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The warranty_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._warranty_date

    @warranty_date.setter
    def warranty_date(self, warranty_date):
        """Sets the warranty_date of this PrestagePurchasingInformationV2.


        :param warranty_date: The warranty_date of this PrestagePurchasingInformationV2.  # noqa: E501
        :type warranty_date: str
        """
        if self.local_vars_configuration.client_side_validation and warranty_date is None:  # noqa: E501
            raise ValueError("Invalid value for `warranty_date`, must not be `None`")  # noqa: E501

        self._warranty_date = warranty_date

    @property
    def version_lock(self):
        """Gets the version_lock of this PrestagePurchasingInformationV2.  # noqa: E501


        :return: The version_lock of this PrestagePurchasingInformationV2.  # noqa: E501
        :rtype: int
        """
        return self._version_lock

    @version_lock.setter
    def version_lock(self, version_lock):
        """Sets the version_lock of this PrestagePurchasingInformationV2.


        :param version_lock: The version_lock of this PrestagePurchasingInformationV2.  # noqa: E501
        :type version_lock: int
        """
        if self.local_vars_configuration.client_side_validation and version_lock is None:  # noqa: E501
            raise ValueError("Invalid value for `version_lock`, must not be `None`")  # noqa: E501

        self._version_lock = version_lock

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
        if not isinstance(other, PrestagePurchasingInformationV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrestagePurchasingInformationV2):
            return True

        return self.to_dict() != other.to_dict()