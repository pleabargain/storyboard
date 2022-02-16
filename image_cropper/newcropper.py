#image_cropper_horst.py
# 2022 by Horst JENS, https://spielend-programmieren.at horstjens@gmail.com

import PySimpleGUI as sg
from PIL import Image
import pathlib
import os
import requests
from io import BytesIO


# desscription crop images

#source_path = "/home/dgd/Desktop/image_cropper/"
source_path = pathlib.Path.cwd() # get current work directory
#destination_path = "/home/dgd/Desktop/image_cropper/"
destination_path = pathlib.Path.cwd()


def motion():
    """
    return mouse cursor in the application

    """
    return f'X, Y = {window.user_bind_event.x, window.user_bind_event.y}'

# im = Image.open(source)
# # (left, upper, right, lower)
# im = im.crop( (1, 40, 190, 230) ) # 
# im.save(final + '1card.png') # saves the image

def update_spinners():
    if x1 is None:
        window["click_coordinates_x1"].update(0)
        window["click_coordinates_y1"].update(0)
        window["click_coordinates_x1"].update(disabled=True)
        window["click_coordinates_y1"].update(disabled=True)
    else:
        window["click_coordinates_x1"].update(disabled=False)
        window["click_coordinates_y1"].update(disabled=False)
    if x2 is None:
        window["click_coordinates_x2"].update(0)
        window["click_coordinates_y2"].update(0)
        window["click_coordinates_x2"].update(disabled=True)
        window["click_coordinates_y2"].update(disabled=True)
    else:
        window["click_coordinates_x2"].update(disabled=False)
        window["click_coordinates_y2"].update(disabled=False)
    if x3 is None:
        window["click_coordinates_x3"].update(0)
        window["click_coordinates_y3"].update(0)
        window["click_coordinates_x3"].update(disabled=True)
        window["click_coordinates_y3"].update(disabled=True)
    else:
        window["click_coordinates_x3"].update(disabled=False)
        window["click_coordinates_y3"].update(disabled=False)
    


def create_rectangles():
    # delete old rectangles
    for i in rectangle_numbers:
          window["canvas1"].delete_figure(i)
    try:
        rows = int(values["number_of_rows"])
        cols = int(values["number_of_columns"])
    except ValueError:
        sg.PopupError("please make sure integer values > 0 are written into the rows and columns fields")
        return
    # make outer red rectangles
    width = x2-x1
    height = y2-y1
    for r in range(rows):
        for c in range(cols):
            rectangle_numbers.append(
                window["canvas1"].draw_rectangle(
                    top_left=(x1 + width * c ,y1 + height * r ),
                    #bottom_right=(x2,y2), line_color="red" ))
                    bottom_right=(x1+ width * c + width, y1 + height * r + height),
                    line_color="red",
                    line_width=2))


    # make also inner green rectangles ?
    if x3 is not None:
        #if (x3 > x2) or (y3 > y2):
        if (x3 > x2) or (y3 > y2) or (x3 <x1) or (y3 < y1):
            pass
        else:
            green_w = x2-x3
            green_h = y2-y3
            for r in range(rows):
                for c in range(cols):
                    rectangle_numbers.append(
                        window["canvas1"].draw_rectangle(
                            top_left=(x1 + width * c ,y1 + height * r ),
                            #bottom_right=(x2,y2), line_color="red" ))
                            bottom_right=(x1+ width * c + width - green_w, 
                                          y1 + height * r + height - green_h),
                            line_color="green"))


    #    rectangle_numbers.append(window["canvas1"].draw_rectangle(top_left=(x1,y1),bottom_right=(x3,y3), line_color="green" ))


# [sg.Button("start conversion"),    ],

helptext = """
Is the image too large to see all of it?
-> Pan the window by holding down the left ALT key
and drag with mouse (holding down left mouse button

Click three times on the image to create sub-rects
Click a fourth time to delete the rectangles
"""


filenames_column = sg.Column(layout=[
    [ sg.Text("choose filename:"),
    sg.Button("sort by date"), 
    sg.Button("sort by name"),
    sg.Button("delete file", button_color="black")],
    [sg.Listbox(values=[],
        key="source_files",
        size=(60,10), 
        horizontal_scroll=True,
        auto_size_text=True,
        enable_events = True, 
        select_mode = sg.LISTBOX_SELECT_MODE_SINGLE),],

])

resultnames_column = sg.Column(layout=[ 
    [sg.Text("sub-image-filenames:")],
    [sg.Text("rows & columns"), 
    sg.Combo(["2x2","2x3","2x4","3x2","3x3","3x4","4x3","other"], 
                key="rowcol", 
                default_value="4x3", 
                enable_events=True,
                )],
    [sg.Text("rows: "), sg.Input("4",key="number_of_rows", size=(5,1)),
        sg.Text("cols: "), sg.Input("3",key="number_of_columns", size=(5,1))],
    [sg.Text("prefix:"), sg.Input("prefix_",size=(20,1), key="prefix" )],
    [sg.Text("suffix:"), sg.Input("_suffix",size=(20,1), key="suffix" )],
    #[sg.Text("filenames without prefix, without suffix.")],
    #[sg.Text("extension will be .png")],
    [sg.Multiline("image_name1\nimage_name2\nimage_name3\nimage_name4\nimage_name5\nimage_name6\nimage_name7\nimage_name8\nimage_name9\nimage_name10\nimage_name11\nimage_name12\n",
        key="image_names",
        size=(20,5)
        ),],
])

mouse_column = sg.Column(layout=[
    [sg.Text("mouse now:"), sg.Text("??", key="mouse_now", size=(20,1)), ],
    # sg.Text("Canvas Topleft X:"), sg.Input("10", key="canvas_x", size=(5,1), enable_events=True),
    # sg.Text(" Y: "), sg.Input("206", key="canvas_y", size=(5,1), enable_events=True) ],
    [sg.Text("last click: "), sg.Text("?,?",key="click_coordinates0"),  sg.Text("click #: 0", key="click_counter"),
     sg.Text(helptext,
             text_color="yellow")],
    [sg.Text("1: topleft of r1, c1: ", key="c1", background_color="green"),
     #sg.Text("?,?",key="click_coordinates1"),],
     sg.Spin(list(range(1200)), key="click_coordinates_x1",enable_events=True),
     sg.Spin(list(range(1200)), key="click_coordinates_y1",enable_events=True),],
    [sg.Text("2: topleft of r2, c2: ", key="c2"),
     # [sg.Text("(if only one row:\nbottomleft of image row1, col2)")],
     #sg.Text("?,?",key="click_coordinates2"),],
     sg.Spin(list(range(1200)), key="click_coordinates_x2",enable_events=True),
     sg.Spin(list(range(1200)), key="click_coordinates_y2",enable_events=True),],
    [sg.Text("3: bottomright r1, c1: ", key="c3"),
     #sg.Text("?,?",key="click_coordinates3")],
     sg.Spin(list(range(1200)), key="click_coordinates_x3",enable_events=True),
     sg.Spin(list(range(1200)), key="click_coordinates_y3",enable_events=True),],
    [sg.Button("start conversion"),    ],
])

layout = [
        [sg.Button("no file"), sg.Button("choose source folder"), sg.Text("",key="sourcefolder"),
         sg.Input("enter url of image here", size=(55,1), key="image_url", enable_events=False),
         sg.Button("load image from url"),
        ],
        # TODO
        # catch this error:
        # Traceback (most recent call last):
        #   File "/home/dgd/Desktop/image_cropper/test_folder/newcropper.py", line 285, in <module>
        #     new = Image.open(BytesIO(response.content))
        #   File "/home/dgd/.local/lib/python3.9/site-packages/PIL/Image.py", line 3008, in open
        #     raise UnidentifiedImageError(
        # PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x7f36b609dd10>



        [filenames_column, 
         resultnames_column,
         mouse_column,
        ],
        [sg.Graph(canvas_size=(1200,1200),
                 pad=0,
                graph_bottom_left=(0,1200),
                graph_top_right=(1200,0),
                key = "canvas1",
                enable_events=True,
                #motion_events=True,
                background_color= "purple",
                           )
                ],
      
        ]

window = sg.Window("image cropper",
                    layout = layout,
                    #size = (1200,900),
                    return_keyboard_events=True,
                    )

window.finalize()

window.bind('<Motion>', 'motion')

sourcefiles = []
sourcefolder = source_path
window["sourcefolder"].update(sourcefolder)
p = pathlib.Path(sourcefolder)
sourcefiles = [file for file in p.glob("*.*") if pathlib.Path(file).suffix.lower() in (".jpg", ".jpeg", ".gif", ".png", ".tiff")]
#print(sourcefiles)
window["source_files"].update(values=[pathlib.Path(file).parts[-1] for file in sourcefiles ])

#event, values = window.read()

x,y = None, None
x1,y1 = None, None
x2,y2 = None, None
x3,y3 = None, None
click_counter = 0
canvas_x, canvas_y = 10, 206 # topleft of canvas 

original = None

filename= None
rectangle_numbers = []

while True:
    event,values = window.read()
    #print("event:", event)
    
    # if event == 'motion':
    #     print(motion())

    if event == sg.WINDOW_CLOSED:
        break

    if event == "canvas_x":
        canvas_x = int(values["canvas_x"])
    if event == "canvas_y":
        canvas_y = int(values["canvas_y"])

    if event == "motion":
        #print(motion())
        window["mouse_now"].update(motion())


    if event == "choose source folder":
        sourcefolder = sg.PopupGetFolder("choose source folder",
                                    default_path = source_path,)
        if sourcefolder is None:
            continue
        p = pathlib.Path(sourcefolder)
        sourcefiles = [file for file in p.glob("*.*") if pathlib.Path(file).suffix.lower() in (".jpg", ".jpeg", ".gif", ".png", ".tiff")]
        #print(sourcefiles)
        window["source_files"].update(values=[pathlib.Path(file).parts[-1] for file in sourcefiles ])

    if event == "source_files":
        name = values["source_files"][0] # only one can be selected
        #print(name)
        filename = pathlib.Path(os.path.join(sourcefolder, name) )
        if filename.suffix.lower() != ".png":
            print("i must convert first into png")
            im = Image.open(filename)
            im.save(filename.stem+".png")
            filename = os.path.join(sourcefolder, filename.stem+".png")
        literal_filename = str(filename) 
        if original is not None:
            # delete old image first 
            window["canvas1"].delete_figure(original)
        original = window["canvas1"].draw_image(filename=literal_filename, location = (0,0))

    if event == "load image from url":
        # open image from url. save it first as "temp.png"
        if not values["image_url"].startswith("http"):
            sg.PopupError("image url must start with http....")
            continue
        name=sg.PopupGetText("please enter local filename (without .png) for image from internet")
        if name is None:
            continue
        response = requests.get(values["image_url"])
        new = Image.open(BytesIO(response.content))
        filename = pathlib.Path(os.path.join(sourcefolder, name +".png") )
        new.save(str(filename))
        if original is not None:
            # delete old image first 
            window["canvas1"].delete_figure(original)
        original = window["canvas1"].draw_image(filename=filename, location = (0,0))
        # update filenames
        p = pathlib.Path(sourcefolder)
        sourcefiles = [file for file in p.glob("*.*") if pathlib.Path(file).suffix.lower() in (".jpg", ".jpeg", ".gif", ".png", ".tiff")]
        window["source_files"].update(values=[pathlib.Path(file).parts[-1] for file in sourcefiles ])

    if event == "no file":
        # deselect all selected files
        window["source_files"].update(set_to_index = []) # select none
        if original is not None:
            window["canvas1"].delete_figure(original)

    if event == "delete file":
        name = values["source_files"][0] # only one can be selected
        filename = pathlib.Path(os.path.join(sourcefolder, name) )
        if filename.suffix == ".py":
            sg.PopupError("please don't delete python files with this app")
            continue
        filename.unlink()
        # reload files
        p = pathlib.Path(sourcefolder)
        sourcefiles = [file for file in p.glob("*.*") if pathlib.Path(file).suffix.lower() in (".jpg", ".jpeg", ".gif", ".png", ".tiff")]
        window["source_files"].update(values=[pathlib.Path(file).parts[-1] for file in sourcefiles ])
        if original is not None:
            window["canvas1"].delete_figure(original)


    if event == "sort by name":
        window["source_files"].update(set_to_index = []) # select none
        names = [pathlib.Path(file).parts[-1] for file in sourcefiles ]
        names.sort()
        window["source_files"].update(values=names)

    if event == "sort by date":
        sorted_paths = sorted(pathlib.Path(source_path).iterdir(), key=os.path.getmtime, reverse=True)
        names = [pathlib.Path(file).parts[-1] for file in sorted_paths]
        window["source_files"].update(values=names)

    # get clicks coordinates
    if event == "canvas1":
        print("clicked at:", values['canvas1'])
        window["click_coordinates0"].update(values['canvas1'])
        x,y = values['canvas1']
        click_counter += 1
        if click_counter > 3:
            click_counter = 0
        if click_counter == 0:
            x1,y1,x2,y2,x3,y3 = None, None, None, None, None, None
            update_spinners()
            window["c1"].update(background_color = "green")
            window["c2"].update(background_color = "grey")
            window["c3"].update(background_color = "grey")
            # delete all old rectangles
            for i in rectangle_numbers:
                window["canvas1"].delete_figure(i)
        elif click_counter == 1:
            x1,y1 = x, y
            x2,y2,x3,y3 = None, None, None, None
            update_spinners()
            window["c1"].update(background_color = "grey")
            window["c2"].update(background_color = "green")
            window["c3"].update(background_color = "grey")
        elif click_counter == 2:
            x2, y2 = x, y
            x3,y3 = None, None
            update_spinners()
            window["c1"].update(background_color = "grey")
            window["c2"].update(background_color = "grey")
            window["c3"].update(background_color = "green")
            # create red (outer) rectangle(s)
               # draw_rectangle(top_left,
               # bottom_right,
               # fill_color = None,
               # line_color = None,
               # line_width = None)
            create_rectangles()
            #rectangle_numbers.append(window["canvas1"].draw_rectangle(top_left=(x1,y1),bottom_right=(x2,y2), line_color="red" ))
        elif click_counter == 3:
            x3, y3 = x, y    
            update_spinners() # important! need to be done to enable x3,y3 spinners
            window["c1"].update(background_color = "grey")
            window["c2"].update(background_color = "grey")
            window["c3"].update(background_color = "grey")
            # create green inner rectangle(s)
            create_rectangles()
            #rectangle_numbers.append(window["canvas1"].draw_rectangle(top_left=(x1,y1),bottom_right=(x3,y3), line_color="green" ))
            

        window["click_counter"].update(f"click #: {click_counter}")
        #window["click_coordinates1"].update(f"{x1},{y1}")
        window["click_coordinates_x1"].update(value= x1)
        window["click_coordinates_y1"].update(value= y1)
        window["click_coordinates_x2"].update(value= x2)
        window["click_coordinates_y2"].update(value= y2)
        window["click_coordinates_x3"].update(value= x3)
        window["click_coordinates_y3"].update(value= y3)
        #window["click_coordinates2"].update(f"{x2},{y2}")
        #window["click_coordinates3"].update(f"{x3},{y3}")

    if event == "rowcol":
        v = values["rowcol"]
        if v == "other":
            continue
        if v.count("x") != 1:
            continue
        r = v.split("x")[0]
        c = v.split("x")[1]
        window["number_of_rows"].update(r)
        window["number_of_columns"].update(c)
        
    if "click_coordinates_" in event:
        # a spinner was changed
        if x1 is not None:
            x1 = int(window["click_coordinates_x1"].get())
            y1 = int(window["click_coordinates_y1"].get())
        if x2 is not None:
            x2 = int(window["click_coordinates_x2"].get())
            y2 = int(window["click_coordinates_y2"].get())
        if x3 is not None:
            x3 = int(window["click_coordinates_x3"].get())
            y3 = int(window["click_coordinates_y3"].get())
        print(x1,x2,x2,y2,x3,y3)
        create_rectangles()

   
    # if event == "get top left":
    #     x1,y1 = x,y
    #     window["click_coordinates1"].update(f"{x1},{y1}"   )
        
    # if event == "get bottom right":
    #     x2,y2 = x,y
    #     window["click_coordinates2"].update(f"{x2},{y2}"   )

    # if event == "crop and reload":
    #     im = Image.open(filename)
    #     # # (left, upper, right, lower)
    #     im = im.crop( (x1, y1, x2,y2) ) # 
    #     im.save(source_path + 'cropped.png') # saves the image
    #     window["canvas1"].delete_figure(original)
    #     original = window["canvas1"].draw_image(filename=source_path + 'cropped.png', location = (0,0))


    if event == "start conversion":
        if x2 is None:
            continue
        if filename is None:
            continue
        cols = int(values["number_of_columns"])
        rows = int(values["number_of_rows"])
        filenames = values["image_names"].splitlines()
        if len(filenames) != rows * cols:
            sg.PopupError(f"please enter {rows*cols} lines into filenames")
            continue
        im = Image.open(filename)

        number = 0

        width = x2-x1
        height = y2-y1
        green_w = 0
        green_h = 0
        if x3 is not None:
            if (x3 > x2) or (y3 > y2):
                green_w, green_h = 0, 0
            else:              
                green_w = x3 - x2
                green_h = y3 - y2
        
        #for r in range(rows+1):
        #    for c in range(cols+1):
        for r in range(rows):
            for c in range(cols):
                #rectangle_numbers.append(
                #window["canvas1"].draw_rectangle(
                #    top_left=(x1 + width * c ,y1 + height * r ),
                #    #bottom_right=(x2,y2), line_color="red" ))
                #    bottom_right=(x1+ width * c + width, y1 + height * r + height),
                new = im.crop(
                                (x1+width * c, 
                                 y1+height * r,
                                 x1+width * c + width - green_w, 
                                 y1 + height * r + height - green_h)
                             ) 
                new.save(str(destination_path.joinpath(values["prefix"]+ filenames[number]+ values["suffix"] + ".png"))) # saves the image
                print("done", number)

                number+=1
        # update source files
        p = pathlib.Path(sourcefolder)
        sourcefiles = [file for file in p.glob("*.*") if pathlib.Path(file).suffix.lower() in (".jpg", ".jpeg", ".gif", ".png", ".tiff")]
        #print(sourcefiles)
        window["source_files"].update(values=[pathlib.Path(file).parts[-1] for file in sourcefiles ])




window.close()


