import os

bids = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    name = input("Enter your name: ")
    bid = float(input("Enter your bid amount: ₹"))
    bids[name] = bid

    more = input("Are there more bidders? (yes/no): ").lower()
    clear_screen()

    if more == "no":
        break

winner = max(bids, key=bids.get)
print(f"\n🎉 {winner} wins with a bid of ₹{bids[winner]}!")
