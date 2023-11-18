from PIL import Image
import stepic


class cipher_text(object):
	"""docstring for cipher_text"""
	def __init__(self,filename):
		self.filename = filename

	def encrypt(self,string, shift):
		cipher = ''
		for char in string:
			if char == ' ':
				cipher = cipher + char
			elif  char.isupper():
				cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
			else:
				cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
		return cipher

	def decrypt(self,string,shift):
	    cipher = ''
	    for char in string: 
	        if char == ' ':
	            cipher = cipher + char
	        elif  char.isupper():
	            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
	        else:
	            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
	    return cipher



	def encryption(self,filetype,info,key):

		location = 'static/'+self.filename
		image = Image.open(location)
		key = int(key)
		cipher_text = self.encrypt(info, key)

		cipher_text = bytes(cipher_text, 'utf-8')

		image = stepic.encode(image,cipher_text)
		image.save(location.split('.')[0]+'1.png','png')
		return True



	def decryption(self,key):

		location = 'static/userImage1.png'
		key = int(key)
		image = Image.open(location)
		info = stepic.decode(image)

		original_text = self.decrypt(info,key)
		return original_text




# encryption('vikash23.jpeg','image','My name is Vikash',2)

# decryption('vikash23.jpeg',2)