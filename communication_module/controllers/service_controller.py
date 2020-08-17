import connexion
import six

from communication_module.models.health import Health  # noqa: E501
from communication_module import util

from flask import jsonify

def health_get():  # noqa: E501
    """health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    response = {
        'status' : 'Communication Service Component is up!'
    }
    print('Heatlh check executed.', flush=True)
    return jsonify(response)
