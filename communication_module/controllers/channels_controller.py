import connexion
import six

from communication_module.models.channel import Channel  # noqa: E501
from communication_module.models.message import Message  # noqa: E501
from communication_module import util


def communication_channels_get(limit=None):  # noqa: E501
    """communication_channels_get

    Obtain information about channels. # noqa: E501

    :param limit: The amount of channels to be returned.
    :type limit: int

    :rtype: List[Channel]
    """
    return 'do some magic!'


def communication_channels_id_delete(id):  # noqa: E501
    """communication_channels_id_delete

    Remove a channel. # noqa: E501

    :param id: Id of channel.
    :type id: 

    :rtype: Channel
    """
    return 'do some magic!'


def communication_channels_id_get(id):  # noqa: E501
    """communication_channels_id_get

    Obtain information about a channel. # noqa: E501

    :param id: Id of channel.
    :type id: 

    :rtype: Channel
    """
    return 'do some magic!'


def communication_channels_id_messages_get(id, limit=None):  # noqa: E501
    """communication_channels_id_messages_get

    Obtain information about messages. # noqa: E501

    :param id: Id of channel.
    :type id: 
    :param limit: The amount of messages to be returned.
    :type limit: int

    :rtype: List[Message]
    """
    return 'do some magic!'


def communication_channels_id_messages_post(id):  # noqa: E501
    """communication_channels_id_messages_post

    Create a message. # noqa: E501

    :param id: Id of channel.
    :type id: 

    :rtype: Message
    """
    return 'do some magic!'


def communication_channels_id_put(id):  # noqa: E501
    """communication_channels_id_put

    Change metadata of a channel. # noqa: E501

    :param id: Id of channel.
    :type id: 

    :rtype: Channel
    """
    return 'do some magic!'


def communication_channels_post():  # noqa: E501
    """communication_channels_post

    Create a channel. # noqa: E501


    :rtype: List[Channel]
    """
    return 'do some magic!'


def communication_messages_id_broadcast_get(id):  # noqa: E501
    """communication_messages_id_broadcast_get

    Broadcast a message. # noqa: E501

    :param id: Id of message.
    :type id: 

    :rtype: Message
    """
    return 'do some magic!'


def communication_messages_id_delete(id):  # noqa: E501
    """communication_messages_id_delete

    Remove a message. # noqa: E501

    :param id: Id of message.
    :type id: 

    :rtype: Message
    """
    return 'do some magic!'


def communication_messages_id_get(id):  # noqa: E501
    """communication_messages_id_get

    Get information about a message. # noqa: E501

    :param id: Id of message.
    :type id: 

    :rtype: Message
    """
    return 'do some magic!'


def communication_messages_id_put(id):  # noqa: E501
    """communication_messages_id_put

    Change metadata of a message. # noqa: E501

    :param id: Id of message.
    :type id: 

    :rtype: Message
    """
    return 'do some magic!'
