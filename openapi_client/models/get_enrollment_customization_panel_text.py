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


class GetEnrollmentCustomizationPanelText(object):
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
        'rank': 'int',
        'body': 'str',
        'subtext': 'str',
        'title': 'str',
        'back_button_text': 'str',
        'continue_button_text': 'str',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'rank': 'rank',
        'body': 'body',
        'subtext': 'subtext',
        'title': 'title',
        'back_button_text': 'backButtonText',
        'continue_button_text': 'continueButtonText',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, display_name=None, rank=None, body=None, subtext=None, title=None, back_button_text=None, continue_button_text=None, id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """GetEnrollmentCustomizationPanelText - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._rank = None
        self._body = None
        self._subtext = None
        self._title = None
        self._back_button_text = None
        self._continue_button_text = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.display_name = display_name
        self.rank = rank
        self.body = body
        if subtext is not None:
            self.subtext = subtext
        self.title = title
        self.back_button_text = back_button_text
        self.continue_button_text = continue_button_text
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def display_name(self):
        """Gets the display_name of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The display_name of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetEnrollmentCustomizationPanelText.


        :param display_name: The display_name of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def rank(self):
        """Gets the rank of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The rank of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this GetEnrollmentCustomizationPanelText.


        :param rank: The rank of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type rank: int
        """
        if self.local_vars_configuration.client_side_validation and rank is None:  # noqa: E501
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def body(self):
        """Gets the body of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The body of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this GetEnrollmentCustomizationPanelText.


        :param body: The body of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type body: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def subtext(self):
        """Gets the subtext of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The subtext of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._subtext

    @subtext.setter
    def subtext(self, subtext):
        """Sets the subtext of this GetEnrollmentCustomizationPanelText.


        :param subtext: The subtext of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type subtext: str
        """

        self._subtext = subtext

    @property
    def title(self):
        """Gets the title of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The title of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetEnrollmentCustomizationPanelText.


        :param title: The title of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def back_button_text(self):
        """Gets the back_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The back_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._back_button_text

    @back_button_text.setter
    def back_button_text(self, back_button_text):
        """Sets the back_button_text of this GetEnrollmentCustomizationPanelText.


        :param back_button_text: The back_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type back_button_text: str
        """
        if self.local_vars_configuration.client_side_validation and back_button_text is None:  # noqa: E501
            raise ValueError("Invalid value for `back_button_text`, must not be `None`")  # noqa: E501

        self._back_button_text = back_button_text

    @property
    def continue_button_text(self):
        """Gets the continue_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The continue_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._continue_button_text

    @continue_button_text.setter
    def continue_button_text(self, continue_button_text):
        """Sets the continue_button_text of this GetEnrollmentCustomizationPanelText.


        :param continue_button_text: The continue_button_text of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type continue_button_text: str
        """
        if self.local_vars_configuration.client_side_validation and continue_button_text is None:  # noqa: E501
            raise ValueError("Invalid value for `continue_button_text`, must not be `None`")  # noqa: E501

        self._continue_button_text = continue_button_text

    @property
    def id(self):
        """Gets the id of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The id of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetEnrollmentCustomizationPanelText.


        :param id: The id of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GetEnrollmentCustomizationPanelText.  # noqa: E501


        :return: The type of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetEnrollmentCustomizationPanelText.


        :param type: The type of this GetEnrollmentCustomizationPanelText.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, GetEnrollmentCustomizationPanelText):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetEnrollmentCustomizationPanelText):
            return True

        return self.to_dict() != other.to_dict()
