import math

# Noktaların Tanımlanması
noktalar = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Örnek noktalar, isteğe bağlı olarak değiştirilebilir

# Öklid Mesafesi İçin Fonksiyon Tanımlama
def öklidMesafesi(nokta1, nokta2):
    x1, y1 = nokta1
    x2, y2 = nokta2
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

# Mesafelerin Hesaplanması
mesafeler = []
for i in range(len(noktalar)):
    for j in range(i+1, len(noktalar)):
        mesafe = öklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum Mesafenin Bulunması
min_mesafe = min(mesafeler)
print("Minimum mesafe:", min_mesafe)
