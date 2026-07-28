(7/27) Appium script that runs against the Calculator mobile app on Android<br>

<b>Summary</b><br>
1) Calculator mobile app running on Pixel 10 - Android 17.0 - API 37 via Android Studio on Windows<br>
2) After each run, results are stored in a MySQL database.<br>
3) There are a total of 3 tests - home, basic calculator and tip calculator
3) PyCharm Dev Environment is on Ubuntu 26.04 - Jenkins (1)<br>
4) Jenkins Instance is running on Ubuntu 26.04 - Jenkins(1)<br>
5) Credentials are hidden via secret text in Jenkins; locally they are hidden via .env<br>

<b>Precondition/Setup:</b>
1) ipconfig to capture IPv4 Address from Windows machine<br>
2) In Windows PowerShell (Admin mode) on Windows, run the following:<br>
   netsh interface portproxy add v4tov4 listenaddress=<Windows IP Address> listenport=5555 connectaddress=127.0.0.1 connectport=5555<br>
   New-NetFirewallRule -DisplayName "Android Emulator ADB" -Direction Inbound -LocalPort 5555 -Protocol TCP -Action Allow<br>
3) Android Emulator needs to be running on host Windows machine<br>
4) From Ubuntu VM, need to perform the following:<br>
   a) adb start-server<br>
   b) adb connect 192.168.150.1:5555 (ip is captured via ipconfig on the Windows machine)<br>
   c) adb devices (to confirm that the Android Emulator is connected)<br>
5) The steps above are NOT baked into the Jenkins job
