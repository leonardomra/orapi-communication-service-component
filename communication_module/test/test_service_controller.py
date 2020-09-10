# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from communication_module.models.health import Health  # noqa: E501
from communication_module.test import BaseTestCase


class TestServiceController(BaseTestCase):
    """ServiceController integration test stubs"""

    def test_health_get(self):
        """Test case for health_get

        
        """
        response = self.client.open(
            '/OR-API/job-api/1.0.0/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
