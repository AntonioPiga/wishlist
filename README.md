# Wishlist Backend

This serves as a functional example of GPT Assistant API interaction. While we currently utilize it as a wishlist, you have the flexibility to create any Assistant to manage user requests.

The repo contains the Nuv package and actions designed to handle simple user requests and preferences. It functions when connected to an external Assistant API (or something similar), specially trained for this purpose.

When users interact, the conversation is sent to a private Slack channel (though it can also be stored in a database to improve data analysis or any other purpose).

## Deploy

1. Create your Assistant API at `https://platform.openai.com/assistant`
2. Insert your variables into `.env.example`
3. Rename `.env.example` -> `.env` 
4. Login into your Nuvolaris environment
5. Deploy the actions to your Nuvolaris environment with `task build`
6. To invoke these actions correctly, follow this schema:

- `createThread` and store threadId returned
- `sendMessage` (passing `threadId` and user messages)
- `list messages` (passing `threadId`)
- `notify` can be invoked everytime is invoked `sendMessage` or when you prefer

### Remember

As specified before, this repository has been created to manage a chatbot wishlist, but your Assistant API could handle everything you need with the same structure. For instance, users can inquire about information regarding you or your organization on your website.
