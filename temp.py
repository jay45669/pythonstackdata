import pandas as pd
import glob

path = r'C:\Users\jrm\Desktop\SPI data\Stack' # Path
all_files = glob.glob(path + "/*.csv")        # หาที่อยู่และชื่อไฟล์ทั้งหมด
df = pd.DataFrame()                             #สร้าง Dataframe

for f in all_files:                         #วนอ่านซ้ำ
    
    alldata = pd.read_csv(f,header=9,usecols=[4,6,8,34,38],error_bad_lines=False)      #อ่านค่า ทั้งหมดในโฟลดเดอร์
    datatype_ground_small = alldata[alldata['Parts name']=='GROUND_BIG']        #sort เฉพาะ Componant
    datasortzero=datatype_ground_small[datatype_ground_small['Volume']!=0]  #Sort 0 ออก
    #Avr = datasortzero["Volume"].mean()         #หาค่าเฉลี่ย
    #mean = pd.DataFrame({"Volume":[Avr]})       #สร้าง Dataframe ของ Avr
    df = df.append(datasortzero)                       #Stack data
    df.to_csv('C:/Users/jrm/Documents/gb_all.csv')   #export ไฟล์
        
print(df)   

