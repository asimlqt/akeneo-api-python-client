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

class InlineResponse20040(object):
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
        'access_token': 'str',
        'expires_in': 'int',
        'token_type': 'str',
        'scope': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'token_type': 'token_type',
        'scope': 'scope',
        'refresh_token': 'refresh_token'
    }

    def __init__(self, access_token=None, expires_in=None, token_type=None, scope=None, refresh_token=None):  # noqa: E501
        """InlineResponse20040 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._expires_in = None
        self._token_type = None
        self._scope = None
        self._refresh_token = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if token_type is not None:
            self.token_type = token_type
        if scope is not None:
            self.scope = scope
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def access_token(self):
        """Gets the access_token of this InlineResponse20040.  # noqa: E501

        Authentication token that should be given in every authenticated request to the API  # noqa: E501

        :return: The access_token of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this InlineResponse20040.

        Authentication token that should be given in every authenticated request to the API  # noqa: E501

        :param access_token: The access_token of this InlineResponse20040.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this InlineResponse20040.  # noqa: E501

        Validity of the token given in seconds, 3600s = 1h by default  # noqa: E501

        :return: The expires_in of this InlineResponse20040.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this InlineResponse20040.

        Validity of the token given in seconds, 3600s = 1h by default  # noqa: E501

        :param expires_in: The expires_in of this InlineResponse20040.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def token_type(self):
        """Gets the token_type of this InlineResponse20040.  # noqa: E501

        Token type, always equal to \"bearer\"  # noqa: E501

        :return: The token_type of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this InlineResponse20040.

        Token type, always equal to \"bearer\"  # noqa: E501

        :param token_type: The token_type of this InlineResponse20040.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

    @property
    def scope(self):
        """Gets the scope of this InlineResponse20040.  # noqa: E501

        Unused, always equal to \"null\"  # noqa: E501

        :return: The scope of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this InlineResponse20040.

        Unused, always equal to \"null\"  # noqa: E501

        :param scope: The scope of this InlineResponse20040.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def refresh_token(self):
        """Gets the refresh_token of this InlineResponse20040.  # noqa: E501

        Use this token when your access token has expired. See <a href=\"/documentation/authentication.html#refresh-an-expired-token\">Refresh an expired token</a> section for more details.  # noqa: E501

        :return: The refresh_token of this InlineResponse20040.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this InlineResponse20040.

        Use this token when your access token has expired. See <a href=\"/documentation/authentication.html#refresh-an-expired-token\">Refresh an expired token</a> section for more details.  # noqa: E501

        :param refresh_token: The refresh_token of this InlineResponse20040.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

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
        if issubclass(InlineResponse20040, dict):
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
        if not isinstance(other, InlineResponse20040):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
