# -*- coding: utf-8 -*-
"""Internet_Speed_Test_Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wN984nrjrVdTnS89BUBWIk_lPQNh2OGT
"""

!pip install speedtest-cli matplotlib

import speedtest
import matplotlib.pyplot as plt

def get_speed_test_results():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # convert to Mbps
    return download_speed, upload_speed

download_speeds = []
upload_speeds = []


for _ in range(5):
    download_speed, upload_speed = get_speed_test_results()
    download_speeds.append(download_speed)
    upload_speeds.append(upload_speed)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 6), download_speeds, label='Download Speed (Mbps)', marker='o')
plt.plot(range(1, 6), upload_speeds, label='Upload Speed (Mbps)', marker='x')
plt.xlabel('Test Number')
plt.ylabel('Speed (Mbps)')
plt.title('Internet Speed Test Results')
plt.legend()
plt.grid(True)
plt.show()