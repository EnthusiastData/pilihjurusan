import streamlit as st

# Daftar pertanyaan
pertanyaan = [
    ("Aku suka ngulik hal teknis seperti coding, logika, atau teka-teki yang bikin mikir keras", "Informatika"),
    ("Aku tertarik bikin aplikasi atau sistem yang bisa dipakai banyak orang", "Sistem Informasi"),
    ("Aku enjoy dengan angka, data keuangan, atau laporan", "Sistem Informasi Akuntansi"),
    ("Aku penasaran gimana game, aplikasi, atau website bisa jalan dari nol", "Informatika"),
    ("Aku suka mikir gimana caranya teknologi bisa bikin kerja orang jadi lebih gampang", "Sistem Informasi"),
    ("Aku tertarik dengan keuangan, bisnis dan teknologi", "Sistem Informasi Akuntansi"),
    ("Belajar bahasa pemrograman terdengar menantang tapi seru", "Informatika"),
    ("Aku tertarik sama dunia startup, bisnis digital, atau e-commerce", "Sistem Informasi"),
    ("Aku suka hal yang rapi, detail dan terstruktur", "Sistem Informasi Akuntansi"),
    ("Aku lebih suka kerja dengan komputer daripada ngobrolin laporan atau administrasi", "Informatika"),
]

st.title("TENTUKAN YANG KAMU BANGET DI UBSI SEKARANG!!")

skor = {"Informatika": 0, "Sistem Informasi": 0, "Sistem Informasi Akuntansi": 0}

st.write("Tentukan yang menjadi pilihanmu:")

for i, (pertanyaan_text, kategori) in enumerate(pertanyaan):
    jawaban = st.radio(f"{i+1}. {pertanyaan_text}", ["Ya", "Tidak"], key=i)
    if jawaban == "Ya":
        skor[kategori] += 1

if st.button("Prediksi"):
    skor_maks = 0
    if any(skor.values()): # Check if any score is greater than 0
        skor_maks = max(skor.values())
        
    rekomendasi = [k for k, v in skor.items() if v == skor_maks]
    
    st.subheader("Jeng...Jeng...Jeng...!!!")
   
    
    if not any(skor.values()):
        st.write("Tidak ada minat yang terdeteksi berdasarkan jawaban Anda. Coba jawab 'Ya' pada beberapa pertanyaan.")
    elif len(rekomendasi) == 1:
        st.write(f"Wah..**{rekomendasi[0]}** ternyata kamu banget!!")
    else:
        st.write(f"Keren!! ga cuma satu, karena **{', '.join(rekomendasi)}** ternyata bisa jadi pilihan yang kamu banget!!")
    
    penjelasan = {
        "Informatika": "Khusus buat yang Very Logic! Di sini kamu bakal belajar coding, algoritma, AI, game, dan teknologi keren lainya. Bakalan sering ngoding, bikin aplikasi & game, Main logika & problem solving, ngulik AI, data dan teknologi masa depan. Cocok buat yang suka tantangan, sabar sama error, ingin jadi programmer, software engineer maupun AI engineer. FUTURE TECHNOLOGY IN YOURE HAND!",
        "Sistem Informasi": "Khusus buat yang Startup Minded! kamu bakal belajar gimana teknologi dipakai buat bantu bisnis, organisasi dan startup. Bakal mengenal banyak sistem aplikasi perusahaan, analisa kebutuhan user, bisnis digital & e-commerce dan manajemen data & sistem. Cocok buat yang suka mikir strategis, pengen kerja di startup atau perusahaan besar menjadi system analyst, IT consultant, maupun product manager. YOU WILL BE THE NEXT HETCOCORN!",
        "Sistem Informasi Akuntansi": "Khusus buat yang Money Oriented With Tech! kamu bakal belajar akuntansi dengan teknologi digital. Bakalan kenal dengan akuntansi berbasis sistem, aplikasi keuangan & ERP, audit digital, dan sistem keuangan perusahaan. Cocok buat yang teliti, rapi, dan ingin kerja di perusahaan besar menjadi akuntan sistem, auditor IT, maupun analis keuangan digital. CUAN..CUAN..CUAN!"
    }
    
    for rec in rekomendasi:
        st.write(f"- **{rec}**: {penjelasan[rec]}")