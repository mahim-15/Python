import re
import sys

def read_code(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

def analyze_complexity(code):
    code_lines = code.splitlines()

    loop_count = 0
    nested_loops = 0
    recursion = False
    max_nesting = 0
    stack = []

    for line in code_lines:
        line = line.strip()

        # Check for loops
        if re.match(r'(for|while)\s*\(.*\)', line) or re.match(r'(for|while)\s+.*:', line):
            loop_count += 1
            stack.append("loop")
            max_nesting = max(max_nesting, len(stack))

        # Check for recursion
        if 'def ' in line or line.startswith("void") or line.startswith("int") or line.startswith("long"):
            func_name = re.findall(r'def (\w+)|(\w+)\s*\(', line)
            if func_name:
                name = [f for f in func_name[0] if f][0]
        elif 'name' in locals() and name in line:
            if '(' in line and ')' in line and line.strip().startswith(name):
                recursion = True

        # Manage loop nesting
        if '{' in line:
            stack.append('{')
        if '}' in line and stack:
            stack.pop()

    # Heuristics
    if recursion:
        complexity = ("O(2^n)", "Ω(1)", "Θ(2^n)")
    elif max_nesting >= 2:
        complexity = ("O(n^2)", "Ω(n)", "Θ(n^2)")
    elif loop_count >= 1:
        complexity = ("O(n)", "Ω(1)", "Θ(n)")
    else:
        complexity = ("O(1)", "Ω(1)", "Θ(1)")

    return complexity

def main():
    filename = input("Enter source code filename: ")
    code = read_code(filename)
    big_o, big_omega, big_theta = analyze_complexity(code)

    print("\nTime Complexity Analysis:")
    print(f"Big O (Worst Case):     {big_o}")
    print(f"Big Omega (Best Case):  {big_omega}")
    print(f"Big Theta (Average):    {big_theta}")

if __name__ == "__main__":
    main()
