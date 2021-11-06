import Model
import Plotting
import json
import shutil
import tkinter as tk
from tkinter.filedialog import *
from PIL import ImageTk


class MainWindow():

    def __init__(self, master, attacker_entry="", attacked_entry=""):
        self.master = master

        # 2 High Level Components
        self.topframe = tk.Frame()
        self.topframe.pack(fill=tk.X)
        self.bottomframe = tk.Frame(self.master)
        self.bottomframe.pack(fill=tk.X)

        # Top Frame

        ## Argumentation Framework
        self.argumentationFrame = tk.LabelFrame(self.topframe,  text="Argumentation Framework")
        self.argumentationFrame.pack(side=tk.LEFT)

        ### Components
        # Loading graph image
        self.img = ImageTk.PhotoImage(file="./data/graph.jpg")
        self.img.height(), self.img.width()

        # Initializing canvas
        self.argumentationCanvas = tk.Canvas(self.argumentationFrame, scrollregion=(0, 0, self.img.width(),
                                                                                    self.img.height()))

        # Setting scrollbars
        self.hbar = tk.Scrollbar(self.argumentationFrame, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.argumentationCanvas.xview)
        self.vbar = tk.Scrollbar(self.argumentationFrame, orient=tk.VERTICAL)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vbar.config(command=self.argumentationCanvas.yview)

        # Refreshing canvas on scroll
        self.argumentationCanvas.config()
        self.argumentationCanvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # Placing graph on canvasPlacing graph on canvas
        self.image_on_canvas = self.argumentationCanvas.create_image(0, 0, image=self.img, anchor=tk.NW)
        self.argumentationCanvas.pack()

        # Update Graph Image
        Plotting.ConstructGraph()

        # Update canvas image
        self.update_canvas()


        ## Argumentation Labelling
        self.argumentationLabelling = tk.LabelFrame(self.topframe, text="Argumentation Labelling")
        self.argumentationLabelling.pack(side=tk.RIGHT)

        ### Components
        # Loading labelgraph image
        self.imglabel = ImageTk.PhotoImage(file="./data/blank.png")
        self.imglabel.height(), self.imglabel.width()

        # Initializing canvas
        self.argumentationlabelCanvas = tk.Canvas(self.argumentationLabelling,
                                                  scrollregion=(0, 0, self.imglabel.width(),
                                                                self.imglabel.height()))

        # Setting scrollbars
        self.hhbar = tk.Scrollbar(self.argumentationLabelling, orient=tk.HORIZONTAL)
        self.hhbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hhbar.config(command=self.argumentationlabelCanvas.xview)
        self.vvbar = tk.Scrollbar(self.argumentationLabelling, orient=tk.VERTICAL)
        self.vvbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vvbar.config(command=self.argumentationlabelCanvas.yview)

        # Refreshing canvas on scroll
        self.argumentationlabelCanvas.config()
        self.argumentationlabelCanvas.config(xscrollcommand=self.hhbar.set, yscrollcommand=self.vvbar.set)

        # Placing labeled graph on canvas
        self.imagelabel_on_canvas = self.argumentationlabelCanvas.create_image(0, 0, image=self.imglabel,
                                                                               anchor=tk.NW)
        self.argumentationlabelCanvas.pack()



        # BottomFrame

        ## User Action Bar
        self.attacksFrame = tk.LabelFrame(self.bottomframe, text="User Action Bar")
        self.attacksFrame.pack(side=tk.TOP)

        self.frame = tk.Frame(self.attacksFrame)
        self.frame.pack(side=tk.BOTTOM)

        self.frame1 = tk.Frame(self.frame)
        self.frame1.pack(side=tk.BOTTOM)

        ### Components
        # Setting the attacker input box
        self.attacker_label = tk.Label(self.attacksFrame, text="Attacker:")
        self.attacker_label.pack(side=tk.LEFT)
        self.attacker_entry = tk.Entry(self.attacksFrame)
        self.attacker_entry.insert(tk.END, attacker_entry)
        self.attacker_entry.pack(side=tk.LEFT)

        # Setting the attacked input box
        self.attacked_label = tk.Label(self.attacksFrame, text="Attacked:")
        self.attacked_label.pack(side=tk.LEFT)
        self.attacked_entry = tk.Entry(self.attacksFrame)
        self.attacked_entry.insert(tk.END, attacked_entry)
        self.attacked_entry.pack(side=tk.LEFT)

        # Setting the add button
        self.add_attacks_btn = tk.Button(self.attacksFrame, text="Add", width=4,
                                         command=self.add_button_click)
        self.add_attacks_btn.pack(side=tk.LEFT)

        # Setting the remove button
        self.rem_attacks_btn = tk.Button(self.attacksFrame, text="Remove", width=4,
                                         command=self.remove_button_click)
        self.rem_attacks_btn.pack(side=tk.LEFT)

        # Setting the open button
        self.open_button = tk.Button(self.frame, text="Open", width=4, command=self.open_button_click)
        self.open_button.pack(side=tk.LEFT)

        # Setting the save button
        self.save_button = tk.Button(self.frame, text="Save", width=4, command=self.save_button_click)
        self.save_button.pack(side=tk.LEFT)

        # Setting the clear button
        self.quit_button = tk.Button(self.frame, text="Clear", width=4, command=self.clear_button_click)
        self.quit_button.pack(side=tk.LEFT)

        # Setting the compute completed labelling button
        self.compute_grounded_button = tk.Button(self.frame, text="Compute Completed Labelling",
                                                 command=self.completed_button_click)
        self.compute_grounded_button.pack(side=tk.LEFT)

        # Setting the compute grounded labelling button
        self.compute_grounded_button = tk.Button(self.frame, text="Compute Grounded Labelling",
                                                 command=self.grounded_button_click)
        self.compute_grounded_button.pack(side=tk.LEFT)

        # Setting the compute preferred labelling button
        self.compute_preferred_button = tk.Button(self.frame1, text="Compute Preferred Labelling",
                                                  command=self.preferred_button_click)
        self.compute_preferred_button.pack(side=tk.LEFT)

        # Setting the compute stabled labelling button
        self.compute_preferred_button = tk.Button(self.frame1, text="Compute Stable Labelling",
                                                  command=self.stable_button_click)
        self.compute_preferred_button.pack(side=tk.LEFT)

        # Setting the compute semi-stabled labelling button
        self.compute_grounded_button = tk.Button(self.frame1, text="Compute Semi-Stable Labelling",
                                                 command=self.semistable_button_click)
        self.compute_grounded_button.pack(side=tk.LEFT)


    def add_button_click(self):

        # Update Model
        # Getting the contents of the attacker and attacked input boxes
        attacker = self.attacker_entry.get()
        attacked = set(self.attacked_entry.get().replace(" ", "").split(","))

        # Save attacker to the arguments
        if attacker != "":
            Model.arguments.add(attacker)

        # Save attacked relations, and save attacked to the arguments
        for i in attacked:
            if len(i) > 0 and attacker != "":
                Model.relations.add((attacker, i))
                if i not in Model.arguments:
                    Model.arguments.add(i)

        # Save the argumentative framework {attacker:attacked}
        framework = Model.framework.get(attacker)
        if framework != None:
            framework = set(framework)
            framework.update(attacked)
            Model.framework[attacker] = framework
        else:
            Model.framework[attacker] = attacked

        # Update Graph Image
        Plotting.ConstructGraph()

        # Update canvas image
        self.update_canvas()


    def remove_button_click(self):

        # Update Model
        # Getting the contents of the attacker and attacked input boxes
        attacker = self.attacker_entry.get()
        attacked = set(self.attacked_entry.get().replace(" ", "").split(","))

        # Update the arguments, attacked relations and argumentative framework
        framework = Model.framework.get(attacker)
        if framework != None:
            framework = set(framework)
            if framework == {""} or framework == set():
                if attacked == {""}:
                    Model.framework.pop(attacker)
                    if Model.is_attacked(attacker) == False:
                        Model.arguments.discard(attacker)
            elif framework != {}:
                for i in attacked:
                    if i in framework:
                        Model.relations.discard((attacker, i))
                        framework.discard(i)
                        Model.framework[attacker] = framework
                        if Model.is_attacker(i) == False:
                            Model.arguments.discard(i)

        # Update Graph Image
        Plotting.ConstructGraph()

        # Update canvas image
        self.update_canvas()


    def open_button_click(self):

        # Clear all content
        self.clear_button_click()

        # Select the file to open and get the file name
        openfilename = tk.StringVar()
        filepath = askopenfilename()
        openfilename.set(filepath)

        # Open and read files into the framework
        f = open(openfilename.get(), 'r')
        read = f.read()
        read = json.loads(read)
        Model.framework = read
        f.close()

        # Updating arguments and attacked relations
        for i in Model.framework:
            Model.arguments.add(i)
            if Model.framework[i] != [""]:
                for j in Model.framework[i]:
                    Model.relations.add((i, j))
                    if j not in Model.arguments:
                        Model.arguments.add(j)

        # Update Graph Image
        Plotting.ConstructGraph()

        # Update canvas image
        self.update_canvas()


    def save_button_click(self):

        # Setting the save file and save file name
        savefilename = tk.StringVar()
        filepath = asksaveasfilename()
        savefilename.set(filepath)

        # setting default, changing data types to lists
        def set_default(obj):
            if isinstance(obj, set):
                return list(obj)
            raise TypeError

        # Writing framework to the json file
        if Model.framework != {}:
            write = json.dumps(Model.framework, default=set_default)
            f = open(savefilename.get() + ".json", 'w')
            f.write(write)
            f.close()


    def clear_button_click(self):

        # Wipe the insert entry
        self.attacker_entry.delete(0, 'end')
        self.attacked_entry.delete(0, 'end')

        # Wipe all model variables
        Model.arguments = set()
        Model.framework = {}
        Model.relations = set()
        Model.argumentslabelling = {}
        Model.argumentslabel = {}

        # Wipe the graph plot
        # Update Graph Image
        Plotting.ConstructGraph()

        # Update labeled graph Image
        shutil.copy2('./data/blank.png', './data/resultlabelgraph.jpg')

        # Update canvas image
        self.update_canvas()

        # Update labeled canvas image
        self.update_labelcanvas()


    def completed_button_click(self):

        # Save the return value of the compute completed extension to label
        label = Model.compute_completed_labelling()

        # Update Coloured Graph Image
        Plotting.ConstructColouredGraph(label)

        # Update labeled canvas image
        self.update_labelcanvas()


    def grounded_button_click(self):

        # Save the return value of the compute grounded extension to label
        label = Model.compute_grounded_labelling()

        # Update Coloured Graph Image
        Plotting.ConstructColouredGraph(label)

        # Update labeled canvas image
        self.update_labelcanvas()


    def preferred_button_click(self):

        # Save the return value of the compute preferred extension to label
        label = Model.compute_preferred_labelling()

        # Update Coloured Graph Image
        Plotting.ConstructColouredGraph(label)

        # Update labeled canvas image
        self.update_labelcanvas()


    def stable_button_click(self):

        # Save the return value of the compute stabled extension to label
        label = Model.compute_stable_labelling()

        # Update Coloured Graph Image
        Plotting.ConstructColouredGraph(label)

        # Update labeled canvas image
        self.update_labelcanvas()


    def semistable_button_click(self):

        # Save the return value of the compute semistabled extension to label
        label = Model.compute_semistable_labelling()

        # Update Coloured Graph Image
        Plotting.ConstructColouredGraph(label)

        # Update labeled canvas image
        self.update_labelcanvas()


    def update_canvas(self):

        # Loading graph image
        self.img = ImageTk.PhotoImage(file="./data/graph.jpg")
        self.img.height(), self.img.width()

        # Setting the item config for the canvas
        self.argumentationCanvas.itemconfig(self.image_on_canvas, image=self.img)

        # Setting scrollbars
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.argumentationCanvas.xview)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vbar.config(command=self.argumentationCanvas.yview)

        # Refreshing canvas on scroll
        self.argumentationCanvas.config(scrollregion=(0, 0, self.img.width(), self.img.height()),
                                        xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.argumentationCanvas.pack()


    def update_labelcanvas(self):

        # Loading labeled graph image
        self.imglabel = ImageTk.PhotoImage(file="./data/resultlabelgraph.jpg")
        self.imglabel.height(), self.imglabel.width()

        # Setting the item config for the canvas
        self.argumentationlabelCanvas.itemconfig(self.imagelabel_on_canvas, image=self.imglabel)

        # Setting scrollbars
        self.hhbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hhbar.config(command=self.argumentationlabelCanvas.xview)
        self.vvbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vvbar.config(command=self.argumentationlabelCanvas.yview)

        # Refreshing  canvas on scroll
        self.argumentationlabelCanvas.config(scrollregion=(0, 0, self.imglabel.width(),
                                                           self.imglabel.height()),
                                        xscrollcommand=self.hhbar.set, yscrollcommand=self.vvbar.set)
        self.argumentationlabelCanvas.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Argument Labellings Tool")

    MainWindow(root)
    root.mainloop()