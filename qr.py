import qrcode
import os
from github import Github
import yaml

# GitHub repository details
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
REPO_NAME = "YOUR_REPO_NAME"
REPO_OWNER = "YOUR_REPO_OWNER"

# The data that you want to store in the QR code
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
filename = "qrcode.png"
img.save(filename)

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Get the repository
repo = g.get_user().get_repo(Saloni-singh22/xebia01)

# Upload the QR code image to the repository
with open(filename, "rb") as file:
    repo.create_file(
        filename,
        f"Committing QR code image: {qr.py}",
        file.read(),
        branch="main"
    )

print("QR code image uploaded to GitHub repository.")

# Save the image in a .yml file
with open("qrcode.yml", "w") as file:
    data = {
        "qrcode_image": f"data:image/png;base64,{img.get_image().tobytes().hex()}"
    }
    yaml.dump(data, file)

print("QR code image saved in qrcode.yml file.")
