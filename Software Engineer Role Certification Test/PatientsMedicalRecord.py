#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getAverageTemperatureForUser' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/medical_records?userId=<userId>&page=<page>
#
# The function is expected to return a String value.
# The function accepts a userId argumnent (Integer).
# In the case of an empty array result, return value '0'
#
import requests

def getAverageTemperatureForUser(userId):
    # Write your code here
    page = 1
    total_records = 0
    total_temperature = 0
    
    # Fetch medical records for each page
    while True:
        url = f"https://jsonmock.hackerrank.com/api/medical_records?userId={userId}&page={page}"
        response = requests.get(url)
        data = response.json()
        
        # If no more pages or no records found, break the loop
        if page > data['total_pages'] or not data['data']:
            break
        
        # Calculate average body temperature for each record
        for record in data['data']:
            temperature = record['vitals']['bodyTemperature']
            total_temperature += temperature
            total_records += 1
        
        page += 1
    
    # Calculate the average temperature
    if total_records > 0:
        average_temperature = total_temperature / total_records
        return "{:.1f}".format(average_temperature)  # Format to one decimal place
    else:
        return '0'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    userId = int(input().strip())

    result = getAverageTemperatureForUser(userId)

    fptr.write(result + '\n')

    fptr.close()
