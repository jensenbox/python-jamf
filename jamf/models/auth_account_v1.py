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


class AuthAccountV1(object):
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
        'username': 'str',
        'real_name': 'str',
        'email': 'str',
        'preferences': 'AccountPreferencesV1',
        'multi_site_admin': 'bool',
        'access_level': 'str',
        'privilege_set': 'str',
        'privileges_by_site': 'dict(str, list[str])',
        'group_ids': 'list[str]',
        'current_site_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'real_name': 'realName',
        'email': 'email',
        'preferences': 'preferences',
        'multi_site_admin': 'multiSiteAdmin',
        'access_level': 'accessLevel',
        'privilege_set': 'privilegeSet',
        'privileges_by_site': 'privilegesBySite',
        'group_ids': 'groupIds',
        'current_site_id': 'currentSiteId'
    }

    def __init__(self, id=None, username=None, real_name=None, email=None, preferences=None, multi_site_admin=None, access_level=None, privilege_set=None, privileges_by_site=None, group_ids=None, current_site_id=None, local_vars_configuration=None):  # noqa: E501
        """AuthAccountV1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._real_name = None
        self._email = None
        self._preferences = None
        self._multi_site_admin = None
        self._access_level = None
        self._privilege_set = None
        self._privileges_by_site = None
        self._group_ids = None
        self._current_site_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if real_name is not None:
            self.real_name = real_name
        if email is not None:
            self.email = email
        if preferences is not None:
            self.preferences = preferences
        if multi_site_admin is not None:
            self.multi_site_admin = multi_site_admin
        if access_level is not None:
            self.access_level = access_level
        if privilege_set is not None:
            self.privilege_set = privilege_set
        if privileges_by_site is not None:
            self.privileges_by_site = privileges_by_site
        if group_ids is not None:
            self.group_ids = group_ids
        if current_site_id is not None:
            self.current_site_id = current_site_id

    @property
    def id(self):
        """Gets the id of this AuthAccountV1.  # noqa: E501


        :return: The id of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthAccountV1.


        :param id: The id of this AuthAccountV1.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this AuthAccountV1.  # noqa: E501


        :return: The username of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthAccountV1.


        :param username: The username of this AuthAccountV1.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def real_name(self):
        """Gets the real_name of this AuthAccountV1.  # noqa: E501


        :return: The real_name of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """Sets the real_name of this AuthAccountV1.


        :param real_name: The real_name of this AuthAccountV1.  # noqa: E501
        :type real_name: str
        """

        self._real_name = real_name

    @property
    def email(self):
        """Gets the email of this AuthAccountV1.  # noqa: E501


        :return: The email of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthAccountV1.


        :param email: The email of this AuthAccountV1.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def preferences(self):
        """Gets the preferences of this AuthAccountV1.  # noqa: E501


        :return: The preferences of this AuthAccountV1.  # noqa: E501
        :rtype: AccountPreferencesV1
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this AuthAccountV1.


        :param preferences: The preferences of this AuthAccountV1.  # noqa: E501
        :type preferences: AccountPreferencesV1
        """

        self._preferences = preferences

    @property
    def multi_site_admin(self):
        """Gets the multi_site_admin of this AuthAccountV1.  # noqa: E501


        :return: The multi_site_admin of this AuthAccountV1.  # noqa: E501
        :rtype: bool
        """
        return self._multi_site_admin

    @multi_site_admin.setter
    def multi_site_admin(self, multi_site_admin):
        """Sets the multi_site_admin of this AuthAccountV1.


        :param multi_site_admin: The multi_site_admin of this AuthAccountV1.  # noqa: E501
        :type multi_site_admin: bool
        """

        self._multi_site_admin = multi_site_admin

    @property
    def access_level(self):
        """Gets the access_level of this AuthAccountV1.  # noqa: E501


        :return: The access_level of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this AuthAccountV1.


        :param access_level: The access_level of this AuthAccountV1.  # noqa: E501
        :type access_level: str
        """
        allowed_values = ["FullAccess", "SiteAccess", "GroupBasedAccess"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and access_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `access_level` ({0}), must be one of {1}"  # noqa: E501
                .format(access_level, allowed_values)
            )

        self._access_level = access_level

    @property
    def privilege_set(self):
        """Gets the privilege_set of this AuthAccountV1.  # noqa: E501


        :return: The privilege_set of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._privilege_set

    @privilege_set.setter
    def privilege_set(self, privilege_set):
        """Sets the privilege_set of this AuthAccountV1.


        :param privilege_set: The privilege_set of this AuthAccountV1.  # noqa: E501
        :type privilege_set: str
        """
        allowed_values = ["ADMINISTRATOR", "AUDITOR", "ENROLLMENT", "CUSTOM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and privilege_set not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `privilege_set` ({0}), must be one of {1}"  # noqa: E501
                .format(privilege_set, allowed_values)
            )

        self._privilege_set = privilege_set

    @property
    def privileges_by_site(self):
        """Gets the privileges_by_site of this AuthAccountV1.  # noqa: E501


        :return: The privileges_by_site of this AuthAccountV1.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._privileges_by_site

    @privileges_by_site.setter
    def privileges_by_site(self, privileges_by_site):
        """Sets the privileges_by_site of this AuthAccountV1.


        :param privileges_by_site: The privileges_by_site of this AuthAccountV1.  # noqa: E501
        :type privileges_by_site: dict(str, list[str])
        """

        self._privileges_by_site = privileges_by_site

    @property
    def group_ids(self):
        """Gets the group_ids of this AuthAccountV1.  # noqa: E501


        :return: The group_ids of this AuthAccountV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this AuthAccountV1.


        :param group_ids: The group_ids of this AuthAccountV1.  # noqa: E501
        :type group_ids: list[str]
        """

        self._group_ids = group_ids

    @property
    def current_site_id(self):
        """Gets the current_site_id of this AuthAccountV1.  # noqa: E501


        :return: The current_site_id of this AuthAccountV1.  # noqa: E501
        :rtype: str
        """
        return self._current_site_id

    @current_site_id.setter
    def current_site_id(self, current_site_id):
        """Sets the current_site_id of this AuthAccountV1.


        :param current_site_id: The current_site_id of this AuthAccountV1.  # noqa: E501
        :type current_site_id: str
        """

        self._current_site_id = current_site_id

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
        if not isinstance(other, AuthAccountV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthAccountV1):
            return True

        return self.to_dict() != other.to_dict()
