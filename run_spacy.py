import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

emotion_sentence = "How would you describe this adjective. "

# console = Console()
# console.print(f"""Finish the sentence:\n
# Read and answer the question:\n
# [bold]{emotion_sentence}[/bold]?""")


doc = nlp(emotion_sentence)
displacy.render(doc, 
                style='dep', 
                # jupyter=True, 
                options={'distance': 100})