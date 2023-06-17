import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect

        # Mendapatkan informasi dari barcode yang terdekripsi
        barcode_info = barcode.data.decode('utf-8')

        # Menandai barcode pada frame dengan persegi panjang hijau
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Menampilkan informasi barcode di atas persegi panjang hijau
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)

        # Menyimpan hasil barcode ke dalam file
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode: " + barcode_info)

    return frame

def main():
    # Membuka kamera
    camera = cv2.VideoCapture(0)

    # Mengecek apakah kamera berhasil dibuka
    if not camera.isOpened():
        print("Gagal membuka kamera")
        return

    # Membaca frame dari kamera
    ret, frame = camera.read()

    while ret:
        # Membaca frame dari kamera
        ret, frame = camera.read()

        # Mencari dan membaca barcode pada frame
        frame = read_barcodes(frame)

        # Menampilkan frame dengan barcode yang telah dibaca
        cv2.imshow('Barcode/QR code reader', frame)

        # Tombol 'ESC' untuk keluar dari program
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Melepaskan kamera dan menutup jendela tampilan
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
