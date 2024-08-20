class Notebook:
    def __init__(self, pages, size='a4', spacing='college'):
        self.pages = pages
        self.size = size
        self.spacing = spacing

journal = Notebook(80, size='letter', spacing='wide')

print(journal.pages)  
print(journal.size)    
print(journal.spacing) 
