import argparse

# change todo_manager to todo_manager_json_ver or vice versa
from todo_manager_json_ver import show_todo, add_todo, remove_todo
# change the other one in the "case _" block down here...

def main():
  parser = argparse.ArgumentParser(description='Todo Manager CLI')

  # Action group (subparsers)
  subparsers = parser.add_subparsers(dest='command', required=True)

  # 1. 'list' command
  parser_list = subparsers.add_parser('list', help='List all current todos')

  # 2. 'add' command
  parser_add = subparsers.add_parser('add', help='Add a new todo item')
  parser_add.add_argument('task', type=str, help='The task description.')

  # 3. 'rm' (remove) command
  parser_remove = subparsers.add_parser('rm', help='Remove a todo item by index')
  parser_remove.add_argument('index', type=int, help='The index of the task to remove.')

  # ...leave this for now...
  '''
  parser.add_argument('--file', '-f', type=str, default='todo.json',
    help='Specify todo file (default: todo.json)')
  parser.add_argument('--verbose', '-v',
    action='store_true', help='Enable verbose output')
  '''

  # Parse & execute
  args = parser.parse_args()

  match args.command:
    case 'list':
      show_todo()
      print()
    case 'add':
      add_todo(args.task) # args.task holds the value from the 'task' argument
      print()
    case 'rm':
      remove_todo(args.index)
      print()
    case _:
      # ...change this too!
      from todo_manager_json_ver import main as interactive_mode
      interactive_mode()

if __name__ == '__main__':
  main()
