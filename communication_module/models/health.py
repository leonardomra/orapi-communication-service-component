# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from communication_module.models.base_model_ import Model
#from communication_module.models.object import Object  # noqa: F401,E501
from communication_module import util


class Health(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status: {}=None):  # noqa: E501
        """Health - a model defined in Swagger

        :param status: The status of this Health.  # noqa: E501
        :type status: Object
        """
        self.swagger_types = {
            'status': Object
        }

        self.attribute_map = {
            'status': 'status'
        }
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Health':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Health of this Health.  # noqa: E501
        :rtype: Health
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> {}:
        """Gets the status of this Health.


        :return: The status of this Health.
        :rtype: Object
        """
        return self._status

    @status.setter
    def status(self, status: {}):
        """Sets the status of this Health.


        :param status: The status of this Health.
        :type status: Object
        """

        self._status = status
