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

class Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts(object):
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
        'identifier': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'identifier': 'identifier',
        'quantity': 'quantity'
    }

    def __init__(self, identifier=None, quantity=None):  # noqa: E501
        """Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._quantity = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if quantity is not None:
            self.quantity = quantity

    @property
    def identifier(self):
        """Gets the identifier of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501


        :return: The identifier of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.


        :param identifier: The identifier of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def quantity(self):
        """Gets the quantity of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501


        :return: The quantity of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.


        :param quantity: The quantity of this Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts, dict):
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
        if not isinstance(other, Apirestv1productsQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
