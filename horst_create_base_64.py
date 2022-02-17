#<img src="data:image/{};base64,{}" width="350">

import base64

# my_string = base64.b64encode(img_file.read())
# image_string = my_string.decode("utf-8")
#imgage name:  "test1.png"
with open("test1.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
image_string = my_string.decode("utf-8")


##<img src="data:image/svg+xml;base64,""" + image_string + '"
##<img src="data:image/png;base64,""" + image_string + '"><br>'
# generate html

html = """
<html>
<head>
<title>
test site
</title>
</head>
<body>
<h1>test with image</h1>
here comes the image:<br>
<img src="data:image/png;base64,{}">
</body>
</html>
""".format(image_string)

with open("test.html", "w") as myfile:
    myfile.write(html)
print("done")