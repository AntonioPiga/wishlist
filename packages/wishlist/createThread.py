from openai import OpenAI

def main(args):
    try:
        client = OpenAI(
            organization=args.get('ORGANIZATION'),
            api_key=args.get('API_KEY_AI')
        )

        empty_thread = client.beta.threads.create()

        return {
            'body': empty_thread.id
        }
    
    except Exception as e:
        raise f"An error occurred: {e}"
