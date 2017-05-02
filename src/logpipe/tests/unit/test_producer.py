from django.test import TestCase
from rest_framework import serializers
from logpipe import Producer
from logpipe.tests.common import StateSerializer, StateModel, TOPIC_STATES
import mock


class CustomStateSerializer(StateSerializer):
    my_ser_method_field = serializers.SerializerMethodField()

    def get_my_ser_method_field(self, obj):
        return 'value-{}'.format(obj['code'])


class ProducerTest(TestCase):
    def test_send_serializer_method_field(self):
        fake_client = mock.MagicMock()
        fake_client.send = mock.MagicMock()
        get_producer_backend = mock.MagicMock()
        get_producer_backend.return_value = fake_client

        with mock.patch('logpipe.producer.get_producer_backend', get_producer_backend):
            producer = Producer(TOPIC_STATES, CustomStateSerializer)

        ny = StateModel()
        ny.id = 5
        ny.code = 'NY'
        ny.name = 'New York'
        producer.send(ny)

        fake_client.send.assert_called_once_with(TOPIC_STATES,
            key='NY',
            value=b'json:{"type":"us-state","version":1,"message":{"code":"NY","name":"New York","my_ser_method_field":"value-NY"}}')
