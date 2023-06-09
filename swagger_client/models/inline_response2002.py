# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2002(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'line': 'int',
        'uuid': 'str',
        'status_code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'line': 'line',
        'uuid': 'uuid',
        'status_code': 'status_code',
        'message': 'message'
    }

    def __init__(self, line=None, uuid=None, status_code=None, message=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._line = None
        self._uuid = None
        self._status_code = None
        self._message = None
        self.discriminator = None
        if line is not None:
            self.line = line
        if uuid is not None:
            self.uuid = uuid
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message

    @property
    def line(self):
        """Gets the line of this InlineResponse2002.  # noqa: E501

        Line number  # noqa: E501

        :return: The line of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this InlineResponse2002.

        Line number  # noqa: E501

        :param line: The line of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._line = line

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse2002.  # noqa: E501

        Product uuid  # noqa: E501

        :return: The uuid of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse2002.

        Product uuid  # noqa: E501

        :param uuid: The uuid of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse2002.  # noqa: E501

        HTTP status code, see <a href=\"/documentation/responses.html#client-errors\">Client errors</a> to understand the meaning of each code  # noqa: E501

        :return: The status_code of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse2002.

        HTTP status code, see <a href=\"/documentation/responses.html#client-errors\">Client errors</a> to understand the meaning of each code  # noqa: E501

        :param status_code: The status_code of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def message(self):
        """Gets the message of this InlineResponse2002.  # noqa: E501

        Message explaining the error  # noqa: E501

        :return: The message of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse2002.

        Message explaining the error  # noqa: E501

        :param message: The message of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2002, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
