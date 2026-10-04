"""30. Cyclic Redundancy Check and Modulo-2 Division (GFG, medium)."""


def crc_encode(data: str, key: str) -> str:
    """data followed by the CRC: the len(key) - 1 bit remainder of mod-2 dividing data + zeros by key."""
    raise NotImplementedError


def crc_check(codeword: str, key: str) -> bool:
    """True if mod-2 dividing codeword by key leaves an all-zero remainder (no error detected)."""
    raise NotImplementedError
