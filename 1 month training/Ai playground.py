import math

def complex_calculator():
    print("=======================================")
    print("      🔢 Advanced Scientific Calculator")
    print("=======================================")
    print("Type mathematical expressions directly!")
    print("Examples:")
    print("  ➤  5 + 6 * (3 - 2)")
    print("  ➤  sin(90)")
    print("  ➤  sqrt(25) + log(100)")
    print("  ➤  pi * 2 ** 2")
    print("Type 'exit' to quit.\n")

    # Define allowed functions and constants
    allowed_names = {name: obj for name, obj in math.__dict__.items() if not name.startswith("__")}
    allowed_names["pi"] = math.pi
    allowed_names["e"] = math.e

    while True:
        expr = input("Enter expression: ").strip()

        if expr.lower() == "exit":
            print("👋 Exiting calculator...")
            break

        try:
            # Evaluate the mathematical expression safely
            result = eval(expr, {"__builtins__": None}, allowed_names)
            print(f"✅ Result: {result}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")


# Run the calculator
complex_calculator()

