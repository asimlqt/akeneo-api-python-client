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

class FamilyCodeVariantsBody(object):
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
        'variant_attribute_sets': 'list[Apirestv1familiesfamilyCodevariantsVariantAttributeSets]',
        'labels': 'Apirestv1familiesfamilyCodevariantsLabels'
    }

    attribute_map = {
        'code': 'code',
        'variant_attribute_sets': 'variant_attribute_sets',
        'labels': 'labels'
    }

    def __init__(self, code=None, variant_attribute_sets=None, labels=None):  # noqa: E501
        """FamilyCodeVariantsBody - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._variant_attribute_sets = None
        self._labels = None
        self.discriminator = None
        self.code = code
        self.variant_attribute_sets = variant_attribute_sets
        if labels is not None:
            self.labels = labels

    @property
    def code(self):
        """Gets the code of this FamilyCodeVariantsBody.  # noqa: E501

        Family variant code  # noqa: E501

        :return: The code of this FamilyCodeVariantsBody.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FamilyCodeVariantsBody.

        Family variant code  # noqa: E501

        :param code: The code of this FamilyCodeVariantsBody.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def variant_attribute_sets(self):
        """Gets the variant_attribute_sets of this FamilyCodeVariantsBody.  # noqa: E501

        Attributes distribution according to the enrichment level  # noqa: E501

        :return: The variant_attribute_sets of this FamilyCodeVariantsBody.  # noqa: E501
        :rtype: list[Apirestv1familiesfamilyCodevariantsVariantAttributeSets]
        """
        return self._variant_attribute_sets

    @variant_attribute_sets.setter
    def variant_attribute_sets(self, variant_attribute_sets):
        """Sets the variant_attribute_sets of this FamilyCodeVariantsBody.

        Attributes distribution according to the enrichment level  # noqa: E501

        :param variant_attribute_sets: The variant_attribute_sets of this FamilyCodeVariantsBody.  # noqa: E501
        :type: list[Apirestv1familiesfamilyCodevariantsVariantAttributeSets]
        """
        if variant_attribute_sets is None:
            raise ValueError("Invalid value for `variant_attribute_sets`, must not be `None`")  # noqa: E501

        self._variant_attribute_sets = variant_attribute_sets

    @property
    def labels(self):
        """Gets the labels of this FamilyCodeVariantsBody.  # noqa: E501


        :return: The labels of this FamilyCodeVariantsBody.  # noqa: E501
        :rtype: Apirestv1familiesfamilyCodevariantsLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this FamilyCodeVariantsBody.


        :param labels: The labels of this FamilyCodeVariantsBody.  # noqa: E501
        :type: Apirestv1familiesfamilyCodevariantsLabels
        """

        self._labels = labels

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
        if issubclass(FamilyCodeVariantsBody, dict):
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
        if not isinstance(other, FamilyCodeVariantsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
