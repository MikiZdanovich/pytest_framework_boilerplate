from abc import ABC
from dataclasses import dataclass


@dataclass()
class BaseLocator(ABC):
    """
    Base class for all locators.
    """
