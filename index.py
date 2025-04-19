from flask import Flask, render_template_string

app = Flask(__name__)

# ======== CLASS =========
class Mahasiswa:
    def __init__(self, nama, nim, prodi, semester, email):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.semester = semester
        self.email = email

class Dosen:
    def __init__(self, nama, nip, matkul, email, prodi):
        self.nama = nama
        self.nip = nip
        self.matkul = matkul
        self.email = email
        self.prodi = prodi

# ======== OBJECT =========
mhs = Mahasiswa("Totti Airindo Al Rizki", "2455201013", "Teknik Informatika", 2, "totti@kampus.ac.id")
dsn = Dosen("Dedy Gusman", "198509162022", "Analisa dan Berorientasi Objek", "dedy@kampus.ac.id", "Teknik Informatika")

# ======== TAMPILAN HTML =========
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sistem Akademik</title>
    <style>
        body {
            background: linear-gradient(to right, #00b4db, #0083b0);
            font-family: Arial, sans-serif;
            color: #fff;
            padding: 20px;
        }
        .card {
            background-color: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        h2 {
            color: #ffeb3b;
        }
    </style>
</head>
<body>
    <h1>Data Sistem Akademik</h1>
    
    <div class="card">
        <h2>Mahasiswa</h2>
        <p><strong>Nama:</strong> {{ mhs.nama }}</p>
        <p><strong>NIM:</strong> {{ mhs.nim }}</p>
        <p><strong>Prodi:</strong> {{ mhs.prodi }}</p>
        <p><strong>Semester:</strong> {{ mhs.semester }}</p>
        <p><strong>Email:</strong> {{ mhs.email }}</p>
    </div>
    
    <div class="card">
        <h2>Dosen</h2>
        <p><strong>Nama:</strong> {{ dsn.nama }}</p>
        <p><strong>NIP:</strong> {{ dsn.nip }}</p>
        <p><strong>Mata Kuliah:</strong> {{ dsn.matkul }}</p>
        <p><strong>Email:</strong> {{ dsn.email }}</p>
        <p><strong>Prodi:</strong> {{ dsn.prodi }}</p>
    </div>
</body>
</html>
'''

@app.route("/")
def home():
    return render_template_string(HTML, mhs=mhs, dsn=dsn)

if __name__ == '__main__':
    app.run(debug=True)
