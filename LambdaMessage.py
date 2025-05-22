import logging
import json

#Configure the logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#def es una palabra reservada para definir funciones en python
def lambda_handler(event, context):
    #extrae el mensaje del evento(event), asumiendo es un simple JSON {"message": "your message here"}
    message = event.get('message','No message provided')

    #manda el mensaje ala variable de log
    logger.info(message)

    return {
        'statusCode': 200,
        'body': json.dumps('message logged successfully')
    }