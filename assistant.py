from abc import ABC, abstractmethod
from typing import Dict, Any

class Assistant(ABC):
    @abstractmethod
    def listen(self) -> str:
        """Listens to user input, typically from a microphone.

        Returns:
            str: The user's spoken input as text.
        """
        pass

    @abstractmethod
    def process_input(self, user_input: str) -> Dict[str, Any]:
        """Processes the user's input and determines the appropriate action.

        Args:
            user_input (str): The user's input text.

        Returns:
            Dict[str, Any]: A dictionary containing information about the processed input, 
                            such as the intent, entities, and any relevant data.
        """
        pass

    @abstractmethod
    def speak(self, text: str):
        """Speaks the given text to the user.

        Args:
            text (str): The text to be spoken.
        """
        pass

    @abstractmethod
    def run(self):
        """Starts the main loop of the assistant."""
        pass
