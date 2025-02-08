import pyshorteners
import qrcode
import matplotlib.pyplot as plt


def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)


def generate_qr(url):
    qr = qrcode.make(url)
    plt.imshow(qr, cmap='gray')
    plt.axis('off')
    plt.show()


def main():
    original_url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(original_url)
    print(f"Shortened URL: {shortened_url}")

    generate_qr(shortened_url)
    print("QR Code displayed successfully!")


if __name__ == "__main__":
    main()
