# breathingthroughmax

A system to track your rate of breath and sonify it in real-time through Max MSP. It emphasizes tenants of biofeedback and can serve as a responsive system for stress relief. 

Setup for data playback (from prerecorded data)

1. Extract package zips from inside the "package" folder and move to the "/Documents/Max 8/Packages" directory located in the user directory
2. Open the Max patch
3. Load the "data.txt" file in the "csvloader" sub-patch (this may take a minute)
4. Start the metro to iterate through the data with button labeled "play"

Setup for real time streaming:

1. Install python-osc (Python 3.5+ required) with "pip install python-osc"
2. Install SensorLog from the iOS App Store (no current equivalent for Android at the moment)
3. Edit the message boxes for the directory of python, the sensorlog.py, local ip, and port information
4. Click "run py host", and check to see if script is running in console
    - Errors from the python file will also appear in the Max console
5. Make sure the SensorLog app reflects the ip and port you have entered
6. From SensorLog, enable the following:
    - logging rate: "100Hz"
    - log format: ", and csv"
    - mode: "client"
    - protocol: "ump"
    - ip and port as above
    - accelerometer: enable
7. Finally, enable "log to stream" and make sure it connects
    - The Max console will also print "Now streaming data..." if data has been received