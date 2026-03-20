def ask(prompt: str) -> str:
    return input(prompt).strip() #clean input on terminal

def banner(title: str): #print section wise banner
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
