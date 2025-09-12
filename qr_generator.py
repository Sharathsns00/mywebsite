import qrcode

# The link or text you want inside the QR
url = "https://sharathsns00.github.io/mywebsite/"  # replace with your website link

# Generate QR code
qr = qrcode.make(url)

# Save as image
qr.save("mywebsite_qr.png")

print("✅ QR code generated and saved as 'mywebsite_qr.png'")