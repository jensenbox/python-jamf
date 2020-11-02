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


class EnrollmentAccessGroupV2(object):
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
        'ldap_server_id': 'str',
        'name': 'str',
        'site_id': 'str',
        'enterprise_enrollment_enabled': 'bool',
        'personal_enrollment_enabled': 'bool',
        'require_eula': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ldap_server_id': 'ldapServerId',
        'name': 'name',
        'site_id': 'siteId',
        'enterprise_enrollment_enabled': 'enterpriseEnrollmentEnabled',
        'personal_enrollment_enabled': 'personalEnrollmentEnabled',
        'require_eula': 'requireEula'
    }

    def __init__(self, id=None, ldap_server_id=None, name=None, site_id=None, enterprise_enrollment_enabled=None, personal_enrollment_enabled=None, require_eula=None, local_vars_configuration=None):  # noqa: E501
        """EnrollmentAccessGroupV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._ldap_server_id = None
        self._name = None
        self._site_id = None
        self._enterprise_enrollment_enabled = None
        self._personal_enrollment_enabled = None
        self._require_eula = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ldap_server_id is not None:
            self.ldap_server_id = ldap_server_id
        if name is not None:
            self.name = name
        if site_id is not None:
            self.site_id = site_id
        if enterprise_enrollment_enabled is not None:
            self.enterprise_enrollment_enabled = enterprise_enrollment_enabled
        if personal_enrollment_enabled is not None:
            self.personal_enrollment_enabled = personal_enrollment_enabled
        if require_eula is not None:
            self.require_eula = require_eula

    @property
    def id(self):
        """Gets the id of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The id of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnrollmentAccessGroupV2.


        :param id: The id of this EnrollmentAccessGroupV2.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def ldap_server_id(self):
        """Gets the ldap_server_id of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The ldap_server_id of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: str
        """
        return self._ldap_server_id

    @ldap_server_id.setter
    def ldap_server_id(self, ldap_server_id):
        """Sets the ldap_server_id of this EnrollmentAccessGroupV2.


        :param ldap_server_id: The ldap_server_id of this EnrollmentAccessGroupV2.  # noqa: E501
        :type ldap_server_id: str
        """

        self._ldap_server_id = ldap_server_id

    @property
    def name(self):
        """Gets the name of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The name of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnrollmentAccessGroupV2.


        :param name: The name of this EnrollmentAccessGroupV2.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def site_id(self):
        """Gets the site_id of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The site_id of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this EnrollmentAccessGroupV2.


        :param site_id: The site_id of this EnrollmentAccessGroupV2.  # noqa: E501
        :type site_id: str
        """

        self._site_id = site_id

    @property
    def enterprise_enrollment_enabled(self):
        """Gets the enterprise_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The enterprise_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._enterprise_enrollment_enabled

    @enterprise_enrollment_enabled.setter
    def enterprise_enrollment_enabled(self, enterprise_enrollment_enabled):
        """Sets the enterprise_enrollment_enabled of this EnrollmentAccessGroupV2.


        :param enterprise_enrollment_enabled: The enterprise_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501
        :type enterprise_enrollment_enabled: bool
        """

        self._enterprise_enrollment_enabled = enterprise_enrollment_enabled

    @property
    def personal_enrollment_enabled(self):
        """Gets the personal_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The personal_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._personal_enrollment_enabled

    @personal_enrollment_enabled.setter
    def personal_enrollment_enabled(self, personal_enrollment_enabled):
        """Sets the personal_enrollment_enabled of this EnrollmentAccessGroupV2.


        :param personal_enrollment_enabled: The personal_enrollment_enabled of this EnrollmentAccessGroupV2.  # noqa: E501
        :type personal_enrollment_enabled: bool
        """

        self._personal_enrollment_enabled = personal_enrollment_enabled

    @property
    def require_eula(self):
        """Gets the require_eula of this EnrollmentAccessGroupV2.  # noqa: E501


        :return: The require_eula of this EnrollmentAccessGroupV2.  # noqa: E501
        :rtype: bool
        """
        return self._require_eula

    @require_eula.setter
    def require_eula(self, require_eula):
        """Sets the require_eula of this EnrollmentAccessGroupV2.


        :param require_eula: The require_eula of this EnrollmentAccessGroupV2.  # noqa: E501
        :type require_eula: bool
        """

        self._require_eula = require_eula

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
        if not isinstance(other, EnrollmentAccessGroupV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrollmentAccessGroupV2):
            return True

        return self.to_dict() != other.to_dict()