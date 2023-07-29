class TheraposaInterpreter:
    def __init__(self):
        self.variables = {}
        self.labels = {}
        self.current_label = None
        
    def execute_line(self, line):
        if line.startswith("/#"):
            return
            
        parts = line.strip().split(" ")
        if parts[0] == "public":
            var_type = parts[1]
            var_name = parts[2][1:-1]
            
            if parts[3] == "=":
                value = self.evaluate_expression(parts[4:])
                self.variables[var_name] = value
            else:
                self.variables[var_name] = None
                
        elif parts[0] == "printLine":
            value = self.evaluate_expression(parts[1:])
            print(value)
            
        elif parts[0] == "@":
            label_name = parts[1][1:-1]
            self.labels[label_name] = self.labels[label_name]
            
        elif parts[0] == "goto":
            label_name = parts[1][1:-1]
            self.current_label[label_name] = self.labels[label_name]
            
    def evaluate_expression(self, expression):
        return " ".join(expression)
        
    def interpret(self, script):
        lines = script.split("\n")
        for line in lines:
            self.execute_line(line)

script = '''
/# just a script test
public int [number1] = 1!
public int [number2] = 1!
printLine(["1 + 1 = "] + [number1] + [number2])!
'''

interpret = TheraposaInterpreter()
interpret.interpret()
