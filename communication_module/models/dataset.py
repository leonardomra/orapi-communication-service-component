# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from communication_module.models.base_model_ import Model
from communication_module import util


class Dataset(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, label: str=None, file_name: str=None, date_created: datetime=None, date_modified: datetime=None):  # noqa: E501
        """Dataset - a model defined in Swagger

        :param id: The id of this Dataset.  # noqa: E501
        :type id: str
        :param label: The label of this Dataset.  # noqa: E501
        :type label: str
        :param file_name: The file_name of this Dataset.  # noqa: E501
        :type file_name: str
        :param date_created: The date_created of this Dataset.  # noqa: E501
        :type date_created: datetime
        :param date_modified: The date_modified of this Dataset.  # noqa: E501
        :type date_modified: datetime
        """
        self.swagger_types = {
            'id': str,
            'label': str,
            'file_name': str,
            'date_created': datetime,
            'date_modified': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'file_name': 'fileName',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified'
        }
        self._id = id
        self._label = label
        self._file_name = file_name
        self._date_created = date_created
        self._date_modified = date_modified

    @classmethod
    def from_dict(cls, dikt) -> 'Dataset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dataset of this Dataset.  # noqa: E501
        :rtype: Dataset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Dataset.


        :return: The id of this Dataset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Dataset.


        :param id: The id of this Dataset.
        :type id: str
        """

        self._id = id

    @property
    def label(self) -> str:
        """Gets the label of this Dataset.


        :return: The label of this Dataset.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this Dataset.


        :param label: The label of this Dataset.
        :type label: str
        """

        self._label = label

    @property
    def file_name(self) -> str:
        """Gets the file_name of this Dataset.


        :return: The file_name of this Dataset.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """Sets the file_name of this Dataset.


        :param file_name: The file_name of this Dataset.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this Dataset.


        :return: The date_created of this Dataset.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime):
        """Sets the date_created of this Dataset.


        :param date_created: The date_created of this Dataset.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """Gets the date_modified of this Dataset.


        :return: The date_modified of this Dataset.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime):
        """Sets the date_modified of this Dataset.


        :param date_modified: The date_modified of this Dataset.
        :type date_modified: datetime
        """

        self._date_modified = date_modified
