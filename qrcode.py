import qrcode #Type 'pip install qrcode ' into the terminal (This will download the qrcode library)
import qrcode.constants

data = "https://sites.google.com/view/idignajr" #Enter the domain of the site you want here

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,

)
qr.add_data(data)
qr.make(fit=True)

qr_img= qr.make_image(fill="black", back_color="white")
qr_img.show()
qr_img.save("qr_kod.png")
