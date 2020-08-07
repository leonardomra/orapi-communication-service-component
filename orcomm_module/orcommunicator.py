from orcomm_module.ortopic import ORTopic 
from orcomm_module.orchannel import ORChannel
from orcomm_module.orqueue import ORQueue

import boto3

class ORCommunicator():
    
    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None):
        self.awsRegion = AWS_REGION
        self.awsAccessKey = AWS_ACCESS_KEY
        self.awsSecretKey = AWS_SECRET_KEY
        self.topics = {}
        self.channels = {}
        self.queues = {}
        
    def addTopic(self, topicName=None, topicArn=None):
        topic = ORTopic(self.awsRegion, self.awsAccessKey, self.awsSecretKey, topicArn)
        self.topics[topicName] = topic

    def addChannel(self, channelName):
        channel = ORChannel(channelName)
        self.channels[channelName] = channel

    def addQueue(self, queueName=None, queueArn=None):
        queue = ORQueue(self.awsRegion, self.awsAccessKey, self.awsSecretKey, queueName)
        self.queues[queueName] = queue

    def getTopics(self):
        return self.topics

    def getChannels(self):
        return self.channels

    def getQueues(self):
        return self.queues

    def getTopic(self, topicName):
        return self.topics[topicName]

    def getChannel(self, channelName):
        return self.channels[channelName]

    def getQueue(self, queueName):
        return self.queues[queueName]

    