from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, INSERT, Label, TOP, filedialog, StringVar, OptionMenu
from tkinter.filedialog import askopenfile 
import os
import pyrebase
import json

firebaseConfig = {
  'apiKey': "AIzaSyAsrplTbnD5bwzczctJCgUPIflJ7l29w0M",
  'authDomain': "calo-a7a97.firebaseapp.com",
  'databaseURL': "https://calo-a7a97-default-rtdb.firebaseio.com",
  'projectId': "calo-a7a97",
  'storageBucket': "calo-a7a97.appspot.com",
  'messagingSenderId': "149607042255",
  'appId': "1:149607042255:web:de2f72df03362b018c7bba",
  'measurementId': "G-75T7B8HP7Y"
}


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()

category = ["Steamed", "Fried", "Grilled", "Dessert", "Drink"]



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/mlgimran/apps/admin/build/assets/frame0")

window = Tk()

window.geometry("607x441")
window.configure(bg = "#FFFFFF")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_requests():
    requests = db.child("Requests").get()
    new_window = Toplevel(window)
    new_window.geometry("607x441")
    new_window.title("Requests")

    row_counter = 0
    for request in requests.each():
        number = str(request.key())
        value = request.val()
        if value is not None:
            result = f"{number}: {str(value)}"
            Label(new_window, text=result, font=('Times New Roman', 15, 'bold'), anchor='w', justify="left").grid(row=row_counter, column=0, sticky="w")
            remove_button = Button(new_window, text="Done", command=lambda num=number: removeRequest(num))
            remove_button.grid(row=row_counter, column=1, sticky="w")
            row_counter += 1

uploadButtonImg = PhotoImage(file=relative_to_assets("button_3.png"))
uploadRecipeFile = PhotoImage(file=relative_to_assets("button_4.png"))
uploadIngredientImg = PhotoImage(file=relative_to_assets("button_5.png"))
submitRecipeImg = PhotoImage(file=relative_to_assets("button_6.png"))
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))


global caloriesValue
global carbsValue
global detailsValue
global nameValue
global proteinValue
global imgPath
global htmlPath
global categoryValue
global ingredientPath
global totalNode
global totalNode2
global totalNode3

totalNode = len(db.child("RecipeDetail").get().val())
totalNode2 = len(db.child("Recipe").get().val())
totalNode3 = len(db.child("Recipes").get().val())


def recipeUpload():
    global step_path
    global img_path
    global ingredient_path
    new_window = Toplevel(window)
    new_window.geometry("607x441")
    new_window.title("Recipe Upload")
    canvas1 = Canvas(
        new_window,
        bg = "#FFFFFF",
        height = 441,
        width = 607,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas1.place(x = 0, y = 0)
    canvas1.create_rectangle(
    0.0,
    0.0,
    607.0,
    46.0,
    fill="#71B359",
    outline="")

    canvas1.create_text(
    0.0,
    0.0,
    anchor="nw",
    text="Recipe Upload",
    fill="#FFFFFF",
    font=("NunitoItalic ExtraBold", 36 * -1)
    )

    canvas1.create_text(
    8.0,
    139.0,
    anchor="nw",
    text="Calories",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )

    canvas1.create_text(
    8.0,
    173.0,
    anchor="nw",
    text="Carbs",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )

    canvas1.create_text(
    8.0,
    211.0,
    anchor="nw",
    text="Details",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )

    canvas1.create_text(
    8.0,
    247.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )

    canvas1.create_text(
    8.0,
    285.0,
    anchor="nw",
    text="Protein",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )

    canvas1.create_text(
    8.0,
    328.0,
    anchor="nw",
    text="Fat",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
    )


    entry_bg_1 = canvas1.create_image(
    133.5,
    149.0,
    image=entry_image_1
)
    entry_1 = Entry(
    new_window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
    entry_1.place(
    x=92.0,
    y=135.0,
    width=83.0,
    height=26.0
)

    entry_bg_2 = canvas1.create_image(
    133.5,
    185.0,
    image=entry_image_2
)
    entry_2 = Entry(
    new_window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
    entry_2.place(
    x=92.0,
    y=171.0,
    width=83.0,
    height=26.0
)

    entry_bg_3 = canvas1.create_image(
    133.5,
    221.0,
    image=entry_image_3
)
    entry_3 = Entry(
    new_window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
    entry_3.place(
    x=92.0,
    y=207.0,
    width=83.0,
    height=26.0
)

    entry_bg_4 = canvas1.create_image(
    133.5,
    257.0,
    image=entry_image_4
)
    entry_4 = Entry(
    new_window, 
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
    entry_4.place(
    x=92.0,
    y=243.0,
    width=83.0,
    height=26.0
)

    entry_bg_5 = canvas1.create_image(
    133.5,
    294.0,
    image=entry_image_5
)
    entry_5 = Entry(
    new_window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    )
    entry_5.place(
    x=92.0,
    y=280.0,
    width=83.0,
    height=26.0
    )
    entry_bg_6 = canvas1.create_image(
    133.5,
    345.0,
    image=entry_image_5
)
    entry_6 = Entry(
    new_window,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    )
    entry_6.place(
    x=92.0,
    y=331.0,
    width=83.0,
    height=26.0
    )

    #Create option menu
    valueInside = StringVar(new_window)
    valueInside.set("Select category")
    questionMenu = OptionMenu(new_window, valueInside, *category)
    questionMenu.place(x=224.0, y=58.0, width=159.0, height=54.0)
    questionMenu.configure(bg="#71B359")
    


    # uploadButton = Button(new_window, text="Upload Image", command=openIMGFile).grid(row=0, column=0, sticky="w")
    uploadButton = Button(new_window, image=uploadButtonImg,borderwidth=0,highlightthickness=0,command=openIMGFile,relief="flat")
    uploadButton.place(x=6.0,y=58.0,width=159.0,height=54.0)
    uploadRecipeFileButton = Button(new_window, image=uploadRecipeFile,borderwidth=0,highlightthickness=0,command=openHTMLFile,relief="flat")
    uploadRecipeFileButton.place(x=448.0, y=58.0, width=159.0,height=54.0)
    uploadIngredientButton = Button(new_window, image=uploadIngredientImg,borderwidth=0,highlightthickness=0,command=openJSONFile,relief="flat")
    uploadIngredientButton.place(x=448.0, y=136.0, width=159.0,height=54.0)
    # submitButton = Button(new_window, image=submitRecipeImg, borderwidth=0,highlightthickness=0,command=submitRecipe,relief="flat")
    # submitButton.place(x=224.0,y=348.0,width=159.0,height=54.0)
    
    def assignCaloriesValues():
        caloriesValue = entry_1.get()
        return caloriesValue
    def assignCarbsValue():
        carbsValue = entry_2.get()
        return carbsValue
    def assignDetailsValue():
        detailsValue = entry_3.get()
        return detailsValue
    def assignNameValue():
        nameValue = entry_4.get()
        return nameValue
    def assignProteinValue():
        proteinValue = entry_5.get()
        return proteinValue
    def assignCategoryValue():
        categoryValue = valueInside.get()
        return categoryValue
    def assignFatValue():
        fatValue = entry_6.get()
        return fatValue



    submitButton = Button(new_window, image=submitRecipeImg, borderwidth=0, highlightthickness=0, command=lambda: uploadImage(calories=assignCaloriesValues(), carbs=assignCarbsValue(),details=assignDetailsValue(),fat=assignFatValue(),category=assignCategoryValue(), name=assignNameValue(), protein=assignProteinValue(),imgPath=img_path,stepPath=step_path, ingredientPath=ingredient_path), relief="flat")

    submitButton.place(x=224.0,y=348.0,width=159.0,height=54.0)



#uploadImage(category=assignCategoryValue, name=assignNameValue, imgPath=)
def removeRequest(num):
    db.child("Requests").child(num).remove()

def addRecipe():
    imgPath = openIMGFile()
    htmlPath = openHTMLFile()
    # storage.child("Steamed/testPic").put("/home/mlgimran/apps/admin/build/assets/frame0/button_1.png")
    
def openIMGFile():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg'), ('Image Files', '*.png')])
    if img_path:
        return (img_path)


def openHTMLFile():
    global step_path 
    step_path = filedialog.askopenfilename(filetypes=[('HTML Files', '*.html')])
    if step_path:
        return (step_path)
    
def openJSONFile():
    global ingredient_path
    ingredient_path = filedialog.askopenfilename(filetypes=[('JSON Files', '*.json')])
    if ingredient_path:
        return (ingredient_path)
    
def getValue(value):
    return value

def uploadImage(calories, carbs, details, fat, category, name, protein, imgPath, stepPath, ingredientPath):
    storage.child(category + "/" + name).put(imgPath)
    storage.child(category + "/" + name + ".html").put(stepPath)
    
    img_url = storage.child(category + "/" + name).get_url(None)
    step_url = storage.child(category + "/" + name + ".html").get_url(None)
    with open(ingredient_path) as f:
        data = json.load(f)
    
    db.child("RecipeDetail").child(totalNode).set({"recipeDetailId": totalNode,"calories": calories, "carbs": carbs, "details": details, "name": name, "protein": protein, "fat": fat, "step": step_url})
    db.child("RecipeDetail").child(totalNode).child("ingredient").set(data)
    db.child("Recipe").child(totalNode2).set({"description": details, "name": name, "url": img_url})
    db.child("Recipes").child(totalNode3).set({"categoryId": totalNode3, "description": details,"imageURL": img_url, "recipeId": totalNode3, "recipeName": name, "url": step_url})
    print(img_url)
    print(step_url)


    
    

    









canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 441,
    width = 607,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    607.0,
    46.0,
    fill="#71B359",
    outline="")

canvas.create_text(
    12.0,
    10.0,
    anchor="nw",
    text="Calo Admin",
    fill="#FFFFFF",
    font=("Inter Black", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=show_requests,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=73.0,
    width=159.0,
    height=54.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=recipeUpload,
    relief="flat"
)
button_2.place(
    x=15.0,
    y=157.0,
    width=159.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
