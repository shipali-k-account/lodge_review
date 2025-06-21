import qrcode # type: ignore
url = "https://lodge-review.onrender.com/review/"
img = qrcode.make(url)
img.save("qr_code.png")
print("QR Code saved as qr_code.png")