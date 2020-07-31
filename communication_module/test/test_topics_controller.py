# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from communication_module.models.event import Event  # noqa: E501
from communication_module.models.topic import Topic  # noqa: E501
from communication_module.test import BaseTestCase


class TestTopicsController(BaseTestCase):
    """TopicsController integration test stubs"""

    def test_communication_events_id_broadcast_get(self):
        """Test case for communication_events_id_broadcast_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/events/{id}/broadcast'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_events_id_delete(self):
        """Test case for communication_events_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/events/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_events_id_get(self):
        """Test case for communication_events_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/events/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_events_id_put(self):
        """Test case for communication_events_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/events/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_events_post(self):
        """Test case for communication_events_post

        
        """
        body = 'body_example'
        headers = [('x_amz_sns_message_type', 'x_amz_sns_message_type_example'),
                   ('x_amz_sns_message_id', 'x_amz_sns_message_id_example'),
                   ('x_amz_sns_topic_arn', 'x_amz_sns_topic_arn_example'),
                   ('x_amz_sns_subscription_arn', 'x_amz_sns_subscription_arn_example')]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/events',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_get(self):
        """Test case for communication_topics_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_id_delete(self):
        """Test case for communication_topics_id_delete

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_id_events_get(self):
        """Test case for communication_topics_id_events_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics/{id}/events'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_id_events_post(self):
        """Test case for communication_topics_id_events_post

        
        """
        headers = [('kind', 'kind_example'),
                   ('job_id', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics/{id}/events'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_id_get(self):
        """Test case for communication_topics_id_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_id_put(self):
        """Test case for communication_topics_id_put

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_communication_topics_post(self):
        """Test case for communication_topics_post

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/communication/topics',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
