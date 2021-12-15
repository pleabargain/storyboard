description

output 
name_thumbnail.jpg (size 150x150pixel)

# goal
images should load into storybuilder at 150 x 150

# need to have 
uniform image size for storybuilder UI
do not delete original file



recursively rename with thumbnail  
recursively resize images  

# imagined process
open folder 
load first image

if jpg 
if width greater than 150 resize proportionally to 150 
if height greater than 150 resize proportionally to 150 and then rename to {image_name}_thumbnail.jpg
if width smaller than 150 resize proportionally to 150 
and fill with white




if png 
if width greater than 150 resize proportionally to 150 
if height greater than 150 resize proportionally to 150 and then rename to {image_name}_thumbnail.png
if width smaller than 150 resize proportionally to 150 
and fill with transparent


nice to have
if resize then fill empty space with white if jpg 
or transparent if png
