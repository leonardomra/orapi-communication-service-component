import connexion
import six
import os
import time
import uuid
import json
from communication_module.models.event import Event  # noqa: E501
from communication_module.models.topic import Topic  # noqa: E501
from communication_module import util
from orcomm_module.oritem import ORItem
from orcomm_module.orcommunicator import ORCommunicator
from dbhandler.mysql_handler import MySQLHandler

db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])
orcomm = ORCommunicator(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])
# add queues & topics
orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME'], os.environ['TRAIN_SQS_QUEUE_ARN'])
orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME'], os.environ['PREDICT_SQS_QUEUE_ARN'])
orcomm.addTopic(os.environ['JOBS_NAME_TOPIC'], os.environ['JOBS_ARN_TOPIC'])


def communication_events_id_broadcast_get(id):  # noqa: E501
    """communication_events_id_broadcast_get

    Broadcast an event. # noqa: E501

    :param id: Id of event.
    :type id: 

    :rtype: Event
    """
    return 'do some magic!'


def communication_events_id_delete(id):  # noqa: E501
    """communication_events_id_delete

    Remove an event. # noqa: E501

    :param id: Id of event.
    :type id: 

    :rtype: Event
    """
    return 'do some magic!'


def communication_events_id_get(id):  # noqa: E501
    """communication_events_id_get

    Obtain information about an event. # noqa: E501

    :param id: Id of event.
    :type id: 

    :rtype: Event
    """
    return 'do some magic!'


def communication_events_id_put(id):  # noqa: E501
    """communication_events_id_put

    Change metadata about an event. # noqa: E501

    :param id: Id of event.
    :type id: 

    :rtype: Event
    """
    return 'do some magic!'


def communication_events_post(body=None, x_amz_sns_message_type=None, x_amz_sns_message_id=None, x_amz_sns_topic_arn=None, x_amz_sns_subscription_arn=None):  # noqa: E501
    """communication_events_post

    Create an event. # noqa: E501

    :param body: The subscription confirmation message is a POST message with a message body that contains a JSON document with name-value pairs.
    :type body: dict | bytes
    :param x_amz_sns_message_type: The type of message. The possible values are SubscriptionConfirmation, Notification, and UnsubscribeConfirmation.
    :type x_amz_sns_message_type: str
    :param x_amz_sns_message_id: A Universally Unique Identifier, unique for each message published. For a notification that Amazon SNS resends during a retry, the message ID of the original message is used.
    :type x_amz_sns_message_id: str
    :param x_amz_sns_topic_arn: The Amazon Resource Name (ARN) for the topic that this message was published to.
    :type x_amz_sns_topic_arn: str
    :param x_amz_sns_subscription_arn: The ARN for the subscription to this endpoint.
    :type x_amz_sns_subscription_arn: str

    :rtype: str
    """
    
    if not connexion.request.is_json:
        body = json.loads(body)
        if 'Message' in body:
            try:
                print('Subject: ', body['Subject'], flush=True )
                body['Message'] = json.loads(body['Message'])
            except json.decoder.JSONDecodeError:
                print('Message cannot be converted into JSON')
    response = orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).tuneTopic(connexion.request.headers, body)
    if response.Type == 'SubscriptionConfirmation':
        return orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).confirmSubscription(response)
    elif response.Type == 'Notification':
        jobId = None
        jobTask = None
        # verify if Job is in DB
        checkJobQuery = ("SELECT id, status, task FROM Job WHERE id = %s")
        params1 = (body['Message']['_id'],)
        results = db.get(checkJobQuery, params1)
        if results:
            jobId = results[0][0]
            jobTask = results[0][2]
        print(jobTask, flush=True)
        if body['Subject'] == 'Send Job':
            return sendStartJobToQueue(body, jobId, jobTask)
        elif body['Subject'] == 'Finish Job':
            print('Job is finished', jobId, flush=True)
            return 'Job is finished'
        return sendStartJobToQueue(body, jobId, jobTask)
    elif response.Type == 'UnsubscribeConfirmation':
        return orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).unsubscribe(response)
    else:
        return 'bad request!', 400

def sendStartJobToQueue(body, jobId, jobTask):
    # determine which queue should the job go
    updateJobQuery = ('UPDATE Job SET status = %s WHERE id = %s')
    params2 = ('queuing', body['Message']['_id'],)
    db.update(updateJobQuery, params2)
    # send the job to queue
    queueResponse = None
    item = ORItem()
    item.MessageAttributes = {
        'jobId': {
            'StringValue': jobId,
            'DataType': 'String'
        },
        'jobStatus': {
            'StringValue': 'queuing',
            'DataType': 'String'
        },
        'jobTask': {
            'StringValue': jobTask,
            'DataType': 'String'
        },
        'JobModifier': {
            'StringValue': str(uuid.uuid4()),
            'DataType': 'String'
        } 
    }
    if jobTask == 'train':
        item.MessageBody = 'Train_' + str(int(time.time()))
        queueResponse = orcomm.getQueue(os.environ['TRAIN_SQS_QUEUE_ARN']).pushItem(item)
    elif jobTask == 'analyse':
        item.MessageBody = 'Analyse_' + str(int(time.time()))
        queueResponse = orcomm.getQueue(os.environ['PREDICT_SQS_QUEUE_ARN']).pushItem(item)
    return queueResponse

def communication_topics_get(limit=None):  # noqa: E501
    """communication_topics_get

    Obtain information about topics. # noqa: E501

    :param limit: The amount of topics to be returned.
    :type limit: int

    :rtype: List[Topic]
    """
    return 'do some magic!'


def communication_topics_id_delete(id):  # noqa: E501
    """communication_topics_id_delete

    Remove a a topic. # noqa: E501

    :param id: Id of topic.
    :type id: 

    :rtype: Topic
    """
    return 'do some magic!'


def communication_topics_id_events_get(id):  # noqa: E501
    """communication_topics_id_events_get

    Obtain information about events. # noqa: E501

    :param id: Id of topic.
    :type id: 

    :rtype: List[Event]
    """
    return 'do some magic!'


def communication_topics_id_events_post(id, kind, job_id):  # noqa: E501
    """communication_topics_id_events_post

    Create an event. # noqa: E501

    :param id: Id of topic.
    :type id: 
    :param kind: Kind of Event.
    :type kind: str
    :param job_id: Id of job.
    :type job_id: 

    :rtype: List[Event]
    """
    return 'do some magic!'


def communication_topics_id_get(id):  # noqa: E501
    """communication_topics_id_get

    Obtain information about a topic. # noqa: E501

    :param id: Id of topic.
    :type id: 

    :rtype: Topic
    """
    return 'do some magic!'


def communication_topics_id_put(id):  # noqa: E501
    """communication_topics_id_put

    Change the metadata of a topic. # noqa: E501

    :param id: Id of topic.
    :type id: 

    :rtype: Topic
    """
    return 'do some magic!'


def communication_topics_post():  # noqa: E501
    """communication_topics_post

    Create a topic. # noqa: E501


    :rtype: List[Topic]
    """
    return 'do some magic!'
