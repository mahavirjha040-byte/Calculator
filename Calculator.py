import tkinter as tk

# ---------- Function: Simple Calculator ----------
def calculator(f_num=None, opr=None, s_num=None, expression=None):
    try:
        if expression is not None:
            # Full expression mode (BODMAS)
            return eval(expression)
        elif f_num is not None and s_num is not None and opr is not None:
            # Step-by-step mode
            if opr == "+":
                return f_num + s_num
            elif opr == "-":
                return f_num - s_num
            elif opr == "*":
                return f_num * s_num
            elif opr == "/":
                return f_num / s_num
            else:
                return "Invalid Operator"
        else:
            return "Incomplete input"
    except Exception as e:
        return f"Error: {e}"

# ---------- Input Phase ----------
First_num = float(input("Type first number: "))
Operation = input("Choose Operator (+, -, *, /): ")
Second_num = float(input("Type second number: "))

# BODMAS expression creation
moreaction = str(First_num) + Operation + str(Second_num)
Result = calculator(expression=moreaction)
print("Result =", Result)

# Store operation details
get_reverse = [str(First_num), Operation, str(Second_num)]

# ---------- Continue operations ----------
more_operation = input("Would you like to continue? (y/n): ")

while more_operation.lower() == "y":
    Operation = input("Choose Operator (+, -, *, /): ")
    Next_num = float(input("Type next number: "))
    
    # Add new operation into expression (maintains full equation)
    moreaction += Operation + str(Next_num)
    
    Result = calculator(expression=moreaction)
    get_reverse.append(Operation)
    get_reverse.append(str(Next_num))
    
    print("Updated Expression:", moreaction)
    print("Result =", Result)
    
    more_operation = input("Would you like to continue? (y/n): ")

# ---------- Reverse check with GUI ----------
Check_reverse = input("Would you like to check numbers in GUI? (y/n): ")

if Check_reverse.lower() == "y":
    index = 0  # define global index

    def show_next():
        global index
        if index < len(get_reverse):
            label.config(text=get_reverse[index])
            index += 1
        else:
            label.config(text="No more items!")

    # Tkinter window setup
    root = tk.Tk()
    root.title("Show One by One")
    root.geometry("300x150")  # fixed: * → x

    label = tk.Label(root, text="Click Next", font=("Arial", 16))
    label.pack(pady=20)

    button = tk.Button(root, text="Next", command=show_next, font=("Arial", 14))
    button.pack()

    root.mainloop()

print("Thank you for using the calculator! 😊")
