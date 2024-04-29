import requests
from PIL import Image
import io

url = "https://source.unsplash.com/random/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the image data using BytesIO
    img = Image.open(io.BytesIO(response.content))
    
    # Display the image
    img.show()
else:
    print("Failed to fetch the image.")
