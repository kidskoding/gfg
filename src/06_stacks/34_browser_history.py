"""34. Custom Browser History (GFG, hard)."""


class BrowserHistory:
    """Start on homepage; visit(url) goes to url and clears forward history; back/forward move up to steps
    pages (stopping at the ends) and return the current url."""

    def __init__(self, homepage: str) -> None:
        raise NotImplementedError

    def visit(self, url: str) -> None:
        raise NotImplementedError

    def back(self, steps: int) -> str:
        raise NotImplementedError

    def forward(self, steps: int) -> str:
        raise NotImplementedError
