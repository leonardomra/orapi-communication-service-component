import boto3

class ORQueue():

    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None, QUEUE_NAME=None):
        session  = boto3.Session(
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        sqs = session.resource('sqs')
        self.queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    def pushItem(self, oritem):
        return self.queue.send_message(MessageBody=oritem.MessageBody, MessageAttributes=oritem.MessageAttributes, MessageGroupId=oritem.MessageBody)
        
    def pullItem(self, messageAttributeNames = []):
        for message in self.queue.receive_messages(MessageAttributeNames=['Author']):
            pass
        
    def getResource(self):
        return self.queue