import qrcode # type: ignore

url = "http://127.0.0.1:8000/review/"
img = qrcode.make(url)
img.save("qr_code.png")
print("QR Code saved as qr_code.png")