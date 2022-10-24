# Python http_server_checker
Previously runing this software install pytest and requests libraries
this software sends http request packets and 
waits for the returned packets to evaluate the state of the Devices/Modem web servers.Each device that has a web server inside could be checked by http's packhet.

Files Description_:
api1.py   : main code for checker web servers.

sites.txt : This file contains the Ips and dns for checking, We can add several modems'sites to check if 
            server modems are working properly.

api1.txt  : This file contains the packets data result returned from de web servers checked.

dict_cod_errors_http.txt : This file contains code errors that modems usually are returning as a result of their theirs work flow .

test_api1.py   :  This file contains the code for testing functions to pass.
