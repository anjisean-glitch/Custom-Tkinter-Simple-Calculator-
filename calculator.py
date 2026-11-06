import customtkinter as ctk
import ast
from CTkMessagebox import CTkMessagebox

def evaluate(node):
  ##if node has a constant, return it
  if isinstance(node, ast.Constant):
    return node.value

  ##if node has an binary operation, run the function again with its left and right values
  elif isinstance(node, ast.BinOp):
    left = evaluate(node.left)
    right = evaluate(node.right)

    ## if the operation is add, add left and right
    if isinstance(node.op, ast.Add):
      return left + right

    ## if the operation is subtract, subtract right from left
    elif isinstance(node.op, ast.Sub):
      return left - right

    ## if the operation is divide, divide left and right
    elif isinstance(node.op, ast.Div):
      return left / right

    ## if the operation is multiply, multiply left and right
    elif isinstance(node.op, ast.Mult):
      return left * right

  ##if node has an unary operation, run the function again with its operand
  elif isinstance(node, ast.UnaryOp):
    operand = evaluate(node.operand)

    ## if operation is add, return +1 * operand
    if isinstance(node.op, ast.UAdd):
      return +1 * operand

    ## if operation is subtract, return -1 * operand
    elif isinstance(node.op, ast.USub):
      return -1 * operand
    
    else:
      raise ValueError("Invalid Expression")

  else:
    raise ValueError("Unsupported Argument")



class Calculator:
  def __init__(self):
    self.root = ctk.CTk()

    self.root.title("My Simple Calculator")
    self.root.geometry("350x450")
    self.root.configure(fg_color="white")

    self.title_lbl = ctk.CTkLabel(self.root, 
                                  text="SIMPLE CALCULATOR", 
                                  fg_color="white", 
                                  text_color="black", 
                                  font=("Arial", 30, "bold"))
    self.title_lbl.pack(padx=10, pady=10)

    self.entry = ctk.CTkEntry(self.root,
                              fg_color="light grey", 
                              text_color="black",
                              width=300, 
                              justify="right",
                              font=("Arial", 25, "bold"))
    
    self.entry.pack(padx=10, pady=5)

    self.entry.configure(state="readonly")

    self.frm1 = ctk.CTkFrame(self.root, fg_color="white")

    for i in range(4):
      self.frm1.grid_columnconfigure(i, weight=1)

    for i in range(5):
      self.frm1.grid_rowconfigure(i, weight=1)

    ## clear and delete buttons
    self.clear_btn = ctk.CTkButton(self.frm1, text="C", text_color="black", fg_color="red", command=self.pressed_clear)
    self.clear_btn.grid(row=0, column=0, sticky="nsew", padx=3)

    self.del_btn = ctk.CTkButton(self.frm1, text="del", text_color="black", fg_color="yellow", command=self.pressed_del)
    self.del_btn.grid(row=0, column=3, sticky="nsew", padx=3)
    ###########################

    ## number buttons
    self.btn_1 = ctk.CTkButton(self.frm1, text="1", text_color="black", fg_color="white", border_color="black", command=self.pressed_1)
    self.btn_1.grid(row=3, column=0, sticky="nsew", padx=3)

    self.btn_2 = ctk.CTkButton(self.frm1, text="2", text_color="black", fg_color="white", command=self.pressed_2)
    self.btn_2.grid(row=3, column=1, sticky="nsew", padx=3)

    self.btn_3 = ctk.CTkButton(self.frm1, text="3", text_color="black", fg_color="white", command=self.pressed_3)
    self.btn_3.grid(row=3, column=2, sticky="nsew", padx=3)

    self.btn_4 = ctk.CTkButton(self.frm1, text="4", text_color="black", fg_color="white", command=self.pressed_4)
    self.btn_4.grid(row=2, column=0, sticky="nsew", padx=3)

    self.btn_5 = ctk.CTkButton(self.frm1, text="5", text_color="black", fg_color="white", command=self.pressed_5)
    self.btn_5.grid(row=2, column=1, sticky="nsew", padx=3)

    self.btn_6 = ctk.CTkButton(self.frm1, text="6", text_color="black", fg_color="white", command=self.pressed_6)
    self.btn_6.grid(row=2, column=2, sticky="nsew", padx=3)

    self.btn_7 = ctk.CTkButton(self.frm1, text="7", text_color="black", fg_color="white", command=self.pressed_7)
    self.btn_7.grid(row=1, column=0, sticky="nsew", padx=3)

    self.btn_8 = ctk.CTkButton(self.frm1, text="8", text_color="black", fg_color="white", command=self.pressed_8)
    self.btn_8.grid(row=1, column=1, sticky="nsew", padx=3)

    self.btn_9 = ctk.CTkButton(self.frm1, text="9", text_color="black", fg_color="white", command=self.pressed_9)
    self.btn_9.grid(row=1, column=2, sticky="nsew", padx=3)

    self.btn_0 = ctk.CTkButton(self.frm1, text="0",text_color="black", fg_color="white", command=self.pressed_0)
    self.btn_0.grid(row=4, column=0, sticky="nsew", padx=3)
    ##########################

    ## decimal and equal buttons
    self.btn_decimal = ctk.CTkButton(self.frm1, text=".", text_color="black", fg_color="white", command=self.pressed_dec)
    self.btn_decimal.grid(row=4, column=1, sticky="nsew", padx=3)
  
    self.btn_equal = ctk.CTkButton(self.frm1, text="=", text_color="white", fg_color="blue", command=self.pressed_equal)
    self.btn_equal.grid(row=4, column=2, sticky="nsew", padx=3)
    #########################

    ## signs
    self.btn_add = ctk.CTkButton(self.frm1, text="+", text_color="black", fg_color="white", command=self.pressed_add)
    self.btn_add.grid(row=1, column=3, sticky="nsew", padx=3)

    self.btn_sub = ctk.CTkButton(self.frm1, text="-", text_color="black", fg_color="white", command=self.pressed_sub)
    self.btn_sub.grid(row=2, column=3, sticky="nsew", padx=3)

    self.btn_mul = ctk.CTkButton(self.frm1, text="*", text_color="black", fg_color="white", command=self.pressed_mul)
    self.btn_mul.grid(row=3, column=3, sticky="nsew", padx=3)

    self.btn_div = ctk.CTkButton(self.frm1, text="/", text_color="black", fg_color="white", command=self.pressed_div)
    self.btn_div.grid(row=4, column=3, sticky="nsew", padx=3)
    #########################

    self.frm1.pack(padx=10, pady=10)


    self.credit = ctk.CTkLabel(self.root, text="Made by Anji", 
                               text_color="darkgrey", 
                               fg_color="white", 
                               font=("Monoblack", 17))
    self.credit.pack()

    ## number assigning values
    self.btn_1_value = ctk.IntVar(value=1)
    self.btn_2_value = ctk.IntVar(value=2)
    self.btn_3_value = ctk.IntVar(value=3)
    self.btn_4_value = ctk.IntVar(value=4)
    self.btn_5_value = ctk.IntVar(value=5)
    self.btn_6_value = ctk.IntVar(value=6)
    self.btn_7_value = ctk.IntVar(value=7)
    self.btn_8_value = ctk.IntVar(value=8)
    self.btn_9_value = ctk.IntVar(value=9)
    self.btn_0_value = ctk.IntVar(value=0)
    ############################

    ## signs values 
    self.btn_add_value = ctk.StringVar(value="+")
    self.btn_sub_value = ctk.StringVar(value="-")
    self.btn_mul_value = ctk.StringVar(value="*")
    self.btn_div_value = ctk.StringVar(value="/")
    self.btn_equal_value = ctk.StringVar(value="=")
    self.btn_dec_value = ctk.StringVar(value=".")


    self.root.mainloop()

  ## function that happens when user presses 1
  def pressed_1(self):
     self.entry.configure(state="normal")
     self.entry.insert("end", self.btn_1_value.get())
     self.entry.configure(state="readonly")
     
  ## function that happens when user presses 2
  def pressed_2(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_2_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 3
  def pressed_3(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_3_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 4
  def pressed_4(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_4_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 5
  def pressed_5(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_5_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 6
  def pressed_6(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_6_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 7
  def pressed_7(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_7_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 8
  def pressed_8(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_8_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 9
  def pressed_9(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_9_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses 0
  def pressed_0(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_0_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses .
  def pressed_dec(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_dec_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses +
  def pressed_add(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_add_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses -
  def pressed_sub(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_sub_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses *
  def pressed_mul(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_mul_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses /
  def pressed_div(self):
    self.entry.configure(state="normal")
    self.entry.insert("end", self.btn_div_value.get())
    self.entry.configure(state="readonly")

  ## function that happens when user presses del
  def pressed_del(self):
    self.entry.configure(state="normal")
    self.entry.delete(len(self.entry.get())-1, "end")
    self.entry.configure(state="readonly")

  ## function that happens when user presses C
  def pressed_clear(self):
    self.entry.configure(state="normal")
    self.entry.delete(0, "end")
    self.entry.configure(state="readonly")
    
  ## function that happens when user presses =
  def pressed_equal(self):
    try:
      self.entry.configure(state="normal")
      expression = self.entry.get()

      ## i use the ast model to turn the text i got from the entry into syntax python can understand
      tree = ast.parse(expression, mode="eval")

      ## i then run what i got as a parameter inside my evaluate function to get the answer and store it inside variable calculator
      calculation = evaluate(tree.body)
      
      self.entry.delete(0, "end")
      self.entry.insert("end", calculation)
      self.entry.configure(state="readonly")

    except(ValueError, AttributeError, ZeroDivisionError, TypeError, SyntaxError) as e:
      CTkMessagebox(title="Error", message=f"An Error occured -- {str(e)}")


Calculator()
