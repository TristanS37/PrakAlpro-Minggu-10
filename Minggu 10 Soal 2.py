def quiz_dari_file(nama_file):
    try:
        print(f"nama file1: {nama_file}")
        with open(nama_file, 'r') as file:
            baris_soal = file.readlines()

        for baris in baris_soal:
            if '||' in baris:
                soal, jawaban = baris.strip().split('||')
                soal = soal.strip()
                jawaban = jawaban.strip()

                print(soal)
                user_jawab = input("Jawab: ").strip()

                if user_jawab.lower() == jawaban.lower():
                    print("Jawaban benar!")
                else:
                    print("Jawaban salah!")
            else:
                print("Format soal salah:", baris)

    except FileNotFoundError:
        print("File tidak ditemukan.")

quiz_dari_file('Prak Alpro/soal.txt')