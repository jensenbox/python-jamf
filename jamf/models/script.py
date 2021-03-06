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


class Script(object):
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
        'info': 'str',
        'notes': 'str',
        'priority': 'str',
        'category_id': 'str',
        'category_name': 'str',
        'parameter4': 'str',
        'parameter5': 'str',
        'parameter6': 'str',
        'parameter7': 'str',
        'parameter8': 'str',
        'parameter9': 'str',
        'parameter10': 'str',
        'parameter11': 'str',
        'os_requirements': 'str',
        'script_contents': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'info': 'info',
        'notes': 'notes',
        'priority': 'priority',
        'category_id': 'categoryId',
        'category_name': 'categoryName',
        'parameter4': 'parameter4',
        'parameter5': 'parameter5',
        'parameter6': 'parameter6',
        'parameter7': 'parameter7',
        'parameter8': 'parameter8',
        'parameter9': 'parameter9',
        'parameter10': 'parameter10',
        'parameter11': 'parameter11',
        'os_requirements': 'osRequirements',
        'script_contents': 'scriptContents'
    }

    def __init__(self, id=None, name=None, info=None, notes=None, priority=None, category_id=None, category_name=None, parameter4=None, parameter5=None, parameter6=None, parameter7=None, parameter8=None, parameter9=None, parameter10=None, parameter11=None, os_requirements=None, script_contents=None, local_vars_configuration=None):  # noqa: E501
        """Script - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._info = None
        self._notes = None
        self._priority = None
        self._category_id = None
        self._category_name = None
        self._parameter4 = None
        self._parameter5 = None
        self._parameter6 = None
        self._parameter7 = None
        self._parameter8 = None
        self._parameter9 = None
        self._parameter10 = None
        self._parameter11 = None
        self._os_requirements = None
        self._script_contents = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if info is not None:
            self.info = info
        if notes is not None:
            self.notes = notes
        if priority is not None:
            self.priority = priority
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if parameter4 is not None:
            self.parameter4 = parameter4
        if parameter5 is not None:
            self.parameter5 = parameter5
        if parameter6 is not None:
            self.parameter6 = parameter6
        if parameter7 is not None:
            self.parameter7 = parameter7
        if parameter8 is not None:
            self.parameter8 = parameter8
        if parameter9 is not None:
            self.parameter9 = parameter9
        if parameter10 is not None:
            self.parameter10 = parameter10
        if parameter11 is not None:
            self.parameter11 = parameter11
        if os_requirements is not None:
            self.os_requirements = os_requirements
        if script_contents is not None:
            self.script_contents = script_contents

    @property
    def id(self):
        """Gets the id of this Script.  # noqa: E501


        :return: The id of this Script.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Script.


        :param id: The id of this Script.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Script.  # noqa: E501


        :return: The name of this Script.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Script.


        :param name: The name of this Script.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def info(self):
        """Gets the info of this Script.  # noqa: E501


        :return: The info of this Script.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Script.


        :param info: The info of this Script.  # noqa: E501
        :type info: str
        """

        self._info = info

    @property
    def notes(self):
        """Gets the notes of this Script.  # noqa: E501


        :return: The notes of this Script.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Script.


        :param notes: The notes of this Script.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def priority(self):
        """Gets the priority of this Script.  # noqa: E501


        :return: The priority of this Script.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Script.


        :param priority: The priority of this Script.  # noqa: E501
        :type priority: str
        """
        allowed_values = ["BEFORE", "AFTER", "AT_REBOOT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and priority not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def category_id(self):
        """Gets the category_id of this Script.  # noqa: E501


        :return: The category_id of this Script.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Script.


        :param category_id: The category_id of this Script.  # noqa: E501
        :type category_id: str
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this Script.  # noqa: E501


        :return: The category_name of this Script.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this Script.


        :param category_name: The category_name of this Script.  # noqa: E501
        :type category_name: str
        """

        self._category_name = category_name

    @property
    def parameter4(self):
        """Gets the parameter4 of this Script.  # noqa: E501


        :return: The parameter4 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter4

    @parameter4.setter
    def parameter4(self, parameter4):
        """Sets the parameter4 of this Script.


        :param parameter4: The parameter4 of this Script.  # noqa: E501
        :type parameter4: str
        """

        self._parameter4 = parameter4

    @property
    def parameter5(self):
        """Gets the parameter5 of this Script.  # noqa: E501


        :return: The parameter5 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter5

    @parameter5.setter
    def parameter5(self, parameter5):
        """Sets the parameter5 of this Script.


        :param parameter5: The parameter5 of this Script.  # noqa: E501
        :type parameter5: str
        """

        self._parameter5 = parameter5

    @property
    def parameter6(self):
        """Gets the parameter6 of this Script.  # noqa: E501


        :return: The parameter6 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter6

    @parameter6.setter
    def parameter6(self, parameter6):
        """Sets the parameter6 of this Script.


        :param parameter6: The parameter6 of this Script.  # noqa: E501
        :type parameter6: str
        """

        self._parameter6 = parameter6

    @property
    def parameter7(self):
        """Gets the parameter7 of this Script.  # noqa: E501


        :return: The parameter7 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter7

    @parameter7.setter
    def parameter7(self, parameter7):
        """Sets the parameter7 of this Script.


        :param parameter7: The parameter7 of this Script.  # noqa: E501
        :type parameter7: str
        """

        self._parameter7 = parameter7

    @property
    def parameter8(self):
        """Gets the parameter8 of this Script.  # noqa: E501


        :return: The parameter8 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter8

    @parameter8.setter
    def parameter8(self, parameter8):
        """Sets the parameter8 of this Script.


        :param parameter8: The parameter8 of this Script.  # noqa: E501
        :type parameter8: str
        """

        self._parameter8 = parameter8

    @property
    def parameter9(self):
        """Gets the parameter9 of this Script.  # noqa: E501


        :return: The parameter9 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter9

    @parameter9.setter
    def parameter9(self, parameter9):
        """Sets the parameter9 of this Script.


        :param parameter9: The parameter9 of this Script.  # noqa: E501
        :type parameter9: str
        """

        self._parameter9 = parameter9

    @property
    def parameter10(self):
        """Gets the parameter10 of this Script.  # noqa: E501


        :return: The parameter10 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter10

    @parameter10.setter
    def parameter10(self, parameter10):
        """Sets the parameter10 of this Script.


        :param parameter10: The parameter10 of this Script.  # noqa: E501
        :type parameter10: str
        """

        self._parameter10 = parameter10

    @property
    def parameter11(self):
        """Gets the parameter11 of this Script.  # noqa: E501


        :return: The parameter11 of this Script.  # noqa: E501
        :rtype: str
        """
        return self._parameter11

    @parameter11.setter
    def parameter11(self, parameter11):
        """Sets the parameter11 of this Script.


        :param parameter11: The parameter11 of this Script.  # noqa: E501
        :type parameter11: str
        """

        self._parameter11 = parameter11

    @property
    def os_requirements(self):
        """Gets the os_requirements of this Script.  # noqa: E501


        :return: The os_requirements of this Script.  # noqa: E501
        :rtype: str
        """
        return self._os_requirements

    @os_requirements.setter
    def os_requirements(self, os_requirements):
        """Sets the os_requirements of this Script.


        :param os_requirements: The os_requirements of this Script.  # noqa: E501
        :type os_requirements: str
        """

        self._os_requirements = os_requirements

    @property
    def script_contents(self):
        """Gets the script_contents of this Script.  # noqa: E501


        :return: The script_contents of this Script.  # noqa: E501
        :rtype: str
        """
        return self._script_contents

    @script_contents.setter
    def script_contents(self, script_contents):
        """Sets the script_contents of this Script.


        :param script_contents: The script_contents of this Script.  # noqa: E501
        :type script_contents: str
        """

        self._script_contents = script_contents

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
        if not isinstance(other, Script):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Script):
            return True

        return self.to_dict() != other.to_dict()
