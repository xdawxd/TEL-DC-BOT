from typing import NoReturn, Iterator

from contextlib import contextmanager


class ErrorHandler:
    @classmethod
    def handle(cls, error: Exception) -> NoReturn:
        """
        Handles the given error basing on its type and raises a proper exception.

        Args:
            error: Expected error.
        """


@contextmanager
def handle_errors(*errors: Exception) -> Iterator[None]:
    """
    Contextmanager used to catch exceptions and pass them to the ErrorHandler.

    Args:
        *errors: Unpacked tuple of caught exceptions.

    Yields:
        Empty iterator.
  """
    try:
        yield
    except errors as errs:
        ErrorHandler.handle(errs)
