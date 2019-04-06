from kombu import Connection, Exchange, Producer, Queue


def create_message():
    return {
        "sku": "ka9s8ks9d8",
        "id": 33233,
        "name": "Teste de messagemm in json"
    }


rabbit_url = "amqp://localhost:5672"

conn = Connection(rabbit_url)

channel = conn.channel()


exchange = Exchange("example-exchange", type="direct")

producer = Producer(exchange=exchange, channel=channel, routing_key="orders")


queue = Queue(name="example-queue", exchange=exchange, routing_key="orders")

queue.maybe_bind(conn)

queue.declare()

msg = create_message()

producer.publish(msg)


