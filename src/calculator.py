def soma (x,y):
    """
    >>> soma(10, 20)
    30
    
    >>> soma(-10, 20)
    10
    
    >>> soma(50, 0.5)
    50.5
    
    >>> soma('10', 10)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser inteiro ou float
    
    """
    
    assert isinstance(x,(int,float)), 'x precisa ser inteiro ou float'
    assert isinstance(y,(int,float)), 'y precisa ser inteiro ou float'
    return x + y

def subtrai(x,y):
    
    """
    >>> subtrai(10,5)
    5
    
    >>> subtrai(-10,-30)
    20
    
    >>subtrai(-10,30)
    -40
    
    """
    
    assert isinstance(x,(int,float)), 'x precisa ser inteiro ou float'
    assert isinstance(y,(int,float)), 'y precisa ser inteiro ou float'
    return x - y

if __name__ == '__main__': #PARA EXECUTAR TESTE NESSE MODULO DIRETAMENTE
    import doctest
    doctest.testmod(verbose=True) 
