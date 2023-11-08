#!/bin/python3
import sys

sensorReportTemplate = """
            "sensorReport": [
                {
                    "type": "Wavenumber",
                    "mft-spectra:type": "%s",
                    "mft-spectra:values": %s
                }
            ]
"""
with open(sys.argv[2], 'r') as file:
    data = file.readlines()
    line = data[0]
    measurements = line.split(";")
    print(sensorReportTemplate % (sys.argv[1], list(map(float, measurements))) )
