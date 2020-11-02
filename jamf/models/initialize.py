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


class Initialize(object):
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
        'activation_code': 'str',
        'institution_name': 'str',
        'is_eula_accepted': 'bool',
        'username': 'str',
        'password': 'str',
        'email': 'str',
        'jss_url': 'str'
    }

    attribute_map = {
        'activation_code': 'activationCode',
        'institution_name': 'institutionName',
        'is_eula_accepted': 'isEulaAccepted',
        'username': 'username',
        'password': 'password',
        'email': 'email',
        'jss_url': 'jssUrl'
    }

    def __init__(self, activation_code=None, institution_name=None, is_eula_accepted=None, username=None, password=None, email=None, jss_url=None, local_vars_configuration=None):  # noqa: E501
        """Initialize - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._activation_code = None
        self._institution_name = None
        self._is_eula_accepted = None
        self._username = None
        self._password = None
        self._email = None
        self._jss_url = None
        self.discriminator = None

        if activation_code is not None:
            self.activation_code = activation_code
        if institution_name is not None:
            self.institution_name = institution_name
        if is_eula_accepted is not None:
            self.is_eula_accepted = is_eula_accepted
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if jss_url is not None:
            self.jss_url = jss_url

    @property
    def activation_code(self):
        """Gets the activation_code of this Initialize.  # noqa: E501


        :return: The activation_code of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._activation_code

    @activation_code.setter
    def activation_code(self, activation_code):
        """Sets the activation_code of this Initialize.


        :param activation_code: The activation_code of this Initialize.  # noqa: E501
        :type activation_code: str
        """

        self._activation_code = activation_code

    @property
    def institution_name(self):
        """Gets the institution_name of this Initialize.  # noqa: E501


        :return: The institution_name of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this Initialize.


        :param institution_name: The institution_name of this Initialize.  # noqa: E501
        :type institution_name: str
        """

        self._institution_name = institution_name

    @property
    def is_eula_accepted(self):
        """Gets the is_eula_accepted of this Initialize.  # noqa: E501


        :return: The is_eula_accepted of this Initialize.  # noqa: E501
        :rtype: bool
        """
        return self._is_eula_accepted

    @is_eula_accepted.setter
    def is_eula_accepted(self, is_eula_accepted):
        """Sets the is_eula_accepted of this Initialize.


        :param is_eula_accepted: The is_eula_accepted of this Initialize.  # noqa: E501
        :type is_eula_accepted: bool
        """

        self._is_eula_accepted = is_eula_accepted

    @property
    def username(self):
        """Gets the username of this Initialize.  # noqa: E501


        :return: The username of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Initialize.


        :param username: The username of this Initialize.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Initialize.  # noqa: E501


        :return: The password of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Initialize.


        :param password: The password of this Initialize.  # noqa: E501
        :type password: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this Initialize.  # noqa: E501


        :return: The email of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Initialize.


        :param email: The email of this Initialize.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def jss_url(self):
        """Gets the jss_url of this Initialize.  # noqa: E501


        :return: The jss_url of this Initialize.  # noqa: E501
        :rtype: str
        """
        return self._jss_url

    @jss_url.setter
    def jss_url(self, jss_url):
        """Sets the jss_url of this Initialize.


        :param jss_url: The jss_url of this Initialize.  # noqa: E501
        :type jss_url: str
        """

        self._jss_url = jss_url

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
        if not isinstance(other, Initialize):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Initialize):
            return True

        return self.to_dict() != other.to_dict()
