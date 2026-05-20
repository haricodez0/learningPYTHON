import qrcode

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\User\\Desktop\\PROJECTS\\all the python stuff\\1 month training\\qrcodes\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")
