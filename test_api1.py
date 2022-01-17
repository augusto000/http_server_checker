from time import time
from api1 import read_code_errors, read_sites_list 
#read_code_errors, read_sites_list
from pytest import approx
import random, pytest,os

os.system('cls')
err_http="dict_cod_errors_http.txt"

dict_errors = read_code_errors(err_http)

def test_read_code_errors():    
    c = dict_errors.get("503")
    z = c.strip('\n')
    assert z == 'Service Unavailable'                   

    c = dict_errors.get("502")
    z = c.strip('\n')
    assert z == 'Bad Gateway' 

    c = dict_errors.get("500")
    z = c.strip('\n')
    assert z == 'Internal Server Error'

    c = dict_errors.get("0")
    #z = c.strip('\n')
    assert c == None                           

    c = dict_errors.get("09")
    #z = c.strip('\n')
    assert c == None                            

sites = "sites.txt"
site_list = read_sites_list(sites)
def test_read_sites_list():
    c = site_list[0]
    assert c == ['10.0.0.1']
    print()
    c = site_list[1]
    assert c ==['192.168.1.1']
    print()
    
    c = site_list[2]
    assert c == ['www.amazon.com']
    print()
    
http_errors = "dict_cod_errors_http.txt" 
dict_errors = read_code_errors(err_http)   
'''
def test_clean_tex():    
    c = clean_tex()
    assert c == ['ï»¿<html><head>\n<met...s>\n</html>']
    print()
'''


#Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_api1.py"])
