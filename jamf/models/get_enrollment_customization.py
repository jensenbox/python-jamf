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


class GetEnrollmentCustomization(object):
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
        'site_id': 'int',
        'display_name': 'str',
        'description': 'str',
        'enrollment_customization_branding_settings': 'EnrollmentCustomizationBrandingSettings',
        'id': 'int'
    }

    attribute_map = {
        'site_id': 'siteId',
        'display_name': 'displayName',
        'description': 'description',
        'enrollment_customization_branding_settings': 'enrollmentCustomizationBrandingSettings',
        'id': 'id'
    }

    def __init__(self, site_id=None, display_name=None, description=None, enrollment_customization_branding_settings=None, id=None, local_vars_configuration=None):  # noqa: E501
        """GetEnrollmentCustomization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._site_id = None
        self._display_name = None
        self._description = None
        self._enrollment_customization_branding_settings = None
        self._id = None
        self.discriminator = None

        self.site_id = site_id
        self.display_name = display_name
        self.description = description
        self.enrollment_customization_branding_settings = enrollment_customization_branding_settings
        if id is not None:
            self.id = id

    @property
    def site_id(self):
        """Gets the site_id of this GetEnrollmentCustomization.  # noqa: E501


        :return: The site_id of this GetEnrollmentCustomization.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this GetEnrollmentCustomization.


        :param site_id: The site_id of this GetEnrollmentCustomization.  # noqa: E501
        :type site_id: int
        """
        if self.local_vars_configuration.client_side_validation and site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def display_name(self):
        """Gets the display_name of this GetEnrollmentCustomization.  # noqa: E501


        :return: The display_name of this GetEnrollmentCustomization.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetEnrollmentCustomization.


        :param display_name: The display_name of this GetEnrollmentCustomization.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this GetEnrollmentCustomization.  # noqa: E501


        :return: The description of this GetEnrollmentCustomization.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetEnrollmentCustomization.


        :param description: The description of this GetEnrollmentCustomization.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def enrollment_customization_branding_settings(self):
        """Gets the enrollment_customization_branding_settings of this GetEnrollmentCustomization.  # noqa: E501


        :return: The enrollment_customization_branding_settings of this GetEnrollmentCustomization.  # noqa: E501
        :rtype: EnrollmentCustomizationBrandingSettings
        """
        return self._enrollment_customization_branding_settings

    @enrollment_customization_branding_settings.setter
    def enrollment_customization_branding_settings(self, enrollment_customization_branding_settings):
        """Sets the enrollment_customization_branding_settings of this GetEnrollmentCustomization.


        :param enrollment_customization_branding_settings: The enrollment_customization_branding_settings of this GetEnrollmentCustomization.  # noqa: E501
        :type enrollment_customization_branding_settings: EnrollmentCustomizationBrandingSettings
        """
        if self.local_vars_configuration.client_side_validation and enrollment_customization_branding_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `enrollment_customization_branding_settings`, must not be `None`")  # noqa: E501

        self._enrollment_customization_branding_settings = enrollment_customization_branding_settings

    @property
    def id(self):
        """Gets the id of this GetEnrollmentCustomization.  # noqa: E501


        :return: The id of this GetEnrollmentCustomization.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetEnrollmentCustomization.


        :param id: The id of this GetEnrollmentCustomization.  # noqa: E501
        :type id: int
        """

        self._id = id

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
        if not isinstance(other, GetEnrollmentCustomization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetEnrollmentCustomization):
            return True

        return self.to_dict() != other.to_dict()
