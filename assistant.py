from abc import ABC, abstractmethod

class Assistant(ABC):
    @abstractmethod
    def listen(self):
        """Listens to user input, typically from a microphone."""
        pass

    @abstractmethod
    def process_input(self, user_input: str):
        """Processes the user's input and determines the appropriate action."""
        pass

    @abstractmethod
    def speak(self, text: str):
        """Speaks the given text to the user."""
        pass

    @abstractmethod
    def run(self):
        """Starts the main loop of the assistant."""
        pass
