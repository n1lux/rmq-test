from kombu import Connection, Exchange, Queue, Consumer

rabbit_url = "amqp://localhost:5672"

conn = Connection(rabbit_url)

exchange = Exchange("example-exchange", type="direct")

queue = Queue(name="example-queue", exchange=exchange, routing_key="orders")


def proccess_message(body, message):
    print(f"The Body is {body}")
    message.ack()


with Consumer(conn, queues=queue, callbacks=[proccess_message], accept=["text/plain", "application/json"]):
    conn.drain_events(timeout=2)