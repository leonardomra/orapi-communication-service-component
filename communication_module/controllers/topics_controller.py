import connexion
import six
import os
import time
import uuid
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from communication_module.models.event import Event  # noqa: E501
from communication_module.models.topic import Topic  # noqa: E501
from communication_module import util
from orcommunicator.oritem import ORItem
from orcommunicator import ORCommunicator
from ordbhandler import MySQLHandler

db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])
orcomm = ORCommunicator(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])
# add queues & topics
# orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME'], os.environ['TRAIN_SQS_QUEUE_ARN'])
# orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME'], os.environ['PREDICT_SQS_QUEUE_ARN'])
#
orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME_TML'], os.environ['TRAIN_SQS_QUEUE_ARN_TML'])
orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME_TML'], os.environ['PREDICT_SQS_QUEUE_ARN_TML'])
#
orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME_QNA'], os.environ['TRAIN_SQS_QUEUE_ARN_QNA'])
orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME_QNA'], os.environ['PREDICT_SQS_QUEUE_ARN_QNA'])
#
orcomm.addQueue(os.environ['TRAIN_SQS_QUEUE_NAME_NER'], os.environ['TRAIN_SQS_QUEUE_ARN_NER'])
orcomm.addQueue(os.environ['PREDICT_SQS_QUEUE_NAME_NER'], os.environ['PREDICT_SQS_QUEUE_ARN_NER'])
#
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
        jobUser = None
        jobOutput = None
        # verify if Job is in DB
        checkJobQuery = ("SELECT id, status, task, user, kind, output, model FROM Job WHERE id = %s")
        params = (body['Message']['_id'],)
        results = db.get(checkJobQuery, params)
        if results:
            jobId = results[0][0]
            jobTask = results[0][2]
            jobUser = results[0][3]
            jobKind = results[0][4]
            jobOutput = results[0][5]
            jobModel = results[0][6]
        if body['Subject'] == 'Send Job':
            print('Job has started', jobId, flush=True)
            sendEmailToUser(jobUser, "Your job (id " + jobId + ") was sent to the queue. Please wait until it's completed....")
            return sendStartJobToQueue(body, jobId, jobTask, jobKind)
        elif body['Subject'] == 'Finish Job':
            print('Job is finished', jobId, flush=True)
            #try:
            message = None
            dataParams = None
            code = None
            if 'code' in body['Message']:
                code = body['Message']['code']
            if 'message' in body['Message']:
                print(body['Message']['message'], flush=True)
            if jobTask == 'train':
                if code != 'executed':
                    if jobOutput is None:
                        message = "Your job (id " + jobId + ") is finished. Unfortunately, there was an error and your model could not be trained."
                        sendEmailToUser(jobUser, message)
                    else:
                        message = "Your job (id " + jobId + ") is finished. Download the model (id " + jobOutput + ") here "
                        dataParams = (jobOutput,)
                        checkDataQuery = ("SELECT location FROM Data WHERE id = %s")
                        dataResults =  db.get(checkDataQuery, dataParams)
                        sendEmailToUser(jobUser, message + os.environ['S3BUCKET_URL'] + dataResults[0][0].replace('openresearch/', ''))
            else:
                if code != 'executed':
                    if jobOutput is None:     
                        message = "Your job (id " + jobId + ") is finished. Unfortunately, there was an error and your results were not computed."
                        sendEmailToUser(jobUser, message)
                    else:
                        message = "Your job (id " + jobId + ") is finished. Download the results (id " + jobOutput + ") here "
                        dataParams = (jobOutput,)
                        checkDataQuery = ("SELECT location FROM Data WHERE id = %s")
                        dataResults =  db.get(checkDataQuery, dataParams)
                        sendEmailToUser(jobUser, message + os.environ['S3BUCKET_URL'] + dataResults[0][0].replace('openresearch/', ''))
            #except Exception as error:
            #    print(error, flush=True)
            return 'Job is finished'
    elif response.Type == 'UnsubscribeConfirmation':
        return orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).unsubscribe(response)
    else:
        return 'bad request!', 400

def sendEmailToUser(jobUser, body):
    getUserQuery = ("SELECT id, firstName, email FROM User WHERE id = %s")
    params = (jobUser,)
    results = db.get(getUserQuery, params)
    firstName = results[0][1]
    userEmail = results[0][2]
    print(results, flush=True)
    smtp = smtplib.SMTP_SSL(host=os.environ['SMTP_SERVER'], port=os.environ['SMTP_SERVER_PORT'])
    smtp.login(os.environ['SMTP_USERNAME'], os.environ['SMTP_PASSWORD'])
    msg = MIMEMultipart()
    msg['From'] = os.environ['SMTP_USERNAME']
    msg['To'] = userEmail
    msg['Subject'] = 'OpenResearchAPI' 
    msg.attach(MIMEText('Hi, ' +  body, 'plain'))
    smtp.send_message(msg)
    del msg
    smtp.quit()

def sendStartJobToQueue(body, jobId, jobTask, jobKind):
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
        'jobKind': {
            'StringValue': jobKind,
            'DataType': 'String'
        },
        'JobModifier': {
            'StringValue': str(uuid.uuid4()),
            'DataType': 'String'
        } 
    }
    if jobTask == 'train':
        item.MessageBody = 'Train_' + str(int(time.time()))
        if jobKind == 'tml':
            queueResponse = orcomm.getQueue(os.environ['TRAIN_SQS_QUEUE_ARN_TML']).pushItem(item)
        elif jobKind == 'qna':
            queueResponse = orcomm.getQueue(os.environ['TRAIN_SQS_QUEUE_ARN_QNA']).pushItem(item)
        elif jobKind == 'ner':
            queueResponse = orcomm.getQueue(os.environ['TRAIN_SQS_QUEUE_ARN_NER']).pushItem(item)
    elif jobTask == 'analyse':
        item.MessageBody = 'Analyse_' + str(int(time.time()))
        if jobKind == 'tml':
            queueResponse = orcomm.getQueue(os.environ['PREDICT_SQS_QUEUE_ARN_TML']).pushItem(item)
        elif jobKind == 'qna':
            queueResponse = orcomm.getQueue(os.environ['PREDICT_SQS_QUEUE_ARN_QNA']).pushItem(item)
        elif jobKind == 'ner':
            queueResponse = orcomm.getQueue(os.environ['PREDICT_SQS_QUEUE_ARN_NER']).pushItem(item)
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
