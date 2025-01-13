import tkinter as tk
import tkinter.font as tkFont
import difflib

#TKİNTER ARA YÜZÜ OLAN
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

# Karakterler benzerliğini hesapladığımız bölüm:
def karakter_benzerlik(kitap1, kitap2):
    ortak_karakterler = set(kitap_ozellikleri[kitap1]['Karakterler']) & set(kitap_ozellikleri[kitap2]['Karakterler'])
    toplam_karakterler = set(kitap_ozellikleri[kitap1]['Karakterler']) | set(kitap_ozellikleri[kitap2]['Karakterler'])
    return len(ortak_karakterler) / len(toplam_karakterler)

# Olay örgüsü benzerliğine bakıyoruz:
def olay_benzerlik(kitap1, kitap2):
    return difflib.SequenceMatcher(None, kitap_ozellikleri[kitap1]['Olay Örgüsü'], kitap_ozellikleri[kitap2]['Olay Örgüsü']).ratio()

# Yazım dili benzerliğini hesaplama:
def yazim_benzerlik(kitap1, kitap2):
    return difflib.SequenceMatcher(None, kitap_ozellikleri[kitap1]['Yazım Dili'], kitap_ozellikleri[kitap2]['Yazım Dili']).ratio()

# Aşağıda kitaplar arasındaki benzerlikleri hesapladık:
def benzerlik_hesapla(kitap1, kitap2):
    # Kitapları alfabetik sıraya göre karşılaştırıyoruz, sıralama farklarını göz ardı ediyoruz!!! :
    if kitap1 > kitap2:
        kitap1, kitap2 = kitap2, kitap1  # Kitapları sıralayarak karşılaştırıyoruz(yüzdeliklerde problem çıkmasın diye).
    
    karakter_benzerlik_orani = karakter_benzerlik(kitap1, kitap2)
    olay_benzerlik_orani = olay_benzerlik(kitap1, kitap2)
    yazim_benzerlik_orani = yazim_benzerlik(kitap1, kitap2)
    
    # Benzerlikleri döndürme/tekrarlama:
    return karakter_benzerlik_orani, olay_benzerlik_orani, yazim_benzerlik_orani

# Tkinter arayüzü buradan itibaren başlıyor.
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitap Karşılaştırma")
        width = 600
        height = 650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Başlık Bölümü:
        self.title_label = tk.Label(root, text="Kitaplar Arasındaki Benzerlikleri Karşılaştırın", font=("Arial", 12))
        self.title_label.place(x=100, y=10, width=400, height=30)

        # Kita Listesi Bölümü:
        self.kitaplar = list(kitap_ozellikleri.keys())
        self.kitap1_var = tk.StringVar(root)
        self.kitap2_var = tk.StringVar(root)

        # 1. Kitap Seçimi Bölümü:
        self.kitap1_label = tk.Label(root, text="1. Kitabı Seçin:", font=("Arial", 10))
        self.kitap1_label.place(x=30, y=50)
        self.kitap1_menu = tk.OptionMenu(root, self.kitap1_var, *self.kitaplar)
        self.kitap1_menu.place(x=155, y=50, width=200)

        # 2. Kitap Seçimi Bölümü:
        self.kitap2_label = tk.Label(root, text="2. Kitabı Seçin:", font=("Arial", 10))
        self.kitap2_label.place(x=30, y=100)
        self.kitap2_menu = tk.OptionMenu(root, self.kitap2_var, *self.kitaplar)
        self.kitap2_menu.place(x=155, y=100, width=200)

        # 1. Kitap Karakterler Bölümü:
        self.kitap1_karakterler_label = tk.Label(root, text="1. Kitap Karakterler:", font=("Arial", 10))
        self.kitap1_karakterler_label.place(x=25, y=150)
        self.kitap1_karakterler_text = tk.Text(root, height=2, width=30, wrap=tk.WORD)
        self.kitap1_karakterler_text.place(x=155, y=150)

        # 2. Kitap Karakterler Bölümü:
        self.kitap2_karakterler_label = tk.Label(root, text="2. Kitap Karakterler:", font=("Arial", 10))
        self.kitap2_karakterler_label.place(x=25, y=200)
        self.kitap2_karakterler_text = tk.Text(root, height=2, width=30, wrap=tk.WORD)
        self.kitap2_karakterler_text.place(x=155, y=200)

        # 1. Kitap Olay Örgüsü Bölümü:
        self.kitap1_olay_label = tk.Label(root, text="1. Kitap Olay Örgüsü:", font=("Arial", 10))
        self.kitap1_olay_label.place(x=25, y=300)
        self.kitap1_olay_text = tk.Text(root, height=7, width=30, wrap=tk.WORD)
        self.kitap1_olay_text.place(x=155, y=250)

        # 2. Kitap Olay Örgüsü Bölümü:
        self.kitap2_olay_label = tk.Label(root, text="2. Kitap Olay Örgüsü:", font=("Arial", 10))
        self.kitap2_olay_label.place(x=25, y=420)
        self.kitap2_olay_text = tk.Text(root, height=7, width=30, wrap=tk.WORD)
        self.kitap2_olay_text.place(x=155, y=380)

        # 1. Kitap Yazım Dili Bölümü:
        self.kitap1_yazim_label = tk.Label(root, text="1. Kitap Yazım Dili:", font=("Arial", 10))
        self.kitap1_yazim_label.place(x=25, y=520)
        self.kitap1_yazim_text = tk.Text(root, height=2, width=30, wrap=tk.WORD)
        self.kitap1_yazim_text.place(x=155, y=510)

        # 2. Kitap Yazım Dili Bölümü:
        self.kitap2_yazim_label = tk.Label(root, text="2. Kitap Yazım Dili:", font=("Arial", 10))
        self.kitap2_yazim_label.place(x=25, y=570)
        self.kitap2_yazim_text = tk.Text(root, height=2, width=30, wrap=tk.WORD)
        self.kitap2_yazim_text.place(x=155, y=560)

        # Karşılaştırma butonunun kodu burada:
        self.compare_button = tk.Button(root, text="Karşılaştır", command=self.compare_books)
        self.compare_button.place(x=410, y=70, width=100, height=30)

        # Sonuçları göstereceğimiz bölümlerin kodları burada:
        self.result_label = tk.Label(root, text="Sonuçlar", font=("Arial", 12))
        self.result_label.place(x=410, y=120)

        self.character_label = tk.Label(root, text="Karakter Benzerliği: ", font=("Arial", 10))
        self.character_label.place(x=410, y=160)

        self.plot_label = tk.Label(root, text="Olay Örgüsü Benzerliği: ", font=("Arial", 10))
        self.plot_label.place(x=410, y=190)

        self.style_label = tk.Label(root, text="Yazım Dili Benzerliği: ", font=("Arial", 10))
        self.style_label.place(x=410, y=220)

        self.overall_label = tk.Label(root, text="Genel Benzerlik: ", font=("Arial", 10))
        self.overall_label.place(x=410, y=250)

        # Tekrar Karşılaştırma Butonu:
        self.restart_button = tk.Button(root, text="Tekrar Karşılaştırma Yap", command=self.restart_comparison)
        self.restart_button.place(x=410, y=300, width=150, height=30)

    def compare_books(self):
        kitap1 = self.kitap1_var.get()
        kitap2 = self.kitap2_var.get()
        
        # Karakterler, olay örgüsü ve yazım dili metinlerini gösterdiğimiz bölümlerin kodları:
        self.kitap1_karakterler_text.delete(1.0, tk.END)
        self.kitap2_karakterler_text.delete(1.0, tk.END)
        self.kitap1_karakterler_text.insert(tk.END, '\n'.join(kitap_ozellikleri[kitap1]['Karakterler']))
        self.kitap2_karakterler_text.insert(tk.END, '\n'.join(kitap_ozellikleri[kitap2]['Karakterler']))

        self.kitap1_olay_text.delete(1.0, tk.END)
        self.kitap2_olay_text.delete(1.0, tk.END)
        self.kitap1_olay_text.insert(tk.END, kitap_ozellikleri[kitap1]['Olay Örgüsü'])
        self.kitap2_olay_text.insert(tk.END, kitap_ozellikleri[kitap2]['Olay Örgüsü'])

        self.kitap1_yazim_text.delete(1.0, tk.END)
        self.kitap2_yazim_text.delete(1.0, tk.END)
        self.kitap1_yazim_text.insert(tk.END, kitap_ozellikleri[kitap1]['Yazım Dili'])
        self.kitap2_yazim_text.insert(tk.END, kitap_ozellikleri[kitap2]['Yazım Dili'])
        
        # Benzerlik hesaplama:
        karakter_benzerlik_orani, olay_benzerlik_orani, yazim_benzerlik_orani = benzerlik_hesapla(kitap1, kitap2)
        genel_benzerlik = (karakter_benzerlik_orani + olay_benzerlik_orani + yazim_benzerlik_orani) / 3
        
        # Sonuçları gösterme:
        self.character_label.config(text=f"Karakter Benzerliği: %{karakter_benzerlik_orani * 100:.2f}")
        self.plot_label.config(text=f"Olay Örgüsü Benzerliği: %{olay_benzerlik_orani * 100:.2f}")
        self.style_label.config(text=f"Yazım Dili Benzerliği: %{yazim_benzerlik_orani * 100:.2f}")
        self.overall_label.config(text=f"Genel Benzerlik: %{genel_benzerlik * 100:.2f}")

    def restart_comparison(self):
        self.kitap1_var.set("")
        self.kitap2_var.set("")
        self.character_label.config(text="Karakter Benzerliği: ")
        self.plot_label.config(text="Olay Örgüsü Benzerliği: ")
        self.style_label.config(text="Yazım Dili Benzerliği: ")
        self.overall_label.config(text="Genel Benzerlik: ")

         # Tüm metin kutularını sıfırlıyoruz.
        self.kitap1_karakterler_text.delete(1.0, tk.END)
        self.kitap2_karakterler_text.delete(1.0, tk.END)
        self.kitap1_olay_text.delete(1.0, tk.END)
        self.kitap2_olay_text.delete(1.0, tk.END)
        self.kitap1_yazim_text.delete(1.0, tk.END)
        self.kitap2_yazim_text.delete(1.0, tk.END)

        # Sonuçları sıfırlıyoruz.
        self.character_label.config(text="Karakter Benzerliği: ")
        self.plot_label.config(text="Olay Örgüsü Benzerliği: ")
        self.style_label.config(text="Yazım Dili Benzerliği: ")
        self.overall_label.config(text="Genel Benzerlik: ")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
