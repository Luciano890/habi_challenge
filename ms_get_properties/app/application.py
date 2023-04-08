"""Application to admin views module."""
from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True)
class APIApp:
    """API Application class.

    Attributes:
        * _saved_responses (dict[str, dict]): Saved responses.
        * _views (dict[str, Callable[..., dict]]): Views.

    Methods:
        * saved_responses(self):
            Get the saved responses.
        * views(self):
            Get the views.
        * path(self, view: Callable[..., dict], path: str, /) -> None:
            Register a view for a given path.
    """
    _saved_responses: dict[str, dict] = field(
        default_factory=lambda: {'/': {'message': '¡Welcome to the Habi Challenge API!'}, }
    )
    _views: dict[str, Callable[..., dict]] = field(default_factory=dict)

    @property
    def saved_responses(self):
        """Get the saved responses."""
        return self._saved_responses

    @property
    def views(self):
        """Get the views."""
        return self._views

    def path(self, view: Callable[..., dict], path: str, /) -> None:
        """Register a view for a given path.
        
        Parameters:
            * view (Callable[..., dict]): View to register.
            * path (str): Path to register the view.
        """
        self._views[path] = view
