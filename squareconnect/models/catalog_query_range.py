# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class CatalogQueryRange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attribute_name=None, attribute_min_value=None, attribute_max_value=None):
        """
        CatalogQueryRange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_min_value': 'int',
            'attribute_max_value': 'int'
        }

        self.attribute_map = {
            'attribute_name': 'attribute_name',
            'attribute_min_value': 'attribute_min_value',
            'attribute_max_value': 'attribute_max_value'
        }

        self._attribute_name = attribute_name
        self._attribute_min_value = attribute_min_value
        self._attribute_max_value = attribute_max_value

    @property
    def attribute_name(self):
        """
        Gets the attribute_name of this CatalogQueryRange.
        The name of the attribute to be searched.

        :return: The attribute_name of this CatalogQueryRange.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this CatalogQueryRange.
        The name of the attribute to be searched.

        :param attribute_name: The attribute_name of this CatalogQueryRange.
        :type: str
        """

        if not attribute_name:
            raise ValueError("Invalid value for `attribute_name`, must not be `None`")
        if len(attribute_name) < 1:
            raise ValueError("Invalid value for `attribute_name`, length must be greater than or equal to `1`")

        self._attribute_name = attribute_name

    @property
    def attribute_min_value(self):
        """
        Gets the attribute_min_value of this CatalogQueryRange.
        The desired minimum value for the search attribute (inclusive).

        :return: The attribute_min_value of this CatalogQueryRange.
        :rtype: int
        """
        return self._attribute_min_value

    @attribute_min_value.setter
    def attribute_min_value(self, attribute_min_value):
        """
        Sets the attribute_min_value of this CatalogQueryRange.
        The desired minimum value for the search attribute (inclusive).

        :param attribute_min_value: The attribute_min_value of this CatalogQueryRange.
        :type: int
        """

        self._attribute_min_value = attribute_min_value

    @property
    def attribute_max_value(self):
        """
        Gets the attribute_max_value of this CatalogQueryRange.
        The desired maximum value for the search attribute (inclusive).

        :return: The attribute_max_value of this CatalogQueryRange.
        :rtype: int
        """
        return self._attribute_max_value

    @attribute_max_value.setter
    def attribute_max_value(self, attribute_max_value):
        """
        Sets the attribute_max_value of this CatalogQueryRange.
        The desired maximum value for the search attribute (inclusive).

        :param attribute_max_value: The attribute_max_value of this CatalogQueryRange.
        :type: int
        """

        self._attribute_max_value = attribute_max_value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
