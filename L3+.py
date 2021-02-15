#infex to post fix
class stack: 
     
    def __init__(self, stack): 
        self.top = -1 
        self.stack = stack 
        self.array = []  
        self.output = []
     
    def isEmpty(self): 
        if self.top == -1:
            return True 
        else:
            False
    
    def peek(self): 
        if self.isEmpty() == True:
            return 0
        return self.array[-1]
     
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
 
    def isOperand(self, ch): 
        return ch.isalpha() 

    def notGreater(self, i): 
        precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
        if self.peek() =="(":
            return False
        a = self.precedence[i] 
        b = self.precedence[self.peek()] 
        if a  <= b:
            return True 
        else:
            return False
    
    def infixToPostfix(self, exp): 
        
        for i in exp: 
             
            if self.isOperand(i): 
                self.output.append(i) 
             
            elif i  == '(': 
                self.push(i) 
 
            elif i == ')': 
                while( (not self.isEmpty()) and 
                                self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
   
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 
   
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        print("".join(self.output))
exp = input("Enter your expression:")
print("The result of infex to postfix is:")
obj = stack(len(exp)) 
obj.infixToPostfix(exp) 