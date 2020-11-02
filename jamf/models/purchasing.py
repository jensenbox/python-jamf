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


class Purchasing(object):
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
        'is_purchased': 'bool',
        'is_leased': 'bool',
        'po_number': 'str',
        'vendor': 'str',
        'apple_care_id': 'str',
        'purchase_price': 'str',
        'purchasing_account': 'str',
        'po_date': 'datetime',
        'warranty_expires_date': 'datetime',
        'lease_expires_date': 'datetime',
        'life_expectancy': 'int',
        'purchasing_contact': 'str'
    }

    attribute_map = {
        'is_purchased': 'isPurchased',
        'is_leased': 'isLeased',
        'po_number': 'poNumber',
        'vendor': 'vendor',
        'apple_care_id': 'appleCareId',
        'purchase_price': 'purchasePrice',
        'purchasing_account': 'purchasingAccount',
        'po_date': 'poDate',
        'warranty_expires_date': 'warrantyExpiresDate',
        'lease_expires_date': 'leaseExpiresDate',
        'life_expectancy': 'lifeExpectancy',
        'purchasing_contact': 'purchasingContact'
    }

    def __init__(self, is_purchased=None, is_leased=None, po_number=None, vendor=None, apple_care_id=None, purchase_price=None, purchasing_account=None, po_date=None, warranty_expires_date=None, lease_expires_date=None, life_expectancy=None, purchasing_contact=None, local_vars_configuration=None):  # noqa: E501
        """Purchasing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_purchased = None
        self._is_leased = None
        self._po_number = None
        self._vendor = None
        self._apple_care_id = None
        self._purchase_price = None
        self._purchasing_account = None
        self._po_date = None
        self._warranty_expires_date = None
        self._lease_expires_date = None
        self._life_expectancy = None
        self._purchasing_contact = None
        self.discriminator = None

        if is_purchased is not None:
            self.is_purchased = is_purchased
        if is_leased is not None:
            self.is_leased = is_leased
        if po_number is not None:
            self.po_number = po_number
        if vendor is not None:
            self.vendor = vendor
        if apple_care_id is not None:
            self.apple_care_id = apple_care_id
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if purchasing_account is not None:
            self.purchasing_account = purchasing_account
        if po_date is not None:
            self.po_date = po_date
        if warranty_expires_date is not None:
            self.warranty_expires_date = warranty_expires_date
        if lease_expires_date is not None:
            self.lease_expires_date = lease_expires_date
        if life_expectancy is not None:
            self.life_expectancy = life_expectancy
        if purchasing_contact is not None:
            self.purchasing_contact = purchasing_contact

    @property
    def is_purchased(self):
        """Gets the is_purchased of this Purchasing.  # noqa: E501


        :return: The is_purchased of this Purchasing.  # noqa: E501
        :rtype: bool
        """
        return self._is_purchased

    @is_purchased.setter
    def is_purchased(self, is_purchased):
        """Sets the is_purchased of this Purchasing.


        :param is_purchased: The is_purchased of this Purchasing.  # noqa: E501
        :type is_purchased: bool
        """

        self._is_purchased = is_purchased

    @property
    def is_leased(self):
        """Gets the is_leased of this Purchasing.  # noqa: E501


        :return: The is_leased of this Purchasing.  # noqa: E501
        :rtype: bool
        """
        return self._is_leased

    @is_leased.setter
    def is_leased(self, is_leased):
        """Sets the is_leased of this Purchasing.


        :param is_leased: The is_leased of this Purchasing.  # noqa: E501
        :type is_leased: bool
        """

        self._is_leased = is_leased

    @property
    def po_number(self):
        """Gets the po_number of this Purchasing.  # noqa: E501


        :return: The po_number of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this Purchasing.


        :param po_number: The po_number of this Purchasing.  # noqa: E501
        :type po_number: str
        """

        self._po_number = po_number

    @property
    def vendor(self):
        """Gets the vendor of this Purchasing.  # noqa: E501


        :return: The vendor of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Purchasing.


        :param vendor: The vendor of this Purchasing.  # noqa: E501
        :type vendor: str
        """

        self._vendor = vendor

    @property
    def apple_care_id(self):
        """Gets the apple_care_id of this Purchasing.  # noqa: E501


        :return: The apple_care_id of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._apple_care_id

    @apple_care_id.setter
    def apple_care_id(self, apple_care_id):
        """Sets the apple_care_id of this Purchasing.


        :param apple_care_id: The apple_care_id of this Purchasing.  # noqa: E501
        :type apple_care_id: str
        """

        self._apple_care_id = apple_care_id

    @property
    def purchase_price(self):
        """Gets the purchase_price of this Purchasing.  # noqa: E501


        :return: The purchase_price of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this Purchasing.


        :param purchase_price: The purchase_price of this Purchasing.  # noqa: E501
        :type purchase_price: str
        """

        self._purchase_price = purchase_price

    @property
    def purchasing_account(self):
        """Gets the purchasing_account of this Purchasing.  # noqa: E501


        :return: The purchasing_account of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_account

    @purchasing_account.setter
    def purchasing_account(self, purchasing_account):
        """Sets the purchasing_account of this Purchasing.


        :param purchasing_account: The purchasing_account of this Purchasing.  # noqa: E501
        :type purchasing_account: str
        """

        self._purchasing_account = purchasing_account

    @property
    def po_date(self):
        """Gets the po_date of this Purchasing.  # noqa: E501


        :return: The po_date of this Purchasing.  # noqa: E501
        :rtype: datetime
        """
        return self._po_date

    @po_date.setter
    def po_date(self, po_date):
        """Sets the po_date of this Purchasing.


        :param po_date: The po_date of this Purchasing.  # noqa: E501
        :type po_date: datetime
        """

        self._po_date = po_date

    @property
    def warranty_expires_date(self):
        """Gets the warranty_expires_date of this Purchasing.  # noqa: E501


        :return: The warranty_expires_date of this Purchasing.  # noqa: E501
        :rtype: datetime
        """
        return self._warranty_expires_date

    @warranty_expires_date.setter
    def warranty_expires_date(self, warranty_expires_date):
        """Sets the warranty_expires_date of this Purchasing.


        :param warranty_expires_date: The warranty_expires_date of this Purchasing.  # noqa: E501
        :type warranty_expires_date: datetime
        """

        self._warranty_expires_date = warranty_expires_date

    @property
    def lease_expires_date(self):
        """Gets the lease_expires_date of this Purchasing.  # noqa: E501


        :return: The lease_expires_date of this Purchasing.  # noqa: E501
        :rtype: datetime
        """
        return self._lease_expires_date

    @lease_expires_date.setter
    def lease_expires_date(self, lease_expires_date):
        """Sets the lease_expires_date of this Purchasing.


        :param lease_expires_date: The lease_expires_date of this Purchasing.  # noqa: E501
        :type lease_expires_date: datetime
        """

        self._lease_expires_date = lease_expires_date

    @property
    def life_expectancy(self):
        """Gets the life_expectancy of this Purchasing.  # noqa: E501


        :return: The life_expectancy of this Purchasing.  # noqa: E501
        :rtype: int
        """
        return self._life_expectancy

    @life_expectancy.setter
    def life_expectancy(self, life_expectancy):
        """Sets the life_expectancy of this Purchasing.


        :param life_expectancy: The life_expectancy of this Purchasing.  # noqa: E501
        :type life_expectancy: int
        """

        self._life_expectancy = life_expectancy

    @property
    def purchasing_contact(self):
        """Gets the purchasing_contact of this Purchasing.  # noqa: E501


        :return: The purchasing_contact of this Purchasing.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_contact

    @purchasing_contact.setter
    def purchasing_contact(self, purchasing_contact):
        """Sets the purchasing_contact of this Purchasing.


        :param purchasing_contact: The purchasing_contact of this Purchasing.  # noqa: E501
        :type purchasing_contact: str
        """

        self._purchasing_contact = purchasing_contact

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
        if not isinstance(other, Purchasing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Purchasing):
            return True

        return self.to_dict() != other.to_dict()
