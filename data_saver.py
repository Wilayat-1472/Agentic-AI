import json

def save_notes(notes):
    try:
        with open("notes.json", "w") as f:
            json.dump(notes, f, indent=4)
        print("Notes saved to notes.json")
        return True
    except OSError as error:
        print(f"Error saving notes: {error}")
        return False
   
def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
        print("Notes loaded from notes.json")
        return notes
    except FileNotFoundError:
        print("No saved notes found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding notes.json. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Error loading notes: {error}")
        return []

notes = load_notes()
while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "1":
        title = input("Enter your title: ")
        content = input("Enter your note: ")
        notes.append({"title": title, "content": content})
        save_notes(notes)
    elif choice == "2":
        if notes:
            print("Your notes:")
            for idx, note in enumerate(notes, start=1):
                 print(f"{idx}. {note['title']}: {note['content']}")
        else:
            print("No notes available.")
    
    elif choice == "3":
            print("Exiting...")
            break
    else:
             print("Invalid choice. Please enter 1, 2, or 3.")   