from openai import OpenAI


async def main(args):
    global ASSISTANT_ID
    ASSISTANT_ID = args.get('PUBLIC_ASSISTANT_WISHLIST_AI_ID')
    
    openai = OpenAI(
        organization=args.get('ORGANIZATION_WISHLIST'),
        apiKey=args.get('API_KEY_WISHLIST')
    )
    
    post = await post_message_on_thread(args['message'], args['threadId'], openai)
   
    
    res = await run_thread(args['threadId'], openai)
    return {
        'body': 'OK'
    }

async def post_message_on_thread(message, thread_id, openai):
    try:
        body = {
            'content': message,
            'role': 'user'
        }
        create_thread_resp = await openai.beta.threads.messages.create(thread_id, body)
        return create_thread_resp
    except Exception as error:
        print('Error creating message on thread:', error)
        raise error

async def run_thread(thread_id, openai):
    try:
        body = {
            'assistant_id': ASSISTANT_ID
        }
        run_thread_resp = await openai.beta.threads.runs.create(thread_id, body)
        return run_thread_resp
    except Exception as error:
        print('Error running thread:', error)
        raise error
