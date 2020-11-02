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


class DeviceEnrollmentPrestage(object):
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
        'display_name': 'str',
        'is_mandatory': 'bool',
        'is_mdm_removable': 'bool',
        'support_phone_number': 'str',
        'support_email_address': 'str',
        'department': 'str',
        'is_default_prestage': 'bool',
        'enrollment_site_id': 'int',
        'is_keep_existing_site_membership': 'bool',
        'is_keep_existing_location_information': 'bool',
        'is_require_authentication': 'bool',
        'authentication_prompt': 'str',
        'is_prevent_activation_lock': 'bool',
        'is_enable_device_based_activation_lock': 'bool',
        'device_enrollment_program_instance_id': 'int',
        'skip_setup_items': 'dict(str, bool)',
        'location_information': 'LocationInformation',
        'purchasing_information': 'PrestagePurchasingInformation',
        'anchor_certificates': 'list[str]',
        'enrollment_customization_id': 'int'
    }

    attribute_map = {
        'display_name': 'displayName',
        'is_mandatory': 'isMandatory',
        'is_mdm_removable': 'isMdmRemovable',
        'support_phone_number': 'supportPhoneNumber',
        'support_email_address': 'supportEmailAddress',
        'department': 'department',
        'is_default_prestage': 'isDefaultPrestage',
        'enrollment_site_id': 'enrollmentSiteId',
        'is_keep_existing_site_membership': 'isKeepExistingSiteMembership',
        'is_keep_existing_location_information': 'isKeepExistingLocationInformation',
        'is_require_authentication': 'isRequireAuthentication',
        'authentication_prompt': 'authenticationPrompt',
        'is_prevent_activation_lock': 'isPreventActivationLock',
        'is_enable_device_based_activation_lock': 'isEnableDeviceBasedActivationLock',
        'device_enrollment_program_instance_id': 'deviceEnrollmentProgramInstanceId',
        'skip_setup_items': 'skipSetupItems',
        'location_information': 'locationInformation',
        'purchasing_information': 'purchasingInformation',
        'anchor_certificates': 'anchorCertificates',
        'enrollment_customization_id': 'enrollmentCustomizationId'
    }

    def __init__(self, display_name=None, is_mandatory=None, is_mdm_removable=None, support_phone_number=None, support_email_address=None, department=None, is_default_prestage=None, enrollment_site_id=None, is_keep_existing_site_membership=None, is_keep_existing_location_information=None, is_require_authentication=None, authentication_prompt=None, is_prevent_activation_lock=None, is_enable_device_based_activation_lock=None, device_enrollment_program_instance_id=None, skip_setup_items=None, location_information=None, purchasing_information=None, anchor_certificates=None, enrollment_customization_id=None, local_vars_configuration=None):  # noqa: E501
        """DeviceEnrollmentPrestage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._is_mandatory = None
        self._is_mdm_removable = None
        self._support_phone_number = None
        self._support_email_address = None
        self._department = None
        self._is_default_prestage = None
        self._enrollment_site_id = None
        self._is_keep_existing_site_membership = None
        self._is_keep_existing_location_information = None
        self._is_require_authentication = None
        self._authentication_prompt = None
        self._is_prevent_activation_lock = None
        self._is_enable_device_based_activation_lock = None
        self._device_enrollment_program_instance_id = None
        self._skip_setup_items = None
        self._location_information = None
        self._purchasing_information = None
        self._anchor_certificates = None
        self._enrollment_customization_id = None
        self.discriminator = None

        self.display_name = display_name
        self.is_mandatory = is_mandatory
        self.is_mdm_removable = is_mdm_removable
        self.support_phone_number = support_phone_number
        self.support_email_address = support_email_address
        self.department = department
        self.is_default_prestage = is_default_prestage
        self.enrollment_site_id = enrollment_site_id
        self.is_keep_existing_site_membership = is_keep_existing_site_membership
        self.is_keep_existing_location_information = is_keep_existing_location_information
        self.is_require_authentication = is_require_authentication
        self.authentication_prompt = authentication_prompt
        self.is_prevent_activation_lock = is_prevent_activation_lock
        self.is_enable_device_based_activation_lock = is_enable_device_based_activation_lock
        self.device_enrollment_program_instance_id = device_enrollment_program_instance_id
        if skip_setup_items is not None:
            self.skip_setup_items = skip_setup_items
        self.location_information = location_information
        self.purchasing_information = purchasing_information
        if anchor_certificates is not None:
            self.anchor_certificates = anchor_certificates
        if enrollment_customization_id is not None:
            self.enrollment_customization_id = enrollment_customization_id

    @property
    def display_name(self):
        """Gets the display_name of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The display_name of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DeviceEnrollmentPrestage.


        :param display_name: The display_name of this DeviceEnrollmentPrestage.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_mandatory of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this DeviceEnrollmentPrestage.


        :param is_mandatory: The is_mandatory of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_mandatory: bool
        """
        if self.local_vars_configuration.client_side_validation and is_mandatory is None:  # noqa: E501
            raise ValueError("Invalid value for `is_mandatory`, must not be `None`")  # noqa: E501

        self._is_mandatory = is_mandatory

    @property
    def is_mdm_removable(self):
        """Gets the is_mdm_removable of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_mdm_removable of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_mdm_removable

    @is_mdm_removable.setter
    def is_mdm_removable(self, is_mdm_removable):
        """Sets the is_mdm_removable of this DeviceEnrollmentPrestage.


        :param is_mdm_removable: The is_mdm_removable of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_mdm_removable: bool
        """
        if self.local_vars_configuration.client_side_validation and is_mdm_removable is None:  # noqa: E501
            raise ValueError("Invalid value for `is_mdm_removable`, must not be `None`")  # noqa: E501

        self._is_mdm_removable = is_mdm_removable

    @property
    def support_phone_number(self):
        """Gets the support_phone_number of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The support_phone_number of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: str
        """
        return self._support_phone_number

    @support_phone_number.setter
    def support_phone_number(self, support_phone_number):
        """Sets the support_phone_number of this DeviceEnrollmentPrestage.


        :param support_phone_number: The support_phone_number of this DeviceEnrollmentPrestage.  # noqa: E501
        :type support_phone_number: str
        """
        if self.local_vars_configuration.client_side_validation and support_phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `support_phone_number`, must not be `None`")  # noqa: E501

        self._support_phone_number = support_phone_number

    @property
    def support_email_address(self):
        """Gets the support_email_address of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The support_email_address of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: str
        """
        return self._support_email_address

    @support_email_address.setter
    def support_email_address(self, support_email_address):
        """Sets the support_email_address of this DeviceEnrollmentPrestage.


        :param support_email_address: The support_email_address of this DeviceEnrollmentPrestage.  # noqa: E501
        :type support_email_address: str
        """
        if self.local_vars_configuration.client_side_validation and support_email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `support_email_address`, must not be `None`")  # noqa: E501

        self._support_email_address = support_email_address

    @property
    def department(self):
        """Gets the department of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The department of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this DeviceEnrollmentPrestage.


        :param department: The department of this DeviceEnrollmentPrestage.  # noqa: E501
        :type department: str
        """
        if self.local_vars_configuration.client_side_validation and department is None:  # noqa: E501
            raise ValueError("Invalid value for `department`, must not be `None`")  # noqa: E501

        self._department = department

    @property
    def is_default_prestage(self):
        """Gets the is_default_prestage of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_default_prestage of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_prestage

    @is_default_prestage.setter
    def is_default_prestage(self, is_default_prestage):
        """Sets the is_default_prestage of this DeviceEnrollmentPrestage.


        :param is_default_prestage: The is_default_prestage of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_default_prestage: bool
        """
        if self.local_vars_configuration.client_side_validation and is_default_prestage is None:  # noqa: E501
            raise ValueError("Invalid value for `is_default_prestage`, must not be `None`")  # noqa: E501

        self._is_default_prestage = is_default_prestage

    @property
    def enrollment_site_id(self):
        """Gets the enrollment_site_id of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The enrollment_site_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: int
        """
        return self._enrollment_site_id

    @enrollment_site_id.setter
    def enrollment_site_id(self, enrollment_site_id):
        """Sets the enrollment_site_id of this DeviceEnrollmentPrestage.


        :param enrollment_site_id: The enrollment_site_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :type enrollment_site_id: int
        """
        if self.local_vars_configuration.client_side_validation and enrollment_site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `enrollment_site_id`, must not be `None`")  # noqa: E501

        self._enrollment_site_id = enrollment_site_id

    @property
    def is_keep_existing_site_membership(self):
        """Gets the is_keep_existing_site_membership of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_keep_existing_site_membership of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_keep_existing_site_membership

    @is_keep_existing_site_membership.setter
    def is_keep_existing_site_membership(self, is_keep_existing_site_membership):
        """Sets the is_keep_existing_site_membership of this DeviceEnrollmentPrestage.


        :param is_keep_existing_site_membership: The is_keep_existing_site_membership of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_keep_existing_site_membership: bool
        """
        if self.local_vars_configuration.client_side_validation and is_keep_existing_site_membership is None:  # noqa: E501
            raise ValueError("Invalid value for `is_keep_existing_site_membership`, must not be `None`")  # noqa: E501

        self._is_keep_existing_site_membership = is_keep_existing_site_membership

    @property
    def is_keep_existing_location_information(self):
        """Gets the is_keep_existing_location_information of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_keep_existing_location_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_keep_existing_location_information

    @is_keep_existing_location_information.setter
    def is_keep_existing_location_information(self, is_keep_existing_location_information):
        """Sets the is_keep_existing_location_information of this DeviceEnrollmentPrestage.


        :param is_keep_existing_location_information: The is_keep_existing_location_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_keep_existing_location_information: bool
        """
        if self.local_vars_configuration.client_side_validation and is_keep_existing_location_information is None:  # noqa: E501
            raise ValueError("Invalid value for `is_keep_existing_location_information`, must not be `None`")  # noqa: E501

        self._is_keep_existing_location_information = is_keep_existing_location_information

    @property
    def is_require_authentication(self):
        """Gets the is_require_authentication of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_require_authentication of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_require_authentication

    @is_require_authentication.setter
    def is_require_authentication(self, is_require_authentication):
        """Sets the is_require_authentication of this DeviceEnrollmentPrestage.


        :param is_require_authentication: The is_require_authentication of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_require_authentication: bool
        """
        if self.local_vars_configuration.client_side_validation and is_require_authentication is None:  # noqa: E501
            raise ValueError("Invalid value for `is_require_authentication`, must not be `None`")  # noqa: E501

        self._is_require_authentication = is_require_authentication

    @property
    def authentication_prompt(self):
        """Gets the authentication_prompt of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The authentication_prompt of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: str
        """
        return self._authentication_prompt

    @authentication_prompt.setter
    def authentication_prompt(self, authentication_prompt):
        """Sets the authentication_prompt of this DeviceEnrollmentPrestage.


        :param authentication_prompt: The authentication_prompt of this DeviceEnrollmentPrestage.  # noqa: E501
        :type authentication_prompt: str
        """
        if self.local_vars_configuration.client_side_validation and authentication_prompt is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_prompt`, must not be `None`")  # noqa: E501

        self._authentication_prompt = authentication_prompt

    @property
    def is_prevent_activation_lock(self):
        """Gets the is_prevent_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_prevent_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_prevent_activation_lock

    @is_prevent_activation_lock.setter
    def is_prevent_activation_lock(self, is_prevent_activation_lock):
        """Sets the is_prevent_activation_lock of this DeviceEnrollmentPrestage.


        :param is_prevent_activation_lock: The is_prevent_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_prevent_activation_lock: bool
        """
        if self.local_vars_configuration.client_side_validation and is_prevent_activation_lock is None:  # noqa: E501
            raise ValueError("Invalid value for `is_prevent_activation_lock`, must not be `None`")  # noqa: E501

        self._is_prevent_activation_lock = is_prevent_activation_lock

    @property
    def is_enable_device_based_activation_lock(self):
        """Gets the is_enable_device_based_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The is_enable_device_based_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: bool
        """
        return self._is_enable_device_based_activation_lock

    @is_enable_device_based_activation_lock.setter
    def is_enable_device_based_activation_lock(self, is_enable_device_based_activation_lock):
        """Sets the is_enable_device_based_activation_lock of this DeviceEnrollmentPrestage.


        :param is_enable_device_based_activation_lock: The is_enable_device_based_activation_lock of this DeviceEnrollmentPrestage.  # noqa: E501
        :type is_enable_device_based_activation_lock: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enable_device_based_activation_lock is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enable_device_based_activation_lock`, must not be `None`")  # noqa: E501

        self._is_enable_device_based_activation_lock = is_enable_device_based_activation_lock

    @property
    def device_enrollment_program_instance_id(self):
        """Gets the device_enrollment_program_instance_id of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The device_enrollment_program_instance_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: int
        """
        return self._device_enrollment_program_instance_id

    @device_enrollment_program_instance_id.setter
    def device_enrollment_program_instance_id(self, device_enrollment_program_instance_id):
        """Sets the device_enrollment_program_instance_id of this DeviceEnrollmentPrestage.


        :param device_enrollment_program_instance_id: The device_enrollment_program_instance_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :type device_enrollment_program_instance_id: int
        """
        if self.local_vars_configuration.client_side_validation and device_enrollment_program_instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_enrollment_program_instance_id`, must not be `None`")  # noqa: E501

        self._device_enrollment_program_instance_id = device_enrollment_program_instance_id

    @property
    def skip_setup_items(self):
        """Gets the skip_setup_items of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The skip_setup_items of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._skip_setup_items

    @skip_setup_items.setter
    def skip_setup_items(self, skip_setup_items):
        """Sets the skip_setup_items of this DeviceEnrollmentPrestage.


        :param skip_setup_items: The skip_setup_items of this DeviceEnrollmentPrestage.  # noqa: E501
        :type skip_setup_items: dict(str, bool)
        """

        self._skip_setup_items = skip_setup_items

    @property
    def location_information(self):
        """Gets the location_information of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The location_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: LocationInformation
        """
        return self._location_information

    @location_information.setter
    def location_information(self, location_information):
        """Sets the location_information of this DeviceEnrollmentPrestage.


        :param location_information: The location_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :type location_information: LocationInformation
        """
        if self.local_vars_configuration.client_side_validation and location_information is None:  # noqa: E501
            raise ValueError("Invalid value for `location_information`, must not be `None`")  # noqa: E501

        self._location_information = location_information

    @property
    def purchasing_information(self):
        """Gets the purchasing_information of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The purchasing_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: PrestagePurchasingInformation
        """
        return self._purchasing_information

    @purchasing_information.setter
    def purchasing_information(self, purchasing_information):
        """Sets the purchasing_information of this DeviceEnrollmentPrestage.


        :param purchasing_information: The purchasing_information of this DeviceEnrollmentPrestage.  # noqa: E501
        :type purchasing_information: PrestagePurchasingInformation
        """
        if self.local_vars_configuration.client_side_validation and purchasing_information is None:  # noqa: E501
            raise ValueError("Invalid value for `purchasing_information`, must not be `None`")  # noqa: E501

        self._purchasing_information = purchasing_information

    @property
    def anchor_certificates(self):
        """Gets the anchor_certificates of this DeviceEnrollmentPrestage.  # noqa: E501

        The Base64 encoded PEM Certificate  # noqa: E501

        :return: The anchor_certificates of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: list[str]
        """
        return self._anchor_certificates

    @anchor_certificates.setter
    def anchor_certificates(self, anchor_certificates):
        """Sets the anchor_certificates of this DeviceEnrollmentPrestage.

        The Base64 encoded PEM Certificate  # noqa: E501

        :param anchor_certificates: The anchor_certificates of this DeviceEnrollmentPrestage.  # noqa: E501
        :type anchor_certificates: list[str]
        """

        self._anchor_certificates = anchor_certificates

    @property
    def enrollment_customization_id(self):
        """Gets the enrollment_customization_id of this DeviceEnrollmentPrestage.  # noqa: E501


        :return: The enrollment_customization_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :rtype: int
        """
        return self._enrollment_customization_id

    @enrollment_customization_id.setter
    def enrollment_customization_id(self, enrollment_customization_id):
        """Sets the enrollment_customization_id of this DeviceEnrollmentPrestage.


        :param enrollment_customization_id: The enrollment_customization_id of this DeviceEnrollmentPrestage.  # noqa: E501
        :type enrollment_customization_id: int
        """

        self._enrollment_customization_id = enrollment_customization_id

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
        if not isinstance(other, DeviceEnrollmentPrestage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceEnrollmentPrestage):
            return True

        return self.to_dict() != other.to_dict()
