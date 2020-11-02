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


class StartupStatus(object):
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
        'step': 'str',
        'step_code': 'str',
        'step_param': 'str',
        'percentage': 'int',
        'warning': 'str',
        'warning_code': 'str',
        'warning_param': 'str',
        'error': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'step': 'step',
        'step_code': 'stepCode',
        'step_param': 'stepParam',
        'percentage': 'percentage',
        'warning': 'warning',
        'warning_code': 'warningCode',
        'warning_param': 'warningParam',
        'error': 'error',
        'error_code': 'errorCode'
    }

    def __init__(self, step=None, step_code=None, step_param=None, percentage=None, warning=None, warning_code=None, warning_param=None, error=None, error_code=None, local_vars_configuration=None):  # noqa: E501
        """StartupStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._step = None
        self._step_code = None
        self._step_param = None
        self._percentage = None
        self._warning = None
        self._warning_code = None
        self._warning_param = None
        self._error = None
        self._error_code = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if step_code is not None:
            self.step_code = step_code
        if step_param is not None:
            self.step_param = step_param
        if percentage is not None:
            self.percentage = percentage
        if warning is not None:
            self.warning = warning
        if warning_code is not None:
            self.warning_code = warning_code
        if warning_param is not None:
            self.warning_param = warning_param
        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code

    @property
    def step(self):
        """Gets the step of this StartupStatus.  # noqa: E501


        :return: The step of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this StartupStatus.


        :param step: The step of this StartupStatus.  # noqa: E501
        :type step: str
        """

        self._step = step

    @property
    def step_code(self):
        """Gets the step_code of this StartupStatus.  # noqa: E501


        :return: The step_code of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._step_code

    @step_code.setter
    def step_code(self, step_code):
        """Sets the step_code of this StartupStatus.


        :param step_code: The step_code of this StartupStatus.  # noqa: E501
        :type step_code: str
        """
        allowed_values = ["SERVER_INIT_START", "SERVER_INIT_ANALYZING_WEBAPP", "SERVER_INIT_POPULATING_NAVIGATION", "SERVER_INIT_POPULATING_OBJECTS", "SERVER_INIT_INITIALIZING_OBJ", "SERVER_INIT_VERIFYING_CACHE", "SERVER_INIT_INITIALIZING_CHANGE_MANAGEMENT", "SERVER_INIT_INITIALIZING_COMMUNICATION_SYSTEM", "SERVER_INIT_INITIALIZING_MDM_QUEUE_MONITOR", "SERVER_INIT_CALCULATING_SMART_GROUPS", "SERVER_INIT_DB_SCHEMA_COMPARE", "SERVER_INIT_DB_TABLE_CHECK_FOR_RENAME", "SERVER_INIT_DB_TABLE_ALTER", "SERVER_INIT_DB_TABLE_ANALYZING", "SERVER_INIT_DB_TABLE_CREATE", "SERVER_INIT_DB_TABLE_DROP", "SERVER_INIT_DB_TABLE_RENAME", "SERVER_INIT_DB_COLUMN_RENAME", "SERVER_INIT_DB_COLUMN_ENCODING_CHANGE_STEP_1", "SERVER_INIT_DB_COLUMN_ENCODING_CHANGE_STEP_2", "SERVER_INIT_DB_COLUMN_ENCODING_CHANGE_STEP_3", "SERVER_INIT_DB_UPGRADE_CHECK", "SERVER_INIT_DB_UPGRADE_COMPLETE", "SERVER_INIT_SS_GENERATE_NOTIFICATIONS", "SERVER_INIT_SS_GENERATE_NOTIFICATIONS_STATUS", "SERVER_INIT_SS_GENERATE_NOTIFICATIONS_FINALIZE", "SERVER_INIT_PKI_MIGRATION_DONE", "SERVER_INIT_PKI_MIGRATION_STATUS", "SERVER_INIT_MEMCACHED_ENDPOINTS_CHECK", "SERVER_INIT_CACHE_FLUSHING", "SERVER_INIT_COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and step_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `step_code` ({0}), must be one of {1}"  # noqa: E501
                .format(step_code, allowed_values)
            )

        self._step_code = step_code

    @property
    def step_param(self):
        """Gets the step_param of this StartupStatus.  # noqa: E501


        :return: The step_param of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._step_param

    @step_param.setter
    def step_param(self, step_param):
        """Sets the step_param of this StartupStatus.


        :param step_param: The step_param of this StartupStatus.  # noqa: E501
        :type step_param: str
        """

        self._step_param = step_param

    @property
    def percentage(self):
        """Gets the percentage of this StartupStatus.  # noqa: E501


        :return: The percentage of this StartupStatus.  # noqa: E501
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this StartupStatus.


        :param percentage: The percentage of this StartupStatus.  # noqa: E501
        :type percentage: int
        """

        self._percentage = percentage

    @property
    def warning(self):
        """Gets the warning of this StartupStatus.  # noqa: E501


        :return: The warning of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this StartupStatus.


        :param warning: The warning of this StartupStatus.  # noqa: E501
        :type warning: str
        """

        self._warning = warning

    @property
    def warning_code(self):
        """Gets the warning_code of this StartupStatus.  # noqa: E501


        :return: The warning_code of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, warning_code):
        """Sets the warning_code of this StartupStatus.


        :param warning_code: The warning_code of this StartupStatus.  # noqa: E501
        :type warning_code: str
        """
        allowed_values = ["SERVER_INIT_WARNING_DB_TABLE_ENCODING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and warning_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `warning_code` ({0}), must be one of {1}"  # noqa: E501
                .format(warning_code, allowed_values)
            )

        self._warning_code = warning_code

    @property
    def warning_param(self):
        """Gets the warning_param of this StartupStatus.  # noqa: E501


        :return: The warning_param of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._warning_param

    @warning_param.setter
    def warning_param(self, warning_param):
        """Sets the warning_param of this StartupStatus.


        :param warning_param: The warning_param of this StartupStatus.  # noqa: E501
        :type warning_param: str
        """

        self._warning_param = warning_param

    @property
    def error(self):
        """Gets the error of this StartupStatus.  # noqa: E501


        :return: The error of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StartupStatus.


        :param error: The error of this StartupStatus.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this StartupStatus.  # noqa: E501


        :return: The error_code of this StartupStatus.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StartupStatus.


        :param error_code: The error_code of this StartupStatus.  # noqa: E501
        :type error_code: str
        """
        allowed_values = ["CACHE_CONFIGURATION_ERROR", "SECONDARY_NODE_STARTUP_ERROR", "MORE_THAN_ONE_CLUSTER_SETTINGS_ERROR", "PRIMARY_NODE_NOT_SET_ERROR", "DATABASE_ERROR", "DATABASE_PASSWORD_MISSING", "EHCACHE_ERROR", "FLAG_INITIALIZATION_FAILED", "MEMCACHED_ERROR", "DATABASE_MYISAM_ERROR", "OLD_VERSION_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and error_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

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
        if not isinstance(other, StartupStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StartupStatus):
            return True

        return self.to_dict() != other.to_dict()