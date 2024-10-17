import os
import random # supaya damage dari pemain dan musuh yang dilawan menjadi random(pada dasarnya ini adalah game judi)
os.system('cls') 

# sebuah fungtion agar pemain wajib untuk memasukkan username 
def tentukan_username():
    global username
    while True:
        os.system('cls')
        username = input("masukan username untuk karakter anda: ")

        if username.strip() == "":
            print("mohon masukan username untuk karakter anda\n")
            os.system('pause')
        else:
            break

# sebuah function untuk menentukan role yang pemain pilih
def tentukan_role():
    global role
    global pakaian
    global senjata
    while True:       
        os.system('cls')
        print("1.kesatria")
        print("2.penyihir")
        pilihan_role = input("masukan role yang anda inginkan (1,2): ")

        if pilihan_role == "1":
            role = "kesatria"
            pakaian = "full armor"
            senjata = "pedang"
            break
        elif pilihan_role == "2":
            role = "penyihir"
            pakaian = "jubah penyihir"
            senjata = "tongkat sihir"
            break
        else:
            print("mohon masukan sesuai role yang ada")
            os.system('pause')

# sebuah function untuk masuk ke menu jelajahi hutan
def jelajahi_hutan():
    while True:
        os.system('cls')
        print(f"""jadi aku pun memutuskan untuk menjelajahi hutan yang dianggap oleh orang orang di desa sebagai hutan terlarang karena telah memakan 
banyak korban,tapi aku tetap memutuskan untuk menjelajahinya,yaa sapa tau dapat harta karun atau apalah gitu yang dapat membuatku kaya
""")
        input("klik enter untuk lanjut")
        os.system('cls')

        print("setelah beberapa jam aku menjelajahi hutan,aku tidak sengaja menemukan sebuah papan tulisan yang bertulis\n")
        print("1.kiri = dungeon kramat")
        print("2.lurus = bukit")
        print("3.kanan = sungai")
        rute = input("pilih rute (1/2/3): ")

        if rute == "1":
            melawan_ambatron()
            break
        elif rute == "2":
            os.system('cls')
            print("aku memutuskan pergi lurus ke bukit untuk istirahat sejenak sambil melihat pemandangan hutan dari atas bukit\n")
            input("klik enter untuk lanjut")
            os.system('cls')
            print("sialnya aku malah di mangsa oleh semut raksasa yang rupanya sama ngeselin kayak semut yang membuatku mati terpleset,tentunya aku pun modar dibuatnya\n")
            break
        elif rute == "3":
            os.system('cls')
            print("aku memutuskan pergi ke kanan menuju sungai untuk mengambil air dari sungai karena aku merasa haus\n")
            input("klik enter untuk lanjut")
            os.system('cls')
            print("setelah aku meminum air sungai,aku pun modar dibuatnya karena sungai tersebut ternyata mengandung eek semut raksasa")
            break
        else:
            print("\nsepertinya aku tersesat di hutan dan\n")
            break

# sebuah menu untuk gelut dengan si ambatron
def melawan_ambatron():
    nyawa = 100
    # agar damage dari kestria dan penyihir bisa beda
    if role == "kesatria":
        skill = random.randrange(5, 35)
        skill2 = random.randrange(15, 30)
    if role == "penyihir":
        skill = random.randrange(1, 50)
        skill2 = random.randrange(10, 25)

    # untuk menyatakan total hp awal milik musuh dan damage dari musuh
    nyawa_musuh = 350
    skill_musuh = random.randrange(1, 10)
    os.system('cls')

    print("""dari informasi yang kudapat dari desa,dungeon adalah sebuah tempat dimana banyak harta dan item bisa ditemukan,
maka dari itu aku pun memutuskan untuk memasuki dungeon kramat ini,agar bisa kaya dan hidup tentram di dunia ini
          """)
    input("klik enter untuk lanjut") 
    os.system('cls')
    print("""aku sudah menelusuri dungeon ini selama hampir setengah hari mungkin,karena di dungeon ini sama sekali tidak ada
yang namanya cahaya matahari,jadi aku tak tau secara tepat sudah berapa lama aku disini,mana aku 
ga bawa makanan sama sekali lagi,mana aku sama sekali belum dapat apa-apa lagi,pengen mulihhhh!!,
jadi aku pun mencoba ke luar dari dungeon ini
""")
    input("klik enter untuk lanjut") 
    os.system('cls')
    print("""dalam perjalanan keluar dari dungeon ini,aku tidak sengaja bertemu dengan sebuah monster dengan kepala manusia
berbadan robot,dari rumor yang kudapat,monster tersebut bernama ambatron,sebuah monster paling kuat di dunia ini,
bahkan raja iblis pun ketar-ketir melihat sosok agung sang ambatron,dan aku pun tak ada pilihan lain selain harus
melawannya,karena dia menghalangi jalan keluar dari dungeon ini
""")
    input("klik enter untuk lanjut") 
    os.system('cls')
    print(f"""anda saat ini sedang melawan sang ambatron dengan rank SSSSSSS dan memliki HP sebesar: {nyawa_musuh}
coba kalahkan monster tersebut menggunakan skill yang anda punya
          """)

    while nyawa_musuh > 0 and nyawa > 0: # agar gelutnya bisa terus terusan sampai salah satu dari mereka ada yang menang

        if role == "kesatria":
            print("Skill:")
            print("1. pedang")
            print("2. perisai")
            
        elif role == "penyihir":
            print("Skill:")
            print("1. angin")
            print("2. tanah")

        pilihan_skill = input("pilih skill (1/2): ")

        if pilihan_skill == "1":
            damage = skill
        elif pilihan_skill == "2":
            damage = skill2
        else:
            damage = 0  

        if damage > 0: # kondisi dimana pemain memilih opsi skill yang ada
            os.system('cls')
            nyawa_musuh -= damage
            print(f"anda menyerang ambatron dan menghasilkan damage sebesar: {damage}")
            print(f"HP musuh: {nyawa_musuh}")

            if nyawa_musuh <= 0:
                os.system('cls')
                print('''aku tak percaya dapat mengalahkan sang ambatron,blud ini gayanya sok keras,kalo di gas ternyata sesak nafas,
dan secara misterius,sebuah portal tiba tiba muncul di depan ku dan terdengar sebuah suara yang mengucapkan 
"selamat pahlawan!,kamu telah menyelamatkan dunia ini dari sang ambatron,maka datanglah era kedamaian!,
sebagai hadiah atas jasa anda,anda dapat memasuki portal ini untuk kembali ke dunia asal anda"
                      
1.kembali ke dunia asal
2.kembali ke desa''')
                kembali_ke = input("anda ingin kembali ke mana? (1/2): ")
                if kembali_ke == "1":
                    os.system('cls')
                    print("aku pun memutuskan untuk kembali ke dunia asal dan menjalani kehidupan bosanku sebagai mahasiswa utm\n")
                    break
                elif kembali_ke == "2":
                    os.system('cls')
                    print("aku pun memutuskan untuk kembali ke desa karena aku bosan dengan kehidupan lamaku\n")
                    break
            
            nyawa -= skill_musuh
            print(f"\nanda diserang oleh ambatron dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                os.system('cls')
                print("sepertinya memang tidak ada cara menang dari sang ambatron\n")
                break
       
        elif damage <= 0: # kondisi dimana pemain salah/tidak memilih opsi skill yang ada
            os.system('cls')

            nyawa_musuh -= damage
            print(f"anda tidak menyerang dan menghasilkan damage sebesar: {damage}")
            print(f"HP ambatron: {nyawa_musuh}")

            nyawa -= skill_musuh
            print(f"\nanda diserang oleh ambatron dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                os.system('cls')
                print("sepertinya memang tidak ada cara menang dari sang ambatron\n")
                break     

# sebuah menu untuk gelut dengan si slime
def melawan_slime():
    nyawa = 100
    # agar damage dari kestria dan penyihir bisa beda
    if role == "kesatria":
        skill = random.randrange(5, 35)
        skill2 = random.randrange(15, 30)
    if role == "penyihir":
        skill = random.randrange(1, 50)
        skill2 = random.randrange(10, 25)

    # untuk menyatakan total hp awal milik musuh dan damage dari musuh
    nyawa_musuh = 50
    skill_musuh = random.randrange(1, 40)
    os.system('cls')

    print(f"""anda saat ini sedang melawan monster slime dengan rank XL dan memliki HP sebesar: {nyawa_musuh}
coba kalahkan monster tersebut menggunakan skill yang anda punya
          """)

    while nyawa_musuh > 0 and nyawa > 0: # agar gelutnya bisa terus terusan sampai salah satu dari mereka ada yang menang

        if role == "kesatria":
            print("Skill:")
            print("1. pedang")
            print("2. perisai")
            
        elif role == "penyihir":
            print("Skill:")
            print("1. angin")
            print("2. tanah")

        pilihan_skill = input("pilih skill (1/2): ")

        if pilihan_skill == "1":
            damage = skill
        elif pilihan_skill == "2":
            damage = skill2
        else:
            damage = 0  

        if damage > 0: # kondisi dimana pemain memilih opsi skill yang ada
            os.system('cls')
            nyawa_musuh -= damage
            print(f"anda menyerang dan menghasilkan damage sebesar: {damage}")
            print(f"HP musuh: {nyawa_musuh}")

            if nyawa_musuh <= 0:
                print("\nSelamat! Anda menang.")
                break
            
            nyawa -= skill_musuh
            print(f"\nanda diserang oleh slime dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                print("Yahahaha noob")
                break
       
        elif damage <= 0: # kondisi dimana pemain salah/tidak memilih opsi skill yang ada
            os.system('cls')

            nyawa_musuh -= damage
            print(f"anda tidak menyerang dan menghasilkan damage sebesar: {damage}")
            print(f"HP musuh: {nyawa_musuh}")

            nyawa -= skill_musuh
            print(f"\nanda diserang oleh slime dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                print("Yahahaha noob")
                break

# submenu untuk melawan raja iblis
def melawan_raja_iblis():
    nyawa = 100
    # agar damage dari kestria dan penyihir bisa beda
    if role == "kesatria":
        skill = random.randrange(5, 35)
        skill2 = random.randrange(15, 30)
    if role == "penyihir":
        skill = random.randrange(1, 50)
        skill2 = random.randrange(10, 25)

    nyawa_musuh = 200
    skill_musuh = random.randrange(5, 20)
    os.system('cls')

    print(f"""anda saat ini sedang melawan sang raja iblis dengan rank SSSSSSS dan memliki HP sebesar: {nyawa_musuh}
coba kalahkan monster tersebut menggunakan skill yang anda punya
          """)

    while nyawa_musuh > 0 and nyawa > 0: # agar gelutnya bisa terus terusan sampai salah satu dari mereka ada yang menang

        if role == "kesatria":
            print("Skill:")
            print("1. pedang")
            print("2. perisai")
        elif role == "penyihir":
            print("Skill:")
            print("1. angin")
            print("2. tanah")

        pilihan_skill = input("pilih skill (1/2): ")

        if pilihan_skill == "1":
            damage = skill
        elif pilihan_skill == "2":
            damage = skill2
        else:
            damage = 0  

        if damage > 0:
            os.system('cls')

            nyawa_musuh -= damage
            print(f"anda menyerang dan menghasilkan damage sebesar: {damage}")
            print(f"HP musuh: {nyawa_musuh}")

            if nyawa_musuh <= 0:
                print("\nSelamat! Anda menang.")
                break
            
            nyawa -= skill_musuh
            print(f"\nanda diserang oleh raja iblis dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                print("Yahahaha noob")
                break
        elif damage <= 0:
            os.system('cls')

            nyawa_musuh -= damage
            print(f"anda tidak menyerang dan menghasilkan damage sebesar: {damage}")
            print(f"HP musuh: {nyawa_musuh}")

            nyawa -= skill_musuh
            print(f"\nanda diserang oleh raja iblis dengan Damage sebesar: {skill_musuh}")
            print(f"HP karakter anda: {nyawa}\n")

            if nyawa <= 0:
                print("Yahahaha noob")
                break
   
# menu untuk menampung opsi lawan slime atau raja iblis
def melawan_monster():
    while True:
        os.system('cls')
        print(f"""aku memang sedang mencari monster,tapi aku tidak menyangka akan langsung bertemu dengan monster yang sangat kuat,
dan sepertinya tidak ada opsi untuk kabur,terpaksa aku harus melawan salah satu dari mereka
              """)
        print("1.slime")
        print("2.raja iblis")
        pilihan_monster = input("pilih monster yang ingin anda lawan (1/2): ")

        if pilihan_monster == "1":
            melawan_slime()
            break
        elif pilihan_monster == "2":
            melawan_raja_iblis()
            break
        else:
            print("\npilih salah satu monster untuk dilawan bodo,jangan jadi pengecut,kau itu tidak bisa lari dari mereka\n")
            os.system('pause')
            
# menu pergi ke desa magis
def pergi_kedesa_magis():
    while True:
        os.system('cls')
        print("""ternyata desa magis yang banyak dibicarakan oleh orang-orang memang seramai apa yang mereka bicarakan,
jujur aja bingung mau mencari apa disini,kurasa aku akan coba untuk keliling dulu\n""")
        input("klik enter untuk lanjut ")
        os.system('cls')
        print("""saat aku keliling di desa magis,aku tidak sengaja melihat seorang kakek kakek yang sedang kesusahan membawa 
barang belanjaannya,dan sepertinya tidak ada yang mau menolongnya,jadi aku pun memutuskan untuk:
              
1.pergi menolongnya
2.pergi membiarkannya""")
        kakek = input("kamu ingin menolongnya atau membiarkannya? (1/2): ")
        if kakek == "1":
            os.system('cls')
            print(f'''{username} = "halo kek,apakah kakek mau saya bantu mengangkat barang belanjaan kakek?,karena seperti kakek ini sedang kesusahan membawanya"
kakek = "ohhh boleh anak muda,mohon bantuannya ya….wahh senang sekali rasanya punggung ini,terima kasih banyak ya sudah mau membantu kakek,tenang saja,rumah kakek tidak jauh dari sini"
{username} = "oh iya sama sama kek,omong omong kakek ini ga ada anak,cucu atau mungkin istri kakek kah untuk membantu kakek?,karena sepertinya kakek ini sudah terlalu tua untuk hidup sendiri"
kakek = "tidak ada,mereka semua sudah meninggal(ucap kakek dengan muka sedih)"
{username} = "kalau boleh tau,kenapa mereka bisa meninggal kek?"
kakek = "mereka meninggal karena di bunuh oleh monster paling kejam yang sudah mengancam dunia ini selama bertahun tahun,nama monsternya adalah ambatron"
{username} = "ternyata kakek ini adalah orang yang kuat,kalo itu aku,mungkin aku hanya akan pasrah dan mengakhiri hidupku"
kakek = "kakek tidaklah sekuat itu,alasan kenapa kakek tetap hidup hanya karena kakek tetap menjaga kenangan tentang mereka sampai ada orang yang mengalahkan si ambatron"
{username} = "tenang saja kek,seseorang pasti akan mengalahkan ambatron"
kakek = "ya semoga saja ya nak,sampai sini saja nak,makasih ya karena sudah mau membantu kakek tua ini
{username} = "iya sama sama kek"
''')
            input("klik enter untuk lanjut")
            os.system('cls')
            print("setelah itu aku pun kembali jalan jalan di desa magis dan pada akhirnya kembali ke desa sleman\n")
            break
        elif kakek == "2":
            os.system('cls')
            print(f'''aku memutuskan untuk tidak menolongnya karena aku berpikir seseorang pada akhirnya mungkin ada yang akan mau menolongnya,
aku pun kembali mengelilingi desa magis sampai aku tidak sengaja melihat sebuah toko pakaian,jadi aku pun memutuskan untuk

1.masuk ke toko pakian
2.lewat saja''')
            toko = input("kamu ingin masuk ke toko pakian atau lewat saja? (1/2): ")
            if toko == "1":
                os.system('cls')
                print(f'''aku pun memutuskan untuk melihat lihat sejenak karena tempat ini kelihatan cukup menarik,dan sapa sangka 
ternyata penjual toko itu sangat cantik,aku pun mencoba untuk mengajaknya untuk berbincang''')
                input("klik enter untuk lanjut: ")
                os.system('cls')
                print(f'''{username} = "Hai, apa kamu yang memiliki toko ini? Karena rasanya seperti menemukan harta karun"
cewek = "(tersenyum) Iya, itu aku! Tapi harta karun yang paling berharga belum kamu temukan"
{username} = "Oh? Apa itu?"
cewek = "Mungkin... cinta sejati?"
{username} = "Hmm, sepertinya aku harus mencari tahu. Bagaimana kalau kita mulai dari kopi setelah jam kerja?"
cewek = "Agak berani, ya? Tapi, kenapa tidak?"
{username} = "Karena aku percaya, di setiap pembelian ada potensi untuk cinta"
cewek = "Kalau begitu, aku akan siapkan diskon spesial untukmu—mungkin janjian pertama!"
{username} = "Deal! Siapa tahu, bisa jadi transaksi seumur hidup"
''')
                input("klik enter untuk lanjut: ")
                os.system('cls')
                print("kami berdua pun akhirnya saling mengenal labih dekat dan akhirnya menikah dan punya 5 anak,Yeyyyy hepi ending\n") # dah mau deadline mas
                break
            elif toko == "2":
                os.system('cls')
                print("""aku pun memutuskan kembali untuk hanya sekedar jalan jalan di desa magis,karena hari sudah mulai petang,
aku pun memutuskan untuk pergi kembali ke desa sleman,saat aku sedang santai berjalan kembali 
ke desa sambil menikmati angin sepoi sepoi,si semut bajigur kembali berulah dan membuatku terpeleset 
sampai meninggal di tempat lagi,mengenaskan kali lah hidupku ini
""")  
                break
            else:
                print("\nmangsut?")
                os.system('pause')
        else:
            print("\nmangsut?")
            os.system('pause')

# menu utama untuk menampung semua sebmenu yang ada
def main_menu():
    tentukan_username()
    tentukan_role()
    while True:
        
        os.system('cls') 
        print(f"""
halo perkenalkan namaku adalah {username},aku adalah seorang mahasiswa di sebuah daerah yang konon disebut sabagai
daerahnya para the klitih,yap betul! seperti pikiran anda,daerah tersebut bernama marley,
dan saat ini aku sedang berkuliah di universitas teknologi marley pada prodi informatika.
""")
        input("klik enter untuk lanjut")
        os.system('cls')
        print(f"""
Tak terasa ternyata aku sudah kuliah di utm selama hampir 3 tahun yang berarti saat ini aku sudah sampai semester 5,
dan beruntungnya aku saat ini bisa menjadi asisten dosen,itung-itung untuk menambah poin dan wawasan baru lahh.
""")
        input("klik enter untuk lanjut")
        os.system('cls')
        print(f"""
dan pada suatu malam yang indah ketika aku sedang mengerjakan tugas yang sangat banyak dari dosenku,aku merasa stress dan
mencoba mencari udara segar,jadi aku pergi keluar untuk sekedar jalan-jalan,sialnya aku malah tersandung seekor semut yang
membuatku jatuh dan langsung meninggal ditempat.
""")
        input("klik enter untuk lanjut")       
        os.system('cls')
        print(f"""
Tiba-tiba aku pun terbangun di dunia lain dengan pakaian {pakaian} dan sebuah {senjata} pada tanganku,beruntungnya aku adalah
seorang WIBU NOLEP(haha anjay) yang tau apa itu isekai jadi aku pun tidak merasa panik
""")
        input("klik enter untuk lanjut")
        break # supaya ketika pemain salah input,tidak langsung memulai cerita dari awal 

    while True: 
        os.system('cls')
        print(f"""
yang pertama kali aku lakukan adalah pergi ke desa dekat dengan tempatku terbangun untuk mengumpulkan berbagai informasi yang ada,
dari informasi yang kudapat,saat ini aku sedang berada di sebuah desa kecil bernama desa sleman yang berada di negri joga,
karena aku merasa gabut,aku pun menjadi petualang dan mencoba untuk :
""")
        print("1.menjelajahi hutan terlarang")
        print("2.melawan monster")
        print("3.pergi ke desa magis")
        print("0.keluar dari petualangan")
        tentukan_alur = input("kamu ingin pergi ke mana (1/2/3/0): ")

        if tentukan_alur == "1":
            os.system('cls')
            jelajahi_hutan()
            break
        elif tentukan_alur == "2":
            os.system('cls')
            melawan_monster()
            break
        elif tentukan_alur == "3":
            os.system('cls')
            pergi_kedesa_magis()
            break
        elif tentukan_alur == "0":
            os.system('cls')
            print("""\nsepertinya berpetualang di dunia lain kelihatan sangat merepotkan,
jadi aku pun memutuskan untuk mengakhiri hidupku dengan harapan dapat kembali ke dunia asalku\n""")
            break
        else:
            print("\nmangsut?")
            os.system('pause')

main_menu()