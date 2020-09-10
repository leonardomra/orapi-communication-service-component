# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from communication_module.models.base_model_ import Model
from communication_module import util


class Topic(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, params: object=None):  # noqa: E501
        """Topic - a model defined in Swagger

        :param id: The id of this Topic.  # noqa: E501
        :type id: str
        :param params: The params of this Topic.  # noqa: E501
        :type params: object
        """
        self.swagger_types = {
            'id': str,
            'params': object
        }

        self.attribute_map = {
            'id': 'id',
            'params': 'params'
        }
        self._id = id
        self._params = params

    @classmethod
    def from_dict(cls, dikt) -> 'Topic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Topic of this Topic.  # noqa: E501
        :rtype: Topic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Topic.


        :return: The id of this Topic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Topic.


        :param id: The id of this Topic.
        :type id: str
        """

        self._id = id

    @property
    def params(self) -> object:
        """Gets the params of this Topic.


        :return: The params of this Topic.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params: object):
        """Sets the params of this Topic.


        :param params: The params of this Topic.
        :type params: object
        """

        self._params = params
