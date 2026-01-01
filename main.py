"""Main entry point for Todo CLI application."""

from src.services.todo_service import TodoService
from src.cli.menu_navigator import MenuNavigator


def main():
    """Main application loop."""
    # Initialize service and menu navigator
    service = TodoService()
    navigator = MenuNavigator(service)

    # Display startup banner
    print("=" * 50)
    print("    Phase I Todo CLI - Menu Navigation")
    print("=" * 50)
    print()

    # Start menu navigator
    try:
        navigator.start()
    except Exception as e:
        # Catch any unexpected errors
        print(f"\nUnexpected error: {e}")
        print("Please restart the application.")


if __name__ == "__main__":
    main()
