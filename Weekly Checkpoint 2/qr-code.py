import qrcode

def main():
    song = "https://www.youtube.com/watch?v=Dkq3LD-4pmM"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(Fill_color = "blue", back_color = "white")
    img.save("youtube-qr.png")
    
if __name__=="__main__":
    main()
