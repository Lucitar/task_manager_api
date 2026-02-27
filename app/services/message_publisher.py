import pika
import json
import logging

logger = logging.getLogger(__name__)

RABBITMQ_HOST = "rabbitmq"
EXCHANGE = "task.exchange"
ROUTING_KEY = "task.created"

def publish_task_created(task_id: int, title: str, description: str, priority: str):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST)
        )
        channel = connection.channel()

        channel.exchange_declare(
            exchange=EXCHANGE,
            exchange_type="direct",
            durable=True
        )

        message = json.dumps({
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority
        })

        channel.basic_publish(
            exchange=EXCHANGE,
            routing_key=ROUTING_KEY,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2  # mensagem persistente
            )
        )

        connection.close()
        logger.info(f"Message published for task {task_id}")

    except Exception as e:
        logger.error(f"Failed to publish message: {e}")