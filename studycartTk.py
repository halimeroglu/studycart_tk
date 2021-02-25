import random
from tkinter import  *

root = Tk()
root.geometry('450x350')
root.title('Study Cart')
root.config(bg="#dfe6e9")

#lists
maths_list = [["Prime Number : A number that is divisible only by itself and 1. Examples : 2,3,5,7,11,13 "],
              ["Odd number : When divided by 2 , leave a remainder of 1. Examples : 1,3,5,7,9,11"],
              ["Even number : Number that can be exactly divided by 2. Examples : 2,4,6,8,10."],
              ["Exponentaion : Involving two numbers, the base b and power n. Examples : 2^3= 8 "],
              ["Negative Numbers : Numbers are less than zero. Examples : -1,-2,-3,-4,-5."]]
physics_list = [["Force : force is any interaction that,when unopposed,will change the motion of an object."],
              ["Energy : The capacity for doing work.It may exist in potential,kinetic and thermal etc."],
              ["Speed of light : speed at which light waves propagate through different materials. 300 metres per second (Britannica)"],
              ["Kinetic energy is a form of energy that an object or a particle has by reason of its motion. (Britannica) "],
              ["Nuclear energy is the energy in the nucleus, or core, of an atom.(nationalgeographic)"]]
chemistry_list = [["An element is a pure substance consisting only of atoms that all have the same numbers of protons in their atomic nuclei. (wikipedia) "],
              ["Mole, a standard scientific unit for measuring large quantities of very small entities such as atoms, molecules, or other specified particles.(Britannica)"],
              ["Hybridization is the idea that atomic orbitals fuse to form newly hybridized orbitals, which in turn, influences molecular geometry and bonding properties.(LibreText)"],
              ["A molecule is an electrically neutral group of two or more atoms held together by chemical bonds. (Wikipedia)"],
              ["Organic chemistry is a branch of chemistry that studies the structure, properties and reactions of organic compounds, which contain carbon in covalent bonding. (Wikipedia) "]]
biology_list = [["The cell is the basic structural, functional, and biological unit of all known organisms. (Wikipedia)"],
              ["Algae are a diverse group of aquatic organisms that have the ability to conduct photosynthesis.(LiveScience)"],
              ["Adenosine 5'-triphosphate, or ATP, is the principal molecule for storing and transferring energy in cells (nature)"],
              ["A ribosome is a complex cellular mechanism used to translate genetic code into chains of amino acids. (biology dictionary)"],
              ["Proteins are large biomolecules, or macromolecules, consisting of one or more long chains of amino acid residues.(wikipedia)"]]
history_list = [["The Baroque was a period in art history that started at the beginning of the 17th-century and continued to evolve until the 18th-century. (study) "],
              ["The Renaissance was a fervent period of European cultural, artistic, political and economic “rebirth” following the Middle Ages.(history)"],
              ["The story of English literature begins with the Germanic tradition of the Anglo-Saxon settlers.(history world)"],
              ["The 17th century. This history of American literature begins with the arrival of English-speaking Europeans in what would become the United States. (britannica)"],
              ["Feminist art production began in the late 1960s, during the second-wave of feminism in the United States and England (the art story)"]]
geometry_list = [["A triangle is a closed, two-dimensional shape with three straight sides. (splash learn) "],
              ["A line can be defined as a straight one- dimensional figure that has no thickness and extends endlessly in both directions. (splash learn)"],
              ["A ray can be defined as a part of a line that has a fixed starting point but no end point.(splash learn)"],
              ["A line segment is a part of a line that is bounded by two distinct end points, and contains every point on the line between its endpoints (wikipedia)"],
              ["Midpoint :  A point on a line segment that divides it into two equal parts.(mathopenref)"]]

#functions
def make_new_page():
    new_page = Toplevel(root)
    new_page.geometry('850x150')
    new_label = Label(new_page,text=text).place(x=20,y=20)
    
def get_maths():
    global text
    text = random.choice(maths_list)
    make_new_page()

def get_physics():
    global text
    text = random.choice(physics_list)
    make_new_page()

def get_chemistry():
    global text
    text = random.choice(chemistry_list)
    make_new_page()

def get_biology():
    global text
    text = random.choice(biology_list)
    make_new_page()

def get_history():
    global text
    text = random.choice(history_list)
    make_new_page()

def get_geometry():
    global text
    text = random.choice(geometry_list)
    make_new_page()

#widgets
title_label = Label(root,text="Study Cart",bg="#dfe6e9",fg="#00cec9",font=('Arial',28)).place(x=125,y=30)
maths_button = Button(root,text="Maths",bg="#00b894",fg="#333333",font=('Arial',11),width=10,command=get_maths).place(x=50,y=120)
physics_button = Button(root,text="Physics",bg="#0984e3",fg="#333333",font=('Arial',11),width=10,command=get_physics).place(x=175,y=120)
chemistry_button = Button(root,text="Chemistry",bg="#6c5ce7",fg="#333333",font=('Arial',11),width=10,command=get_chemistry).place(x=300,y=120)
biology_button = Button(root,text="Biology",bg="#e17055",fg="#333333",font=('Arial',11),width=10,command=get_biology).place(x=50,y=180)
history_button = Button(root,text="History",bg="#d63031",fg="#333333",font=('Arial',11),width=10,command=get_history).place(x=175,y=180)
geometry_button = Button(root,text="Geometry",bg="#e84393",fg="#333333",font=('Arial',11),width=10,command=get_geometry).place(x=300,y=180)


root.mainloop()