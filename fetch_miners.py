import os
import requests

os.system("rm -rf tmp* linux windows; mkdir tmp_l tmp_w linux windows")

github_releases = {
    "nanominer": "https://api.github.com/repos/nanopool/nanominer/releases/latest",
    "lolminer": "https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest",
    "gminer": "https://api.github.com/repos/develsoftware/GMinerRelease/releases/latest",
    "rigel": "https://api.github.com/repos/rigelminer/rigel/releases/latest",
}

for miner, url in github_releases.items():
    download_url = ""
    miner_filename = ""
    data = requests.get(url)
    for asset in data.json()["assets"]:
        if "lin" in asset["name"].lower():
            archive_extension = asset["name"].split(".")[-1]
            download_url = asset["browser_download_url"]
            miner_archive = requests.get(download_url)
            with open(f"{miner}.{archive_extension}", "wb") as miner_file:
                miner_file.write(miner_archive.content)
            os.system(f"tar -xf {miner}.{archive_extension} -C tmp_l/")
            os.system(f"rm -rf {miner}.{archive_extension}")
            print(f"Downloaded {miner}.{archive_extension}")

        if "win" in asset["name"].lower():
            archive_extension = asset["name"].split(".")[-1]
            download_url = asset["browser_download_url"]
            miner_archive = requests.get(download_url)
            with open(f"{miner}.{archive_extension}", "wb") as miner_file:
                miner_file.write(miner_archive.content)
            os.system(f"unzip -q {miner}.{archive_extension} -d tmp_w/")
            os.system(f"rm -rf {miner}.{archive_extension}")
            print(f"Downloaded {miner}.{archive_extension}")

os.system('find tmp_l -name "nanominer" -exec cp {} linux/nanom \;')
os.system('find tmp_l -name "lolMiner" -exec cp {} linux/lolm \;')
os.system('find tmp_l -name "miner" -exec cp {} linux/gmnr \;')
os.system('find tmp_l -name "rigel" -exec cp {} linux/rgmnr \;')
os.system("rm -rf tmp_l")

os.system('find tmp_w -name "nanominer.exe" -exec cp {} windows/nanom.exe \;')
os.system('find tmp_w -name "lolMiner.exe" -exec cp {} windows/lolm.exe \;')
os.system('find tmp_w -name "miner.exe" -exec cp {} windows/gmnr.exe \;')
os.system('find tmp_w -name "rigel.exe" -exec cp {} windows/rgmnr.exe \;')
os.system('find tmp_w -name "*.dll" -exec cp {} windows/ \;')
os.system("rm -rf tmp_w")
