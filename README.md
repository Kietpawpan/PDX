# PDX [Version 2.0.2]
โปรแกรม PDX (Personal Data Expert) เป็นซอฟแวร์ปัญญาประดิษฐ์ (AI) สำหรับให้ความเห็นแก่เจ้าหน้าที่ฝ่ายเลขานุการคณะกรรมการข้อมูลข่าวสารของ สป.ทส. เพื่อเสนอความเห็นประกอบการพิจารณาของคณะกรรมการฯ ว่าสมควรปฏิเสธคำขอหรือสมควรเปิดเผยข้อมูลส่วนบุคคลตามที่มีผู้ยื่นคำขอ ตามมาตรา 11 แห่งพระราชบัญญัติข้อมูลข่าวสารของราชการ พ.ศ. 2540 และพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 เหตุที่ต้องพัฒนาโปรแกรมนี้ เพราะพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ได้เริ่มบังคับใช้ตั้งแต่วันที่ 6 มิถุนายน 2565 แต่เจ้าหน้าที่ของรัฐยังขาดความรู้ความเข้าใจเกี่ยวกับการพิจารณาปฏิเสธคำขอข้อมูลส่วนบุคคลหรือการเปิดเผยข้อมูลส่วนบุคคลให้ถูกต้องตามกฎหมาย สป.ทส. โดยกองกลาง (ส่วนข้อมูลข่าวสารและบริการร่วม) จึงดำเนินโครงการพัฒนาปัญญาประดิษฐ์ ช่วยพิจารณาการเปิดเผยข้อมูลส่วนบุคคลของสำนักงานปลัดกระทรวงทรัพยากรธรรมชาติและสิงแวดล้อม เพื่อแก้ไขปัญหาดังกล่าว 

## วัตถุประสงค์ของซอฟแวร์
เพื่อเป็นเครื่องมือของฝ่ายเลขานุการคณะกรรมการข้อมูลข่าวสารของ สป.ทส. ในการให้บริการข้อมูลข่าวสารแก่ประชาชน โดยช่วยเสนอความเห็นประกอบการพิจารณาของคณะกรรมการฯ ว่าสมควรปฏิเสธคำขอหรือสมควรเปิดเผยข้อมูลส่วนบุคคลตามที่มีผู้ยื่นคำขอ ตามมาตรา 11 แห่งพระราชบัญญัติข้อมูลข่าวสารของราชการ พ.ศ. 2540 และพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 หรือไม่ อย่างไร เพราะเหตุใด ทั้งนี้ เพื่อให้การพิจารณามีคำสั่งปฏิเสธคำขอหรือเปิดเผยข้อมูลข่าวสารตามคำขอ เป็นไปอย่างรวดเร็วและถูกต้องตามเจตนารมณ์ของกฎหมาย ทั้งนี้ ผู้ใช้งานสามารถขอความเห็นของ AI ได้อย่างสะดวก รวดเร็ว เข้าถึงได้ง่าย ตลอด 24 ชั่วโมง ทุกวัน (ไม่เว้นวันหยุดราชการ)  
  
## ข้อมูลนำเข้า (input)
ผู้ใช้งานต้องแจ้งข้อเท็จจริง ตามที่ AI ร้องขอ โดยกดเลือกคำตอบบนหน้าต่างของโปรแกรม PDX 

## ข้อมูลนำออก (output)
1. ความเห็นของ AI เป็นข้อความภาษาไทย แสดงในกล่องข้อความ (Message Box) หลังจาก AI รวบรวมข้อเท็จจริงและประมวลผลตามข้อกฎหมายที่เกี่ยวข้อง แล้วประมวลผลตามข้อเท็จจริงและข้อกฎหมาย แบบ decision tree 
2. ความเห็นของ AI เป็นข้อความในไฟล์ .txt สำหรับคัดลอกและนำไปใช้งาน

## วิธีใช้งาน
1. ดาวน์โหลดไฟล์ source code (zip) ของโปรแกรม PDX ที่ https://github.com/Kietpawpan/PDX/releases
2. แตกไฟล์ (Unzip) และวางไฟล์ PDX.pyw บน Desktop ของเครื่องคอมพิวเตอร์ PC หรือ Notebook บนระบบปฏิบัติการ Windows 
3. ดาวโหลดโปรแกรม Python จาก https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe และติดตั้งโปรแกรมนี้ บนคอมพิวเตอร์เครื่องเดียวกัน
4. เปิดไฟล์ PDX.pyw โดยคลิกซ้ายที่ icon ไฟล์ดังกล่าว จำนวน 2 ครั้งติดกัน (double clicks)
5. กดปุ่ม RUN บนแถบเมนูของโปรแกรม PDX เพื่ออ่าน Disclaimer
- ถ้ากด Yes จะสามารถใช้งานโปรแกรมต่อไป โดยตอบคำถามต่าง ๆ ของ AI จนกว่า AI จะให้ความเห็น  
- ถ้ากด No ต้องกดปุ่ม OK เพื่อออกจากโปรแกรม


## Algorithm และ Source Code
https://raw.githubusercontent.com/Kietpawpan/PDX/main/PDX.pyw?token=GHSAT0AAAAAABWB7RZA7CNPCEYBBW2SUT22YV2R5AA

## Version History
- 2.0.2 เพิ่มกรณีเจ้าของข้อมูลเป็นผู้เยาว์ บุคคลไร้ความสามารถ หรือเสมือนไร้ความสามารถ
- 2.0.1 ปรับปรุงข้อความใน Disclaimer และ README
- 2.0.0 ปรับปรุง GUI และเพิ่มแถบเมนูและเมนูย่อย
- 1.0.0 เป็น prototype
