# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from communication_module.models.item import Item  # noqa: E501
from communication_module.models.queue import Queue  # noqa: E501
from communication_module.test import BaseTestCase


class TestQueuesController(BaseTestCase):
    """QueuesController integration test stubs"""

    def test_communication_items_id_delete(self):
        """Test case for communication_items_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/items/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_items_id_get(self):
        """Test case for communication_items_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/items/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_items_id_put(self):
        """Test case for communication_items_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/items/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_get(self):
        """Test case for communication_queues_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_id_delete(self):
        """Test case for communication_queues_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_id_get(self):
        """Test case for communication_queues_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_id_items_get(self):
        """Test case for communication_queues_id_items_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues/{id}/items'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_id_items_post(self):
        """Test case for communication_queues_id_items_post

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues/{id}/items'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_id_put(self):
        """Test case for communication_queues_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_queues_post(self):
        """Test case for communication_queues_post

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/queues',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
