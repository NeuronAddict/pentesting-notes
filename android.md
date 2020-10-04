# android

https://docs.koodous.com/

## mitm proxy with android

https://docs.mitmproxy.org/stable/howto-install-system-trusted-ca-android/

## Add certificate to android

https://medium.com/hackers-secrets/adding-a-certificate-to-android-system-trust-store-ae8ca3519a85


# root device

https://android.stackexchange.com/questions/171442/root-android-virtual-device-with-android-7-1-1

## burp 

RTFM : https://developer.android.com/training/articles/security-config

https://laconicwolf.com/2019/07/21/using-burp-suite-with-android-devices/
https://blog.ropnop.com/configuring-burp-suite-with-android-nougat/
https://medium.com/androgoat/intercept-https-traffic-from-android-app-androgoat-part-2-60f7777b237d
https://medium.com/@bastian.ohm/analyse-network-traffic-with-burp-suite-on-android-3cefbf02af2e

## apktool

- use last version (jar on https://ibotpeaches.github.io/Apktool/)
- do not use package appt/aapt2... version. Use lastest android build tools
- be careful of frameworks, if corrupted, clean framework folder

## resign apk

```
keytool -genkey -v -keystore burp.keystore -storepass <password> -alias android -keypass <password> -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -keystore burp.keystore -storepass <password> -keypass <password> app.apk android
```

## extract app from device

```
adb shell pm list packages
adb shell pm path <package>
adb pull <path>

adb shell pm list packages | grep post
adb shell pm path com.tunnelworkshop.postern
adb pull /data/app/com.tunnelworkshop.postern-6pW_bRJGP95txOIXs-tQhA==/base.apk
```

## reinstall

```
adb shell pm clear com.package.foo
adb uninstall com.package.foo
adb install com.package.foo
```

https://stackoverflow.com/questions/12483720/adb-how-to-reinstall-an-app-without-retaining-the-data 

## analyze

https://androguard.readthedocs.io/en/latest/intro/gettingstarted.html
https://resources.infosecinstitute.com/android-penetration-tools-walkthrough-series-androguard/
https://androlyze.readthedocs.io/en/latest/index.html


# old apks

- uptodown.com
- apkpure.com
- androidapksfree.com
- apkmonk.com/
