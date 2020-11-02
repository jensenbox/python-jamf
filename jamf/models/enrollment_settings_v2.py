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


class EnrollmentSettingsV2(object):
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
        'install_single_profile': 'bool',
        'signing_mdm_profile_enabled': 'bool',
        'mdm_signing_certificate': 'CertificateIdentityV2',
        'restrict_reenrollment': 'bool',
        'flush_location_information': 'bool',
        'flush_location_history_information': 'bool',
        'flush_policy_history': 'bool',
        'flush_extension_attributes': 'bool',
        'flush_mdm_commands_on_reenroll': 'str',
        'mac_os_enterprise_enrollment_enabled': 'bool',
        'management_username': 'str',
        'management_password': 'str',
        'management_password_set': 'bool',
        'password_type': 'str',
        'random_password_length': 'int',
        'create_management_account': 'bool',
        'hide_management_account': 'bool',
        'allow_ssh_only_management_account': 'bool',
        'ensure_ssh_running': 'bool',
        'launch_self_service': 'bool',
        'sign_quick_add': 'bool',
        'developer_certificate_identity': 'CertificateIdentityV2',
        'developer_certificate_identity_details': 'CertificateDetails',
        'mdm_signing_certificate_details': 'CertificateDetails',
        'ios_enterprise_enrollment_enabled': 'bool',
        'ios_personal_enrollment_enabled': 'bool',
        'personal_device_enrollment_type': 'str'
    }

    attribute_map = {
        'install_single_profile': 'installSingleProfile',
        'signing_mdm_profile_enabled': 'signingMdmProfileEnabled',
        'mdm_signing_certificate': 'mdmSigningCertificate',
        'restrict_reenrollment': 'restrictReenrollment',
        'flush_location_information': 'flushLocationInformation',
        'flush_location_history_information': 'flushLocationHistoryInformation',
        'flush_policy_history': 'flushPolicyHistory',
        'flush_extension_attributes': 'flushExtensionAttributes',
        'flush_mdm_commands_on_reenroll': 'flushMdmCommandsOnReenroll',
        'mac_os_enterprise_enrollment_enabled': 'macOsEnterpriseEnrollmentEnabled',
        'management_username': 'managementUsername',
        'management_password': 'managementPassword',
        'management_password_set': 'managementPasswordSet',
        'password_type': 'passwordType',
        'random_password_length': 'randomPasswordLength',
        'create_management_account': 'createManagementAccount',
        'hide_management_account': 'hideManagementAccount',
        'allow_ssh_only_management_account': 'allowSshOnlyManagementAccount',
        'ensure_ssh_running': 'ensureSshRunning',
        'launch_self_service': 'launchSelfService',
        'sign_quick_add': 'signQuickAdd',
        'developer_certificate_identity': 'developerCertificateIdentity',
        'developer_certificate_identity_details': 'developerCertificateIdentityDetails',
        'mdm_signing_certificate_details': 'mdmSigningCertificateDetails',
        'ios_enterprise_enrollment_enabled': 'iosEnterpriseEnrollmentEnabled',
        'ios_personal_enrollment_enabled': 'iosPersonalEnrollmentEnabled',
        'personal_device_enrollment_type': 'personalDeviceEnrollmentType'
    }

    def __init__(self, install_single_profile=False, signing_mdm_profile_enabled=False, mdm_signing_certificate=None, restrict_reenrollment=False, flush_location_information=False, flush_location_history_information=False, flush_policy_history=False, flush_extension_attributes=False, flush_mdm_commands_on_reenroll='DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED', mac_os_enterprise_enrollment_enabled=False, management_username='', management_password='null', management_password_set=None, password_type='STATIC', random_password_length=8, create_management_account=True, hide_management_account=False, allow_ssh_only_management_account=False, ensure_ssh_running=True, launch_self_service=False, sign_quick_add=False, developer_certificate_identity=None, developer_certificate_identity_details=None, mdm_signing_certificate_details=None, ios_enterprise_enrollment_enabled=True, ios_personal_enrollment_enabled=False, personal_device_enrollment_type='PERSONALDEVICEPROFILES', local_vars_configuration=None):  # noqa: E501
        """EnrollmentSettingsV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._install_single_profile = None
        self._signing_mdm_profile_enabled = None
        self._mdm_signing_certificate = None
        self._restrict_reenrollment = None
        self._flush_location_information = None
        self._flush_location_history_information = None
        self._flush_policy_history = None
        self._flush_extension_attributes = None
        self._flush_mdm_commands_on_reenroll = None
        self._mac_os_enterprise_enrollment_enabled = None
        self._management_username = None
        self._management_password = None
        self._management_password_set = None
        self._password_type = None
        self._random_password_length = None
        self._create_management_account = None
        self._hide_management_account = None
        self._allow_ssh_only_management_account = None
        self._ensure_ssh_running = None
        self._launch_self_service = None
        self._sign_quick_add = None
        self._developer_certificate_identity = None
        self._developer_certificate_identity_details = None
        self._mdm_signing_certificate_details = None
        self._ios_enterprise_enrollment_enabled = None
        self._ios_personal_enrollment_enabled = None
        self._personal_device_enrollment_type = None
        self.discriminator = None

        if install_single_profile is not None:
            self.install_single_profile = install_single_profile
        if signing_mdm_profile_enabled is not None:
            self.signing_mdm_profile_enabled = signing_mdm_profile_enabled
        if mdm_signing_certificate is not None:
            self.mdm_signing_certificate = mdm_signing_certificate
        if restrict_reenrollment is not None:
            self.restrict_reenrollment = restrict_reenrollment
        if flush_location_information is not None:
            self.flush_location_information = flush_location_information
        if flush_location_history_information is not None:
            self.flush_location_history_information = flush_location_history_information
        if flush_policy_history is not None:
            self.flush_policy_history = flush_policy_history
        if flush_extension_attributes is not None:
            self.flush_extension_attributes = flush_extension_attributes
        if flush_mdm_commands_on_reenroll is not None:
            self.flush_mdm_commands_on_reenroll = flush_mdm_commands_on_reenroll
        if mac_os_enterprise_enrollment_enabled is not None:
            self.mac_os_enterprise_enrollment_enabled = mac_os_enterprise_enrollment_enabled
        if management_username is not None:
            self.management_username = management_username
        if management_password is not None:
            self.management_password = management_password
        if management_password_set is not None:
            self.management_password_set = management_password_set
        if password_type is not None:
            self.password_type = password_type
        if random_password_length is not None:
            self.random_password_length = random_password_length
        if create_management_account is not None:
            self.create_management_account = create_management_account
        if hide_management_account is not None:
            self.hide_management_account = hide_management_account
        if allow_ssh_only_management_account is not None:
            self.allow_ssh_only_management_account = allow_ssh_only_management_account
        if ensure_ssh_running is not None:
            self.ensure_ssh_running = ensure_ssh_running
        if launch_self_service is not None:
            self.launch_self_service = launch_self_service
        if sign_quick_add is not None:
            self.sign_quick_add = sign_quick_add
        if developer_certificate_identity is not None:
            self.developer_certificate_identity = developer_certificate_identity
        if developer_certificate_identity_details is not None:
            self.developer_certificate_identity_details = developer_certificate_identity_details
        if mdm_signing_certificate_details is not None:
            self.mdm_signing_certificate_details = mdm_signing_certificate_details
        if ios_enterprise_enrollment_enabled is not None:
            self.ios_enterprise_enrollment_enabled = ios_enterprise_enrollment_enabled
        if ios_personal_enrollment_enabled is not None:
            self.ios_personal_enrollment_enabled = ios_personal_enrollment_enabled
        if personal_device_enrollment_type is not None:
            self.personal_device_enrollment_type = personal_device_enrollment_type

    @property
    def install_single_profile(self):
        """Gets the install_single_profile of this EnrollmentSettingsV2.  # noqa: E501


        :return: The install_single_profile of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._install_single_profile

    @install_single_profile.setter
    def install_single_profile(self, install_single_profile):
        """Sets the install_single_profile of this EnrollmentSettingsV2.


        :param install_single_profile: The install_single_profile of this EnrollmentSettingsV2.  # noqa: E501
        :type install_single_profile: bool
        """

        self._install_single_profile = install_single_profile

    @property
    def signing_mdm_profile_enabled(self):
        """Gets the signing_mdm_profile_enabled of this EnrollmentSettingsV2.  # noqa: E501


        :return: The signing_mdm_profile_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._signing_mdm_profile_enabled

    @signing_mdm_profile_enabled.setter
    def signing_mdm_profile_enabled(self, signing_mdm_profile_enabled):
        """Sets the signing_mdm_profile_enabled of this EnrollmentSettingsV2.


        :param signing_mdm_profile_enabled: The signing_mdm_profile_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :type signing_mdm_profile_enabled: bool
        """

        self._signing_mdm_profile_enabled = signing_mdm_profile_enabled

    @property
    def mdm_signing_certificate(self):
        """Gets the mdm_signing_certificate of this EnrollmentSettingsV2.  # noqa: E501


        :return: The mdm_signing_certificate of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: CertificateIdentityV2
        """
        return self._mdm_signing_certificate

    @mdm_signing_certificate.setter
    def mdm_signing_certificate(self, mdm_signing_certificate):
        """Sets the mdm_signing_certificate of this EnrollmentSettingsV2.


        :param mdm_signing_certificate: The mdm_signing_certificate of this EnrollmentSettingsV2.  # noqa: E501
        :type mdm_signing_certificate: CertificateIdentityV2
        """

        self._mdm_signing_certificate = mdm_signing_certificate

    @property
    def restrict_reenrollment(self):
        """Gets the restrict_reenrollment of this EnrollmentSettingsV2.  # noqa: E501


        :return: The restrict_reenrollment of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_reenrollment

    @restrict_reenrollment.setter
    def restrict_reenrollment(self, restrict_reenrollment):
        """Sets the restrict_reenrollment of this EnrollmentSettingsV2.


        :param restrict_reenrollment: The restrict_reenrollment of this EnrollmentSettingsV2.  # noqa: E501
        :type restrict_reenrollment: bool
        """

        self._restrict_reenrollment = restrict_reenrollment

    @property
    def flush_location_information(self):
        """Gets the flush_location_information of this EnrollmentSettingsV2.  # noqa: E501


        :return: The flush_location_information of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._flush_location_information

    @flush_location_information.setter
    def flush_location_information(self, flush_location_information):
        """Sets the flush_location_information of this EnrollmentSettingsV2.


        :param flush_location_information: The flush_location_information of this EnrollmentSettingsV2.  # noqa: E501
        :type flush_location_information: bool
        """

        self._flush_location_information = flush_location_information

    @property
    def flush_location_history_information(self):
        """Gets the flush_location_history_information of this EnrollmentSettingsV2.  # noqa: E501


        :return: The flush_location_history_information of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._flush_location_history_information

    @flush_location_history_information.setter
    def flush_location_history_information(self, flush_location_history_information):
        """Sets the flush_location_history_information of this EnrollmentSettingsV2.


        :param flush_location_history_information: The flush_location_history_information of this EnrollmentSettingsV2.  # noqa: E501
        :type flush_location_history_information: bool
        """

        self._flush_location_history_information = flush_location_history_information

    @property
    def flush_policy_history(self):
        """Gets the flush_policy_history of this EnrollmentSettingsV2.  # noqa: E501


        :return: The flush_policy_history of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._flush_policy_history

    @flush_policy_history.setter
    def flush_policy_history(self, flush_policy_history):
        """Sets the flush_policy_history of this EnrollmentSettingsV2.


        :param flush_policy_history: The flush_policy_history of this EnrollmentSettingsV2.  # noqa: E501
        :type flush_policy_history: bool
        """

        self._flush_policy_history = flush_policy_history

    @property
    def flush_extension_attributes(self):
        """Gets the flush_extension_attributes of this EnrollmentSettingsV2.  # noqa: E501


        :return: The flush_extension_attributes of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._flush_extension_attributes

    @flush_extension_attributes.setter
    def flush_extension_attributes(self, flush_extension_attributes):
        """Sets the flush_extension_attributes of this EnrollmentSettingsV2.


        :param flush_extension_attributes: The flush_extension_attributes of this EnrollmentSettingsV2.  # noqa: E501
        :type flush_extension_attributes: bool
        """

        self._flush_extension_attributes = flush_extension_attributes

    @property
    def flush_mdm_commands_on_reenroll(self):
        """Gets the flush_mdm_commands_on_reenroll of this EnrollmentSettingsV2.  # noqa: E501


        :return: The flush_mdm_commands_on_reenroll of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: str
        """
        return self._flush_mdm_commands_on_reenroll

    @flush_mdm_commands_on_reenroll.setter
    def flush_mdm_commands_on_reenroll(self, flush_mdm_commands_on_reenroll):
        """Sets the flush_mdm_commands_on_reenroll of this EnrollmentSettingsV2.


        :param flush_mdm_commands_on_reenroll: The flush_mdm_commands_on_reenroll of this EnrollmentSettingsV2.  # noqa: E501
        :type flush_mdm_commands_on_reenroll: str
        """
        allowed_values = ["DELETE_NOTHING", "DELETE_ERRORS", "DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED", "DELETE_EVERYTHING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flush_mdm_commands_on_reenroll not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `flush_mdm_commands_on_reenroll` ({0}), must be one of {1}"  # noqa: E501
                .format(flush_mdm_commands_on_reenroll, allowed_values)
            )

        self._flush_mdm_commands_on_reenroll = flush_mdm_commands_on_reenroll

    @property
    def mac_os_enterprise_enrollment_enabled(self):
        """Gets the mac_os_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501


        :return: The mac_os_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._mac_os_enterprise_enrollment_enabled

    @mac_os_enterprise_enrollment_enabled.setter
    def mac_os_enterprise_enrollment_enabled(self, mac_os_enterprise_enrollment_enabled):
        """Sets the mac_os_enterprise_enrollment_enabled of this EnrollmentSettingsV2.


        :param mac_os_enterprise_enrollment_enabled: The mac_os_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :type mac_os_enterprise_enrollment_enabled: bool
        """

        self._mac_os_enterprise_enrollment_enabled = mac_os_enterprise_enrollment_enabled

    @property
    def management_username(self):
        """Gets the management_username of this EnrollmentSettingsV2.  # noqa: E501


        :return: The management_username of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: str
        """
        return self._management_username

    @management_username.setter
    def management_username(self, management_username):
        """Sets the management_username of this EnrollmentSettingsV2.


        :param management_username: The management_username of this EnrollmentSettingsV2.  # noqa: E501
        :type management_username: str
        """

        self._management_username = management_username

    @property
    def management_password(self):
        """Gets the management_password of this EnrollmentSettingsV2.  # noqa: E501


        :return: The management_password of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: str
        """
        return self._management_password

    @management_password.setter
    def management_password(self, management_password):
        """Sets the management_password of this EnrollmentSettingsV2.


        :param management_password: The management_password of this EnrollmentSettingsV2.  # noqa: E501
        :type management_password: str
        """

        self._management_password = management_password

    @property
    def management_password_set(self):
        """Gets the management_password_set of this EnrollmentSettingsV2.  # noqa: E501


        :return: The management_password_set of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._management_password_set

    @management_password_set.setter
    def management_password_set(self, management_password_set):
        """Sets the management_password_set of this EnrollmentSettingsV2.


        :param management_password_set: The management_password_set of this EnrollmentSettingsV2.  # noqa: E501
        :type management_password_set: bool
        """

        self._management_password_set = management_password_set

    @property
    def password_type(self):
        """Gets the password_type of this EnrollmentSettingsV2.  # noqa: E501


        :return: The password_type of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: str
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this EnrollmentSettingsV2.


        :param password_type: The password_type of this EnrollmentSettingsV2.  # noqa: E501
        :type password_type: str
        """
        allowed_values = ["STATIC", "RANDOM"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and password_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `password_type` ({0}), must be one of {1}"  # noqa: E501
                .format(password_type, allowed_values)
            )

        self._password_type = password_type

    @property
    def random_password_length(self):
        """Gets the random_password_length of this EnrollmentSettingsV2.  # noqa: E501


        :return: The random_password_length of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: int
        """
        return self._random_password_length

    @random_password_length.setter
    def random_password_length(self, random_password_length):
        """Sets the random_password_length of this EnrollmentSettingsV2.


        :param random_password_length: The random_password_length of this EnrollmentSettingsV2.  # noqa: E501
        :type random_password_length: int
        """

        self._random_password_length = random_password_length

    @property
    def create_management_account(self):
        """Gets the create_management_account of this EnrollmentSettingsV2.  # noqa: E501


        :return: The create_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._create_management_account

    @create_management_account.setter
    def create_management_account(self, create_management_account):
        """Sets the create_management_account of this EnrollmentSettingsV2.


        :param create_management_account: The create_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :type create_management_account: bool
        """

        self._create_management_account = create_management_account

    @property
    def hide_management_account(self):
        """Gets the hide_management_account of this EnrollmentSettingsV2.  # noqa: E501


        :return: The hide_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._hide_management_account

    @hide_management_account.setter
    def hide_management_account(self, hide_management_account):
        """Sets the hide_management_account of this EnrollmentSettingsV2.


        :param hide_management_account: The hide_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :type hide_management_account: bool
        """

        self._hide_management_account = hide_management_account

    @property
    def allow_ssh_only_management_account(self):
        """Gets the allow_ssh_only_management_account of this EnrollmentSettingsV2.  # noqa: E501


        :return: The allow_ssh_only_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_only_management_account

    @allow_ssh_only_management_account.setter
    def allow_ssh_only_management_account(self, allow_ssh_only_management_account):
        """Sets the allow_ssh_only_management_account of this EnrollmentSettingsV2.


        :param allow_ssh_only_management_account: The allow_ssh_only_management_account of this EnrollmentSettingsV2.  # noqa: E501
        :type allow_ssh_only_management_account: bool
        """

        self._allow_ssh_only_management_account = allow_ssh_only_management_account

    @property
    def ensure_ssh_running(self):
        """Gets the ensure_ssh_running of this EnrollmentSettingsV2.  # noqa: E501


        :return: The ensure_ssh_running of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._ensure_ssh_running

    @ensure_ssh_running.setter
    def ensure_ssh_running(self, ensure_ssh_running):
        """Sets the ensure_ssh_running of this EnrollmentSettingsV2.


        :param ensure_ssh_running: The ensure_ssh_running of this EnrollmentSettingsV2.  # noqa: E501
        :type ensure_ssh_running: bool
        """

        self._ensure_ssh_running = ensure_ssh_running

    @property
    def launch_self_service(self):
        """Gets the launch_self_service of this EnrollmentSettingsV2.  # noqa: E501


        :return: The launch_self_service of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._launch_self_service

    @launch_self_service.setter
    def launch_self_service(self, launch_self_service):
        """Sets the launch_self_service of this EnrollmentSettingsV2.


        :param launch_self_service: The launch_self_service of this EnrollmentSettingsV2.  # noqa: E501
        :type launch_self_service: bool
        """

        self._launch_self_service = launch_self_service

    @property
    def sign_quick_add(self):
        """Gets the sign_quick_add of this EnrollmentSettingsV2.  # noqa: E501


        :return: The sign_quick_add of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._sign_quick_add

    @sign_quick_add.setter
    def sign_quick_add(self, sign_quick_add):
        """Sets the sign_quick_add of this EnrollmentSettingsV2.


        :param sign_quick_add: The sign_quick_add of this EnrollmentSettingsV2.  # noqa: E501
        :type sign_quick_add: bool
        """

        self._sign_quick_add = sign_quick_add

    @property
    def developer_certificate_identity(self):
        """Gets the developer_certificate_identity of this EnrollmentSettingsV2.  # noqa: E501


        :return: The developer_certificate_identity of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: CertificateIdentityV2
        """
        return self._developer_certificate_identity

    @developer_certificate_identity.setter
    def developer_certificate_identity(self, developer_certificate_identity):
        """Sets the developer_certificate_identity of this EnrollmentSettingsV2.


        :param developer_certificate_identity: The developer_certificate_identity of this EnrollmentSettingsV2.  # noqa: E501
        :type developer_certificate_identity: CertificateIdentityV2
        """

        self._developer_certificate_identity = developer_certificate_identity

    @property
    def developer_certificate_identity_details(self):
        """Gets the developer_certificate_identity_details of this EnrollmentSettingsV2.  # noqa: E501


        :return: The developer_certificate_identity_details of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: CertificateDetails
        """
        return self._developer_certificate_identity_details

    @developer_certificate_identity_details.setter
    def developer_certificate_identity_details(self, developer_certificate_identity_details):
        """Sets the developer_certificate_identity_details of this EnrollmentSettingsV2.


        :param developer_certificate_identity_details: The developer_certificate_identity_details of this EnrollmentSettingsV2.  # noqa: E501
        :type developer_certificate_identity_details: CertificateDetails
        """

        self._developer_certificate_identity_details = developer_certificate_identity_details

    @property
    def mdm_signing_certificate_details(self):
        """Gets the mdm_signing_certificate_details of this EnrollmentSettingsV2.  # noqa: E501


        :return: The mdm_signing_certificate_details of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: CertificateDetails
        """
        return self._mdm_signing_certificate_details

    @mdm_signing_certificate_details.setter
    def mdm_signing_certificate_details(self, mdm_signing_certificate_details):
        """Sets the mdm_signing_certificate_details of this EnrollmentSettingsV2.


        :param mdm_signing_certificate_details: The mdm_signing_certificate_details of this EnrollmentSettingsV2.  # noqa: E501
        :type mdm_signing_certificate_details: CertificateDetails
        """

        self._mdm_signing_certificate_details = mdm_signing_certificate_details

    @property
    def ios_enterprise_enrollment_enabled(self):
        """Gets the ios_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501


        :return: The ios_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._ios_enterprise_enrollment_enabled

    @ios_enterprise_enrollment_enabled.setter
    def ios_enterprise_enrollment_enabled(self, ios_enterprise_enrollment_enabled):
        """Sets the ios_enterprise_enrollment_enabled of this EnrollmentSettingsV2.


        :param ios_enterprise_enrollment_enabled: The ios_enterprise_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :type ios_enterprise_enrollment_enabled: bool
        """

        self._ios_enterprise_enrollment_enabled = ios_enterprise_enrollment_enabled

    @property
    def ios_personal_enrollment_enabled(self):
        """Gets the ios_personal_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501


        :return: The ios_personal_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: bool
        """
        return self._ios_personal_enrollment_enabled

    @ios_personal_enrollment_enabled.setter
    def ios_personal_enrollment_enabled(self, ios_personal_enrollment_enabled):
        """Sets the ios_personal_enrollment_enabled of this EnrollmentSettingsV2.


        :param ios_personal_enrollment_enabled: The ios_personal_enrollment_enabled of this EnrollmentSettingsV2.  # noqa: E501
        :type ios_personal_enrollment_enabled: bool
        """

        self._ios_personal_enrollment_enabled = ios_personal_enrollment_enabled

    @property
    def personal_device_enrollment_type(self):
        """Gets the personal_device_enrollment_type of this EnrollmentSettingsV2.  # noqa: E501


        :return: The personal_device_enrollment_type of this EnrollmentSettingsV2.  # noqa: E501
        :rtype: str
        """
        return self._personal_device_enrollment_type

    @personal_device_enrollment_type.setter
    def personal_device_enrollment_type(self, personal_device_enrollment_type):
        """Sets the personal_device_enrollment_type of this EnrollmentSettingsV2.


        :param personal_device_enrollment_type: The personal_device_enrollment_type of this EnrollmentSettingsV2.  # noqa: E501
        :type personal_device_enrollment_type: str
        """
        allowed_values = ["USERENROLLMENT", "PERSONALDEVICEPROFILES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and personal_device_enrollment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `personal_device_enrollment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(personal_device_enrollment_type, allowed_values)
            )

        self._personal_device_enrollment_type = personal_device_enrollment_type

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
        if not isinstance(other, EnrollmentSettingsV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrollmentSettingsV2):
            return True

        return self.to_dict() != other.to_dict()
