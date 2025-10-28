import json

# --- load and save ---

# define file name constant
TODO_FILE = 'todo.json'

def load_todo():
  try:
    with open(TODO_FILE, 'r') as file:
      return json.load(file) # returns a list of strings
  except FileNotFoundError:
    return []
  except json.JSONDecodeError:
    # Handle case where file exists but is empty or invalid JSON
    print(f"'{TODO_FILE}' is corrupt or empty. Starting with an empty list.")
    return []

def save_todo(todo_list):
  with open(TODO_FILE, 'w') as file:
    json.dump(todo_list, file, indent=2)

# --- utilities ---

def show_todo():
  todo_list = load_todo()
  print()

  if not todo_list:
    print('📜 No todos yet! Use [a] to add some.')
    return

  longest_line = max(len(line) for line in todo_list)
  num_width = len(str(len(todo_list))) + 2

  print(f'{"No.":>{num_width}} | To-Do 📜')
  if any([not line.isascii() for line in todo_list]):
    print('-'*(num_width + 1)+ '+' + '-'*2*longest_line + '---')
  else:
    print('-'*(num_width + 1)+ '+' + '-'*(longest_line - 3) + '-------')
  for numero in range(len(todo_list)):
    print(f'{numero+1:>{num_width}} | {todo_list[numero]}')

def add_todo(todo=None): # <-- Accept optional index
  print()

  if todo is None: # <-- if no todo were passed
    # Interactice mode logic
    todo = input('📝 Type a new to-do: ')

  if not todo:
    print('📝 Todo cannot be empty!')
    return

  todo_list = load_todo()
  todo_list.append(todo)
  save_todo(todo_list)
  print(f"📝 ✓ Added: {todo}")

def remove_todo(index=None): # <-- Accept optional index
  todo_list = load_todo()
  print()

  if not todo_list:
    print('🚮 No todos to remove!')
    return

  try:
    if index is None: # <-- if no index were passed
      # Interactive mode logic
      todo_index = int(input(f'🚮 Enter the index to be removed [1-{len(todo_list)}]: '))
    else:
      todo_index = index

    # Validation logic
    if not 1 <= todo_index <= len(todo_list): raise IndexError
    else:
      removed_item = todo_list.pop(todo_index-1)
      save_todo(todo_list)
      print(f"🚮 ✓ Removed: {removed_item}")
  except (ValueError, TypeError, IndexError):
    print('🚮 Invalid index.')

def main_menu():
  print('--- TO-DO MANAGER ---')
  print('[s] to show list of to-do 📜')
  print('[a] to add a new to-do 📝')
  print('[r] to remove a to-do 🚮')
  print('[q] to quit ⮑')
  print()

# --- main ---

def main():
  print()
  attempt = 0
  while attempt < 3:
    main_menu()
    keystroke = input('Press a key to choose an action: ')

    if keystroke == 's':
      show_todo()
      attempt = 0
    elif keystroke == 'a':
      add_todo()
      attempt = 0
    elif keystroke == 'r':
      remove_todo()
      attempt = 0
    elif keystroke == 'q':
      print('See you later!\n')
      break
    else:
      print('Please choose an action by pressing the right key.')
      attempt += 1
    print()

if __name__ == '__main__':
  main()
