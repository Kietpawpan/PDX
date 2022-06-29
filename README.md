# PDX
PDX (Personal Data Expert) เป็นโปรแกรมคอมพิวเตอร์ ประเภทซอฟแวร์ปัญญาประดิษฐ์ (AI) สำหรับให้ความเห็นแก่เจ้าหน้าที่ของรัฐ เพื่อประกอบการพิจารณาเสนอร่างคำสั่ง กรณีมีผู้ยื่นคำขอข้อมูลส่วนบุคคลต่อหน่วยงานของรัฐ ตามมาตรา 11 แห่งพระราชบัญญัติข้อมูลข่าวสารของราชการ พ.ศ. 2540 และพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 สืบเนื่องจากเจ้าหน้าที่ของรัฐที่เกี่ยวข้องยังขาดความรู้ความเข้าใจเกี่ยวกับการพิจารณาปฏิเสธคำขอข้อมูลส่วนบุคคลหรือการเปิดเผยข้อมูลส่วนบุคคลให้ถูกต้องตามพระราชบัญญัติข้อมูลข่าวสารของราชการ พ.ศ. 2540 และพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ซอฟแวร์นี้ จึงพัฒนาขึ้น ภายใต้โครงการพัฒนาปัญญาประดิษฐ์ ช่วยพิจารณาการเปิดเผยข้อมูลส่วนบุคคลของสำนักงานปลัดกระทรวงทรัพยากรธรรมชาติและสิงแวดล้อม 

## วัตถุประสงค์ของซอฟแวร์
เพื่อให้คำปรึกษาแก่เจ้าหน้าที่ของรัฐ ในฐานะผู้ควบคุมข้อมูลส่วนบุคคล ในการพิจารณามีคำสั่งปฏิเสธหรือเปิดเผยข้อมูลข่าวสาร กรณีมีผู้ยื่นคำขอข้อมูลส่วนบุคคลต่อหน่วยงานของรัฐ ตามมาตรา 11 แห่งพระราชบัญญัติข้อมูลข่าวสารของราชการ พ.ศ. 2540 และพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ทั้งนี้ เพื่อให้การพิจารณามีคำสั่งปฏิเสธคำขอหรือเปิดเผยข้อมูลข่าวสารตามคำขอ เป็นไปอย่างรวดเร็วและถูกต้องตามเจตนารมณ์ของกฎหมาย โดยผู้ใช้งานสามารถขอรับคำปรึกษาจาก AI ได้ตลอด 24 ชั่วโมง  
  
## ข้อมูลนำเข้า
ผู้ใช้งานต้องแจ้งข้อเท็จจริง ตามที่ AI ร้องขอ โดยกดเลือกคำตอบบนหน้าต่างของโปรแกรม PDX 

## ข้อมูลผลลัพท์
AI เสนอความเห็นเป็นข้อความภาษาไทย ปรากฏในกล่องข้อความ (Message Box) หลังจากมีการรวบรวมข้อเท็จจริงและประมวลผลตามข้อกฎหมายที่เกี่ยวข้อง ซึ่งเก็บไว้ในสมองของ AI ที่เชื่อมโยงข้อเท็จจริงและข้อกฎหมายเพื่อการตัดสินใจแบบ decision tree

## วิธีใช้งาน
1. ดาวน์โหลดไฟล์ source code (zip) โปรแกรม PDX ที่ https://github.com/Kietpawpan/PDX/releases
2. แตกไฟล์ (Unzip) และวางไฟล์ PDX.pyw บน Desktop ของเครื่องคอมพิวเตอร์ PC หรือ Notebook บนระบบปฏิบัติการ Windows 
3. ดาวโหลดโปรแกรม Python ที่ https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe และติดตั้งบนเครื่องคอมพิวเตอร์นั้น 
4. เปิดไฟล์ PDX.pyw
5. กดปุ่ม START อ่านข้อมูล Disclaimer แล้วกดปุ่ม Yes หรือ No ตามที่เห็นสมควร
- ถ้ากด Yes จะสามารถใช้งานโปรแกรมต่อไป โดยอ่านคำถามและเลือกคำตอบที่ถูกต้องตามข้อเท็จจริง จนกว่า AI จะให้ความเห็น  
- ถ้ากด No ต้องกดปุ่ม OK เพื่อปิดโปรแกรม


## Algorithm และ Source Code
อ้างถึง https://raw.githubusercontent.com/Kietpawpan/PDX/main/PDX.pyw?token=GHSAT0AAAAAABWB7RZA7CNPCEYBBW2SUT22YV2R5AA

## ผู้พัฒนาซอฟแวร์
นายมนตรี เกียรติเผ่าพันธ์ monte.k @ mnre.go.th
