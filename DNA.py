import os
import binascii
from time import time
#@Author Jurijus Pacalovas 

namez = input("Compress: c Extract: e Check file: check ")

class Compression:



    def compress_file(self):
        if namez=="c":
        
            corridors = 0
            cor = 7
            namea = "file.Secret"
            namem = ""
            namema = "?"
            e5 = 0
            e1 = ""
            e6 = 0
            e7 = 255
            sda3 = ""
            sda4 = ""
            sda5 = ""
            assxw = 0
            blockw = 5
            blockw1 = 4
            input_file = input("What is name of file? ")
            nameas = input_file
            nac = len(nameas)
            nameas = input_file + ".bin"
            nac = len(nameas)
            countraz = 0
            cvf = 2
            cvf1 = 0
            s = ""
            e2 = 0
            e3 = 2
            e4 = ""
            c = 2
            sw = 2
            elw = 0
            sda3 = ""
            sda2 = ""
            sscvf = 0
            qqqqwzl = 0
            block = 1
            r = ""
            x = 0
            x1 = 0
            x2 = 0
            x = time()
            with open(nameas, "w") as f4:

                            f4.write(s)

            with open(nameas, "a") as f3:

                            f3.write(s)
    
            with open(input_file, "rb") as binary_file:
                data = binary_file.read()
                s = str(data)
                lenf1 = len(data)
                lenf5 = len(data)
                assx = 0
                qqqwz = 0
    
                while assx < 10:
                    cvf = cvf + 1
                    countraz = countraz + 1
                    with open(nameas, "ab") as f2:
                        if countraz == 1:
                            sda = bin(int(binascii.hexlify(data), 16))[2:]
                            lenf = len(sda)
                            lenf1 = len(data)
                            xc = (lenf1 * 8) - lenf
                            z = 0
                            if xc != 0:
                                while z < xc:
                                    sda = "0" + sda
                                    z = z + 1
                            sda = sda + sda2
                            if countraz == 1:
                                sda2 = sda
                            n = int(sda2, 2)
                            qqwslenf = len(sda2)
                            qqwslenf = (qqwslenf / 8) * 2
                            qqwslenf = str(qqwslenf)
                            qqwslenf = "%0" + qqwslenf + "x"
                            jl = binascii.unhexlify(qqwslenf % n)
                            sssssw = len(jl)
                            data = jl
                            qqqwz = qqqwz + 1
                            if countraz == 1:
                                lenf5 = len(data)
                            sda = bin(int(binascii.hexlify(data), 16))[2:]
                            lenf = len(sda)
                            xc = (lenf1 * 8) - lenf
                            z = 0
                            if xc != 0:
                                while z < xc:
                                    sda = "0" + sda
                                    z = z + 1
                            sda2 = sda
                            lenf3 = len(sda2)
                        lenf2 = len(sda2)
                        c = 1
                        block = 0
    
                        while block < lenf2:
                            e4 = sda2[block:block + 9]
                            if e4 == "000000000":
                                e4 = "011100101"
                                sda4 += e4
                            elif e4 == "011100101":
                                e4 = "000000000"
                                sda4 += e4
                            else:
                                sda4 += e4
                            block += 9
    
                        sda2 = sda4
                        sda4 = ""
                        if c == 1:
                            block = 0
    
                            while block < lenf2:
                                e4 = sda2[block:block + 8]
                                e1 = e4
                                remaider = cvf1 % blockw + block // 16 + block
                                r1 = (block // 8) + (block // blockw)
                                r2 = (block // 8) + block + (block // 8)
                                r3 = block % 3 + (block // 8)
                                r4 = block % 4 + (block // blockw)
                                if remaider == 0 and r1 == 0 or remaider == 0 and r2 == blockw or remaider == 0 and r3 == 0 or remaider == 0 and r4 == 0:
                                    e1 = e4[4:8] + e4[2:4] + e4[0:2]
                                if remaider == 0 and r1 == blockw or remaider == 0 and r2 == blockw or remaider == 0 and r3 == blockw or remaider == 0 and r4 == blockw:
                                    e1 = e4[4:8] + e4[0:4]
                                if remaider == 0:
                                    e1 = e4[4:8] + e4[2:4] + e4[0:2]
                                if remaider == 1:
                                    e1 = e4[4:8] + e4[0:4]
                                e5 = int(e1, 2)
    
                                if e5 == e6:
                                    sda3 = format(e7, "08b")
                                elif e5 == e7:
                                    sda3 = format(e6, "08b")
                                else:
                                    sda3 = format(e5, "08b")
                                sda4 += sda3
                                blockw += 1
                                if blockw == 15:
                                    blockw == 1
                                block += 8
                            e6 += 3
                            e7 -= 3
                            if e6 >= 255:
                                e6 = 0
                            if e7 <= 0:
                                e7 = 255
                            sda2 = sda4
                            blockw = 5
                            sda4 = ""
                            block = 0
                            e8 = 0
                            ch1 = ""
                            ch = 0
                            r1 = ""
                            r2 = ""
    
                            r3 = 0
                            r4 = ""
                            e9 = "1"
                          
    
                            e9 = 0
                            r5 = ""
                            e10 = ""
                            s = ""
                            sda10 = ""
                            sda11 = ""
                            start = 1
    
                            while block < lenf2:
                                e4 = sda2[block + 4:block + 7]
                                e5 = sda2[block:block + 8]
                                ch1 = sda2[block + 1:block + 3]
                                r1 = sda2[block:block + 1]
                                r2 = sda2[block + 7:block + 8]
                                r4 = sda2[block + 6:block + 7]
                                r5 = sda2[block + 1:block + 2]
                                e8 += 1
                                if len(e5) == 8:
                                    e1 = int(e4, 2)
                                    e9 = int(r5, 2)
                                ch = int(ch1, 2)
                                r3 = int(r1, 2)
                                sda5 = ""
                                sda6 = ""
                                sda7 = ""
                                sda9 = ""
                                if r3 == e8 and ch == e8 and len(e5) == 8 and e9 != e8 and start == 1:
                                    e1 = format(e8, "01b")  # 2catsr2&00/01
                                    sda5 = e1 + e1 + e5[3:8]
                                    start = 0
                                    e10 = "2"
                                    sda10 += sda5
                                    if len(sda6) == 15:
                                        sda5 = ""
                                        sda3 = ""
                                elif e9 == e8 and r3 == e8 and len(e5) == 8 and start == 1:
                                    sda5 = e5
                                else:
                                    if e10 == "0":  # nac
                                        sda3 = sda10 + "0" + e5
                                        sda4 += sda3
                                        sda10 = ""
                                        start = 1
                                    elif e10 == "2":  # can
                                        sda3 = sda10 + "1" + e5
                                        sda4 += sda3
                                        sda10 = ""
                                        start = 1
                                if e8 == 1:
                                    e8 = 0
                                block += 8
                            if e10 == "0":  # 0 not compression after compression
                                sda3 = sda10 + "0" + e5
                                sda4 += sda3
                            elif e10 == "2":  # can # compression after not compression
                                sda3 = sda10 + "1" + e5
                                sda4 += sda3
                            if len(sda10) == 0:
                                sda4 += "0"
                            else:
                                sda4 += "1"
                            sda10 = ""
                            sda2 = sda4
                            cvf1 += 1
                            if cvf1 == 1:
                                long_1 = len(sda2)
                                add_bits = ""
                                count_bits = 8 - long_1 % 8
                                z = 0
                                if count_bits != 0:
                                    while z < count_bits:
                                        add_bits = "0" + add_bits
                                        z = z + 1
                                sda2 = add_bits + sda2
                                n = int(sda2, 2)
                                qqwslenf = len(sda2)
                                qqwslenf = (qqwslenf / 8) * 2
                                qqwslenf = str(qqwslenf)
                                qqwslenf = "%0" + qqwslenf + "x"
                                jl = binascii.unhexlify(qqwslenf % n)
                                sssssw = len(jl)
                                data = jl
                                qqqwz = qqqwz + 1
                                szxzzza = ""
                                szxzs = ""
                                assxw = assxw + 1
                                if assxw == 1:
                                    assx = 10
                                    if assx == 10:
                                        f2.write(jl)
                                        x2 = time()
                                        x3 = x2 - x
                                        return print(x3)

    def extract_and_reverse_compression(self):
        if namez == "e":
            nameas = input("What is the name of the compressed file? ")

            sda2 = ""
            cvf1 = 0
            blockw = 5
            e6 = 0
            e7 = 255

            with open(nameas, "rb") as compressed_file:
                data = compressed_file.read()
                sda2 = bin(int(binascii.hexlify(data), 16))[2:]
                lenf2 = len(sda2)
                
                while cvf1 < 23:
                    block = 0
                    sda4 = ""
                    
                    while block < lenf2:
                        e4 = sda2[block:block+9]
                        
                        if e4 == "000000000":
                            e4 = "011100101"
                            sda4 += e4
                        elif e4 == "011100101":
                            e4 = "000000000"
                            sda4 += e4
                        else:
                            sda4 += e4
                        
                        block += 9
                    
                    sda2 = sda4
                    sda4 = ""
                    
                    block = 0
                    
                    while block < lenf2:
                        e4 = sda2[block:block+8]
                        e1 = e4
                        remaider = cvf1 % blockw + block // 16 + block
                        
                        r1 = (block // 8) + (block // blockw)
                        r2 = (block // 8) + block + (block // 8)
                        r3 = block % 3 + (block // 8)
                        r4 = block % 4 + (block // blockw)
                        
                        if remaider == 0 and (r1 == 0 or r2 == blockw or r3 == 0 or r4 == 0):
                            e1 = e4[4:8] + e4[2:4] + e4[0:2]
                        elif remaider == 0 and (r1 == blockw or r2 == blockw or r3 == blockw or r4 == blockw):
                            e1 = e4[4:8] + e4[0:4]
                        elif remaider == 0:
                            e1 = e4[4:8] + e4[2:4] + e4[0:2]
                        elif remaider == 1:
                            e1 = e4[4:8] + e4[0:4]
                        
                        e5 = int(e1, 2)
                        
                        if e5 == e6:
                            sda3 = format(e7, "08b")
                        elif e5 == e7:
                            sda3 = format(e6, "08b")
                        else:
                            sda3 = format(e5, "08b")
                        
                        sda4 += sda3
                        blockw += 1
                        
                        if blockw == 15:
                            blockw == 1
                        
                        block += 8
                    
                    e6 += 3
                    e7 -= 3
                    
                    if e6 >= 255:
                        e6 = 0
                    if e7 <= 0:
                        e7 = 255
                    
                    cvf1 += 1
                    sda2 = sda4
                    blockw = 5
                    sda4 = ""
                
                n = int(sda2, 2)
                qqwslenf = len(sda2)
                qqwslenf = (qqwslenf / 8) * 2
                qqwslenf = str(qqwslenf)
                qqwslenf = "%0" + qqwslenf + "x"
                jl = binascii.unhexlify(qqwslenf % n)
                sssssw = len(jl)
                
                # Save the extracted data to a file
                output_file_name = "extracted_data.bin"
                with open(output_file_name, "wb") as output_file:
                    output_file.write(jl)
                
                return output_file_name

d = Compression()
xw1 = d.extract_and_reverse_compression()


d=Compression()



xw=d.compress_file()

print(xw)



xw1=d.extract_and_reverse_compression()

print(xw1)      
