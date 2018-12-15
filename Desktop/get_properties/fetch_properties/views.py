import paramiko
from scp import SCPClient
import socket
import re,ftplib
import os
import mysql.connector
from django.shortcuts import render,redirect
import requests

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='mcjca032162', username='chefsolo', password='solochef')

print ("Connected")
sftp =ssh.open_sftp()

def query_with_fetchall(request):
    try:
        #db_info1 = db_info.readlines() ssh lopala undali idi
        db = mysql.connector.connect(host='mcjca032162', database='properties_desync', user='root', password='support_1') 
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM Servers")
        rows = mycursor.fetchall()
 
        print('Total Row(s):', len(rows))
        for row in rows:
            print(row)
        return render(request,'db_pro.html')
    except Exception as e:
        print ("caused Exception1:",e)

    finally:
        db.close()
  
query_with_fetchall(request):
