class PersistSaveError(Exception): 
    """
    Occurs when object insertion faild
    """
    ...

class PersistNotFound(Exception): 
    """
    Occurs when it cannot find object
    with specified condition.
    """
    ...