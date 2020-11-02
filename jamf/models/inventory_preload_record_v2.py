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


class InventoryPreloadRecordV2(object):
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
        'serial_number': 'str',
        'device_type': 'str',
        'username': 'str',
        'full_name': 'str',
        'email_address': 'str',
        'phone_number': 'str',
        'position': 'str',
        'department': 'str',
        'building': 'str',
        'room': 'str',
        'po_number': 'str',
        'po_date': 'str',
        'warranty_expiration': 'str',
        'apple_care_id': 'str',
        'life_expectancy': 'str',
        'purchase_price': 'str',
        'purchasing_contact': 'str',
        'purchasing_account': 'str',
        'lease_expiration': 'str',
        'bar_code1': 'str',
        'bar_code2': 'str',
        'asset_tag': 'str',
        'vendor': 'str',
        'extension_attributes': 'list[InventoryPreloadExtensionAttribute]'
    }

    attribute_map = {
        'id': 'id',
        'serial_number': 'serialNumber',
        'device_type': 'deviceType',
        'username': 'username',
        'full_name': 'fullName',
        'email_address': 'emailAddress',
        'phone_number': 'phoneNumber',
        'position': 'position',
        'department': 'department',
        'building': 'building',
        'room': 'room',
        'po_number': 'poNumber',
        'po_date': 'poDate',
        'warranty_expiration': 'warrantyExpiration',
        'apple_care_id': 'appleCareId',
        'life_expectancy': 'lifeExpectancy',
        'purchase_price': 'purchasePrice',
        'purchasing_contact': 'purchasingContact',
        'purchasing_account': 'purchasingAccount',
        'lease_expiration': 'leaseExpiration',
        'bar_code1': 'barCode1',
        'bar_code2': 'barCode2',
        'asset_tag': 'assetTag',
        'vendor': 'vendor',
        'extension_attributes': 'extensionAttributes'
    }

    def __init__(self, id=None, serial_number=None, device_type=None, username=None, full_name=None, email_address=None, phone_number=None, position=None, department=None, building=None, room=None, po_number=None, po_date=None, warranty_expiration=None, apple_care_id=None, life_expectancy=None, purchase_price=None, purchasing_contact=None, purchasing_account=None, lease_expiration=None, bar_code1=None, bar_code2=None, asset_tag=None, vendor=None, extension_attributes=None, local_vars_configuration=None):  # noqa: E501
        """InventoryPreloadRecordV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._serial_number = None
        self._device_type = None
        self._username = None
        self._full_name = None
        self._email_address = None
        self._phone_number = None
        self._position = None
        self._department = None
        self._building = None
        self._room = None
        self._po_number = None
        self._po_date = None
        self._warranty_expiration = None
        self._apple_care_id = None
        self._life_expectancy = None
        self._purchase_price = None
        self._purchasing_contact = None
        self._purchasing_account = None
        self._lease_expiration = None
        self._bar_code1 = None
        self._bar_code2 = None
        self._asset_tag = None
        self._vendor = None
        self._extension_attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.serial_number = serial_number
        self.device_type = device_type
        if username is not None:
            self.username = username
        if full_name is not None:
            self.full_name = full_name
        if email_address is not None:
            self.email_address = email_address
        if phone_number is not None:
            self.phone_number = phone_number
        if position is not None:
            self.position = position
        if department is not None:
            self.department = department
        if building is not None:
            self.building = building
        if room is not None:
            self.room = room
        if po_number is not None:
            self.po_number = po_number
        if po_date is not None:
            self.po_date = po_date
        if warranty_expiration is not None:
            self.warranty_expiration = warranty_expiration
        if apple_care_id is not None:
            self.apple_care_id = apple_care_id
        if life_expectancy is not None:
            self.life_expectancy = life_expectancy
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if purchasing_contact is not None:
            self.purchasing_contact = purchasing_contact
        if purchasing_account is not None:
            self.purchasing_account = purchasing_account
        if lease_expiration is not None:
            self.lease_expiration = lease_expiration
        if bar_code1 is not None:
            self.bar_code1 = bar_code1
        if bar_code2 is not None:
            self.bar_code2 = bar_code2
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if vendor is not None:
            self.vendor = vendor
        if extension_attributes is not None:
            self.extension_attributes = extension_attributes

    @property
    def id(self):
        """Gets the id of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The id of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPreloadRecordV2.


        :param id: The id of this InventoryPreloadRecordV2.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def serial_number(self):
        """Gets the serial_number of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The serial_number of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this InventoryPreloadRecordV2.


        :param serial_number: The serial_number of this InventoryPreloadRecordV2.  # noqa: E501
        :type serial_number: str
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def device_type(self):
        """Gets the device_type of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The device_type of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InventoryPreloadRecordV2.


        :param device_type: The device_type of this InventoryPreloadRecordV2.  # noqa: E501
        :type device_type: str
        """
        if self.local_vars_configuration.client_side_validation and device_type is None:  # noqa: E501
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Computer", "Mobile Device", "Unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and device_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def username(self):
        """Gets the username of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The username of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InventoryPreloadRecordV2.


        :param username: The username of this InventoryPreloadRecordV2.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def full_name(self):
        """Gets the full_name of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The full_name of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this InventoryPreloadRecordV2.


        :param full_name: The full_name of this InventoryPreloadRecordV2.  # noqa: E501
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def email_address(self):
        """Gets the email_address of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The email_address of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this InventoryPreloadRecordV2.


        :param email_address: The email_address of this InventoryPreloadRecordV2.  # noqa: E501
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def phone_number(self):
        """Gets the phone_number of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The phone_number of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InventoryPreloadRecordV2.


        :param phone_number: The phone_number of this InventoryPreloadRecordV2.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def position(self):
        """Gets the position of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The position of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this InventoryPreloadRecordV2.


        :param position: The position of this InventoryPreloadRecordV2.  # noqa: E501
        :type position: str
        """

        self._position = position

    @property
    def department(self):
        """Gets the department of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The department of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this InventoryPreloadRecordV2.


        :param department: The department of this InventoryPreloadRecordV2.  # noqa: E501
        :type department: str
        """

        self._department = department

    @property
    def building(self):
        """Gets the building of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The building of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._building

    @building.setter
    def building(self, building):
        """Sets the building of this InventoryPreloadRecordV2.


        :param building: The building of this InventoryPreloadRecordV2.  # noqa: E501
        :type building: str
        """

        self._building = building

    @property
    def room(self):
        """Gets the room of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The room of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this InventoryPreloadRecordV2.


        :param room: The room of this InventoryPreloadRecordV2.  # noqa: E501
        :type room: str
        """

        self._room = room

    @property
    def po_number(self):
        """Gets the po_number of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The po_number of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._po_number

    @po_number.setter
    def po_number(self, po_number):
        """Sets the po_number of this InventoryPreloadRecordV2.


        :param po_number: The po_number of this InventoryPreloadRecordV2.  # noqa: E501
        :type po_number: str
        """

        self._po_number = po_number

    @property
    def po_date(self):
        """Gets the po_date of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The po_date of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._po_date

    @po_date.setter
    def po_date(self, po_date):
        """Sets the po_date of this InventoryPreloadRecordV2.


        :param po_date: The po_date of this InventoryPreloadRecordV2.  # noqa: E501
        :type po_date: str
        """

        self._po_date = po_date

    @property
    def warranty_expiration(self):
        """Gets the warranty_expiration of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The warranty_expiration of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._warranty_expiration

    @warranty_expiration.setter
    def warranty_expiration(self, warranty_expiration):
        """Sets the warranty_expiration of this InventoryPreloadRecordV2.


        :param warranty_expiration: The warranty_expiration of this InventoryPreloadRecordV2.  # noqa: E501
        :type warranty_expiration: str
        """

        self._warranty_expiration = warranty_expiration

    @property
    def apple_care_id(self):
        """Gets the apple_care_id of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The apple_care_id of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._apple_care_id

    @apple_care_id.setter
    def apple_care_id(self, apple_care_id):
        """Sets the apple_care_id of this InventoryPreloadRecordV2.


        :param apple_care_id: The apple_care_id of this InventoryPreloadRecordV2.  # noqa: E501
        :type apple_care_id: str
        """

        self._apple_care_id = apple_care_id

    @property
    def life_expectancy(self):
        """Gets the life_expectancy of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The life_expectancy of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._life_expectancy

    @life_expectancy.setter
    def life_expectancy(self, life_expectancy):
        """Sets the life_expectancy of this InventoryPreloadRecordV2.


        :param life_expectancy: The life_expectancy of this InventoryPreloadRecordV2.  # noqa: E501
        :type life_expectancy: str
        """

        self._life_expectancy = life_expectancy

    @property
    def purchase_price(self):
        """Gets the purchase_price of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The purchase_price of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this InventoryPreloadRecordV2.


        :param purchase_price: The purchase_price of this InventoryPreloadRecordV2.  # noqa: E501
        :type purchase_price: str
        """

        self._purchase_price = purchase_price

    @property
    def purchasing_contact(self):
        """Gets the purchasing_contact of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The purchasing_contact of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_contact

    @purchasing_contact.setter
    def purchasing_contact(self, purchasing_contact):
        """Sets the purchasing_contact of this InventoryPreloadRecordV2.


        :param purchasing_contact: The purchasing_contact of this InventoryPreloadRecordV2.  # noqa: E501
        :type purchasing_contact: str
        """

        self._purchasing_contact = purchasing_contact

    @property
    def purchasing_account(self):
        """Gets the purchasing_account of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The purchasing_account of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._purchasing_account

    @purchasing_account.setter
    def purchasing_account(self, purchasing_account):
        """Sets the purchasing_account of this InventoryPreloadRecordV2.


        :param purchasing_account: The purchasing_account of this InventoryPreloadRecordV2.  # noqa: E501
        :type purchasing_account: str
        """

        self._purchasing_account = purchasing_account

    @property
    def lease_expiration(self):
        """Gets the lease_expiration of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The lease_expiration of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._lease_expiration

    @lease_expiration.setter
    def lease_expiration(self, lease_expiration):
        """Sets the lease_expiration of this InventoryPreloadRecordV2.


        :param lease_expiration: The lease_expiration of this InventoryPreloadRecordV2.  # noqa: E501
        :type lease_expiration: str
        """

        self._lease_expiration = lease_expiration

    @property
    def bar_code1(self):
        """Gets the bar_code1 of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The bar_code1 of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._bar_code1

    @bar_code1.setter
    def bar_code1(self, bar_code1):
        """Sets the bar_code1 of this InventoryPreloadRecordV2.


        :param bar_code1: The bar_code1 of this InventoryPreloadRecordV2.  # noqa: E501
        :type bar_code1: str
        """

        self._bar_code1 = bar_code1

    @property
    def bar_code2(self):
        """Gets the bar_code2 of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The bar_code2 of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._bar_code2

    @bar_code2.setter
    def bar_code2(self, bar_code2):
        """Sets the bar_code2 of this InventoryPreloadRecordV2.


        :param bar_code2: The bar_code2 of this InventoryPreloadRecordV2.  # noqa: E501
        :type bar_code2: str
        """

        self._bar_code2 = bar_code2

    @property
    def asset_tag(self):
        """Gets the asset_tag of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The asset_tag of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this InventoryPreloadRecordV2.


        :param asset_tag: The asset_tag of this InventoryPreloadRecordV2.  # noqa: E501
        :type asset_tag: str
        """

        self._asset_tag = asset_tag

    @property
    def vendor(self):
        """Gets the vendor of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The vendor of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this InventoryPreloadRecordV2.


        :param vendor: The vendor of this InventoryPreloadRecordV2.  # noqa: E501
        :type vendor: str
        """

        self._vendor = vendor

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this InventoryPreloadRecordV2.  # noqa: E501


        :return: The extension_attributes of this InventoryPreloadRecordV2.  # noqa: E501
        :rtype: list[InventoryPreloadExtensionAttribute]
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this InventoryPreloadRecordV2.


        :param extension_attributes: The extension_attributes of this InventoryPreloadRecordV2.  # noqa: E501
        :type extension_attributes: list[InventoryPreloadExtensionAttribute]
        """

        self._extension_attributes = extension_attributes

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
        if not isinstance(other, InventoryPreloadRecordV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryPreloadRecordV2):
            return True

        return self.to_dict() != other.to_dict()
