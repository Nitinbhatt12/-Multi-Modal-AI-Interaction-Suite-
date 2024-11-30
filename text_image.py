import requests
from PIL import Image
from io import BytesIO
from gtts import gTTS
import os

# Function to fetch an image from Unsplash API
def fetch_image(query):
    access_key = '20ZSk4jYNHS4JF-oJuLOao3W8ouK7jmZRhEJkysimsw'  # Replace with your actual Unsplash API access key
    url = f'https://api.unsplash.com/search/photos?query={query}&client_id={access_key}'
    
    response = requests.get(url)
    
    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        
        # Check if any image data is returned
        if data['results'] and isinstance(data['results'], list) and len(data['results']) > 0:
            image_url = data['results'][0]['urls']['regular']
            img_response = requests.get(image_url)
            img = Image.open(BytesIO(img_response.content))
            return img
        else:
            print(f"No images found for '{query}'.")
            return None
    else:
        print(f"Failed to fetch data from Unsplash. Status code: {response.status_code}")
        return None

# Function to generate speech for the given text
def generate_speech(text):
    tts = gTTS(text)
    speech_filename = 'speech.mp3'
    tts.save(speech_filename)
    print(f"Speech saved as {speech_filename}")
    os.system(f"start {speech_filename}")  # This will play the speech on Windows

# Main function
def text_to_image_and_speech(query):
    # Fetch image related to the query
    image = fetch_image(query)
    
    if image:
        # Show the image
        image.show()
        
        # Save the image
        image.save(f'{query}_image.jpg')
        print(f"Image saved as {query}_image.jpg")
        

# Example usage
if __name__ == "__main__":
    try:
        with open('recent_text.txt', 'r') as file:
            text = file.read().strip()  # Read text from the file and strip any extra whitespace
            text_to_image_and_speech(text)  # Pass the text to the main function
    except FileNotFoundError:
        print("Error: 'recent_text.txt' file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
