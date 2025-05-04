def bandingkan_file(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            max_len = max(len(lines1), len(lines2))
            berbeda = False

            for i in range(max_len):
                baris1 = lines1[i].strip() if i < len(lines1) else ''
                baris2 = lines2[i].strip() if i < len(lines2) else ''
                if baris1 != baris2:
                    print(f"Baris ke-{i+1} berbeda:")
                    print(f"  File 1: {baris1}")
                    print(f"  File 2: {baris2}")
                    berbeda = True

            if not berbeda:
                print("Kedua file sama persis.")

    except FileNotFoundError:
        print("Salah satu atau kedua file tidak ditemukan.")
bandingkan_file('Prak Alpro/file1.txt', 'Prak Alpro/file2.txt')