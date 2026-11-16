class TextEditor:
    """Gerenciador de Texto com de Sistema Undo/Redo (Pilhas)"""
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def save_state(self):
        self.undo_stack.append(self.text)
        self.redo_stack.clear()
    
    def write(self, new_text: str):
        self.save_state()
        self.text += new_text
        print(f"\n[Ação] Texto adicionado. Estado atual: '{self.text}' ")
    
    def undo(self):
        if not self.undo_stack:
            print("\n[Aviso] Nada para desfazer (Undo Stack vazia)")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print(f"\n[Undo] Ação desfeita. Estado atual: '{self.text}' ")
    
    def redo(self):
        if not self.redo_stack:
            print("\n[Aviso] Nada para refazer (Redo Stack vazia)")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print(f"\n[Redo] Ação refeita. Estado atual: '{self.text}'")
    
    def show(self):
        print(f"\n============== TEXTO ATUAL ==============\n{self.text if self.text else "<vazio>"}\n")

if __name__ == "__main__":
    editor = TextEditor()
    editor.write("Olá, ")
    editor.write("mundo!")
    editor.show()
    
    editor.undo()
    editor.show()
    
    editor.redo()
    editor.show()