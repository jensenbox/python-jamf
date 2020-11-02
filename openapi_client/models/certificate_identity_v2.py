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


class CertificateIdentityV2(object):
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
        'filename': 'str',
        'keystore_password': 'str',
        'identity_keystore': 'list[str]',
        'md5_sum': 'str'
    }

    attribute_map = {
        'filename': 'filename',
        'keystore_password': 'keystorePassword',
        'identity_keystore': 'identityKeystore',
        'md5_sum': 'md5Sum'
    }

    def __init__(self, filename='null', keystore_password='', identity_keystore=None, md5_sum='', local_vars_configuration=None):  # noqa: E501
        """CertificateIdentityV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filename = None
        self._keystore_password = None
        self._identity_keystore = None
        self._md5_sum = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if keystore_password is not None:
            self.keystore_password = keystore_password
        if identity_keystore is not None:
            self.identity_keystore = identity_keystore
        if md5_sum is not None:
            self.md5_sum = md5_sum

    @property
    def filename(self):
        """Gets the filename of this CertificateIdentityV2.  # noqa: E501


        :return: The filename of this CertificateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this CertificateIdentityV2.


        :param filename: The filename of this CertificateIdentityV2.  # noqa: E501
        :type filename: str
        """

        self._filename = filename

    @property
    def keystore_password(self):
        """Gets the keystore_password of this CertificateIdentityV2.  # noqa: E501


        :return: The keystore_password of this CertificateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._keystore_password

    @keystore_password.setter
    def keystore_password(self, keystore_password):
        """Sets the keystore_password of this CertificateIdentityV2.


        :param keystore_password: The keystore_password of this CertificateIdentityV2.  # noqa: E501
        :type keystore_password: str
        """

        self._keystore_password = keystore_password

    @property
    def identity_keystore(self):
        """Gets the identity_keystore of this CertificateIdentityV2.  # noqa: E501

        The base 64 encoded certificate.  # noqa: E501

        :return: The identity_keystore of this CertificateIdentityV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._identity_keystore

    @identity_keystore.setter
    def identity_keystore(self, identity_keystore):
        """Sets the identity_keystore of this CertificateIdentityV2.

        The base 64 encoded certificate.  # noqa: E501

        :param identity_keystore: The identity_keystore of this CertificateIdentityV2.  # noqa: E501
        :type identity_keystore: list[str]
        """

        self._identity_keystore = identity_keystore

    @property
    def md5_sum(self):
        """Gets the md5_sum of this CertificateIdentityV2.  # noqa: E501

        The md5 checksum of the certificate file. Intended to be used in verifification the cert being used to sign QuickAdd packages.  # noqa: E501

        :return: The md5_sum of this CertificateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._md5_sum

    @md5_sum.setter
    def md5_sum(self, md5_sum):
        """Sets the md5_sum of this CertificateIdentityV2.

        The md5 checksum of the certificate file. Intended to be used in verifification the cert being used to sign QuickAdd packages.  # noqa: E501

        :param md5_sum: The md5_sum of this CertificateIdentityV2.  # noqa: E501
        :type md5_sum: str
        """

        self._md5_sum = md5_sum

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
        if not isinstance(other, CertificateIdentityV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateIdentityV2):
            return True

        return self.to_dict() != other.to_dict()
