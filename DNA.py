import os  
from time import time
import binascii
import math
import os.path
namez =input("compress: c extract: e ")
#@Author Jurijus pacalovas


class compression:


    def cryptograpy_compression(self):




                self.name = "Created: Jurijus pacalovas Price Portal 1000 000 000 Euro cost Date: 26/07/2021 17:11 Deep 14.5 ERA"




                if namez=="c":




                    corridors=0




                    cor=7




                    name=input("What is name of file? ")




                    namea="file.Secret"




                    namem=""




                    namema="?"


                    e5=0




                    e1=""




                    e6=0




                    e7=255


                    sda3=""




                    sda4=""




                    sda5=""




                    assxw=0


                    blockw=5




                    blockw1=4


                    nameas=name


                    nac=len(nameas)


                    nameas=name+".bin"


                    nac=len(nameas)


                    countraz=0




                    cvf=2




                    cvf1=0


                    s=""


                    e2=0


                    e3=2




                    e4=""


                    c=2


                    sw=2


                    elw=0




                    sda3=""




                    sda2=""


                    sscvf=0


                    qqqqwzl=0


                    block=1
                    r=""
                    x=0


                    x1=0


                    x2=0


                    x = time()




                    with open(nameas, "w") as f4:


                            f4.write(s)


                    with open(nameas, "a") as f3:


                            f3.write(s)


                    with open(name, "rb") as binary_file:


                       # Read the whole file at once




                        data = binary_file.read()




                        s=str(data)


                        lenf1=len(data)


                        lenf5=len(data)




                        assx=0


                        qqqwz=0




                        while assx<10:


                            aas1=0


                            a1=0






                            cvf=cvf+1




                            countraz=countraz+1


                            with open(nameas, "ab") as f2:




                                if countraz==1:




                                    sda=bin(int(binascii.hexlify(data),16))[2:]




                                    lenf=len(sda)




                                    lenf1=len(data)




                                




                                    xc=(lenf1*8)-lenf




                                    z=0




                                    if xc!=0:




                                        while z<xc:




                                            sda="0"+sda




                                            z=z+1


                                    sda=sda+sda2


                                    if countraz==1:




                                        sda2=sda






                                    n = int(sda2, 2)






                                    qqwslenf=len(sda2)




                                    qqwslenf=(qqwslenf/8)*2




                                    qqwslenf=str(qqwslenf)




                                    qqwslenf="%0"+qqwslenf+"x"




                                    jl=binascii.unhexlify(qqwslenf % n)




                                    sssssw=len(jl)




                                    data=jl




                                    qqqwz=qqqwz+1


                                    if countraz==1:




                                        lenf5=len(data)


                                    sda=bin(int(binascii.hexlify(data),16))[2:]




                                    lenf=len(sda)


                                    xc=(lenf1*8)-lenf




                                    z=0




                                    if xc!=0:




                                        while z<xc:




                                            sda="0"+sda




                                            z=z+1


                                    sda2=sda




                                    lenf3=len(sda2)




                                lenf2=len(sda2)




                                c=1




                                block=0


                                while block<lenf2:




                                                   e4=sda2[block:block+9]




                                                   if e4=="000000000":




                                                       e4="011100101"




                                                       sda4+=e4




                                                   elif e4=="011100101":




                                                       e4="000000000"




                                                       sda4+=e4


                                                   else:




                                                       sda4+=e4


                                                   block+=9  




                                sda2=sda4




                                sda4=""                              




                                if c==1:


                                    block=0


                                    while block<lenf2:


                                        e4=sda2[block:block+8]


                                        e1=e4


                                        remaider=cvf1%blockw+block//16+block




                                        r1=(block//8)+(block//blockw)




                                        r2=(block//8)+block+(block//8)




                                        r3=block%3+(block//8)




                                        r4=block%4+(block//blockw)










                                        if remaider==0 and r1==0 or remaider==0 and r2==blockw or remaider==0 and r3==0 or remaider==0 and r4==0:




                                            e1=e4[4:8]+e4[2:4]+e4[0:2]










                                        if remaider==0 and r1==blockw or remaider==0 and r2==blockw or remaider==0 and r3==blockw or remaider==0 and r4==blockw:




                                            e1=e4[4:8]+e4[0:4] 




                                        if remaider==0:




                                            e1=e4[4:8]+e4[2:4]+e4[0:2]




                                        if remaider==1:




                                            e1=e4[4:8]+e4[0:4]                                          




                                        e5=int(e1,2)




                                        if e5==e6:






                                            sda3=format(e7,"08b")




                                        elif e5==e7:


                                            sda3=format(e6,"08b")


                                        else:




                                            sda3=format(e5,"08b")




                                        sda4+=sda3


                                        blockw+=1




                                        if blockw==15:




                                            blockw==1


                                        block+=8                                    


                                    e6+=3




                                    e7-=3




                                    if e6>=255:




                                        e6=0




                                    if e7<=0:




                                        e7=255


                                    sda2=sda4




                                    blockw=5


                                    sda4=""


                                    block=0
                                    e8=0
                                    ch1=""
                                    ch=0
                                    r1=""
                                    r2=""
                                    r3=0
                                    r4=""
                                    e9="1"
                                    e9=0
                                    r5=""
                                    e10=""
                                    sda10=""
                                    sda11=""
                                    start=1
                                    while block<lenf2:
                                        
                                        #14 D




                                        e4=sda2[block+4:block+7]
                                        e5=sda2[block:block+8]
                                        ch1=sda2[block+1:block+3]
                                        r1=sda2[block:block+1]
                                        r2=sda2[block+7:block+8]
                                        r4=sda2[block+6:block+7]
                                        r5=sda2[block+1:block+2]  
                                        
                                        
                                        e8+=1
                                        if len(e5)==8:
                                            e1=int(e4,2)
                                            e9=int(r5,2)
                                        ch=int(ch1,2)
                                        r3=int(r1,2)
                                        sda5=""
                                        sda6=""
                                        sda7=""
                                        sda9=""
                                        
                                        #2 Cats algorithm: the same or two different of count numbers. 
#000 001 010 011 100 101 110 111; 01000, 01000 
#00,01,10,11    
                                        
                                    
                                        if r3==e8 and ch==e8 and len(e5)==8 and e9!=e8 and start==1:
                                         
                                       
                                              
                                                e1=format(e8,"01b")#2catsr2&00/01
                                            
                                          
                                               
                                                sda5=e1+e1+e5[3:8]
                                                start=0
                                                
                                                e10="2"
                                                sda10+sda5
                                                if len(sda6)==15:
                                                    sda5=""
                                                    sda3=""
                                                
                                                
                                             
                                                #print(len(sda5))                                         
                                          
                                               
                                             
                                               
                                               
                                        elif e9==e8 and r3==e8 and len(e5)==8 and start==1:
                                            

                                               sda5=e5
                                               #print(len(sda5))
                                        
                                                  
                                               e10="0"
                                               start=0
                                               
                                             
                                               sda10+=sda5


                                               
         
                                            
                                                                           
                                        else:
                                               if e10=="0":#nac
                                                   sda3=sda10+"0"+e5
                                                   sda4+=sda3
                                                   sda10=""
                                                   start=1
                                               
                                           
                                               elif e10=="2":#can
                                                  sda3=sda10+"1"+e5
                                                  sda4+=sda3
                                                  sda10=""
                                                  start=1
                                  
                                
                                             
                                            

                                               
                                        
                                            
                                            
                             
                                            
                                        if e8==1:
                                         
                                         
                                            e8=0                                       
                                        
                                         
                                    
                                        
                                        block+=8
                                                                      
                                    
                                    if e10=="0":#0 not compressuon after compression
                                                   sda3=sda10+"0"+e5
                                                   sda4+=sda3
                                                 
                                    elif e10=="2":#can # compression after not compression
                                                  sda3=sda10+"1"+e5
                                                  sda4+=sda3
                                                

                                    if len(sda10)==0:
                                        sda4+="0"
                                    else:
                                        sda4+="1"
                                    sda10=""
                                    sda2=sda4
                                    cvf1+=1
                                    
                                    #print(len(sda2))


                                    if cvf1==4:
                                     
                                        long_1=len(sda2)
                                        add_bits=""
                                        count_bits=8-long_1%8
                                        z=0
                                        if count_bits!=0:
                                            while z<count_bits:
                                                add_bits="0"+add_bits
                                                z=z+1
                                        
                                     
                                        sda2=add_bits+sda2                                    




                                        n = int(sda2, 2)




                                        




                                        qqwslenf=len(sda2)




                                        qqwslenf=(qqwslenf/8)*2




                                        qqwslenf=str(qqwslenf)




                                        qqwslenf="%0"+qqwslenf+"x"




                                     




                                        jl=binascii.unhexlify(qqwslenf % n)




                                        sssssw=len(jl)




                                        data=jl




                                        qqqwz=qqqwz+1




                                        szxzzza=""




                                        szxzs=""




                                    




                                        assxw=assxw+1




                                        if assxw==1:




                                                assx=10




                                                if assx==10:




                                                  




                                                    f2.write(jl)




                                                    x2 = time()




                                                    x3=x2-x




                                                    return print(x3)

class extraction:

    def cryptography_extraction(self):
        namez = input("extract: e ")
        if namez == "e":
            name = input("Enter the name of the compressed file (e.g., file.Secret): ")

            with open(name, "rb") as binary_file:
                data = binary_file.read()
                sda2 = bin(int(binascii.hexlify(data), 16))[2:]

            cvf1 = 0
            sda10 = ""
            e10 = ""
            start = 1
            block = 0
            original_data = ""

            while block < len(sda2):
                e4 = sda2[block + 4:block + 7]
                e5 = sda2[block:block + 8]
                ch1 = sda2[block + 1:block + 3]
                r1 = sda2[block:block + 1]
                r2 = sda2[block + 7:block + 8]
                r4 = sda2[block + 6:block + 7]
                r5 = sda2[block + 1:block + 2]

                e8 = 0
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
                    e1 = format(e8, "01b")
                    sda5 = e1 + e1 + e5[3:8]
                    start = 0
                    e10 = "2"
                    sda10 += sda5
                    if len(sda6) == 15:
                        sda5 = ""
                        sda3 = ""

                elif e9 == e8 and r3 == e8 and len(e5) == 8 and start == 1:
                    sda5 = e5

                    e10 = "0"
                    start = 0

                    sda10 += sda5

                else:
                    if e10 == "0":
                        sda3 = sda10 + "0" + e5
                        original_data += sda3
                        sda10 = ""
                        start = 1

                    elif e10 == "2":
                        sda3 = sda10 + "1" + e5
                        original_data += sda3
                        sda10 = ""
                        start = 1

                if e8 == 1:
                    e8 = 0

                block += 8

            if e10 == "0":
                sda3 = sda10 + "0" + e5
                original_data += sda3

            elif e10 == "2":
                sda3 = sda10 + "1" + e5
                original_data += sda3

            original_data = original_data[:-8]  # Remove the padding bits
            original_bytes = bytearray(int(original_data[i:i + 8], 2) for i in range(0, len(original_data), 8))

            output_file_name = input("Enter the name of the output file: ")
            with open(output_file_name, "wb") as output_file:
                output_file.write(original_bytes)

            print("Extraction complete.")

if __name__ == "__main__":
    extractor = extraction()
    extractor.cryptography_extraction()



d=compression()



xw=d.cryptograpy_compression()

print(xw)

