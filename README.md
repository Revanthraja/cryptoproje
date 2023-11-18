# Image Encryption and Decryption Application

This Flask-based application provides functionalities for encrypting and decrypting text information into images using steganography. Steganography is a technique used to hide information within an image. The application uses the Stepic library for encoding and decoding text messages into images.

## Description

This application enables users to:

- **Encrypt Text into an Image:** Users can upload an image file and input text along with a key to encrypt the text into the image.
- **Decrypt Text from an Image:** Users can upload an encrypted image and provide the decryption key to retrieve the hidden text.

## Installation

### Prerequisites

- Python 3.x
- pip package manager

### Steps to Run the Application Locally

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Set up the configuration by editing the `config.json` file. Provide necessary parameters like admin password, user details, and secret keys.
4. Run the Flask application:
    ```bash
    python app.py
    ```
5. Access the application via a web browser at `http://localhost:5000`.

## Usage

1. **Login:** Access the application by logging in using the provided credentials.
2. **Dashboard:** Encrypt text into an image by uploading a file, providing text information, and a key. The encrypted image can be downloaded afterward.
3. **Decryption:** Decrypt text from an encrypted image by uploading the image file and providing the decryption key.
4. **Change Password:** Admin users can change the application's login password using a secret key.

## File Structure

- **app.py:** Main Flask application file containing the routes and logic for different functionalities.
- **cipher.py:** Contains the `cipher_text` class with methods for encryption and decryption using steganography.
- **static:** Directory to store uploaded images and encrypted/decrypted images.

## Dependencies

- Flask: Web framework for building the application.
- PIL (Python Imaging Library): Python library to handle image-related operations.
- Stepic: Library used for steganography - hiding text within images.

## Author

- [Revanthraja M](https://github.com/revanthrajam)

## License

This project is licensed under the [MIT License](LICENSE).
