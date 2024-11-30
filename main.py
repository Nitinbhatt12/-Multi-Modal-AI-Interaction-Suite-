from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv(dotenv_path='.env')

# Access the variables
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG')

# Print to verify
print("API Key:", api_key)
print("Database URL:", database_url)
print("Debug Mode:", debug_mode)


# # from pyht import Client
# from dotenv import load_dotenv
# # from pyht.client import TTSOptions
# import os
# load_dotenv()

# # client = Client(
# #     user_id=os.getenv("PLAY_HT_USER_ID"),
# #     api_key=os.getenv("PLAY_HT_API_KEY"),
# # )
# # options = TTSOptions(voice="s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json")
# # # for chunk in client.tts("Hi, I'm Jennifer from Play. How can I help you today?", options):
# # #     # do something with the audio chunk
# # #     print(type(chunk))

# # some_iterable_text_stream = "Hi, I'm Jennifer from Play. How can I help you today?"
# # for chunk in client.stream_tts_input(some_iterable_text_stream, options):
# #     # do something with the audio chunk
# #     print(type(chunk))

# print('hello')
# print(os.getenv("PLAY_HT_USER_ID"))