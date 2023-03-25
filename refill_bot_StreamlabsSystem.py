import os
import datetime

def refill_counter():
    # Check if the file exists
    if not os.path.exists("refill_counter.txt"):
        with open("refill_counter.txt", "w") as f:
            f.write("0")

    # Read the current count from the file
    with open("refill_counter.txt", "r") as f:
        count = int(f.read())

    # Increment the count
    count += 1

    # Write the new count to the file
    with open("refill_counter.txt", "w") as f:
        f.write(str(count))

def last_refill():
    # Get the current date and time
    now = datetime.datetime.now()

    # Write the date and time to a file
    with open("last_refill.txt", "w") as f:
        f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Send a message to chat
    Parent.SendStreamMessage(f"Refill complete at {now.strftime('%Y-%m-%d %H:%M:%S')}")

def handle_command():
    if "!refill":
        refill_counter()
        last_refill()

handle_command()