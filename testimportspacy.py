import spacy
from spacy import displacy
from pathlib import Path

nlp = spacy.load('en_core_web_sm') 
                # parse=True, 
                # tag=True, 
                # entity=True

sentence_nlp = nlp("John go home to your family")
svg = displacy.render(sentence_nlp, style="dep")

# output_path = Path("dependency_plot.svg") # you can keep there only "dependency_plot.svg" if you want to save it in the same folder where you run the script 
output_path = Path("dependency_plot.png") # you can keep there only "dependency_plot.svg" if you want to save it in the same folder where you run the script 

# output_path.open("w", encoding="utf-8").write(svg)

output_path.open("w", encoding="utf-8").write(png)