numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]

a = 0
b = 553
# Loop while untuk mencetak bilangan ganjil hingga melewati 553
while a < len(numbers):
    if numbers[a] % 2 != 0 and numbers[a] <= b:
        print(numbers[a])
    a += 1


# while i < len(numbers):
#     print(numbers)
#     if numbers == 553:
#             break
        
# loop untuk membuat pola
for i in range(1, 5 + 1):
    for j in range(i):
        print("*", end="")
    print()  # Pindah ke baris baru

print()
# Inisialisasi variabel untuk menyimpan hasil penjumlahan
total = 0

# Loop untuk bilangan ganjil dari 1 hingga 19 dengan langkah 2
for i in range(1, 20, 2):
    total += i 

# Menampilkan hasil penjumlahan
print("1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 =", total)