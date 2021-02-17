import io

from PIL import Image
from pyzbar.pyzbar import decode


class PaymentQRCode:
    def __init__(self, qr_code_image):
        self.qr_code_image = qr_code_image
        self.n1_app_launch_code = ""
        self.n2_sys_mark = ""
        self.n3_version = ""
        self.n4_codepage = ""
        self.n5_function = ""
        self.n6_bic = ""
        self.n7_recipient = ""
        self.n8_account = ""
        self.n9_currency = ""
        self.n9_amount = ""
        self.n10_recipient_code = ""
        self.n11_goal = ""
        self.n12_invoice_reference = ""
        self.n13_payment_purpose = ""
        self.n14_display = ""
        self.qr_decoded = ""

    def parse(self):
        self.qr_decoded = decode(Image.open(self.qr_code_image))
        binary_stream = io.BytesIO()
        binary_stream.write(self.qr_decoded[0].data)
        binary_stream.seek(0)
        _lines = list(map(lambda x: x[:-1].decode("utf-8"), binary_stream.readlines()))
        if len(_lines) > 0: self.n1_app_launch_code = _lines[0]
        if len(_lines) > 1: self.n2_sys_mark = _lines[1]
        if len(_lines) > 2: self.n3_version = _lines[2]
        if len(_lines) > 3: self.n4_codepage = _lines[3]
        if len(_lines) > 4: self.n5_function = _lines[4]
        if len(_lines) > 5: self.n6_bic = _lines[5]
        if len(_lines) > 6: self.n7_recipient = _lines[6]
        if len(_lines) > 7: self.n8_account = _lines[7]
        if len(_lines) > 8:
            self.n9_currency = _lines[8][:3]
            self.n9_amount = float(_lines[8][3:])
        if len(_lines) > 9: self.n10_recipient_code = _lines[9]
        if len(_lines) > 10: self.n11_goal = _lines[10]
        if len(_lines) > 11: self.n12_invoice_reference = _lines[11]
        if len(_lines) > 12: self.n13_payment_purpose = _lines[12]
        if len(_lines) > 13: self.n14_display = _lines[13]
        return self

    def __str__(self):
        return f"RAW QR-code data: {self.qr_decoded}\n" \
               f"Application launch code: {self.n1_app_launch_code}\n" \
               f"System mark: {self.n2_sys_mark}\n" \
               f"Version: {self.n3_version}\n" \
               f"Encoding type: {self.n4_codepage}\n" \
               f"Function: {self.n5_function}\n" \
               f"BIC: {self.n6_bic}\n" \
               f"Recipient: {self.n7_recipient}\n" \
               f"Recipient's account: {self.n8_account}\n" \
               f"Amount and Currency: {self.n9_currency} {self.n9_amount}\n" \
               f"Recipient's identifier: {self.n10_recipient_code}\n" \
               f"Goal: {self.n11_goal}\n" \
               f"Reference: {self.n12_invoice_reference}\n" \
               f"Payment purpose: {self.n13_payment_purpose}\n" \
               f"Display: {self.n14_display}\n"
