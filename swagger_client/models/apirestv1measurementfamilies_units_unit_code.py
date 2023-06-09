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

class Apirestv1measurementfamiliesUnitsUnitCode(object):
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
        'code': 'str',
        'labels': 'Apirestv1measurementfamiliesUnitsUnitCodeLabels',
        'convert_from_standard': 'list[Apirestv1measurementfamiliesUnitsUnitCodeConvertFromStandard]',
        'symbol': 'str'
    }

    attribute_map = {
        'code': 'code',
        'labels': 'labels',
        'convert_from_standard': 'convert_from_standard',
        'symbol': 'symbol'
    }

    def __init__(self, code=None, labels=None, convert_from_standard=None, symbol=None):  # noqa: E501
        """Apirestv1measurementfamiliesUnitsUnitCode - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._labels = None
        self._convert_from_standard = None
        self._symbol = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if labels is not None:
            self.labels = labels
        if convert_from_standard is not None:
            self.convert_from_standard = convert_from_standard
        if symbol is not None:
            self.symbol = symbol

    @property
    def code(self):
        """Gets the code of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501

        Measurement unit code. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :return: The code of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Apirestv1measurementfamiliesUnitsUnitCode.

        Measurement unit code. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :param code: The code of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def labels(self):
        """Gets the labels of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501


        :return: The labels of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :rtype: Apirestv1measurementfamiliesUnitsUnitCodeLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Apirestv1measurementfamiliesUnitsUnitCode.


        :param labels: The labels of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :type: Apirestv1measurementfamiliesUnitsUnitCodeLabels
        """

        self._labels = labels

    @property
    def convert_from_standard(self):
        """Gets the convert_from_standard of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501

        Calculation to convert the unit from the standard unit. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :return: The convert_from_standard of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :rtype: list[Apirestv1measurementfamiliesUnitsUnitCodeConvertFromStandard]
        """
        return self._convert_from_standard

    @convert_from_standard.setter
    def convert_from_standard(self, convert_from_standard):
        """Sets the convert_from_standard of this Apirestv1measurementfamiliesUnitsUnitCode.

        Calculation to convert the unit from the standard unit. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :param convert_from_standard: The convert_from_standard of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :type: list[Apirestv1measurementfamiliesUnitsUnitCodeConvertFromStandard]
        """

        self._convert_from_standard = convert_from_standard

    @property
    def symbol(self):
        """Gets the symbol of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501

        Measurement unit symbol. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :return: The symbol of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Apirestv1measurementfamiliesUnitsUnitCode.

        Measurement unit symbol. More details <a href='/concepts/target-market-settings.html#focus-on-the-units'>here</a>.  # noqa: E501

        :param symbol: The symbol of this Apirestv1measurementfamiliesUnitsUnitCode.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

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
        if issubclass(Apirestv1measurementfamiliesUnitsUnitCode, dict):
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
        if not isinstance(other, Apirestv1measurementfamiliesUnitsUnitCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
