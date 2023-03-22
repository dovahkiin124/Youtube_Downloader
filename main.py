from pytube import YouTube
#Ia url-u videoului
url=input("Intrudu url-ul videoului de pe Youtube: ")
#Creeaza un obiect Youtube nou
video=YouTube(url)
#Ia calitatea cea mai inalta pe care o poate suporta videoul
stream=video.streams.get_highest_resolution()
#Downloadeaza videoul
stream.download("C:/Users/Asus/videos")


