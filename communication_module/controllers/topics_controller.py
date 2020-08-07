import connexion
import six
import os
import json
from communication_module.models.event import Event  # noqa: E501
from communication_module.models.topic import Topic  # noqa: E501
from communication_module import util
from orcomm_module.orcommunicator import ORCommunicator
from orcomm_module.oritem import ORItem
from dbhandler.mysql_handler import MySQLHandler

orcomm = ORCommunicator(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])
orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME'], os.environ['TRAIN_SQS_QUEUE_ARN'])
orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME'], os.environ['PREDICT_SQS_QUEUE_ARN'])


db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])

checkJobQuery = ("SELECT id, status, task FROM Job WHERE id = %s")
params1 = ('0598789d-2cb2-412a-9b90-b61ec40274d8',)
results = db.get(checkJobQuery, params1)
jobId = None
jobStatus = None
jobTask = None

if not results:
    print('List is empty')
else:
    jobId = results[0][0]
    jobStatus = results[0][1]
    jobTask = results[0][2]

updateJobQuery = ("UPDATE Job SET status = %s WHERE id = %s")
params2 = ('queuing', jobId)
db.update(updateJobQuery, params2)

if jobTask == 'train':
    print('Train Queue')
    item = ORItem()
    item.MessageBody = 'Train'
    orcomm.getQueue(os.environ['TRAIN_SQS_QUEUE_NAME']).pushItem(item)
elif  jobTask == 'analyse':
    print('Predict Queue')

'''
{   
    "Type": "Notification", 
    "MessageId": "7e6ed391-9e73-51d6-a62b-8437b6e8b596", 
    "TopicArn": "arn:aws:sns:eu-central-1:773905262711:Jobs", 
    "Subject": "Send Job", 
    "Message": {
        "_id": "0598789d-2cb2-412a-9b90-b61ec40274d8", 
        "_user": "767f245a-cc82-11ea-a60b-bf77def8d078", 
        "_label": "my label", 
        "_description": "my description", 
        "_kind": "tml", 
        "_model": "cb2ef793-125b-44a0-b46e-d5f134fc1db4", 
        "_data_source": "41e2e1e6-8581-4909-9fc3-166d9670b8c5", 
        "_data_sample": "ecc26842-28a4-41b5-95ea-57233943267c", 
        "_status": "waiting", 
        "_output": null, 
        "_date_created": null, 
        "_date_modified": null, 
        "task": "train"}, 
    "Timestamp": "2020-08-06T15:48:43.799Z", 
    "SignatureVersion": "1", 
    "Signature": "mihASNRgDlwF26c7AcELVaPREVMBXk1L9WW6nQAjMzv1Z9PVZ8kI8p7SNkmlhLtuJnhIgwoFWVj3mQyQwNREAwdyEfg7LFgBvoMHM4OnCkuuBVq9bUXVspdfYDHWJ8hNmk7nyf0kQRrocH0OYFlhb/QTx5JPerEQD4CkUhIGU+h1dVw8FulmYti7oRypItAc/dHVg3RmkVVefXCY6V2se6wZmq/wd619TaYp+D5x4YN1NNWaUjCWU/fVy1ozhUeY/LPkSoUUDKru3pmArCVoUq8oOJQbrGghlPAez5nfLkJelEHHeLSeTSmTiO7FusZt4OkGo2MSXcJWuVrPZ8Hk4A==", 
    "SigningCertURL": "https://sns.eu-central-1.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem", 
    "UnsubscribeURL": "https://sns.eu-central-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-central-1:773905262711:Jobs:00ad30b7-9bc1-48e6-8613-145056f8385e"}
'''


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
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    else:
        body = json.loads(body)
    
    #print(connexion.request.headers, flush=True)
    print(body, flush=True)
    
    response = orcomm.topic.tuneTopic(connexion.request.headers, body)
    if response.Type == 'SubscriptionConfirmation':
        return orcomm.topic.confirmSubscription(response)
    elif response.Type == 'Notification':
       
        jobId = None
        jobStatus = None
        jobTask = None
        # verify if Job is in DB
        checkJobQuery = ("SELECT id, status, task FROM Job WHERE id = %s")
        params1 = (body.Message._id,)
        results = db.get(checkJobQuery, params1)
        if not results:
            print('List is empty')
        else:
            jobId = results[0][0]
            jobStatus = results[0][1]
            jobTask = results[0][2]
        # determine which queue should the job go
        updateJobQuery = ("UPDATE Job SET status = %s WHERE id = %s")
        params2 = ('queuing', body.Message._id,)
        db.update(updateJobQuery, params2)
        
        # send the job to queue
        # update status of job in DB
        
        
        
        
        return "will return to "
    elif response.Type == 'UnsubscribeConfirmation':
        return orcomm.topic.unsubscribe(response)


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
