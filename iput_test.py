def greet(name):
    print(f"Hello, {name}! Nice to meet you.")

def main():
    # Prompt the user for their name
    user_name = input("Please enter your name: ")
    
    # Call the greet function with the user's input
    greet(user_name)

if __name__ == "__main__":
    main()