# Isaac St Hubert Module 1.3 10/26/2025
# This program asks the user for the number of bottles and counts down to 0

# Beer bottle countdown function
def bottles_of_beer(count):
    for c in range(count, 0, -1):
        if c > 1:
            print(f"{c} bottles of beer on the wall, {c} bottles of beer.")
            print(f"Take one down and pass it around, {c - 1} bottle(s) of beer on the wall.\n")
        else:
            # Handles the 1 bottle case
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")

def main():
    num_bottles = int(input("How many bottles of beer are on the wall? "))
    bottles_of_beer(num_bottles)
    print("Time to buy more bottles of beer.")

if __name__ == "__main__":
    main()

