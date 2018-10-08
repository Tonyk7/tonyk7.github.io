#!/bin/sh
# apt-ftparchive packages ./ > ./Packages
dpkg-scanpackages ./debs/ > Packages
sed -i -e '/^SHA/d' ./Packages
bzip2 -c9k ./Packages > ./Packages.bz2
printf "Origin: Tonyk7's Repo\nLabel: Tonyk7\nSuite: stable\nVersion: 1.0\nCodename: Tonyk7\nArchitecture: iphoneos-arm\nComponents: main\nDescription: Tonyk7's Tweaks\nmd5sum:\n "$(cat ./Packages | md5 -r | cut -d ' ' -f 1)" "$(stat -f%z Packages)" Packages\n "$(cat ./Packages.bz2 | md5 -r | cut -d ' ' -f 1)" "$(stat -f%z Packages.bz2)" Packages.bz2\n" >Release;
python3 generate_packageinfo.py
exit 0