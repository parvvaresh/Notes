def hamming_distance(str1: str, str2: str) -> int:
    """
    Calculate the Hamming distance between two strings.
    
    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.
    
    Returns:
    int: The Hamming distance between the two strings.
    
    Raises:
    ValueError: If the input strings are not of the same length.
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    
    return sum(1 for x, y in zip(str1, str2) if x != y)
