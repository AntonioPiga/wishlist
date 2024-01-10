from openai import OpenAI

def main(args):
    try:
        client = OpenAI(
            organization=args['ORGANIZATION_WISHLIST'],
            apiKey=args['API_KEY_WISHLIST']
        )

        empty_thread = client.beta.threads.create()

        return {
        'body': empty_thread
        }
    
    except Exception as e:
        raise f"An error occurred: {e}"
