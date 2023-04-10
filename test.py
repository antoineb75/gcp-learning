from typing import List, Generator


def regularfunc() -> List[int]:
    """This works and it's fine."""
    ret = []
    for n in range(10):
        ret.append(n * 10)
        
    return ret
    

def smallergen() -> Generator[int, None, None]:
    """This also works. Favor this one."""
    for n in range(10):
        yield n * 10
        
        
# Intended Usage:
print("Regular func:", regularfunc())
print("Smaller gen:", list(smallergen()))