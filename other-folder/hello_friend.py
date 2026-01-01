import sys

print("=== FRIEND GREETER ===")

if len(sys.argv) >1:
    friend_name =sys.argv[1]
    print(f"Hello, {friend_name}! How are you today?")
else:
    print("Please tell me your name!")
    print("Example: python hello_friend.py Vishal")
    