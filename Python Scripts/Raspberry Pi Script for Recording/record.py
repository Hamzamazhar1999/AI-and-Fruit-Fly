# Import necessary modules
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from libcamera import controls
import time
import os
from subprocess import call

# Prompt the user for a file name
test_num = input("File Name:")

# Create a Picamera2 instance
picam2 = Picamera2()

# Configure video settings
video_config = picam2.create_video_configuration(main={"size": (1024, 768)},
                                                  lores={"size": (1024, 768)},
                                                  display="main")
picam2.configure(video_config)

# Start the camera with a preview
picam2.start(show_preview=True)

# Set camera controls such as frame rate, contrast, exposure, etc.
picam2.set_controls({"FrameRate": 30, "Contrast": 1, "ExposureValue": 0.0,
                     "AfMode": controls.AfModeEnum.Manual,
                     "LensPosition": 10, "ExposureTime": 5000})

# Create an H.264 video encoder
encoder = H264Encoder(bitrate=10000000)

# Define output file names
output = test_num + ".h264"
output_converted = test_num + ".mp4"

# Start recording with the encoder
picam2.start_recording(encoder, output)

# Wait for 15 seconds
time.sleep(15)
print("15 SECONDS: Start LED!")

# Wait for 5 more seconds
time.sleep(5)
print("Stop LED!")

# Wait for an additional 40 seconds
time.sleep(40)

# Stop recording
picam2.stop_recording()

# Stop the preview
picam2.stop_preview()

# Use MP4Box to convert the recorded video from H.264 to MP4 format
command = "MP4Box -add " + output + " -fps 30 " + output_converted

# Execute the MP4Box command
call([command], shell=True)

# Remove the original H.264 file
os.remove(output)
