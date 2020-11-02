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


class GetMobileDevicePrestageV2(object):
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
        'mandatory': 'bool',
        'mdm_removable': 'bool',
        'support_phone_number': 'str',
        'support_email_address': 'str',
        'department': 'str',
        'default_prestage': 'bool',
        'enrollment_site_id': 'str',
        'keep_existing_site_membership': 'bool',
        'keep_existing_location_information': 'bool',
        'require_authentication': 'bool',
        'authentication_prompt': 'str',
        'prevent_activation_lock': 'bool',
        'enable_device_based_activation_lock': 'bool',
        'device_enrollment_program_instance_id': 'str',
        'skip_setup_items': 'dict(str, bool)',
        'location_information': 'LocationInformationV2',
        'purchasing_information': 'PrestagePurchasingInformationV2',
        'anchor_certificates': 'list[str]',
        'enrollment_customization_id': 'str',
        'language': 'str',
        'region': 'str',
        'auto_advance_setup': 'bool',
        'allow_pairing': 'bool',
        'multi_user': 'bool',
        'supervised': 'bool',
        'maximum_shared_accounts': 'int',
        'configure_device_before_setup_assistant': 'bool',
        'names': 'MobileDevicePrestageNamesV2',
        'send_timezone': 'bool',
        'timezone': 'str',
        'id': 'str',
        'profile_uuid': 'str',
        'site_id': 'str',
        'version_lock': 'int'
    }

    attribute_map = {
        'display_name': 'displayName',
        'mandatory': 'mandatory',
        'mdm_removable': 'mdmRemovable',
        'support_phone_number': 'supportPhoneNumber',
        'support_email_address': 'supportEmailAddress',
        'department': 'department',
        'default_prestage': 'defaultPrestage',
        'enrollment_site_id': 'enrollmentSiteId',
        'keep_existing_site_membership': 'keepExistingSiteMembership',
        'keep_existing_location_information': 'keepExistingLocationInformation',
        'require_authentication': 'requireAuthentication',
        'authentication_prompt': 'authenticationPrompt',
        'prevent_activation_lock': 'preventActivationLock',
        'enable_device_based_activation_lock': 'enableDeviceBasedActivationLock',
        'device_enrollment_program_instance_id': 'deviceEnrollmentProgramInstanceId',
        'skip_setup_items': 'skipSetupItems',
        'location_information': 'locationInformation',
        'purchasing_information': 'purchasingInformation',
        'anchor_certificates': 'anchorCertificates',
        'enrollment_customization_id': 'enrollmentCustomizationId',
        'language': 'language',
        'region': 'region',
        'auto_advance_setup': 'autoAdvanceSetup',
        'allow_pairing': 'allowPairing',
        'multi_user': 'multiUser',
        'supervised': 'supervised',
        'maximum_shared_accounts': 'maximumSharedAccounts',
        'configure_device_before_setup_assistant': 'configureDeviceBeforeSetupAssistant',
        'names': 'names',
        'send_timezone': 'sendTimezone',
        'timezone': 'timezone',
        'id': 'id',
        'profile_uuid': 'profileUuid',
        'site_id': 'siteId',
        'version_lock': 'versionLock'
    }

    def __init__(self, display_name=None, mandatory=None, mdm_removable=None, support_phone_number=None, support_email_address=None, department=None, default_prestage=None, enrollment_site_id=None, keep_existing_site_membership=None, keep_existing_location_information=None, require_authentication=None, authentication_prompt=None, prevent_activation_lock=None, enable_device_based_activation_lock=None, device_enrollment_program_instance_id=None, skip_setup_items=None, location_information=None, purchasing_information=None, anchor_certificates=None, enrollment_customization_id=None, language=None, region=None, auto_advance_setup=None, allow_pairing=None, multi_user=None, supervised=None, maximum_shared_accounts=None, configure_device_before_setup_assistant=None, names=None, send_timezone=None, timezone=None, id=None, profile_uuid=None, site_id=None, version_lock=None, local_vars_configuration=None):  # noqa: E501
        """GetMobileDevicePrestageV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._mandatory = None
        self._mdm_removable = None
        self._support_phone_number = None
        self._support_email_address = None
        self._department = None
        self._default_prestage = None
        self._enrollment_site_id = None
        self._keep_existing_site_membership = None
        self._keep_existing_location_information = None
        self._require_authentication = None
        self._authentication_prompt = None
        self._prevent_activation_lock = None
        self._enable_device_based_activation_lock = None
        self._device_enrollment_program_instance_id = None
        self._skip_setup_items = None
        self._location_information = None
        self._purchasing_information = None
        self._anchor_certificates = None
        self._enrollment_customization_id = None
        self._language = None
        self._region = None
        self._auto_advance_setup = None
        self._allow_pairing = None
        self._multi_user = None
        self._supervised = None
        self._maximum_shared_accounts = None
        self._configure_device_before_setup_assistant = None
        self._names = None
        self._send_timezone = None
        self._timezone = None
        self._id = None
        self._profile_uuid = None
        self._site_id = None
        self._version_lock = None
        self.discriminator = None

        self.display_name = display_name
        self.mandatory = mandatory
        self.mdm_removable = mdm_removable
        self.support_phone_number = support_phone_number
        self.support_email_address = support_email_address
        self.department = department
        self.default_prestage = default_prestage
        self.enrollment_site_id = enrollment_site_id
        self.keep_existing_site_membership = keep_existing_site_membership
        self.keep_existing_location_information = keep_existing_location_information
        self.require_authentication = require_authentication
        self.authentication_prompt = authentication_prompt
        self.prevent_activation_lock = prevent_activation_lock
        self.enable_device_based_activation_lock = enable_device_based_activation_lock
        self.device_enrollment_program_instance_id = device_enrollment_program_instance_id
        if skip_setup_items is not None:
            self.skip_setup_items = skip_setup_items
        self.location_information = location_information
        self.purchasing_information = purchasing_information
        if anchor_certificates is not None:
            self.anchor_certificates = anchor_certificates
        if enrollment_customization_id is not None:
            self.enrollment_customization_id = enrollment_customization_id
        if language is not None:
            self.language = language
        if region is not None:
            self.region = region
        self.auto_advance_setup = auto_advance_setup
        self.allow_pairing = allow_pairing
        self.multi_user = multi_user
        self.supervised = supervised
        self.maximum_shared_accounts = maximum_shared_accounts
        self.configure_device_before_setup_assistant = configure_device_before_setup_assistant
        if names is not None:
            self.names = names
        self.send_timezone = send_timezone
        self.timezone = timezone
        if id is not None:
            self.id = id
        if profile_uuid is not None:
            self.profile_uuid = profile_uuid
        if site_id is not None:
            self.site_id = site_id
        if version_lock is not None:
            self.version_lock = version_lock

    @property
    def display_name(self):
        """Gets the display_name of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The display_name of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetMobileDevicePrestageV2.


        :param display_name: The display_name of this GetMobileDevicePrestageV2.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def mandatory(self):
        """Gets the mandatory of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The mandatory of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this GetMobileDevicePrestageV2.


        :param mandatory: The mandatory of this GetMobileDevicePrestageV2.  # noqa: E501
        :type mandatory: bool
        """
        if self.local_vars_configuration.client_side_validation and mandatory is None:  # noqa: E501
            raise ValueError("Invalid value for `mandatory`, must not be `None`")  # noqa: E501

        self._mandatory = mandatory

    @property
    def mdm_removable(self):
        """Gets the mdm_removable of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The mdm_removable of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._mdm_removable

    @mdm_removable.setter
    def mdm_removable(self, mdm_removable):
        """Sets the mdm_removable of this GetMobileDevicePrestageV2.


        :param mdm_removable: The mdm_removable of this GetMobileDevicePrestageV2.  # noqa: E501
        :type mdm_removable: bool
        """
        if self.local_vars_configuration.client_side_validation and mdm_removable is None:  # noqa: E501
            raise ValueError("Invalid value for `mdm_removable`, must not be `None`")  # noqa: E501

        self._mdm_removable = mdm_removable

    @property
    def support_phone_number(self):
        """Gets the support_phone_number of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The support_phone_number of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._support_phone_number

    @support_phone_number.setter
    def support_phone_number(self, support_phone_number):
        """Sets the support_phone_number of this GetMobileDevicePrestageV2.


        :param support_phone_number: The support_phone_number of this GetMobileDevicePrestageV2.  # noqa: E501
        :type support_phone_number: str
        """
        if self.local_vars_configuration.client_side_validation and support_phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `support_phone_number`, must not be `None`")  # noqa: E501

        self._support_phone_number = support_phone_number

    @property
    def support_email_address(self):
        """Gets the support_email_address of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The support_email_address of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._support_email_address

    @support_email_address.setter
    def support_email_address(self, support_email_address):
        """Sets the support_email_address of this GetMobileDevicePrestageV2.


        :param support_email_address: The support_email_address of this GetMobileDevicePrestageV2.  # noqa: E501
        :type support_email_address: str
        """
        if self.local_vars_configuration.client_side_validation and support_email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `support_email_address`, must not be `None`")  # noqa: E501

        self._support_email_address = support_email_address

    @property
    def department(self):
        """Gets the department of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The department of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this GetMobileDevicePrestageV2.


        :param department: The department of this GetMobileDevicePrestageV2.  # noqa: E501
        :type department: str
        """
        if self.local_vars_configuration.client_side_validation and department is None:  # noqa: E501
            raise ValueError("Invalid value for `department`, must not be `None`")  # noqa: E501

        self._department = department

    @property
    def default_prestage(self):
        """Gets the default_prestage of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The default_prestage of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._default_prestage

    @default_prestage.setter
    def default_prestage(self, default_prestage):
        """Sets the default_prestage of this GetMobileDevicePrestageV2.


        :param default_prestage: The default_prestage of this GetMobileDevicePrestageV2.  # noqa: E501
        :type default_prestage: bool
        """
        if self.local_vars_configuration.client_side_validation and default_prestage is None:  # noqa: E501
            raise ValueError("Invalid value for `default_prestage`, must not be `None`")  # noqa: E501

        self._default_prestage = default_prestage

    @property
    def enrollment_site_id(self):
        """Gets the enrollment_site_id of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The enrollment_site_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_site_id

    @enrollment_site_id.setter
    def enrollment_site_id(self, enrollment_site_id):
        """Sets the enrollment_site_id of this GetMobileDevicePrestageV2.


        :param enrollment_site_id: The enrollment_site_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :type enrollment_site_id: str
        """
        if self.local_vars_configuration.client_side_validation and enrollment_site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `enrollment_site_id`, must not be `None`")  # noqa: E501

        self._enrollment_site_id = enrollment_site_id

    @property
    def keep_existing_site_membership(self):
        """Gets the keep_existing_site_membership of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The keep_existing_site_membership of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._keep_existing_site_membership

    @keep_existing_site_membership.setter
    def keep_existing_site_membership(self, keep_existing_site_membership):
        """Sets the keep_existing_site_membership of this GetMobileDevicePrestageV2.


        :param keep_existing_site_membership: The keep_existing_site_membership of this GetMobileDevicePrestageV2.  # noqa: E501
        :type keep_existing_site_membership: bool
        """
        if self.local_vars_configuration.client_side_validation and keep_existing_site_membership is None:  # noqa: E501
            raise ValueError("Invalid value for `keep_existing_site_membership`, must not be `None`")  # noqa: E501

        self._keep_existing_site_membership = keep_existing_site_membership

    @property
    def keep_existing_location_information(self):
        """Gets the keep_existing_location_information of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The keep_existing_location_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._keep_existing_location_information

    @keep_existing_location_information.setter
    def keep_existing_location_information(self, keep_existing_location_information):
        """Sets the keep_existing_location_information of this GetMobileDevicePrestageV2.


        :param keep_existing_location_information: The keep_existing_location_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :type keep_existing_location_information: bool
        """
        if self.local_vars_configuration.client_side_validation and keep_existing_location_information is None:  # noqa: E501
            raise ValueError("Invalid value for `keep_existing_location_information`, must not be `None`")  # noqa: E501

        self._keep_existing_location_information = keep_existing_location_information

    @property
    def require_authentication(self):
        """Gets the require_authentication of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The require_authentication of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._require_authentication

    @require_authentication.setter
    def require_authentication(self, require_authentication):
        """Sets the require_authentication of this GetMobileDevicePrestageV2.


        :param require_authentication: The require_authentication of this GetMobileDevicePrestageV2.  # noqa: E501
        :type require_authentication: bool
        """
        if self.local_vars_configuration.client_side_validation and require_authentication is None:  # noqa: E501
            raise ValueError("Invalid value for `require_authentication`, must not be `None`")  # noqa: E501

        self._require_authentication = require_authentication

    @property
    def authentication_prompt(self):
        """Gets the authentication_prompt of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The authentication_prompt of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._authentication_prompt

    @authentication_prompt.setter
    def authentication_prompt(self, authentication_prompt):
        """Sets the authentication_prompt of this GetMobileDevicePrestageV2.


        :param authentication_prompt: The authentication_prompt of this GetMobileDevicePrestageV2.  # noqa: E501
        :type authentication_prompt: str
        """
        if self.local_vars_configuration.client_side_validation and authentication_prompt is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_prompt`, must not be `None`")  # noqa: E501

        self._authentication_prompt = authentication_prompt

    @property
    def prevent_activation_lock(self):
        """Gets the prevent_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The prevent_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_activation_lock

    @prevent_activation_lock.setter
    def prevent_activation_lock(self, prevent_activation_lock):
        """Sets the prevent_activation_lock of this GetMobileDevicePrestageV2.


        :param prevent_activation_lock: The prevent_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :type prevent_activation_lock: bool
        """
        if self.local_vars_configuration.client_side_validation and prevent_activation_lock is None:  # noqa: E501
            raise ValueError("Invalid value for `prevent_activation_lock`, must not be `None`")  # noqa: E501

        self._prevent_activation_lock = prevent_activation_lock

    @property
    def enable_device_based_activation_lock(self):
        """Gets the enable_device_based_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The enable_device_based_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._enable_device_based_activation_lock

    @enable_device_based_activation_lock.setter
    def enable_device_based_activation_lock(self, enable_device_based_activation_lock):
        """Sets the enable_device_based_activation_lock of this GetMobileDevicePrestageV2.


        :param enable_device_based_activation_lock: The enable_device_based_activation_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :type enable_device_based_activation_lock: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_device_based_activation_lock is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_device_based_activation_lock`, must not be `None`")  # noqa: E501

        self._enable_device_based_activation_lock = enable_device_based_activation_lock

    @property
    def device_enrollment_program_instance_id(self):
        """Gets the device_enrollment_program_instance_id of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The device_enrollment_program_instance_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._device_enrollment_program_instance_id

    @device_enrollment_program_instance_id.setter
    def device_enrollment_program_instance_id(self, device_enrollment_program_instance_id):
        """Sets the device_enrollment_program_instance_id of this GetMobileDevicePrestageV2.


        :param device_enrollment_program_instance_id: The device_enrollment_program_instance_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :type device_enrollment_program_instance_id: str
        """
        if self.local_vars_configuration.client_side_validation and device_enrollment_program_instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_enrollment_program_instance_id`, must not be `None`")  # noqa: E501

        self._device_enrollment_program_instance_id = device_enrollment_program_instance_id

    @property
    def skip_setup_items(self):
        """Gets the skip_setup_items of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The skip_setup_items of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._skip_setup_items

    @skip_setup_items.setter
    def skip_setup_items(self, skip_setup_items):
        """Sets the skip_setup_items of this GetMobileDevicePrestageV2.


        :param skip_setup_items: The skip_setup_items of this GetMobileDevicePrestageV2.  # noqa: E501
        :type skip_setup_items: dict(str, bool)
        """

        self._skip_setup_items = skip_setup_items

    @property
    def location_information(self):
        """Gets the location_information of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The location_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: LocationInformationV2
        """
        return self._location_information

    @location_information.setter
    def location_information(self, location_information):
        """Sets the location_information of this GetMobileDevicePrestageV2.


        :param location_information: The location_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :type location_information: LocationInformationV2
        """
        if self.local_vars_configuration.client_side_validation and location_information is None:  # noqa: E501
            raise ValueError("Invalid value for `location_information`, must not be `None`")  # noqa: E501

        self._location_information = location_information

    @property
    def purchasing_information(self):
        """Gets the purchasing_information of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The purchasing_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: PrestagePurchasingInformationV2
        """
        return self._purchasing_information

    @purchasing_information.setter
    def purchasing_information(self, purchasing_information):
        """Sets the purchasing_information of this GetMobileDevicePrestageV2.


        :param purchasing_information: The purchasing_information of this GetMobileDevicePrestageV2.  # noqa: E501
        :type purchasing_information: PrestagePurchasingInformationV2
        """
        if self.local_vars_configuration.client_side_validation and purchasing_information is None:  # noqa: E501
            raise ValueError("Invalid value for `purchasing_information`, must not be `None`")  # noqa: E501

        self._purchasing_information = purchasing_information

    @property
    def anchor_certificates(self):
        """Gets the anchor_certificates of this GetMobileDevicePrestageV2.  # noqa: E501

        The Base64 encoded PEM Certificate  # noqa: E501

        :return: The anchor_certificates of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._anchor_certificates

    @anchor_certificates.setter
    def anchor_certificates(self, anchor_certificates):
        """Sets the anchor_certificates of this GetMobileDevicePrestageV2.

        The Base64 encoded PEM Certificate  # noqa: E501

        :param anchor_certificates: The anchor_certificates of this GetMobileDevicePrestageV2.  # noqa: E501
        :type anchor_certificates: list[str]
        """

        self._anchor_certificates = anchor_certificates

    @property
    def enrollment_customization_id(self):
        """Gets the enrollment_customization_id of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The enrollment_customization_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_customization_id

    @enrollment_customization_id.setter
    def enrollment_customization_id(self, enrollment_customization_id):
        """Sets the enrollment_customization_id of this GetMobileDevicePrestageV2.


        :param enrollment_customization_id: The enrollment_customization_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :type enrollment_customization_id: str
        """

        self._enrollment_customization_id = enrollment_customization_id

    @property
    def language(self):
        """Gets the language of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The language of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GetMobileDevicePrestageV2.


        :param language: The language of this GetMobileDevicePrestageV2.  # noqa: E501
        :type language: str
        """

        self._language = language

    @property
    def region(self):
        """Gets the region of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The region of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this GetMobileDevicePrestageV2.


        :param region: The region of this GetMobileDevicePrestageV2.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def auto_advance_setup(self):
        """Gets the auto_advance_setup of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The auto_advance_setup of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._auto_advance_setup

    @auto_advance_setup.setter
    def auto_advance_setup(self, auto_advance_setup):
        """Sets the auto_advance_setup of this GetMobileDevicePrestageV2.


        :param auto_advance_setup: The auto_advance_setup of this GetMobileDevicePrestageV2.  # noqa: E501
        :type auto_advance_setup: bool
        """
        if self.local_vars_configuration.client_side_validation and auto_advance_setup is None:  # noqa: E501
            raise ValueError("Invalid value for `auto_advance_setup`, must not be `None`")  # noqa: E501

        self._auto_advance_setup = auto_advance_setup

    @property
    def allow_pairing(self):
        """Gets the allow_pairing of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The allow_pairing of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._allow_pairing

    @allow_pairing.setter
    def allow_pairing(self, allow_pairing):
        """Sets the allow_pairing of this GetMobileDevicePrestageV2.


        :param allow_pairing: The allow_pairing of this GetMobileDevicePrestageV2.  # noqa: E501
        :type allow_pairing: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_pairing is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_pairing`, must not be `None`")  # noqa: E501

        self._allow_pairing = allow_pairing

    @property
    def multi_user(self):
        """Gets the multi_user of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The multi_user of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._multi_user

    @multi_user.setter
    def multi_user(self, multi_user):
        """Sets the multi_user of this GetMobileDevicePrestageV2.


        :param multi_user: The multi_user of this GetMobileDevicePrestageV2.  # noqa: E501
        :type multi_user: bool
        """
        if self.local_vars_configuration.client_side_validation and multi_user is None:  # noqa: E501
            raise ValueError("Invalid value for `multi_user`, must not be `None`")  # noqa: E501

        self._multi_user = multi_user

    @property
    def supervised(self):
        """Gets the supervised of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The supervised of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._supervised

    @supervised.setter
    def supervised(self, supervised):
        """Sets the supervised of this GetMobileDevicePrestageV2.


        :param supervised: The supervised of this GetMobileDevicePrestageV2.  # noqa: E501
        :type supervised: bool
        """
        if self.local_vars_configuration.client_side_validation and supervised is None:  # noqa: E501
            raise ValueError("Invalid value for `supervised`, must not be `None`")  # noqa: E501

        self._supervised = supervised

    @property
    def maximum_shared_accounts(self):
        """Gets the maximum_shared_accounts of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The maximum_shared_accounts of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: int
        """
        return self._maximum_shared_accounts

    @maximum_shared_accounts.setter
    def maximum_shared_accounts(self, maximum_shared_accounts):
        """Sets the maximum_shared_accounts of this GetMobileDevicePrestageV2.


        :param maximum_shared_accounts: The maximum_shared_accounts of this GetMobileDevicePrestageV2.  # noqa: E501
        :type maximum_shared_accounts: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_shared_accounts is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_shared_accounts`, must not be `None`")  # noqa: E501

        self._maximum_shared_accounts = maximum_shared_accounts

    @property
    def configure_device_before_setup_assistant(self):
        """Gets the configure_device_before_setup_assistant of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The configure_device_before_setup_assistant of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._configure_device_before_setup_assistant

    @configure_device_before_setup_assistant.setter
    def configure_device_before_setup_assistant(self, configure_device_before_setup_assistant):
        """Sets the configure_device_before_setup_assistant of this GetMobileDevicePrestageV2.


        :param configure_device_before_setup_assistant: The configure_device_before_setup_assistant of this GetMobileDevicePrestageV2.  # noqa: E501
        :type configure_device_before_setup_assistant: bool
        """
        if self.local_vars_configuration.client_side_validation and configure_device_before_setup_assistant is None:  # noqa: E501
            raise ValueError("Invalid value for `configure_device_before_setup_assistant`, must not be `None`")  # noqa: E501

        self._configure_device_before_setup_assistant = configure_device_before_setup_assistant

    @property
    def names(self):
        """Gets the names of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The names of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: MobileDevicePrestageNamesV2
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this GetMobileDevicePrestageV2.


        :param names: The names of this GetMobileDevicePrestageV2.  # noqa: E501
        :type names: MobileDevicePrestageNamesV2
        """

        self._names = names

    @property
    def send_timezone(self):
        """Gets the send_timezone of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The send_timezone of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: bool
        """
        return self._send_timezone

    @send_timezone.setter
    def send_timezone(self, send_timezone):
        """Sets the send_timezone of this GetMobileDevicePrestageV2.


        :param send_timezone: The send_timezone of this GetMobileDevicePrestageV2.  # noqa: E501
        :type send_timezone: bool
        """
        if self.local_vars_configuration.client_side_validation and send_timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `send_timezone`, must not be `None`")  # noqa: E501

        self._send_timezone = send_timezone

    @property
    def timezone(self):
        """Gets the timezone of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The timezone of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this GetMobileDevicePrestageV2.


        :param timezone: The timezone of this GetMobileDevicePrestageV2.  # noqa: E501
        :type timezone: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def id(self):
        """Gets the id of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The id of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetMobileDevicePrestageV2.


        :param id: The id of this GetMobileDevicePrestageV2.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def profile_uuid(self):
        """Gets the profile_uuid of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The profile_uuid of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._profile_uuid

    @profile_uuid.setter
    def profile_uuid(self, profile_uuid):
        """Sets the profile_uuid of this GetMobileDevicePrestageV2.


        :param profile_uuid: The profile_uuid of this GetMobileDevicePrestageV2.  # noqa: E501
        :type profile_uuid: str
        """

        self._profile_uuid = profile_uuid

    @property
    def site_id(self):
        """Gets the site_id of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The site_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this GetMobileDevicePrestageV2.


        :param site_id: The site_id of this GetMobileDevicePrestageV2.  # noqa: E501
        :type site_id: str
        """

        self._site_id = site_id

    @property
    def version_lock(self):
        """Gets the version_lock of this GetMobileDevicePrestageV2.  # noqa: E501


        :return: The version_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :rtype: int
        """
        return self._version_lock

    @version_lock.setter
    def version_lock(self, version_lock):
        """Sets the version_lock of this GetMobileDevicePrestageV2.


        :param version_lock: The version_lock of this GetMobileDevicePrestageV2.  # noqa: E501
        :type version_lock: int
        """

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
        if not isinstance(other, GetMobileDevicePrestageV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetMobileDevicePrestageV2):
            return True

        return self.to_dict() != other.to_dict()
