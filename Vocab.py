from Tkinter import *
import random
from sys import exit

class askWords:


    def __init__(self, master):
        self.master = master

        self.vocab = {}
        
        self.question_text = StringVar()
        self.reward_text = StringVar()
        self.streak = 0
        self.tries = 1
        
        # Populates the dictionary with words from a text file
        with open('vocabulary.txt') as in_file:
            for line in in_file:
               self.eng_word, self.fre_word = line.split(':', 1)
               self.vocab[self.eng_word] = self.fre_word.rstrip('\n')
        
        self.english = random.choice(self.vocab.keys())
        self.french = self.vocab[self.english]
         
        self.frame = Frame(self.master, width=455, height=150)
        self.frame.pack()

        self.question_text.set(''.join(("What is the french for ", self.english, " ?")))
        
        self.question = Label(self.master, textvariable=self.question_text)
        self.question.pack()
        self.question.place(y=10)
        
        self.entry = Entry(self.master, width=60)
        self.entry.pack()
        self.entry.place(x=5, y=50)
        
        self.go_button = Button(self.master, text="Go!", width=8, command=self.go)
        self.go_button.pack()
        self.go_button.place(y=47, x=380)
        
        self.reward = Message(self.master, textvariable=self.reward_text, width=200)
        self.reward.pack()
        self.reward.place(y=80, x=5)
        
        self.change_button = Button(self.master, text="Add words", width=8, command=self.add_words)
        self.change_button.pack()
        self.change_button.place(y=119, x=380)
        
    def go(self):
        self.ans = self.entry.get()
        if self.ans != self.french and self.tries < 2:
            self.reward_text.set(''.join(("Sorry, that's wrong. The first letter of the word is '", self.french[0], "'. Try again!")))
            self.tries += 1
        elif self.ans != self.french and  self.tries < 3:
            self.tries += 1
            self.reward_text.set(''.join(("Sorry, wrong again! The first two letters of the word are '", self.french[0], "' and '" + self.french[1] + "'. Last try!")))
        elif self.ans == self.french:
            if self.streak < 2:
                self.reward_text.set(''.join(("You got it! And it only took you ", str(self.tries), " tries!")))
            else:
                self.reward_text.set(''.join(("You got it! And it only took you ", str(self.tries), " tries! \nYou're on a ", str(self.streak), " word streak!")))
            self.english = random.choice(self.vocab.keys())
            self.french = self.vocab[self.english]

            self.question_text.set(''.join(("What is the french for ", self.english, " ?")))
            self.tries = 1
            self.streak += 1
        elif self.tries == 3:
            self.reward_text.set(''.join(("You guessed wrong too many times. The word was '", self.french, "'.")))
            self.english = random.choice(self.vocab.keys())
            self.french = self.vocab[self.english]

            self.question_text.set(''.join(("What is the french for ", self.english, " ?")))
            self.tries = 1
            self.streak = 0

        self.entry.delete(0, END)

    def update(self):
        self.e = self.eng_entry.get()
        self.f = self.fre_entry.get()
        with open('vocabulary.txt', 'a') as self.vocab_file:
            self.vocab_file.write(''.join((self.e, ":", self.f, "\n")))

    def add_words(self):
        self.top = Toplevel(width = 450, height = 110)
        self.top.title("Update")

        self.add_button = Button(self.top, text="Add", command=self.update, width=8)
        self.add_button.pack()
        self.add_button.place(x=49, y=80)

        self.quit_button = Button(self.top, text="Quit", command=self.exit_prog)
        self.quit_button.pack()
        self.quit_button.place(x=5, y=80)

        self.eng_label = Label(self.top, text="English: ")
        self.eng_label.pack()
        self.eng_label.place(x=5, y=8)

        self.fre_label = Label(self.top, text="French: ")
        self.fre_label.pack()
        self.fre_label.place(x=5, y=50)

        self.eng_entry = Entry(self.top, width=60)
        self.eng_entry.pack()
        self.eng_entry.place(x=60, y=10)

        self.fre_entry = Entry(self.top, width=60)
        self.fre_entry.pack()
        self.fre_entry.place(x=60, y=48)

    def exit_prog(self):
        self.top.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Vocabulary')
    app = askWords(root)
    root.mainloop()
