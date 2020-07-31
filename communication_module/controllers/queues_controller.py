import connexion
import six

from communication_module.models.item import Item  # noqa: E501
from communication_module.models.queue import Queue  # noqa: E501
from communication_module import util


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


def communication_queues_id_items_get(id, limit=None):  # noqa: E501
    """communication_queues_id_items_get

    Obtain information about queue items. # noqa: E501

    :param id: Id of queue.
    :type id: 
    :param limit: The amount of queue items to be returned.
    :type limit: int

    :rtype: List[Item]
    """
    return 'do some magic!'


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
