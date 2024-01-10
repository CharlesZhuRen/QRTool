import qrcode
import cv2
from pyzbar import pyzbar


def encode(text: str, filename: str):
    img = qrcode.make(text)
    filepath = "img/" + filename + ".png"
    img.save(filepath)
    print("Save as {}".format(filepath))


def encode_advanced(text: str, filename: str, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filepath = "img/" + filename + ".png"
    img.save(filepath)

    print("Save as {}".format(filepath))


def decode(filepath):
    qr_code = cv2.imread(filepath)
    data = pyzbar.decode(qr_code)
    print(data)
    text = data[0].data.decode('utf-8')
    print(text)


def scan_qrcode(qr_code):
    data = pyzbar.decode(qr_code)
    return data[0].data.decode('utf-8')


def decode_via_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('scan qrcode', frame)

        text = None
        try:
            text = scan_qrcode(frame)
        except Exception as e:
            pass

        if text:
            print(text)
            break

        key = cv2.waitKey(10)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    # encode("Happy New Year", "p1")

    # decode('img/p1.png')

    decode_via_camera()
