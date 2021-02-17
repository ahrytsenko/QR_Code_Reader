from payment_qr_code.paymentqrcode import PaymentQRCode


def parse_qr_code(image_file):
    qr_code = PaymentQRCode(image_file)
    print(qr_code.parse())


parse_qr_code('data\\qrcode01.png')
parse_qr_code('data\\qrcode02.png')
parse_qr_code('data\\qrcode03.png')
parse_qr_code('data\\qrcode04.png')
parse_qr_code('data\\qrcode0501.png')
parse_qr_code('data\\qrcode0502.png')
parse_qr_code('data\\qrcode0601.png')
parse_qr_code('data\\qrcode0602.png')
parse_qr_code('data\\qrcode0701.png')
parse_qr_code('data\\qrcode0702.png')
