import os
import json

with open("Packages", "r") as package_file:
	tweaks = package_file.read().split("\n\n")

def get_single_tweak(bundleID, important_info_list_only=False):
	for tweak in tweaks:
		if bundleID in tweak:
			if important_info_list_only:
				tweak = tweak.replace("\n", ": ").split(": ")
				del tweak[::2]
				return tweak
			return tweak

def get_all_tweaks(important_info_list_only=False):
	temp_tweaks = []
	for tweak in tweaks:
		if important_info_list_only:
			tweak = tweak.replace("\n", ": ").split(": ")
			del tweak[::2]
			temp_tweaks.append(tweak)
	if len(temp_tweaks) <= 0:
		return tweaks
	return temp_tweaks

def supported_version_from_desc(description):
	version = description.split("iOS ")[1]
	while not version[len(version)-1].isdigit(): version = version[:-1]
	while not version[0].isdigit(): version = version[1:]
	return version

def generate_tweak_info(important_tweak_list):
	tweak_info = {
		"name": important_tweak_list[12],
		"desc_short": important_tweak_list[10],
		"compatitle": "iOS %s" % supported_version_from_desc(important_tweak_list[10]),
		"changelog": "<strong>0.1</strong><br>+ Initial Release.<br>",
		"screenshot": "null"
	}
	return tweak_info


for tweak in get_all_tweaks(important_info_list_only=True):
	if len(tweak) <= 0:
		break
	tweak_packageinfo_filename = "packageInfo/%s" % tweak[0]
	if not os.path.exists(tweak_packageinfo_filename):
		print("Creating package info for %s..." % tweak[12])
		with open(tweak_packageinfo_filename, "a+") as tweak_file:
			json.dump(generate_tweak_info(tweak), tweak_file, indent=4, sort_keys=False)