import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

text_msg = "Hai_students you are well disciplined, but need improvement"
qr.add_data(text_msg)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("students_qr.png")

print("QR code generated and saved as students_qr.png")