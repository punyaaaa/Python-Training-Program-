import qrcode

upi_id = "sampleupi@okaxis"
name = "Punya Y Poojary"
amount = "100"

upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

qr = qrcode.make(upi_url)

qr.save("gpay_qr.png")

print("GPay QR Code saved as 'gpay_qr.png'. Scan it in GPay to pay ₹100 to:", name)
