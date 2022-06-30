# Create the Home Screen
# Import module for creating GUI
import tkinter
from tkinter import *

# Import module for creating the menu tab
from tkinter import Menu

# Import module for showing message boxes
# (disclaimer, error warning, and outputs)
from tkinter import messagebox

# Import the webbrowser module for linking to Read Me at Github
import webbrowser

# Import the time module for counting the time to close the program
# when the user clicks No for disapproving the software usage condition
import time

tab1 = "Run"
tab1_1 = "ขอความเห็นจาก AI"
tab1_2 = "ออกจากโปรแกรม"
tab2 = "Help"
tab2_1 = "คู่มือการใช้งาน"
tab2_3 = "พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562"
tab2_2 = "ติดต่อผู้พัฒนา"
developer = "นายมนตรี เกียรติเผ่าพันธ์ ผู้อำนวยการส่วนข้อมูลข่าวสารและบริการร่วม " \
            "กองกลาง สป.ทส. โทร. 081 985 1897 " \
            "อีเมล monte.k@mnre.go.th"

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu, tearoff="off")
        fileMenu.add_command(label=tab1_1, command=Disclaimer)
        fileMenu.add_command(label=tab1_2, command=self.exitProgram)
        menu.add_cascade(label=tab1, menu=fileMenu)

        helpMenu = Menu(menu, tearoff="off")
        helpMenu.add_command(label=tab2_1, command=openReadMe)
        helpMenu.add_command(label=tab2_3, command=goToLaws)
        helpMenu.add_command(label=tab2_2, command=contactDeveloper)
        menu.add_cascade(label=tab2, menu=helpMenu)

    def exitProgram(self):
        exit()

# Create object
root = Tk()

# Set the title with the copyright symbol and the developer's organization
root.title("โปรแกรม Personal Data Expert (PDX) \xa9 กองกลาง สป.ทส.")

# Set the program window size
root.geometry("500x300")

# Set the font size of the program screen to 20 px
root.option_add("*font", "25")

root.option_add('*Dialog.msg.font', 40)

# Create frame
frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")

# Set the program name
programName = "PDX"

# Set the font name and font size variables in the program window
programNameFont = "Arial Bold"
programNameFontSize = 40
fontColor = "lightgray"

# Set the disclaimer text
disclaimerText = "ซอฟต์แวร์นี้ พัฒนาโดยนายมนตรี เกียรติเผ่าพันธ์ ผู้อำนวยการส่วนข้อมูลข่าวสาร" \
                 "และบริการร่วม กองกลาง สป.ทส. ภายใต้โครงการพัฒนาปัญญาประดิษฐ์ " \
                 "ช่วยพิจารณาการเปิดเผยข้อมูลส่วนบุคคลของสำนักงานปลัดกระทรวง" \
                 "ทรัพยากรธรรมชาติและสิ่งแวดล้อม และเผยแพร่ซอฟต์แวร์นี้ " \
                 "เพื่อทดสอบประสิทธิภาพการทำงานของซอฟแวร์ ผู้พัฒนา " \
                 "จึงไม่รับรองความถูกต้องหรือประสิทธิภาพการทำงานของ" \
                 "ซอฟต์แวร์ ตลอดจนไม่รับประกันความเสียหายต่าง ๆ " \
                 "อันเกิดจากการใช้ซอฟต์แวร์นี้ ท่านยอมรับ" \
                 "ข้อตกลงการใช้ซอฟแวร์นี้หรือไม่?"

# Set the data type of warning text
warningText = StringVar()

# Set the warning text when the user clicks the confirm button
# without clicking and choice
warningText.set("โปรดเลือกคำตอบก่อนกดปุ่มยืนยัน โดยกดที่คำถาม กดคำตอบ แล้วกดยืนยัน")

# Set the option IDs and their values for decision tree (3 layers)
Option1 = "- เจ้าของข้อมูลส่วนบุคคล"
Option2 = "- ไม่ใช่ เจ้าของข้อมูลส่วนบุคคล"

Option1_1 = "1.1 ขอสำเนาหรือขอให้เปิดเผยถึงการได้มา"
Option1_2 = "1.2 ขอข้อมูลรูปแบบที่อ่านหรือใช้งานทั่วไปด้วยเครื่องมือหรือ" \
            "อุปกรณ์ที่ทำงานได้โดยอัตโนมัติ และสามารถใช้หรือเปิดเผย" \
            "ข้ออมูลส่วนบุคคลได้ด้วยวิธีการอัตโนมัติ"
Option1_3 = "1.3 ขอข้อมูลตามข้อ 1.2 ที่ส่งหรือโอนไปยังผู้ควบคุมข้อมูลส่วนบุคคลอื่นโดยตรง"

Option2_1 = "2.1 ได้รับความยินยอมจากเจ้าของข้อมูล"
Option2_2 = "2.2 ไม่ได้รับ ความยินยอมจากเจ้าของข้อมูล"

Option1_1_1 = "1.1.1 มีกฎหมายหรือมีคำสั่งศาลห้ามเปิดเผยและจะกระทบสิทธิเสรีภาพของบุคคลอื่น"
Option1_1_2 = "1.1.2 ไม่เข้าเงื่อนไขดังกล่าว"

Option1_2_1 = "1.2.1 เป็นการปฏิบัติหน้าที่เพื่อประโยชน์สาธารณะ หรือ" \
              "การใช้สิทธินั้นละเมิดสิทธิหรือเสรีภาพของบุคคลอื่น"
Option1_2_2 = "1.2.2 ไม่เข้าเงื่อนไขดังกล่าว"

Option2_1_1 = "2.1.1 มีการขอความยินยอม ถูกต้องตามหมวด 2 แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562"
Option2_1_2 = "2.1.2 มีการขอความยินยอม แต่ดำเนินการไม่ถูกต้องตามหมวด 2 แห่ง พ.ร.บ. ฉบับเดียวกัน"

Option2_2_1 = "- เป็นข้อมูลส่วนบุคคล ตามมาตรา 24 หรือ 26 แห่ง พ.ร.บ. ข้อมูลส่วนบุคคล " \
              "พ.ศ. 2562 หรือกฎหมายอื่น ที่บัญญัติให้เปิดเผยได้" \
              "โดยไม่ต้องขอความยินยอมจากเจ้าของข้อมูล"
Option2_2_2 = "- เป็นข้อมูลส่วนบุคคล ที่ไม่มีบทบัญญัติแห่งกฎหมายใด บัญญัติให้เปิดเผยได้ " \
              "โดยไม่ต้องขอความยินยอมจากเจ้าของข้อมูล"

# Set the dropdown menu options
choices0 = [Option1, Option2]
choices1_1 = [Option1_1, Option1_2, Option1_3]
choices1_1_1 = [Option1_1_1, Option1_1_2]
choices1_2 = [Option1_2_1, Option1_2_2]
choices2_1 = [Option2_1, Option2_2]
choices2_2 = [Option2_2_1, Option2_2_2]
choices2_1_1 = [Option2_1_1, Option2_1_2]

# Set the datatype of menu text
question0 = StringVar()
question1 = StringVar()
question2 = StringVar()
question1_1 = StringVar()
question1_2 = StringVar()
question2_1 = StringVar()
question2_2 = StringVar()

# Set the datatype of output text
output1_1_1 = StringVar()
output1_1_2 = StringVar()
output1_2_1 = StringVar()
output1_2_2 = StringVar()
output2_1_1 = StringVar()
output2_1_2 = StringVar()
output1_3 = StringVar()
output2_2_1 = StringVar()
output2_2_2 = StringVar()

# Set the questions
question0.set("ผู้ขอเป็นบุคคลใด?")
question1.set("ขอข้อมูลประเภทใด?")
question2.set("ได้รับความยินยอมหรือไม่ อย่างไร?")
question1_1.set("หากปฏิเสธการเปิดเผย จะเข้าเงื่อนไขใด?")
question1_2.set("หากปฏิเสธการเปิดเผย จะมีเหตุผลใด?")
question2_1.set("การขอความยินยอม มีลักษณะตามข้อใด?")
question2_2.set("ข้อมูลข่าวสารตามคำขอ มีลักษณะตามข้อใด")

# Set the output text for each decision branch
output1_1_1.set("สมควรปฏิเสธการเปิดเผย เนื่องจากเป็นการปฏิบัติตามกฎหมายหรือคำสั่งศาล "
                "และการเข้าถึงและขอรับสำเนาข้อมูลส่วนบุคคลนั้นจะส่งผลกระทบ"
                "ที่อาจก่อให้เกิดความเสียหายต่อสิทธิและเสรีภาพของบุคคลอื่น "
                "ตามมาตรา 30 วรรคสอง แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล "
                "พ.ศ. 2562")
output1_1_2.set("ให้ดำเนินการตามคำขอโดยไม่ชักช้า "
                "แต่ต้องไม่เกินสามสิบวันนับแต่วันที่ได้รับคำขอ ตามมาตรา 30 วรรคสี่ "
                "แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 "
                "เนื่องจากเป็นการขอเข้าถึงและขอรับสำเนา"
                "ข้อมูลส่วนบุคคลที่เกี่ยวกับตน ซึ่งอยู่ในความรับผิดชอบของผู้ควบคุมข้อมูล"
                "ส่วนบุคคล หรือขอให้เปิดเผยถึงการได้มาซึ่งข้อมูลส่วนบุคคลดังกล่าว"
                "ที่ตนไม่ได้ให้ความยินยอม โดยไม่เข้าเงื่อนไขตามมาตรา "
                "30 วรรคสอง แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 "
                "ที่ผู้ควบคุมข้อมูลส่วนบุคคลอาจปฏิเสธคำขอได้")
output1_2_1.set("สมควรปฏิเสธการเปิดเผย เนื่องจากเป็นการปฏิบัติหน้าที่เพื่อประโยชน์สาธารณะ"
                "หรือเป็นการปฏิบัติหน้าที่ตามกฎหมาย และบันทึกการปฏิเสธคำขอพร้อม"
                "ด้วยเหตุผลไว้ในรายการตามมาตรา 39 แห่ง พ.ร.บ. "
                "คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 อนึ่ง หากการใช้สิทธิขอข้อมูลนั้น "
                "ละเมิดสิทธิหรือเสรีภาพของบุคคลอื่น ก็สามารถปฏิเสธการเปิดเผยได้ "
                "ทั้งนี้ เป็นการปฏิบัติตามมาตรา 31 วรรคสาม "
                "แห่ง พ.ร.บ. ฉบับเดียวกัน")
output1_2_2.set("ให้ดำเนินการตามคำขอโดยไม่ชักช้า "
                "แต่ต้องไม่เกินสามสิบวันนับแต่วันที่ได้รับคำขอ "
                "ตามตามมาตรา 31 แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล "
                "พ.ศ. 2562 เนื่องจากไม่เข้าเงื่อนไขที่อาจปฏิเสธคำขอได้")
output2_1_1.set("สมควรเปิดเผย เนื่องจากได้รับความยินยอม"
                "จากเจ้าของข้อมูลส่วนบุคคล อย่างถูกต้องตามหมวด 2 แห่ง พ.ร.บ. "
                "คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ทั้งนี้ "
                "ต้องตรวจสอบวัตถุประสงค์ของการนำข้อมูลไปใช้ที่ระบุในคำขอ "
                "ต้องไม่แตกต่างจากวัตถุประสงค์ที่ได้แจ้งให้เจ้าของข้อมูลทราบ "
                "เว้นแต่มีบทบัญญัติแห่ง พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 "
                "หรือกฎหมายอื่น บัญญัติให้เปิดเผยเพื่อการนั้นได้")
output2_1_2.set("สมควรปฏิเสธคำขอ เนื่องจากการขอความยินยอมจากเจ้าของ"
                "ข้อมูลส่วนบุคคลไม่เป็นไปตามที่กำหนดไว้ในหมวด 2 "
                "แห่ง พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 "
                "จึงไม่มีผลผูกพันเจ้าของข้อมูลส่วนบุคคล และไม่ทำให้"
                "ผู้ควบคุมข้อมูลส่วนบุคคลสามารถเปิดเผยข้อมูลส่วนบุคคลได้ "
                "จึงต้องปฏิเสธคำขอ ตามมาตรา 19 วรรคเจ็ด แห่ง พ.ร.บ. คุ้มครอง"
                "ข้อมูลส่วนบุคคล พ.ศ. 2562")
output1_3.set("ให้ดำเนินการตามคำขอโดยไม่ชักช้า แต่ต้องไม่เกินสามสิบวันนับแต่วันที่ได้รับคำขอ "
              "เว้นแต่โดยสภาพทางเทคนิคไม่สามารถทำได้ ตามมาตรา 31 แห่ง "
              "พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 เนื่องจากเป็น"
              "ข้อมูลส่วนบุคคลที่ผู้ควบคุมข้อมูลส่วนบุคคลส่งหรือโอนข้อมูลส่วนบุคคล"
              "ในรูปแบบที่สามารถอ่านหรือใช้งานโดยทั่วไปได้ด้วยเครื่องมือหรืออุปกรณ์"
              "ที่ทำงานได้โดยอัตโนมัติและสามารถใช้หรือเปิดเผยข้อมูลส่วนบุคคลได้"
              "ด้วยวิธีการอัตโนมัตดังกล่าวไปยังผู้ควบคุมข้อมูลส่วนบุคคลอื่นโดยตรง")
output2_2_1.set("สมควรเปิดเผยข้อมูล ตามบทบัญญัติของกฎหมายที่ให้กระทำได้"
                "โดยไม่ต้องขอความยินยอมจากเจ้าของข้อมูล ทั้งนี้ เป็นการปฏิบัติตาม"
                "มาตรา 19 แห่ง พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562")
output2_2_2.set("สมควรปฏิเสธการเปิดเผย เนื่องจากไม่ใช่ข้อมูลส่วนบุคคลที่เก็บรวบรวม"
                "ได้โดยได้รับยกเว้นไม่ต้องขอความยินยอมตามมาตรา 24 หรือมาตรา 26"
                " แห่ง พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 "
                "และผู้ยื่นคำขอไม่ได้รับความยินยอมเป็นหนังสือจากเจ้าของ"
                "ข้อมูลส่วนบุคคล จึงต้องปฏิบัติตามมาตรา 27 แห่ง พ.ร.บ. "
                "คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 ห้ามมิให้ผู้ควบ"
                "คุมข้อมูลส่วนบุคคลเปิดเผยข้อมูลส่วนบุคคลโดยไม่ได้รับความ"
                "ยินยอมจากเจ้าของข้อมูลส่วนบุคคล")

def reset():
    for child in root.winfo_children():
        child.destroy()

# Create Open Readme function. To open the url
def openReadMe():
    # Define which url to pen
    webbrowser.open('https://github.com/Kietpawpan/PDX#readme')

def contactDeveloper():
    messagebox.showinfo("Contact", developer)

def goToLaws():
    webbrowser.open('https://www.mdes.go.th/law/detail/3541')

def AIEngine():
    # Clear the app screen
    reset()

    # Create the menu
    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master

            menu = Menu(self.master)
            self.master.config(menu=menu)

            fileMenu = Menu(menu, tearoff="off")
            fileMenu.add_command(label=tab1_1, command=Disclaimer)
            fileMenu.add_command(label=tab1_2, command=self.exitProgram)
            menu.add_cascade(label=tab1, menu=fileMenu)

            helpMenu = Menu(menu, tearoff="off")
            helpMenu.add_command(label=tab2_1, command=openReadMe)
            helpMenu.add_command(label=tab2_3, command=goToLaws)
            helpMenu.add_command(label=tab2_2, command=contactDeveloper)
            menu.add_cascade(label=tab2, menu=helpMenu)

        def exitProgram(self):
            exit()

    # Place the menu in the root window
    app = Window(root)

    # Create a blank row on the Home Screen
    label = Label(root, text="")
    label.pack()

    # Show the program name on the Home Screen
    label = Label(root, text=programName, font=(programNameFont, programNameFontSize), fg=fontColor)
    label.pack()

    # Create a blank row on the Home Screen
    label = Label(root, text="")
    label.pack()

    # Create Dropdown menu for the first question
    drop0 = OptionMenu(root, question0, *choices0)
    drop0.pack()

    # Create button, it will change label text
    button = Button(root, text="ยืนยัน", command=Query).pack()

    # Create a blank row on the Home Screen
    label = Label(root, text="")
    label.pack()



# Set the result for each clicks on each option (1.1 - 1.3) of Question 0
# If the selected option of Question 0 is Option 1 (Data Owner),
# then show Question 1 (What types of data being requested?),
# and drop the choices of Question 1 (Choices1_1),
# including 3 options (Copy/source data, machine-readable data, and transferred data)
# Add the button beneath the question, which leads to the next decision point,
# that deals with the effect of each selected choice of Question 1
def Query():
    # If the user clicks Option 1
    if question0.get() == Option1: # Owner
        # Clear the app screen
        reset()

        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()

        # Place the menu in the root window
        app = Window(root)

        # Add a blank line
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg=fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show Question 1 due to the selected Option 1, and drop its choices
        drop1_1 = OptionMenu(root, question1, *choices1_1) # What types of data being requested?
        # Locate the choices on the screen
        drop1_1.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1).pack()
    # If Option 2 is clicked,
    elif question0.get() == Option2:
        # Clear the app screen
        reset()

        # Create the menu
        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()
        # Place the menu in the root window
        app = Window(root)

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg=fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Set the question and the choices for Option 2.1
        drop2_1 = OptionMenu(root, question2, *choices2_1)
        # Locate the choices on the screen
        drop2_1.pack()
        # Show Button for Question 1.1
        button = Button(root, text="ยืนยัน", command=Query2).pack()
    # If the user clicks the confirm button without clicking any choice,
    else:
        # Show the warning message
        messagebox.showwarning("Warning", warningText.get())

# Set effect when clicking each choice of Question 2 (Owner's allowance)
def Query2():
    # If Choice 2.1 (with owner's allowance) is selected,
    if question2.get() == Option2_1:

        # Clear the app screen
        reset()

        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()
            def exitProgram(self):
                exit()

        # Place the menu in the root window
        app = Window(root)

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg = fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # and show Question 2.1 (Legally?) with its choices
        drop2_1 = OptionMenu(root, question2_1, *choices2_1_1)
        # Locate the choices on the screen
        drop2_1.pack()
        # Show Button leading to Query 2.1.1
        button = Button(root, text="ยืนยัน", command=Query2_1_1).pack()

    # If Choice 2.2 (No owner's allowance) is selected, then reject the disclosure
    elif question2.get() == Option2_2:
        # Clear the app screen
        reset()

        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()

        # Place the menu in the root window
        app = Window(root)


        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg=fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # and show Question 2.2 (Laws allows?) with its choices
        drop2_2 = OptionMenu(root, question2_2, *choices2_2)
        # Locate the choices on the screen
        drop2_2.pack()
        # Show Button leading to Query 2.2
        button = Button(root, text="ยืนยัน", command=Query2_2).pack()
    # If the user clicks the confirm button without clicking any choice,
    else:
        # Show the warning message
        messagebox.showwarning("Warning", warningText.get())

# Set the effect of clicking choices in Question 2.2
def Query2_2():
    # If Option 2.2.1 (Laws allows) is clicked,
    if question2_2.get() == Option2_2_1:
        # show text "Done!"
        Output2_2_1Label = Label(root, text="Done!")
        Output2_2_1Label.pack()
        # then, show Output 2.2.1 as text in the message box
        messagebox.showinfo("AI Opinion (Output 2.2.1)", output2_2_1.get())
    # If Option 2.2.2 (No laws allows) is clicked,
    elif question2_2.get() == Option2_2_2:
        # show text "Done!"
        Output2_2_2Label = Label(root, text="Done!")
        Output2_2_2Label.pack()
        # then, show Output 2.2.2 as text in the message box.
        messagebox.showinfo("AI Opinion (Output 2.2.2)", output2_2_2.get())
    # If no choice is clicked, but the confirmation button is clicked,
    else:
        # show the warning message
        messagebox.showwarning("Warning", warningText.get())

# Set the effect for each choice of Question 2.1 (Legally asked for permission)
def Query2_1_1():
       # If Choice 2.1.1 (Legal permission) is selected
       if question2_1.get() == Option2_1_1:
           # Show the text "Done!" on the screen
           Output2_1_1Label = Label(root, text="Done!")
           # Locate the text on the screen
           Output2_1_1Label.pack()
           # then, show Output 2.1.1 as text in the message box.
           # Show the message box to give the expert opinion for Node 2.1.1
           messagebox.showinfo("AI Opinion (Output 2.1.1)", output2_1_1.get())
       # If Choice 2.1.2 is selected, then give the opinion
       elif question2_1.get() == Option2_1_2:
           Output2_1_2Label = Label(root, text="Done!")
           Output2_1_2Label.pack()
           # then, show Output 2.1.2 as text in the message box.
           # Show the message box to give the expert opinion for Node 2.1.2
           messagebox.showinfo("AI Opinion (Output 2.1.2)", output2_1_2.get())
       # If the user clicks the confirm button without clicking any choice,
       else:
           # Show the warning message
            messagebox.showwarning("Warning", warningText.get())
# Set the effect for each selected choice for "What types of data being requested?"
def Query1():
    # If Option 1.1 (copy or source) is clicked, show Question 1.1 (Is there laws?)
    if question1.get() == Option1_1:
        # Clear the app screen
        reset()

        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()

        # Place the menu in the root window
        app = Window(root)

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg=fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Set the question and show the choices for Option 1.1.1,
        # whether there is laws or no laws to refuse the request
        drop1_1 = OptionMenu(root, question1_1, *choices1_1_1)
        # Locate the choices on the screen
        drop1_1.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1_1).pack()

    # If Option 1.2 (Machine-readable data) is clicked, show Question 1.2 (Authority)
    elif question1.get() == Option1_2:
        # Clear the app screen
        reset()

        # Create the menu
        class Window(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.master = master

                menu = Menu(self.master)
                self.master.config(menu=menu)

                fileMenu = Menu(menu, tearoff="off")
                fileMenu.add_command(label=tab1_1, command=Disclaimer)
                fileMenu.add_command(label=tab1_2, command=self.exitProgram)
                menu.add_cascade(label=tab1, menu=fileMenu)

                helpMenu = Menu(menu, tearoff="off")
                helpMenu.add_command(label=tab2_1, command=openReadMe)
                helpMenu.add_command(label=tab2_3, command=goToLaws)
                helpMenu.add_command(label=tab2_2, command=contactDeveloper)
                menu.add_cascade(label=tab2, menu=helpMenu)

            def exitProgram(self):
                exit()

        # Place the menu in the root window
        app = Window(root)

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Show the program name on the Home Screen
        label = Label(root, text=programName, font=(
            programNameFont,
            programNameFontSize),
                      fg=fontColor)
        label.pack()

        # Create a blank row on the Home Screen
        label = Label(root, text="")
        label.pack()

        # Set the question and show the choices for Option 1.2,
        # whether there is authority or not
        drop1_2 = OptionMenu(root, question1_2, *choices1_2)
        # Locate the choices on the screen
        drop1_2.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1_2).pack()

    # If Option 1.3 is clicked (Transferred data), go to Output 1.3
    elif question1.get() == Option1_3:
        Output1_3Label = Label(root, text="Done!")
        Output1_3Label.pack()
        # then, show Output 1.3 as text in the message box.
        # Show the message box to give the expert opinion for Node 1.3
        messagebox.showinfo("AI Opinion (Output 1.3)", output1_3.get())

    # If the user clicks the confirm button without clicking any choice,
    else:
        # Show the warning message
        messagebox.showwarning("Warning", warningText.get())

# Set the output for each choice in Question 1.1 (Is there laws?)
def Query1_1():
    # If the answer is Option 1.1.1 (Yes, there is the laws)
    if question1_1.get() == Option1_1_1:
        # Show text on the program screen: Done!
        Output1_1_1Label = Label(root, text="Done!")
        Output1_1_1Label.pack()
        # then, show Output 1.1.1 as text in the message box.
        # Show the message box to give the expert opinion for Node 1.1.1
        messagebox.showinfo("AI Opinion (Output 1.1.1)", output1_1_1.get())

    # If the answer is Option 1.1.2 (No, there is no laws)
    elif question1_1.get() == Option1_1_2:
        # Show text on the program screen: Done!
        Output1_1_2Label = Label(root, text="Done!")
        Output1_1_2Label.pack()
        # Show the message box to give the expert opinion for Node 1.1.1
        messagebox.showinfo("AI Opinion (Output 1.1.2)", output1_1_2.get())

    # If the user clicks the confirm button without clicking any choice,
    else:
        # Show the warning message
        messagebox.showwarning("Warning", warningText.get())

# Set the output for each choice in Question 1.2 (Machine-readable?)
def Query1_2():
    # If the answer is Option 1.2.1 (Yes, authority)
    if question1_2.get() == Option1_2_1:
        # Show text on the program screen: Done!
        Output1_2_1Label = Label(root, text="Done!")
        Output1_2_1Label.pack()
        # then, show Output 1.2.1 as text in the message box.
        # Show the message box to give the expert opinion
        messagebox.showinfo("AI Opinion (Output 1.2.1)", output1_2_1.get())

    # If the answer is Option 1.2.2 (Yes, Not authority)
    # Show text on the program screen: Done!
    elif question1_2.get() == Option1_2_2:
        Output1_2_2Label = Label(root, text="Done!")
        Output1_2_2Label.pack()
        # then, show Output 1.2.2 as text in the message box.
        # Show the message box to give the expert opinion
        messagebox.showinfo("AI Opinion (Output 1.2.2)", output1_2_2.get())
    # If the user clicks the confirm button without clicking any choice,
    else:
        # Show the warning message
        messagebox.showwarning("Warning", warningText.get())

def Disclaimer():
    response = messagebox.askquestion("Disclaimer", disclaimerText)
    if response == 'yes':
        AIEngine()
    elif response == "no":
        messagebox.showinfo("Response", "โปรดกดปุ่ม OK เพื่อออกจากโปรแกรม")
        time.sleep(0)
        root.quit()


# Add the program (root) in the menu window
app = Window(root)

# Execute tkinter
root.mainloop()

