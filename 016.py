# Write a Python program to generate a QR code for the text "Python Programming is fun!" and save it as an image file.

# Import the qrcode library for generating QR codes
import qrcode

# Create a QR code image from the given text
image = qrcode.make("Python Programming is fun!")

# Save the generated QR code image as a PNG file
image.save("py.png")

# Print a success message
print("QR code generated successfully!!!")
