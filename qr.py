import qrcode
import cv2
import numpy as np

# Function to generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code saved as 'qrcode.png'")

# Function to scan QR code and generate image
def scan_qr_code():
    detector = cv2.QRCodeDetector()
    image, _, _ = detector.detectAndDecode(cv2.imread("qrcode.png"))

    if image:
        # Generate an image based on the decoded data
        img = np.zeros((500, 500, 3), np.uint8)
        img.fill(255)
        cv2.putText(img, image, (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imwrite("generated_image.png", img)
        print("Image generated and saved as 'generated_image.png'")
    else:
        print("Failed to scan QR code")

# Example usage
generate_qr_code("Hello, World!")
scan_qr_code()
