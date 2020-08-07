import boto3

class ORQueue():

    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None, QUEUE_NAME=None):
        self.sqs = boto3.client(
            'sqs',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        self.queue = self.sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    def pushItem(self, oritem):
        self.queue.send_message(MessageBody=oritem.MessageBody, MessageAttributes=oritem.MessageAttributes)

    def pullItem(self):
        pass