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


class LocationInformationV2(object):
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
        'username': 'str',
        'realname': 'str',
        'phone': 'str',
        'email': 'str',
        'room': 'str',
        'position': 'str',
        'department_id': 'str',
        'building_id': 'str',
        'id': 'str',
        'version_lock': 'int'
    }

    attribute_map = {
        'username': 'username',
        'realname': 'realname',
        'phone': 'phone',
        'email': 'email',
        'room': 'room',
        'position': 'position',
        'department_id': 'departmentId',
        'building_id': 'buildingId',
        'id': 'id',
        'version_lock': 'versionLock'
    }

    def __init__(self, username=None, realname=None, phone=None, email=None, room=None, position=None, department_id=None, building_id=None, id=None, version_lock=None, local_vars_configuration=None):  # noqa: E501
        """LocationInformationV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._realname = None
        self._phone = None
        self._email = None
        self._room = None
        self._position = None
        self._department_id = None
        self._building_id = None
        self._id = None
        self._version_lock = None
        self.discriminator = None

        self.username = username
        self.realname = realname
        self.phone = phone
        self.email = email
        self.room = room
        self.position = position
        self.department_id = department_id
        self.building_id = building_id
        self.id = id
        self.version_lock = version_lock

    @property
    def username(self):
        """Gets the username of this LocationInformationV2.  # noqa: E501


        :return: The username of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LocationInformationV2.


        :param username: The username of this LocationInformationV2.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def realname(self):
        """Gets the realname of this LocationInformationV2.  # noqa: E501


        :return: The realname of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._realname

    @realname.setter
    def realname(self, realname):
        """Sets the realname of this LocationInformationV2.


        :param realname: The realname of this LocationInformationV2.  # noqa: E501
        :type realname: str
        """
        if self.local_vars_configuration.client_side_validation and realname is None:  # noqa: E501
            raise ValueError("Invalid value for `realname`, must not be `None`")  # noqa: E501

        self._realname = realname

    @property
    def phone(self):
        """Gets the phone of this LocationInformationV2.  # noqa: E501


        :return: The phone of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this LocationInformationV2.


        :param phone: The phone of this LocationInformationV2.  # noqa: E501
        :type phone: str
        """
        if self.local_vars_configuration.client_side_validation and phone is None:  # noqa: E501
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this LocationInformationV2.  # noqa: E501


        :return: The email of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LocationInformationV2.


        :param email: The email of this LocationInformationV2.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def room(self):
        """Gets the room of this LocationInformationV2.  # noqa: E501


        :return: The room of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this LocationInformationV2.


        :param room: The room of this LocationInformationV2.  # noqa: E501
        :type room: str
        """
        if self.local_vars_configuration.client_side_validation and room is None:  # noqa: E501
            raise ValueError("Invalid value for `room`, must not be `None`")  # noqa: E501

        self._room = room

    @property
    def position(self):
        """Gets the position of this LocationInformationV2.  # noqa: E501


        :return: The position of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this LocationInformationV2.


        :param position: The position of this LocationInformationV2.  # noqa: E501
        :type position: str
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def department_id(self):
        """Gets the department_id of this LocationInformationV2.  # noqa: E501


        :return: The department_id of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this LocationInformationV2.


        :param department_id: The department_id of this LocationInformationV2.  # noqa: E501
        :type department_id: str
        """
        if self.local_vars_configuration.client_side_validation and department_id is None:  # noqa: E501
            raise ValueError("Invalid value for `department_id`, must not be `None`")  # noqa: E501

        self._department_id = department_id

    @property
    def building_id(self):
        """Gets the building_id of this LocationInformationV2.  # noqa: E501


        :return: The building_id of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this LocationInformationV2.


        :param building_id: The building_id of this LocationInformationV2.  # noqa: E501
        :type building_id: str
        """
        if self.local_vars_configuration.client_side_validation and building_id is None:  # noqa: E501
            raise ValueError("Invalid value for `building_id`, must not be `None`")  # noqa: E501

        self._building_id = building_id

    @property
    def id(self):
        """Gets the id of this LocationInformationV2.  # noqa: E501


        :return: The id of this LocationInformationV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocationInformationV2.


        :param id: The id of this LocationInformationV2.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version_lock(self):
        """Gets the version_lock of this LocationInformationV2.  # noqa: E501


        :return: The version_lock of this LocationInformationV2.  # noqa: E501
        :rtype: int
        """
        return self._version_lock

    @version_lock.setter
    def version_lock(self, version_lock):
        """Sets the version_lock of this LocationInformationV2.


        :param version_lock: The version_lock of this LocationInformationV2.  # noqa: E501
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
        if not isinstance(other, LocationInformationV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationInformationV2):
            return True

        return self.to_dict() != other.to_dict()
