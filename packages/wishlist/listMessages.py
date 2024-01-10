from openai import OpenAI
from openai.core import sleep


async def main(args):
    global ASSISTANT_ID
    ASSISTANT_ID = args['PUBLIC_ASSISTANT_WISHLIST_AI_ID']
    
    openai = OpenAI(
        organization=args['ORGANIZATION_WISHLIST'],
        apiKey=args['API_KEY_ASSISTANT_AI']
    )
    
    res = await list_last_assistant_thread_messages(args.get('threadId'), openai)
    return {
        'body': res['text']['value']
    }

async def list_last_assistant_thread_messages(thread_id, openai, max_attempts=5):
    try:
        response = await openai.beta.threads.messages.list(thread_id)
  
        all_messages = response['data']
        print(all_messages)
  
        assistant_messages = [message for message in all_messages if message['role'] == 'assistant']
        last_assistant_message = assistant_messages[0] if assistant_messages else None
  
        if last_assistant_message and last_assistant_message['content']:
            text_value = last_assistant_message['content'][0]['value']
            return {'text': {'value': text_value}}
        else:
            if max_attempts > 0:
                await sleep(5000)
                return await list_last_assistant_thread_messages(thread_id, openai, max_attempts - 1)
            else:
                raise ValueError('Maximum attempts reached. Unable to retrieve assistant message.')
    except Exception as error:
        print('Error running thread:', error)
        raise error
