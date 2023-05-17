import tkinter as tk
import nltk
from nltk.parse.corenlp import CoreNLPDependencyParser
from nltk.tree import Tree
from tkinter import scrolledtext


def process_sentence(sentence):
    output_str = ""

    def print_step(stack, action):
        nonlocal output_str
        output_str += "Stack: " + str(stack) + "\n"
        if action:
            output_str += "Action: " + action + "\n"
        output_str += "\n"

    l=[]
    tagged_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))

    parser = CoreNLPDependencyParser()

    parse = next(parser.raw_parse(sentence))
    dg = parse.to_conll(10)

     
    parse_tree, = parser.raw_parse(sentence)

    parse_tree_text.delete("1.0", tk.END)

    parse_tree_text.insert(tk.END, parse_tree.to_conll(4))

    
    deps_text.delete("1.0", tk.END)
    for triple in parse_tree.triples():
        deps_text.insert(tk.END, str(triple) + "\n")

    class parts():
        def __init__(self,index,word,head_index,dep):
            self.word=word
            self.index=index
            self.head_index=head_index
            self.dep=dep
        def is_head(self,temp):
            if self.head_index==temp.index:
                return -1
            elif self.index==temp.head_index:
                return 1
            else :
                return 0


    buffer=[]
    dg=list(dg.strip().split("\n"))
    for i in dg:
        t=list(i.strip().split("\t"))

        buffer.append(parts(int(t[0]),t[1],int(t[6]),t[7]))


    stack=[]
    for i in buffer:
        if i.head_index==0:
            stack.append("root")
    k1=[]     
    def funct(stack,buffer):
        nonlocal output_str
        output_str += "[ "
        output_str += "root , "
        for i in stack[1:]:
            output_str += i.word + " , "
        output_str += "] \t"

        output_str += "[ "
        for i in buffer:
            output_str += i.word + " , "
        output_str += "] \t"
    funct(stack,buffer)
    output_str += "init\n"
    while(len(buffer)!=0):
        t=buffer.pop(0)
        m=0
        i=len(stack)-1
        stack.append(t)
        output_str += "\n"
        funct(stack,buffer)
        output_str += "shift\n"
        m=0
        while i<len(stack) and i>=1:
        
            if stack[i].head_index==t.index:
                k=stack.pop(i)
                funct(stack,buffer)
                output_str += "left arc "
                output_str += f"{k.word} <-- {t.word}\t"
                output_str += "\n"
            elif stack[i].index==t.head_index and m==0:
                m=1
                stack.pop()
                funct(stack,buffer)
                output_str += "\n"
                if stack[i].index < t.index:
                    output_str += "right arc "
                    output_str += f"{stack[i].word} --> {t.word} "

                else:
                    output_str += "left arc "
                    output_str += f"{t.word} <-- {stack[i].word}  "
            i-=1 
    t=stack.pop()
    output_str += "\n"
    funct(stack=stack,buffer=buffer)
    output_str += "right arc "
    output_str += f"root --> {t.word} "
    output_str += "\n"
    
    return output_str



root = tk.Tk()
root.title("Dependency Parser")



input_frame = tk.Frame(root)
input_frame.pack()

input_label = tk.Label(input_frame, text="Enter a sentence:")
input_label.pack()

input_entry = tk.Entry(input_frame, width=50)
input_entry.pack()



def process_button():
    sentence = input_entry.get()
    output = process_sentence(sentence)
    output_text.delete("1.0", tk.END)
    output_text.insert("end", output)
    
process_button = tk.Button(root, text="Parse", command=process_button)
process_button.pack()



parse_tree_label = tk.Label(root, text="Parse Tree:")
parse_tree_label.pack()

parse_tree_text = scrolledtext.ScrolledText(root, width=80, height=10)
parse_tree_text.pack()


deps_label = tk.Label(root, text="Dependency Triples:")
deps_label.pack()

deps_text = scrolledtext.ScrolledText(root, width=80, height=10)
deps_text.pack()


output_frame = tk.Frame(root)
output_frame.pack()

output_label = tk.Label(root, text="Steps To Generate Parser Output:")
output_label.pack()

output_text = scrolledtext.ScrolledText(root, height=20,width=100)
output_text.pack()

root.mainloop()
