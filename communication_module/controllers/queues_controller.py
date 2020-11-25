import connexion
import six
import os
import json
from communication_module.models.item import Item  # noqa: E501
from communication_module.models.queue import Queue  # noqa: E501
from communication_module import util
from orcommunicator import ORCommunicator
from ordbhandler import MySQLHandler

#db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])
orcomm = ORCommunicator(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])

def communication_items_id_delete(id):  # noqa: E501
    """communication_items_id_delete

    Remove queue item. # noqa: E501

    :param id: Id of item.
    :type id: 

    :rtype: Item
    """
    return 'do some magic!'


def communication_items_id_get(id):  # noqa: E501
    """communication_items_id_get

    Get information about a queue item. # noqa: E501

    :param id: Id of item.
    :type id: 

    :rtype: Item
    """
    return 'do some magic!'


def communication_items_id_put(id):  # noqa: E501
    """communication_items_id_put

    Change metadata of queue item. # noqa: E501

    :param id: Id of item.
    :type id: 

    :rtype: Item
    """
    return 'do some magic!'


def communication_queues_get(limit=None):  # noqa: E501
    """communication_queues_get

    Obtain information about queues. # noqa: E501

    :param limit: The amount of queues to be returned.
    :type limit: int

    :rtype: List[Queue]
    """
    return 'do some magic!'


def communication_queues_id_delete(id):  # noqa: E501
    """communication_queues_id_delete

    Remove a queue. # noqa: E501

    :param id: Id of queue.
    :type id: 

    :rtype: Queue
    """
    return 'do some magic!'


def communication_queues_id_get(id):  # noqa: E501
    """communication_queues_id_get

    Obtain information about a queue. # noqa: E501

    :param id: Id of queue.
    :type id: 

    :rtype: Queue
    """
    return 'do some magic!'


def communication_queues_id_items_get(id_=None, limit=None):  # noqa: E501
    """communication_queues_id_items_get

    Obtain information about queue items. # noqa: E501

    :param id: Id of queue.
    :type id: 
    :param limit: The amount of queue items to be returned.
    :type limit: int

    :rtype: List[Item]
    """
    queue = Queue()
    queue.id = id_
    queue.params = { 'limit': limit }
    items = orcomm.itemsForQueue(os.environ['TRAIN_SQS_QUEUE_NAME'], os.environ['TRAIN_SQS_QUEUE_ARN'], ['jobId', 'jobStatus', 'jobTask', 'order'], queue.params['limit'], False)
    response = []
    for item in items:
        response.append(json.dumps(item.summarize()))
    return response


def communication_queues_id_items_post(id):  # noqa: E501
    """communication_queues_id_items_post

    Create queue item. # noqa: E501

    :param id: Id of queue.
    :type id: 

    :rtype: Item
    """
    return 'do some magic!'


def communication_queues_id_put(id):  # noqa: E501
    """communication_queues_id_put

    Change metadata of a queue. # noqa: E501

    :param id: Id of queue.
    :type id: 

    :rtype: Queue
    """
    return 'do some magic!'


def communication_queues_post():  # noqa: E501
    """communication_queues_post

    Create a queue. # noqa: E501


    :rtype: List[Queue]
    """
    return 'do some magic!'
