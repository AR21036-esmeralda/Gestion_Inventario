import pytest
from MODULO_MOVIMIENTOS_INVENTARIO import stock_valorizado

def test_validar_stock_valorizado():
    inventario = {

    "P001" : {"stock": 10, "precio":100},
    "P002" : {"stock": 5, "precio":20}      
    } 
    resultado = stock_valorizado(inventario)
    assert resultado == 1100


   