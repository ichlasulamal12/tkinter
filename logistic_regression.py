## cara jalankan python logistic_regression.py

# Import library untuk membaca dan menulis file CSV
import csv

# Import library untuk menyimpan dan memuat model
import pickle

# Import library untuk membangun model regresi logistik
from sklearn.linear_model import LogisticRegression

# Import library untuk Tkinter GUI
import tkinter as tk

# Buat objek Tkinter untuk membuat GUI
root = tk.Tk()

# Buat label untuk menampilkan judul
title = tk.Label(root, text="Regresi Logistik")
title.pack()

# Baca data dari file CSV
data = []
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# Dapatkan data X dan y dari data
X = []
y = []
for row in data:
    X.append([float(row[0]), float(row[1])])
    y.append(int(row[2]))

# Buat label dan entry untuk menerima input
label1 = tk.Label(root, text="Nilai X1:")
entry1 = tk.Entry(root)
label1.pack()
entry1.pack()

label2 = tk.Label(root, text="Nilai X2:")
entry2 = tk.Entry(root)
label2.pack()
entry2.pack()

# Buat fungsi yang dipanggil ketika tombol "Predict" diklik
def on_click():
    # Dapatkan input dari entry
    x1 = float(entry1.get())
    x2 = float(entry2.get())

    # Buat objek model regresi logistik
    model = LogisticRegression()

    # Latih model menggunakan data
    model.fit(X, y)

    # Buat input baru dari data yang dimasukkan
    X_new = [[x1, x2]]

    # Gunakan model untuk memprediksi data baru
    predictions = model.predict(X_new)

    # Tampilkan hasil prediksi ke label
    prediction_label.config(text="Prediksi: {}".format(predictions[0]))

    # Simpan model ke file
    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)

# Buat tombol "Predict"
predict_button = tk.Button(root, text="Predict", command=on_click)
predict_button.pack()

# Buat label untuk menampilkan hasil prediksi
prediction_label = tk.Label(root, text="")
prediction_label.pack()

# Jalankan GUI
root.mainloop()