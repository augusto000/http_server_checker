import requests, sys, os
from requests.models import Response

def main():
    
    errors_http="dict_cod_errors_http.txt"
    errors_dict = read_code_errors(errors_http)
    
    print_errors_dict(errors_dict) 
    
        
    arch ="sites.txt"
    site = read_sites_list(arch)
    print("---SITES ---------------------------------------------------------------")
    for i in site:
        try:
            s = i[0]
            url = f"http://{s}/"
            response = requests.get(url)
            #If response from WebServers is code 200
            if response.status_code ==200 :  
                h = response.headers['content-type']
                enco= response.encoding
                tex = response.text
                parsed_tex = clean_tex(tex)
                jso = response.json
                parsed_data=f"{response.status_code} {url}{h}{enco}{jso}"        
                #parsed_data=f"{url}{h}{enco}{jso}{parsed_tex}"        
                print_returned_data(parsed_data)
            elif response.status_code >= 300:
                h = response.headers['content-type']
                enco= response.encoding
                tex = response.text
                parsed_tex = clean_tex(tex)#no saving this yet
                jso = response.json
                print(f"Posible report on code {response.status_code} HTTP found on  {i}")
                print("Check the log at this same folder on api1.txt")    
                parsed_data=f"{response.status_code} {i} {url} {h}{enco} {jso}"        
                #print_returned_data(parsed_data)  thi line records the file in the pc
                print_returned_data(parsed_data)
            else:   
                h = response.headers['content-type']
                enco= response.encoding
                tex = response.text
                parsed_tex = clean_tex(tex)
                jso = response.json
                print(f"Posible report on code {response.status_code} HTTP found on  {i}")
                print("Check the log at this same folder on api1.txt")    
                parsed_data=f"#####{response.status_code} {i}{url}{h}{enco}{jso}"        
                #print_returned_data(parsed_data)  thi line records the file in the pc
                print_returned_data(parsed_data)
        except ConnectionError as e:
            r=f"This site {i} refused the connection, the name error is ",sys.exc_info()[0]
            print_returned_data(r)
        except requests.exceptions.ConnectionError as e:
            j = f"This site {i} seems do not exist delette it and reestart the program \
                  the name error is ",sys.exc_info()[0]
            print_returned_data(j)    
        except SyntaxError as e:
            t=f"empty expression not allowed, name error ",sys.exc_info()[0]
            print_returned_data(t)    
        except NameError as e:
            t = f"url is not defined, name error ",sys.exc_info()[0]
            print_returned_data(t)        
"""This cls function clean the windows """
def cls():
    lambda :os.system("cls")

def print_errors_dict(errors_dict) :
    cls()
    print("----------------------------------------------")
    print("    ****   HTTP Code Errors List")
    print("----------------------------------------------")
    for key, value in errors_dict.items():
        x=errors_dict.get(key)
        cleaned_x=x.strip('\n')
        print(f"{key} - {cleaned_x}")  
        print()          

def read_code_errors(errors_http):
    try:
        errors_code={}
        #this width, only read and loads
        with open(errors_http, "rt") as file_err:
            for row in file_err:
                clean_row = row.strip('-')
                splited=clean_row.split("-")
                key = splited[0]
                value = splited[1]
                errors_code[key]= value               
            return errors_code    
    except FileNotFoundError as e:
        print("File not found, the name error is ",sys.exc_info()[0])        
    except PermissionError as e:
        print("It is not allowed open this File , the name error is ",sys.exc_info()[0])        
    except IOError as e:
        print("The error name is ",sys.exc_info()[0])    

def clean_tex(t):
    try:
        clean_t=t.strip()
        splited_cleaned = clean_t.split('[]')
        print()
        return splited_cleaned
    except ValueError as e:
        print("The name of this error is ",sys.exc_info[0])    

def print_returned_data(parsed):
    try:
        with open("api1.txt",  "at") as api:
            print(parsed, file=api)            
    except FileNotFoundError as e:
        print("File not found, the name error is ",sys.exc_info()[0])        
    except PermissionError as e:
        print("It is not allowed open this File , the name error is ",sys.exc_info()[0])        

def read_sites_list(file):
    sites_list=[]
    try:                  #read sites.txt"
        with open (file, mode="rt") as file_:
            for line in file_:
                clean_line = line.strip('\n')
                length = len(clean_line)
                #check if the digits of the word is greater then zero
                if length > 0  :
                    splited_line = clean_line.split(',')
                    sites_list.append(splited_line)
            return sites_list 
    except FileNotFoundError as e:
        print("File not found ")
        print("The name error is ",sys.exc_info()[0])
    except PermissionError as e:
        print("Not allowed to access this file", sys.exc_info()[0])
        
if __name__=='__main__':
    main()
    
