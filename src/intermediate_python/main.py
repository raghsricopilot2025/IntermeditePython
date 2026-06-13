"""Entry point for the IntermediatePython project."""
from . import osmodule


def main() -> None:
    """Run the project."""
    print("Hello from IntermediatePython!")
    osmodule.show_info()

if __name__ == "__main__":
    main()
