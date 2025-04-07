import qrcode

pdf_url = "https://raw.githubusercontent.com/Tristanruel/a-PDF/8e7f5c663e00ae1a3583228a28880a19382559cb/Americanization_Now_and_Then_.pdf"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(pdf_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("pdf_qrcode.png")

print("QR code generated and saved as 'pdf_qrcode.png'.")
