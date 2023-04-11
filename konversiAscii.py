import tkinter as tk

# untuk mengkonversi string menjadi nilai ASCII dan bilangan biner, desimal, oktal, dan heksadesimal
def convert_string(string):
    ascii_value = [ord(char) for char in string] # konversi string menjadi nilai ASCII
    decimal_value = int(''.join([str(ord(char)) for char in string])) # konversi string menjadi nilai desimal
    binary_value = bin(decimal_value) # konversi nilai desimal menjadi nilai biner
    octal_value = oct(decimal_value) # konversi nilai desimal menjadi nilai oktal
    hexadecimal_value = hex(decimal_value) # konversi nilai desimal menjadi nilai heksadesimal
    
    return (ascii_value, decimal_value, binary_value, octal_value, hexadecimal_value)

# untuk menampilkan hasil konversi pada layar
def display_conversion():
    input_string = input_entry.get() # ambil nilai input dari pengguna
    ascii_value, decimal_value, binary_value, octal_value, hexadecimal_value = convert_string(input_string) # konversi nilai input
    
    # tampilkan hasil konversi pada layar
    ascii_label.config(text=f"ASCII Value: {ascii_value}")
    decimal_label.config(text=f"Decimal Value: {decimal_value}")
    binary_label.config(text=f"Binary Value: {binary_value}")
    octal_label.config(text=f"Octal Value: {octal_value}")
    hexadecimal_label.config(text=f"Hexadecimal Value: {hexadecimal_value}")

# buat jendela aplikasi
root = tk.Tk()
root.title("String Converter")
root['bg'] = "#B9EDDD"
root.geometry("700x500+0+0")

# buat label dan input untuk memasukkan string
input_label = tk.Label(root, text="Input String:", background='#B9EDDD')
input_label.grid(row=0, column=0)

input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

# buat tombol untuk mengkonversi string
convert_button = tk.Button(root, text="Convert",background='#577D86', command=display_conversion)
convert_button.grid(row=1, column=0, columnspan=2)

# buat label untuk menampilkan hasil konversi
ascii_label = tk.Label(root, text="", background='#B9EDDD')
ascii_label.grid(row=2, column=0, columnspan=2)

decimal_label = tk.Label(root, text="", background='#B9EDDD')
decimal_label.grid(row=3, column=0, columnspan=2)

binary_label = tk.Label(root, text="", background='#B9EDDD')
binary_label.grid(row=4, column=0, columnspan=2)

octal_label = tk.Label(root, text="", background='#B9EDDD')
octal_label.grid(row=5, column=0, columnspan=2)

hexadecimal_label = tk.Label(root, text="", background='#B9EDDD')
hexadecimal_label.grid(row=6, column=0, columnspan=2)

root.mainloop()