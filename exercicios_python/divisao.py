def divisao(x,y):
    """
    >>> divisao(10,20)
    0.5
    
    >>> divisao(10,2)
    5.0
    """
    assert isinstance(x,(int,float)), 'x tem que ser inteiro ou flutuante'
    assert isinstance(y,(int,float)), 'y tem que ser inteiro ou float'
    return x / y

def divisao_com_resultado_inteiro(x,y):
    """
    >>> divisao_com_resultado_inteiro(10,20)
    0
    
    >>> divisao_com_resultado_inteiro(10,2)
    5
    """
    assert isinstance(x,(int,float)), 'x tem que ser inteiro ou float'
    assert isinstance(y,(int,float)), 'y tem que ser inteiro ou float'
    return x // y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
