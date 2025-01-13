import difflib

#TKİNTER ARA YÜZÜ OLMAYAN
# Aşağıda kitapları ve özelliklerini verdik.

kitap_ozellikleri = {
    'Dune': {
        'Karakterler': ['Paul Atreides', 'Duke Leto Atreides', 'Baron Harkonnen'],
        'Olay Örgüsü': '''Paul Atreides, Arrakis gezegenine hükmetmeye gelen bir aristokrat ailesinin varisi olarak, gezegenin sahip olduğu değerli baharat üretiminin ortasında bir iç savaşın içine çekilir. Paul, ailesini korumak için zor bir yolculuğa çıkar ve Arrakis'in yerel halkı Fremenler ile işbirliği yaparak bu gezegeni fethetmeye çalışır. Aksiyon, ihanet, kehanet ve liderlik temaları işlenir.''',
        'Yazım Dili': 'Bilim kurgu, epik, felsefi'
    },
    'Romeo ve Juliet': {
        'Karakterler': ['Romeo Montague', 'Juliet Capulet', 'Mercutio'],
        'Olay Örgüsü': '''İki genç, Romeo ve Juliet, aileleri arasında süregelen düşmanlığa rağmen birbirlerine aşık olurlar. Ancak, ailelerinin savaşları yüzünden birbirlerine kavuşamazlar. Romeo ve Juliet’in trajik hikâyesi, aşk, aile, öfke ve kader gibi evrensel temaları işler.''',
        'Yazım Dili': 'Trajik, dramatik, şiirsel'
    },
    'Sherlock Holmes': {
        'Karakterler': ['Sherlock Holmes', 'Dr. Watson', 'Professor Moriarty'],
        'Olay Örgüsü': '''Sherlock Holmes, dedektiflik yetenekleriyle ünlü bir kahramandır. Dr. Watson ise ona yardımcı olan sadık arkadaşıdır. Holmes, zeka ve gözlem yeteneklerini kullanarak, karmaşık suçları çözmeye çalışırken, en büyük düşmanı olan Professor Moriarty ile mücadele eder. Romanlar, mantık, dedektiflik ve insan doğasının karanlık yönlerini işler.''',
        'Yazım Dili': 'Dedektif, mantıklı, analitik'
    },
    'Harry Potter': {
        'Karakterler': ['Harry Potter', 'Hermione Granger', 'Ron Weasley'],
        'Olay Örgüsü': '''Harry Potter, büyücü dünyasına ait bir yetimdir ve Hogwarts adlı büyücülük okuluna kabul edilir. Hogwarts'ta yeni arkadaşlar edinirken, karanlık güçlerin lideri olan Lord Voldemort ile savaşmaya başlar. Aile, dostluk ve cesaret temaları bu fantastik seride işler.''',
        'Yazım Dili': 'Fantastik, macera, çocuk edebiyatı'
    },
    'Fahrenheit 451': {
        'Karakterler': ['Guy Montag', 'Clarisse McClellan', 'Captain Beatty'],
        'Olay Örgüsü': '''Guy Montag, kitapları yakmakla görevli bir itfaiyecidir. Ancak, Clarisse ile tanıştıktan sonra, kitapların aslında çok değerli olduğunu fark eder ve toplumda başkaldırarak özgür düşünceyi savunmaya başlar. Kitaplar, özgürlük ve bilinçlenme üzerine bir alegoridir.''',
        'Yazım Dili': 'Distopik, alegorik, felsefi'
    },
    '1984': {
        'Karakterler': ['Winston Smith', 'Big Brother', 'Julia'],
        'Olay Örgüsü': 'Totaliter bir toplumda bireysel özgürlüğü savunma çabası.',
        'Yazım Dili': 'Distopik, sert, düşündürücü'
    },
    'The Great Gatsby': {
        'Karakterler': ['Jay Gatsby', 'Nick Carraway', 'Daisy Buchanan'],
        'Olay Örgüsü': '1920’lerin Amerika’sındaki sınıf farkları, aşk ve hayallerin peşinden gitmek.',
        'Yazım Dili': 'Romantik, yüce, yoğun'
    },
    'Moby Dick': {
        'Karakterler': ['Ishmael', 'Ahab', 'Moby Dick'],
        'Olay Örgüsü': 'Bir balina avına çıkan denizcilerin öyküsü.',
        'Yazım Dili': 'Felsefi, detaylı, destansı'
    },
    'War and Peace': {
        'Karakterler': ['Pierre Bezukhov', 'Andrei Bolkonsky', 'Natasha Rostova'],
        'Olay Örgüsü': 'Napolyon’un Rusya’yı işgali ve etkileri.',
        'Yazım Dili': 'Destansı, tarihi, dramatik'
    },
    'Frankenstein': {
        'Karakterler': ['Victor Frankenstein', 'Yaratık'],
        'Olay Örgüsü': 'Bilim insanı Victor Frankenstein’ın yarattığı yaratıkla mücadelesi.',
        'Yazım Dili': 'Gotik, korku, dram'
    },
    'Pride and Prejudice': {
        'Karakterler': ['Elizabeth Bennet', 'Mr. Darcy'],
        'Olay Örgüsü': 'Toplumsal sınıf, aşk ve evlilik üzerine bir hikaye.',
        'Yazım Dili': 'Romantik, toplumsal eleştiri'
    },
    'To Kill a Mockingbird': {
        'Karakterler': ['Scout Finch', 'Atticus Finch', 'Tom Robinson'],
        'Olay Örgüsü': 'Güney Amerika’da ırkçılıkla mücadele, adaletin sorgulanması.',
        'Yazım Dili': 'Duygusal, etkileyici'
    },
    'The Catcher in the Rye': {
        'Karakterler': ['Holden Caulfield'],
        'Olay Örgüsü': 'Ergenlik, yalnızlık ve toplumsal dışlanma üzerine bir içsel yolculuk.',
        'Yazım Dili': 'İçsel, bireysel, samimi'
    },
    'The Hobbit': {
        'Karakterler': ['Bilbo Baggins', 'Gandalf', 'Thorin'],
        'Olay Örgüsü': 'Bir grup cüce ile büyük bir hazineyi aramak için yapılan yolculuk.',
        'Yazım Dili': 'Fantastik, eğlenceli, macera dolu'
    },
    'Brave New World': {
        'Karakterler': ['Bernard Marx', 'Lenina Crowne'],
        'Olay Örgüsü': 'Yapay bir toplumda bireysel özgürlüklerin kaybı.',
        'Yazım Dili': 'Distopik, eleştirel'
    },
    'Dracula': {
        'Karakterler': ['Count Dracula', 'Jonathan Harker'],
        'Olay Örgüsü': 'Bir vampirin Londra’ya gelmesi ve insanları etkisi altına alması.',
        'Yazım Dili': 'Gotik, korku'
    },
    'The Odyssey': {
        'Karakterler': ['Odysseus'],
        'Olay Örgüsü': 'Yunan kahramanı Odysseus’un evine dönüş yolculuğu.',
        'Yazım Dili': 'Destansı, mitolojik'
    },
    'The Brothers Karamazov': {
        'Karakterler': ['Dmitri Karamazov', 'Ivan Karamazov', 'Alyosha Karamazov'],
        'Olay Örgüsü': 'Ahlaki çatışmalar, kardeşler arasındaki ilişkiler.',
        'Yazım Dili': 'Felsefi, derin'
    },
    'Crime and Punishment': {
        'Karakterler': ['Rodion Raskolnikov', 'Sonia Marmeladov'],
        'Olay Örgüsü': 'Bir cinayet işleyen adamın vicdanı ile mücadelesi.',
        'Yazım Dili': 'Psikolojik, dramatik'
    }
}

# Kitapları listeliyoruz.
def kitaplar_listele():
    print("Kitaplar: ")
    kitaplar = list(kitap_ozellikleri.keys())
    for index, kitap in enumerate(kitaplar, 1):
        print(f"{index}. {kitap}")
    return kitaplar

# Karakterler benzerliğini hesaplıyoruz burada.
def karakter_benzerlik(kitap1, kitap2):
    ortak_karakterler = set(kitap_ozellikleri[kitap1]['Karakterler']) & set(kitap_ozellikleri[kitap2]['Karakterler'])
    toplam_karakterler = set(kitap_ozellikleri[kitap1]['Karakterler']) | set(kitap_ozellikleri[kitap2]['Karakterler'])
    return len(ortak_karakterler) / len(toplam_karakterler)

# Olay örgüsü benzerliğini hesaplıyoruz.
def olay_benzerlik(kitap1, kitap2):
    return difflib.SequenceMatcher(None, kitap_ozellikleri[kitap1]['Olay Örgüsü'], kitap_ozellikleri[kitap2]['Olay Örgüsü']).ratio()

# Yazım dili benzerliğini hesaplıyoruz.
def yazim_benzerlik(kitap1, kitap2):
    return difflib.SequenceMatcher(None, kitap_ozellikleri[kitap1]['Yazım Dili'], kitap_ozellikleri[kitap2]['Yazım Dili']).ratio()

# Kitaplar arasındaki benzerlikleri hesaplama
def benzerlik_hesapla(kitap1, kitap2):
    karakter_benzerlik_orani = karakter_benzerlik(kitap1, kitap2)
    olay_benzerlik_orani = olay_benzerlik(kitap1, kitap2)
    yazim_benzerlik_orani = yazim_benzerlik(kitap1, kitap2)
    
    print(f"\n{kitap1} ve {kitap2} arasındaki karşılaştırmalar:")
    
    # Karakterler karşılaştırması
    print(f"\nKarakterler Benzerliği: %{karakter_benzerlik_orani * 100:.2f}")
    print(f"{kitap1} Karakterleri: {', '.join(kitap_ozellikleri[kitap1]['Karakterler'])}")
    print(f"{kitap2} Karakterleri: {', '.join(kitap_ozellikleri[kitap2]['Karakterler'])}")
    
    # Olay örgüsü karşılaştırması
    print(f"\nOlay Örgüsü Benzerliği: %{olay_benzerlik_orani * 100:.2f}")
    print(f"{kitap1} Olay Örgüsü: {kitap_ozellikleri[kitap1]['Olay Örgüsü']}")
    print(f"{kitap2} Olay Örgüsü: {kitap_ozellikleri[kitap2]['Olay Örgüsü']}")
    
    # Yazım dili karşılaştırması
    print(f"\nYazım Dili Benzerliği: %{yazim_benzerlik_orani * 100:.2f}")
    print(f"{kitap1} Yazım Dili: {kitap_ozellikleri[kitap1]['Yazım Dili']}")
    print(f"{kitap2} Yazım Dili: {kitap_ozellikleri[kitap2]['Yazım Dili']}")
    
    # Ortalamasını döndür
    ortalama_benzerlik = (karakter_benzerlik_orani + olay_benzerlik_orani + yazim_benzerlik_orani) / 3
    return ortalama_benzerlik

# Kitapları karşılaştırma
def kitaplari_karistir():
    kitaplar = kitaplar_listele()
    secim1 = int(input(f"Hangi kitapla karşılaştırma yapmak istersiniz? (1-{len(kitaplar)}): "))
    secim2 = int(input(f"Karşılaştırılacak diğer kitabı seçin (1-{len(kitaplar)}): "))
    
    kitap1 = kitaplar[secim1 - 1]
    kitap2 = kitaplar[secim2 - 1]

    benzerlik = benzerlik_hesapla(kitap1, kitap2)
    print(f"\n{kitap1} ve {kitap2} arasındaki genel benzerlik oranı: %{benzerlik * 100:.2f}")

# Kullanıcıya tekrar kitap karşılaştırması yapma seçeneği sunma
def tekrar_karistir():
    while True:
        kitaplari_karistir()
        devam = input("Başka bir karşılaştırma yapmak ister misiniz? (Evet/Hayır): ").strip().lower()
        if devam != 'evet':
            break

# Ana fonksiyon
if __name__ == "__main__":
    tekrar_karistir()
