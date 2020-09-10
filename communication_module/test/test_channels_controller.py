# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from communication_module.models.channel import Channel  # noqa: E501
from communication_module.models.message import Message  # noqa: E501
from communication_module.test import BaseTestCase


class TestChannelsController(BaseTestCase):
    """ChannelsController integration test stubs"""

    def test_communication_channels_get(self):
        """Test case for communication_channels_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_id_delete(self):
        """Test case for communication_channels_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_id_get(self):
        """Test case for communication_channels_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_id_messages_get(self):
        """Test case for communication_channels_id_messages_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels/{id}/messages'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_id_messages_post(self):
        """Test case for communication_channels_id_messages_post

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels/{id}/messages'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_id_put(self):
        """Test case for communication_channels_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_channels_post(self):
        """Test case for communication_channels_post

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/channels',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_messages_id_broadcast_get(self):
        """Test case for communication_messages_id_broadcast_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/messages/{id}/broadcast'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_messages_id_delete(self):
        """Test case for communication_messages_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/messages/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_messages_id_get(self):
        """Test case for communication_messages_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/messages/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_messages_id_put(self):
        """Test case for communication_messages_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/messages/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
