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


class SsoKeystoreResponseWithDetails(object):
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
        'keystore': 'SsoKeystoreResponse',
        'keystore_details': 'SsoKeystoreDetails'
    }

    attribute_map = {
        'keystore': 'keystore',
        'keystore_details': 'keystoreDetails'
    }

    def __init__(self, keystore=None, keystore_details=None, local_vars_configuration=None):  # noqa: E501
        """SsoKeystoreResponseWithDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keystore = None
        self._keystore_details = None
        self.discriminator = None

        if keystore is not None:
            self.keystore = keystore
        if keystore_details is not None:
            self.keystore_details = keystore_details

    @property
    def keystore(self):
        """Gets the keystore of this SsoKeystoreResponseWithDetails.  # noqa: E501


        :return: The keystore of this SsoKeystoreResponseWithDetails.  # noqa: E501
        :rtype: SsoKeystoreResponse
        """
        return self._keystore

    @keystore.setter
    def keystore(self, keystore):
        """Sets the keystore of this SsoKeystoreResponseWithDetails.


        :param keystore: The keystore of this SsoKeystoreResponseWithDetails.  # noqa: E501
        :type keystore: SsoKeystoreResponse
        """

        self._keystore = keystore

    @property
    def keystore_details(self):
        """Gets the keystore_details of this SsoKeystoreResponseWithDetails.  # noqa: E501


        :return: The keystore_details of this SsoKeystoreResponseWithDetails.  # noqa: E501
        :rtype: SsoKeystoreDetails
        """
        return self._keystore_details

    @keystore_details.setter
    def keystore_details(self, keystore_details):
        """Sets the keystore_details of this SsoKeystoreResponseWithDetails.


        :param keystore_details: The keystore_details of this SsoKeystoreResponseWithDetails.  # noqa: E501
        :type keystore_details: SsoKeystoreDetails
        """

        self._keystore_details = keystore_details

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
        if not isinstance(other, SsoKeystoreResponseWithDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SsoKeystoreResponseWithDetails):
            return True

        return self.to_dict() != other.to_dict()
