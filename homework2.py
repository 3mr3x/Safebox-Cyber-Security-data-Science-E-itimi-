class Film:
    def __init__(self, ad, yonetmen, yil):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil

class FilmDeposu:
    def __init__(self):
        self.filmler = []
    
    def film_ekle(self, film):
        self.filmler.append(film)
    
    def film_ara(self, ad):
        for film in self.filmler:
            if film.ad == ad:
                return film
        return None

# FilmDeposu örneği oluşturalım
depo = FilmDeposu()

# Film ekleyelim
film1 = Film("The Shawshank Redemption", "Frank Darabont", 1994)
depo.film_ekle(film1)

film2 = Film("The Godfather", "Francis Ford Coppola", 1972)
depo.film_ekle(film2)

# Film arayalım
film_ad = "The Shawshank Redemption"
aranan_film = depo.film_ara(film_ad)

if aranan_film:
    print("Film bulundu:")
    print("Ad:", aranan_film.ad)
    print("Yönetmen:", aranan_film.yonetmen)
    print("Yıl:", aranan_film.yil)
else:
    print("Film bulunamadı.")
