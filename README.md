Appium script that runs against the Calculator mobile app (Pixel 10 - Android 17.0 / API 37.0)

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
