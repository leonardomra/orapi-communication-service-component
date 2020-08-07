class ORItem():

    def __init__(self):
        self._attributes = {}
        self._body = None
        self._messageAttributes = {}
        self._messageId = None

    @property
    def Attributes(self) -> {}:
        return self._attributes

    @Attributes.setter
    def Attributes(self, _attributes: {}):
        """
        Supported attributes:
            ApproximateReceiveCount
            ApproximateFirstReceiveTimestamp
            MessageDeduplicationId
            MessageGroupId
            SenderId
            SentTimestamp
            SequenceNumber
        """
        self._attributes = _attributes

    @property
    def MessageAttributes(self) -> {}:
        return self._messageAttributes

    @MessageAttributes.setter
    def MessageAttributes(self, _messageAttributes: {}):
        """
        Example:
            {
                'Author': {
                    'StringValue': 'Daniel',
                    'DataType': 'String'
                }
            }
        """
        self._messageAttributes = _messageAttributes

    @property
    def MessageBody(self) -> str:
        return self._body

    @MessageBody.setter
    def MessageBody(self, _body: str):
        self._body = _body

    @property
    def MessageId(self) -> str:
        return self._messageId

    @MessageId.setter
    def MessageId(self, _messageId: str):
        self._messageId = _messageId