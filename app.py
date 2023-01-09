#import os
from flask import Flask
#from azure.monitor.opentelemetry.exporter import AzureMonitorMetricExporter
app = Flask(__name__)

#exporter = AzureMonitorMetricExporter(
#    connection_string=os.environ["InstrumentationKey=b2ee777e-d3d1-4bd9-aa4f-d3c58d2b0a64"]
#)

@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework!!!"

if __name__ == "__main__":
    app.run()
