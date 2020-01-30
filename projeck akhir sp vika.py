namaF=['vika','edo','yani']
hargaberas=[]
tanggungan=[]
totalzakatF=[50000,12000,40000]
namaM=['vika','edo','yani']
hargaemas=[]
tabungan=[]
totalzakatM=[50000,12000,40000]
total=[]
total1=[]

while True:
    print("==========SELAMAT DATANG===========")
    print("======PROGRAM AMALAN AKHIRAT=======")
    print("1.customer \n2.Admin")
    masuk=int(input("Masuk sebagai = "))  
    print(" ")
    if masuk==1:
        while True:
            print("=========SELAMAT DATANG===========")
            print("1.Membayar Zakat \n2.Total zakat \n3.Pengertian Zakat Fitrah \n4.Pengertian Zakat Mall \n5.Selesai")
            pilihan=int(input("Masukkan pilihan anda = "))
            if pilihan==1:
                print("Macam Macam Zakat \n1.Fitrah \n2.Mall")
                pilihanzakat=int(input("Pilih Sesuai Nomer = "))
                if pilihanzakat==1:
                    a=input("Masukkan nama anda : ")
                    c=int(input("Masukkan harga beras 1 kg : "))
                    d=int(input("Berapa jumlah anggota keluarga yang anda tanggung = "))
                    total=d*c*25/10
                    namaF.append(a)
                    hargaberas.append(c)
                    totalzakatF.append(total)
                    print(namaF)
                    print(totalzakatF)
                    
                elif pilihanzakat==2:
                    b=input("Masukkan nama anda : ")
                    e=int(input("Masukkan harga emas saat ini : "))
                    emas=e*85
                    f=int(input("Masukkan total tabungan anda selama 1 tahun = "))
                    if f>=emas:
                        g=f*25/1000
                        namaM.append(b)
                        hargaemas.append(e)
                        tabungan.append(f)
                        totalzakatM.append(g)
                        print(totalzakatM)
                    else:
                        print("")
                        print("Anda belum bisa melakukan zakat Mall untuk saat ini")
                        print("")
                else:
                    print()
                    print("SILAKAN COBA LAGI")
                    print()
                    
            elif pilihan==2:
                print("=============Total Zakat=============")
                print("")
                print("jumlah zakat fitrah = ",sum(totalzakatF))
                total.append(totalzakatF)
                print("jumlah zakat mall = ",sum(totalzakatM))
                total1.append(totalzakatM)
                  
            elif pilihan==3:
                print("=================================================Zakat Fitrah=======================================================")
                print()
                print("Zakat fitrah adalah zakat yang wajib dikeluarkan umat Muslim menjelang hari raya Idul Fitri atau pada bulan Ramadan.")
                print("Zakat fitrah dapat dibayar dengan setara 3,5 liter (2,5 kilogram) makanan pokok dari daerah yang bersangkutan.")
                print("Makanan pokok di Indonesia adalah nasi, maka yang dapat dijadikan sebagai zakat adalah berupa beras.")
                print()
            elif pilihan==4:
                print("===================================================Zakat Mall=========================================================")
                print()
                print("Zakat maal (harta) adalah zakat penghasilan seperti hasil pertanian, hasil pertambangan, hasil laut, hasil perniagaan,")
                print("hasil ternak, harta temuan, emas dan perak. Masing-masing jenis penghasilan memiliki perhitungannya sendiri.")
                print()
            elif pilihan==5:
                keluar=input("Apa Anda Yakin Untuk Keluar = ya / tidak ")
                print("")
                if keluar=="ya":
                    break
                else:
                    print()

    elif masuk==2:
        u=("vika")
        p=("vika")
        i=0
        while True:
            print("=============================================")
            print("================Silakan Login================")
            print("=============================================")
            print("")
            while True:
                u=input("Masukkan Username = ")
                p=input("Masukkan Password = ")
                if u=="vika" and p=="vika":
                    break
                print("")
                print("SILAKAN COBA LAGI!!")
                print("")
                i+=1
                if i==3:
                    print("Maaf kami terpaksa untuk mengeluarkan anda ")
                    exit()
            while True:
                print("=========SELAMAT DATANG==========")
                print("1.Melihat semua orang yang berzakat \n2.Menghapus data pezakat \n3.Ascending zakat fitrah \n4.descending zakat mall \n5.Selesai")
                pilihan=int(input("Pilih sesuai nomor = "))
                if pilihan==1:
                    print("Pilih Jenis Zakat \n1.Zakat Fitrah\n2.Zakat Mall")
                    pilih=int(input("pilih sesuai nomor = "))
                    if pilih==1:
                        for i in range (len(namaF)):
                            print(i+1,".",namaF[i]," berzakat sebesar = ",totalzakatF[i])
                    elif pilih==2:
                        for i in range (len(namaM)):
                            print(i+1,".",namaM[i]," berzakat sebesar = ",totalzakatM[i])
                    
                elif pilihan==2:
                    print("pilih hapus jenis data zakat \n1.Zakat Fitrah \n2.Zakat Mall ")
                    pilihan=int(input("Pilih sesuai nomor = "))
                    if pilihan==1:
                        hapus=input("Hapus data sesuai nama = ")
                        index=namaF.index(hapus)
                        print(index)    
                        namaF.remove(namaF[index])
                        print("")
                        print("Selamat data telah terhapus")
                        print("")
                    elif pilihan==2:
                        hapus=input("Hapus data sesuai nama = ")
                        index=namaM.index(hapus)
                        print(index)    
                        namaM.remove(namaM[index])
                        print("")
                        print("Selamat data telah terhapus")
                        print("")
                elif pilihan==3:
                    print("Ascending zakat fitrah")
                    for i in range (len(totalzakatF)):
                        totalzakatF[i]=int(totalzakatF[i])
                    b=len(totalzakatF)
                    for x in range(b-1,0,-1):
                        for y in range(x):
                            if totalzakatF[y]>totalzakatF[y+1]:
                                temp=totalzakatF[y+1]
                                totalzakatF[y+1]=totalzakatF[y]
                                totalzakatF[y]=temp
                    print(totalzakatF)
                            
                elif pilihan==4:
                    print("Descending zakat mall")
                    for i in range (len(totalzakatM)):
                        totalzakatM[i]=int(totalzakatM[i])
                    b=len(totalzakatM)
                    for x in range(b-1,0,-1):
                        for y in range(x):
                            if totalzakatM[y]<totalzakatM[y+1]:
                                temp=totalzakatM[y+1]
                                totalzakatM[y+1]=totalzakatM[y]
                                totalzakatM[y]=temp
                    print(totalzakatM)
                elif pilihan==5:
                    break
                    
                else:
                    print("")
                    print("Silakan Coba Lagi!!")
                    print("")
            break

