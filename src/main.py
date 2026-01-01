"""Main entry point for the Todo CLI application."""

from src.services.todo_service import TodoService
from src.cli.menu import CommandMenu


def main():
    """Main application loop."""
    # Initialize service and menu
    service = TodoService()
    menu = CommandMenu(service)

    print("Todo CLI - Phase I")
    print("Type 'help' for available commands, 'exit' to quit\n")

    # Main command loop
    while True:
        try:
            # Get user input
            user_input = input("Todo CLI > ").strip()

            # Skip empty input
            if not user_input:
                continue

            # Parse command
            command, args = menu.parse_command(user_input)

            # Handle exit
            if command in ["exit", "quit"]:
                print("Goodbye!")
                break

            # Execute command
            result = menu.execute_command(command, args)
            if result:
                print(result)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
