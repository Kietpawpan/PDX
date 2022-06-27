# Import module
import tkinter
from tkinter import *

# Import message box module
from tkinter import messagebox

# Create object
root = Tk()

# Set the title, GUI size, and font size
root.title("PDX-v1.0.0")
root.geometry("700x300")
root.option_add("*font", "20")

# Set the option IDs and their values for decision tree (3 layers)
Option1 = "เจ้าของข้อมูลส่วนบุคคล"
Option2 = "ไม่ใช่ เจ้าของข้อมูลส่วนบุคคล"

Option1_1 = "1.1 ขอสำเนาหรือขอให้เปิดเผยถึงการได้มา"
Option1_2 = "1.2 ขอข้อมูลรูปแบบที่อ่านหรือใช้งานทั่วไปด้วยเครื่องมืออัตโนมัติ"
Option1_3 = "1.3 ขอข้อมูลที่ส่งหรือโอนไปผู้ควบคุมอื่น"

Option2_1 = "2.1 ได้รับความยินยอมจากเจ้าของข้อมูล"
Option2_2 = "2.2 ไม่ได้รับ ความยินยอมจากเจ้าของข้อมูล"

Option1_1_1 = "1.1.1 มีกฎหมายหรือมีคำสั่งศาลห้ามเปิดเผยและจะกระทบสิทธิเสรีภาพของบุคคลอื่น"
Option1_1_2 = "1.1.2 ไม่เข้าเงื่อนไขดังกล่าว"

Option1_2_1 = "1.2.1 ปฏิบัติหน้าที่เพื่อประโยชน์สาธารณะ"
Option1_2_2 = "1.2.2 ไม่เข้าเงื่อนไขดังกล่าว"

Option2_1_1 = "2.1.1 การขอความยินยอม ถูกต้อง ตามกฎหมาย"
Option2_1_2 = "2.1.2 การขอความยินยอม ไม่ถูกต้อง ตามกฎหมาย"

# Set the dropdown menu options
choices0 = [Option1, Option2]
choices1_1 = [Option1_1, Option1_2, Option1_3]
choices1_1_1 = [Option1_1_1, Option1_1_2]
choices1_2 = [Option1_2_1, Option1_2_2]
choices2_1 = [Option2_1, Option2_2]
choices2_1_1 = [Option2_1_1, Option2_1_2]

# Set the datatype of menu text
question0 = StringVar()
question1 = StringVar()
question2 = StringVar()
question1_1 = StringVar()
question1_2 = StringVar()
question2_1 = StringVar()



# Set the questions
question0.set("ผู้ขอเป็นบุคคลใด?")
question1.set("ขอข้อมูลประเภทใด?")
question2.set("ได้รับความยินยอมหรือไม่ อย่างไร?")
question1_1.set("หากปฏิเสธการเปิดเผย จะเข้าเงื่อนไขใด?")
question1_2.set("เป็นอำนาจหน้าที่?")
question2_1.set("การขอความยินยอม มีลักษณะตามข้อใด?")


# Create the function to clear screen of the root window
def reset():
    for child in root.winfo_children():
        child.destroy()

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
        # Reset the screen
        reset()
        # Show Question 1 due to the selected Option 1, and drop its choices
        drop1_1 = OptionMenu(root, question1, *choices1_1) # What types of data being requested?
        # Locate the choices on the screen
        drop1_1.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1).pack()
    else:
        reset()
        # Set the question and the choices for Option 2.1
        drop2_1 = OptionMenu(root, question2, *choices2_1)
        # Locate the choices on the screen
        drop2_1.pack()
        # Show Button for Question 1.1
        button = Button(root, text="ยืนยัน", command=Query2).pack()

# Set effect when clicking each choice of Question 2 (Owner's allowance)
def Query2():
    # If Choice 2.1 (with owner's allowance) is selected,
    if question2.get() == Option2_1:
    # then reset the screen
        reset()
        # and show Question 2.1 (Legally?) with its choices
        drop2_1 = OptionMenu(root, question2_1, *choices2_1_1)
        # Locate the choices on the screen
        drop2_1.pack()
        # Show Button leading to Query 2.1.1
        button = Button(root, text="ยืนยัน", command=Query2_1_1).pack()
    # If Choice 2.2 (No owner's allowance) is selected, then reject the disclosure
    else:
        Output2_2Label = Label(root, text="Done!")
        Output2_2Label.pack()
        # then, show Output 2.2 as text in the message box.
        # Show the message box to give the expert opinion for Node 2.2
        messagebox.showinfo("AI Opinion (Output 2.2)", "ปฏิเสธ เนื่องจากไม่ได้รับ"
                                                         "ความยินยอมเป็นหนังสือ"
                                                         "จากเจ้าของข้อมูลส่วนบุคคล"
                            )
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
           messagebox.showinfo("AI Opinion (Output 2.1.1)", "เปิดเผย เนื่องจากได้รับ"
                                                             "ความยินยอมเป็นหนังสือ"
                                                             "จากเจ้าของข้อมูลส่วนบุคคล"
                                                         "อย่างถูกต้องตามกฎหมาย"
                                )
       # If Choice 2.1.2 is selected, then give the opinion
       else:
           Output2_1_2Label = Label(root, text="Done!")
           Output2_1_2Label.pack()
           # then, show Output 2.1.2 as text in the message box.
           # Show the message box to give the expert opinion for Node 2.1.2
           messagebox.showinfo("AI Opinion (Output 2.1.2)", "ปฏิเสธ แม้ว่าจะได้รับ"
                                                             "ความยินยอมเป็นหนังสือ"
                                                             "จากเจ้าของข้อมูลส่วนบุคคล"
                                                             "แต่การขอนั้น ไม่ถูกต้องตามกฎหมาย"
                               )
# Set the effect for each selected choice for "What types of data being requested?"
def Query1():
    # If Option 1.1 (copy or source) is clicked, show Question 1.1 (Is there laws?)
    if question1.get() == Option1_1:
        # Reset the screen
        reset()
        # Set the question and show the choices for Option 1.1.1,
        # whether there is laws or no laws to refuse the request
        drop1_1 = OptionMenu(root, question1_1, *choices1_1_1)
        # Locate the choices on the screen
        drop1_1.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1_1).pack()

    # If Option 1.2 (Machine-readable data) is clicked, show Question 1.2 (Authority)
    elif question1.get() == Option1_2:
        # Reset the screen
        reset()
        # Set the question and show the choices for Option 1.2,
        # whether there is authority or not
        drop1_2 = OptionMenu(root, question1_2, *choices1_2)
        # Locate the choices on the screen
        drop1_2.pack()
        # Show Button leading to Query 1.1.1
        button = Button(root, text="ยืนยัน", command=Query1_2).pack()
    # If Option 1.3 is clicked (Transferred data), go to Output 1.3.0
    else:
        Output1_3_0Label = Label(root, text="Done!")
        Output1_3_0Label.pack()
        # then, show Output 1.1.1 as text in the message box.
        # Show the message box to give the expert opinion for Node 1.1.1
        messagebox.showinfo("AI Opinion (Output 1.3.0)", "เปิดเผย เนื่องจากเป็นข้อมูลที่โอนไป"
                                                         "ต่างประเทศ")
# Set the output for each choice in Question 1.1 (Is there laws?)
def Query1_1():
    # If the answer is Option 1.1.1 (Yes, there is the laws)
    if question1_1.get() == Option1_1_1:
        # Show text on the program screen: Done!
        Output1_1_1Label = Label(root, text="Done!")
        Output1_1_1Label.pack()
        # then, show Output 1.1.1 as text in the message box.
        # Show the message box to give the expert opinion for Node 1.1.1
        messagebox.showinfo("AI Opinion (Output 1.1.1)", "ปฏิเสธ และบันทึก เนื่องจากมีกฎหมายหรือคำสั่งศาล"
                                          "และการเปิดเผยจะกระทบสิทธิเสรีภาพของบุคคลอื่น")
    else:
        # If the answer is Option 1.1.2 (No, there is no laws)
        # Show text on the program screen: Done!
        Output1_1_2Label = Label(root, text="Done!")
        Output1_1_2Label.pack()
        # Show the message box to give the expert opinion for Node 1.1.1
        messagebox.showinfo("AI Opinion (Output 1.1.2)", "เปิดเผย เนื่องจากไม่มีกฎหมายหรือคำสั่งศาล"
                                          "และการเปิดเผยจะกระทบสิทธิเสรีภาพของบุคคลอื่น")

# Set the output for each choice in Question 1.2 (Machine-readable?)
def Query1_2():
    # If the answer is Option 1.2.1 (Yes, authority)
    if question1_2.get() == Option1_2_1:
        # Show text on the program screen: Done!
        Output1_2_1Label = Label(root, text="Done!")
        Output1_2_1Label.pack()
        # then, show Output 1.2.1 as text in the message box.
        # Show the message box to give the expert opinion
        messagebox.showinfo("AI Opinion (Output 1.2.1)", "ปฏิเสธ และบันทึก เนื่องจากเป็นการปฏิบัติหน้าที่")
    # If the answer is Option 1.2.2 (Yes, Not authority)
    # Show text on the program screen: Done!
    else:
        Output1_2_2Label = Label(root, text="Done!")
        Output1_2_2Label.pack()
        # then, show Output 1.2.2 as text in the message box.
        # Show the message box to give the expert opinion
        messagebox.showinfo("AI Opinion (Output 1.2.2)", "เปิดเผย เนื่องจากไม่ใช่การปฏิบัติหน้าที่")


# Create Dropdown menu for the first question
drop0 = OptionMenu(root, question0, *choices0)
drop0.pack()

# Create button, it will change label text
button = Button(root, text="ยืนยัน", command=Query).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()

# Design the message box to show after the user reaches Node 1.1.1
node1_1_1InfoBox = Tk()
node1_1_1InfoBox.geometry("300x200")
node1_1_1InfoBox.mainloop()
