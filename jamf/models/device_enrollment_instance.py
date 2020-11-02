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


class DeviceEnrollmentInstance(object):
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
        'supervision_identity_id': 'str',
        'site_id': 'str',
        'server_name': 'str',
        'server_uuid': 'str',
        'admin_id': 'str',
        'org_name': 'str',
        'org_email': 'str',
        'org_phone': 'str',
        'org_address': 'str',
        'token_expiration_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'supervision_identity_id': 'supervisionIdentityId',
        'site_id': 'siteId',
        'server_name': 'serverName',
        'server_uuid': 'serverUuid',
        'admin_id': 'adminId',
        'org_name': 'orgName',
        'org_email': 'orgEmail',
        'org_phone': 'orgPhone',
        'org_address': 'orgAddress',
        'token_expiration_date': 'tokenExpirationDate'
    }

    def __init__(self, id=None, name=None, supervision_identity_id=None, site_id=None, server_name=None, server_uuid=None, admin_id=None, org_name=None, org_email=None, org_phone=None, org_address=None, token_expiration_date=None, local_vars_configuration=None):  # noqa: E501
        """DeviceEnrollmentInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._supervision_identity_id = None
        self._site_id = None
        self._server_name = None
        self._server_uuid = None
        self._admin_id = None
        self._org_name = None
        self._org_email = None
        self._org_phone = None
        self._org_address = None
        self._token_expiration_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if supervision_identity_id is not None:
            self.supervision_identity_id = supervision_identity_id
        if site_id is not None:
            self.site_id = site_id
        if server_name is not None:
            self.server_name = server_name
        if server_uuid is not None:
            self.server_uuid = server_uuid
        if admin_id is not None:
            self.admin_id = admin_id
        if org_name is not None:
            self.org_name = org_name
        if org_email is not None:
            self.org_email = org_email
        if org_phone is not None:
            self.org_phone = org_phone
        if org_address is not None:
            self.org_address = org_address
        if token_expiration_date is not None:
            self.token_expiration_date = token_expiration_date

    @property
    def id(self):
        """Gets the id of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The id of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceEnrollmentInstance.


        :param id: The id of this DeviceEnrollmentInstance.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The name of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceEnrollmentInstance.


        :param name: The name of this DeviceEnrollmentInstance.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def supervision_identity_id(self):
        """Gets the supervision_identity_id of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The supervision_identity_id of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._supervision_identity_id

    @supervision_identity_id.setter
    def supervision_identity_id(self, supervision_identity_id):
        """Sets the supervision_identity_id of this DeviceEnrollmentInstance.


        :param supervision_identity_id: The supervision_identity_id of this DeviceEnrollmentInstance.  # noqa: E501
        :type supervision_identity_id: str
        """

        self._supervision_identity_id = supervision_identity_id

    @property
    def site_id(self):
        """Gets the site_id of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The site_id of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this DeviceEnrollmentInstance.


        :param site_id: The site_id of this DeviceEnrollmentInstance.  # noqa: E501
        :type site_id: str
        """

        self._site_id = site_id

    @property
    def server_name(self):
        """Gets the server_name of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The server_name of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this DeviceEnrollmentInstance.


        :param server_name: The server_name of this DeviceEnrollmentInstance.  # noqa: E501
        :type server_name: str
        """

        self._server_name = server_name

    @property
    def server_uuid(self):
        """Gets the server_uuid of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The server_uuid of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._server_uuid

    @server_uuid.setter
    def server_uuid(self, server_uuid):
        """Sets the server_uuid of this DeviceEnrollmentInstance.


        :param server_uuid: The server_uuid of this DeviceEnrollmentInstance.  # noqa: E501
        :type server_uuid: str
        """

        self._server_uuid = server_uuid

    @property
    def admin_id(self):
        """Gets the admin_id of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The admin_id of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._admin_id

    @admin_id.setter
    def admin_id(self, admin_id):
        """Sets the admin_id of this DeviceEnrollmentInstance.


        :param admin_id: The admin_id of this DeviceEnrollmentInstance.  # noqa: E501
        :type admin_id: str
        """

        self._admin_id = admin_id

    @property
    def org_name(self):
        """Gets the org_name of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The org_name of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this DeviceEnrollmentInstance.


        :param org_name: The org_name of this DeviceEnrollmentInstance.  # noqa: E501
        :type org_name: str
        """

        self._org_name = org_name

    @property
    def org_email(self):
        """Gets the org_email of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The org_email of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._org_email

    @org_email.setter
    def org_email(self, org_email):
        """Sets the org_email of this DeviceEnrollmentInstance.


        :param org_email: The org_email of this DeviceEnrollmentInstance.  # noqa: E501
        :type org_email: str
        """

        self._org_email = org_email

    @property
    def org_phone(self):
        """Gets the org_phone of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The org_phone of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._org_phone

    @org_phone.setter
    def org_phone(self, org_phone):
        """Sets the org_phone of this DeviceEnrollmentInstance.


        :param org_phone: The org_phone of this DeviceEnrollmentInstance.  # noqa: E501
        :type org_phone: str
        """

        self._org_phone = org_phone

    @property
    def org_address(self):
        """Gets the org_address of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The org_address of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._org_address

    @org_address.setter
    def org_address(self, org_address):
        """Sets the org_address of this DeviceEnrollmentInstance.


        :param org_address: The org_address of this DeviceEnrollmentInstance.  # noqa: E501
        :type org_address: str
        """

        self._org_address = org_address

    @property
    def token_expiration_date(self):
        """Gets the token_expiration_date of this DeviceEnrollmentInstance.  # noqa: E501


        :return: The token_expiration_date of this DeviceEnrollmentInstance.  # noqa: E501
        :rtype: str
        """
        return self._token_expiration_date

    @token_expiration_date.setter
    def token_expiration_date(self, token_expiration_date):
        """Sets the token_expiration_date of this DeviceEnrollmentInstance.


        :param token_expiration_date: The token_expiration_date of this DeviceEnrollmentInstance.  # noqa: E501
        :type token_expiration_date: str
        """

        self._token_expiration_date = token_expiration_date

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
        if not isinstance(other, DeviceEnrollmentInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceEnrollmentInstance):
            return True

        return self.to_dict() != other.to_dict()