class Inputs:
    """
    A manager for an inputs.txt file.

    Automatically parses and creates a stack from an input file.
    """
    def __init__(self, filepath="inputs") -> None:
        """
        Initialize the Inputs object.

        Args:
            filepath (str): The path to the inputs file.
        """
        self.inputs = []
        with open(filepath) as inputsFile:
            for line in inputsFile:
                if line:
                    self.inputs.append(line.strip())

    def __iter__(self):
        return self.inputs.__iter__()

    def __len__(self):
        return len(self.inputs)

    def push(self, input_: str) -> None:
        """Add an input to the top of the stack."""
        self.inputs.append(input_)

    def pop(self) -> str:
        """Remove and return the top input from the stack."""
        return self.inputs.pop()

    def peek(self) -> str:
        """Return the top input from the stack."""
        return self.inputs[-1]
