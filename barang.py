import tkinter as tk
from tkinter import messagebox

# Inisialisasi data stok sebagai dictionary
stok_barang = {}

# Fungsi untuk menambahkan barang baru
def tambah_barang():
    nama_barang = entry_nama.get().lower()
    try:
        jumlah = int(entry_jumlah.get())
        if nama_barang in stok_barang:
            messagebox.showerror("Error", "Barang sudah ada dalam stok!")
        elif jumlah < 0:
            messagebox.showerror("Error", "Jumlah stok tidak boleh negatif!")
        else:
            stok_barang[nama_barang] = jumlah
            messagebox.showinfo("Sukses", f"Barang '{nama_barang}' berhasil ditambahkan.")
    except ValueError:
        messagebox.showerror("Error", "Jumlah stok harus berupa angka!")
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)

# Fungsi untuk mengurangi stok barang
def kurang_barang():
    nama_barang = entry_nama.get().lower()
    try:
        kurang = int(entry_jumlah.get())
        if nama_barang in stok_barang:
            if stok_barang[nama_barang] - kurang < 0:
                messagebox.showerror("Error", "Jumlah pengurangan melebihi stok yang tersedia!")
            else:
                stok_barang[nama_barang] -= kurang
                messagebox.showinfo("Sukses", f"Barang '{nama_barang}' berhasil dikurangi.")
        else:
            messagebox.showerror("Error", "Barang tidak ditemukan dalam stok!")
    except ValueError:
        messagebox.showerror("Error", "Jumlah stok harus berupa angka!")
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)

# Fungsi untuk mengupdate stok barang
def update_stok():
    nama_barang = entry_nama.get().lower()
    try:
        tambahan = int(entry_jumlah.get())
        if nama_barang in stok_barang:
            if stok_barang[nama_barang] + tambahan < 0:
                messagebox.showerror("Error", "Stok tidak cukup untuk pengurangan ini!")
            else:
                stok_barang[nama_barang] += tambahan
                messagebox.showinfo("Sukses", f"Stok '{nama_barang}' berhasil diupdate.")
        else:
            messagebox.showerror("Error", "Barang tidak ditemukan dalam stok!")
    except ValueError:
        messagebox.showerror("Error", "Jumlah stok harus berupa angka!")
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    if not stok_barang:
        messagebox.showinfo("Info", "Stok barang kosong!")
    else:
        daftar = "\n".join([f"{barang.capitalize()} : {jumlah}" for barang, jumlah in stok_barang.items()])
        messagebox.showinfo("Daftar Stok Barang", daftar)

# Fungsi untuk mencari barang
def cari_barang():
    nama_barang = entry_nama.get().lower()
    if nama_barang in stok_barang:
        messagebox.showinfo("Info", f"Barang '{nama_barang}' tersedia dengan stok: {stok_barang[nama_barang]}")
    else:
        messagebox.showerror("Error", f"Barang '{nama_barang}' tidak ditemukan!")
    entry_nama.delete(0, tk.END)

# Fungsi untuk keluar dari aplikasi
def keluar():
    root.destroy()

# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Manajemen Stok Barang")
root.geometry("400x300")

# Label dan Entry
tk.Label(root, text="Nama Barang:").grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root, width=25)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="Jumlah Stok:").grid(row=1, column=0, padx=10, pady=10)
entry_jumlah = tk.Entry(root, width=25)
entry_jumlah.grid(row=1, column=1)

# Tombol Menu
tk.Button(root, text="Tambah Barang", command=tambah_barang).grid(row=2, column=0, pady=10)
tk.Button(root, text="Kurangi Barang", command=kurang_barang).grid(row=2, column=1, pady=10)
tk.Button(root, text="Update Stok", command=update_stok).grid(row=3, column=0, pady=10)
tk.Button(root, text="Tampilkan Barang", command=tampilkan_barang).grid(row=3, column=1, pady=10)
tk.Button(root, text="Cari Barang", command=cari_barang).grid(row=4, column=0, pady=10)
tk.Button(root, text="Keluar", command=keluar).grid(row=4, column=1, pady=10)

# Menjalankan aplikasi
root.mainloop()
