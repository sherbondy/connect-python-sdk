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


class BatchUpsertCatalogObjectsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, objects=None, updated_at=None, id_mappings=None):
        """
        BatchUpsertCatalogObjectsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[Error]',
            'objects': 'list[CatalogObject]',
            'updated_at': 'str',
            'id_mappings': 'list[CatalogIdMapping]'
        }

        self.attribute_map = {
            'errors': 'errors',
            'objects': 'objects',
            'updated_at': 'updated_at',
            'id_mappings': 'id_mappings'
        }

        self._errors = errors
        self._objects = objects
        self._updated_at = updated_at
        self._id_mappings = id_mappings

    @property
    def errors(self):
        """
        Gets the errors of this BatchUpsertCatalogObjectsResponse.
        The set of [Error](#type-error)s encountered.

        :return: The errors of this BatchUpsertCatalogObjectsResponse.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this BatchUpsertCatalogObjectsResponse.
        The set of [Error](#type-error)s encountered.

        :param errors: The errors of this BatchUpsertCatalogObjectsResponse.
        :type: list[Error]
        """

        self._errors = errors

    @property
    def objects(self):
        """
        Gets the objects of this BatchUpsertCatalogObjectsResponse.
        The created [CatalogObject](#type-catalogobject)s

        :return: The objects of this BatchUpsertCatalogObjectsResponse.
        :rtype: list[CatalogObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this BatchUpsertCatalogObjectsResponse.
        The created [CatalogObject](#type-catalogobject)s

        :param objects: The objects of this BatchUpsertCatalogObjectsResponse.
        :type: list[CatalogObject]
        """

        self._objects = objects

    @property
    def updated_at(self):
        """
        Gets the updated_at of this BatchUpsertCatalogObjectsResponse.
        The database [timestamp](#workingwithdates) of this update in RFC 3339 format, e.g., \"2016-09-04T23:59:33.123Z\".

        :return: The updated_at of this BatchUpsertCatalogObjectsResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this BatchUpsertCatalogObjectsResponse.
        The database [timestamp](#workingwithdates) of this update in RFC 3339 format, e.g., \"2016-09-04T23:59:33.123Z\".

        :param updated_at: The updated_at of this BatchUpsertCatalogObjectsResponse.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def id_mappings(self):
        """
        Gets the id_mappings of this BatchUpsertCatalogObjectsResponse.
        The mapping between client and server IDs for this Upsert.

        :return: The id_mappings of this BatchUpsertCatalogObjectsResponse.
        :rtype: list[CatalogIdMapping]
        """
        return self._id_mappings

    @id_mappings.setter
    def id_mappings(self, id_mappings):
        """
        Sets the id_mappings of this BatchUpsertCatalogObjectsResponse.
        The mapping between client and server IDs for this Upsert.

        :param id_mappings: The id_mappings of this BatchUpsertCatalogObjectsResponse.
        :type: list[CatalogIdMapping]
        """

        self._id_mappings = id_mappings

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
