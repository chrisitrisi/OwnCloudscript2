import subprocess

# WebDAV-Server-Details
username = "christopher.schieszl"
password = "60145720210430"
base_url = "https://cloud.bulme.at/remote.php/webdav/"
folder_name = "ownCloudCloudUploads"
file_path = r"C:\Users\chris\OneDrive\Desktop\Private\owncloud\ownCloud_Manual.pdf"

# 1. Ordner auf dem WebDAV-Server erstellen
def create_webdav_folder():
    create_folder_cmd = [
        "curl",
        "-u", f"{username}:{password}",
        "-X", "MKCOL",
        f"{base_url}{folder_name}/"
    ]
    try:
        print("Erstelle Ordner...")
        result = subprocess.run(create_folder_cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("Ordner erfolgreich erstellt!")
        else:
            print(f"Fehler beim Erstellen des Ordners: {result.stderr}")
    except Exception as e:
        print(f"Fehler: {e}")

# 2. Datei auf den WebDAV-Server hochladen
def upload_file_to_webdav():
    upload_file_cmd = [
        "curl",
        "-u", f"{username}:{password}",
        "-T", file_path,
        f"{base_url}{folder_name}/"
    ]
    try:
        print("Lade Datei hoch...")
        result = subprocess.run(upload_file_cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("Datei erfolgreich hochgeladen!")
        else:
            print(f"Fehler beim Hochladen der Datei: {result.stderr}")
    except Exception as e:
        print(f"Fehler: {e}")

# Hauptprogramm
if __name__ == "__main__":
    create_webdav_folder()
    upload_file_to_webdav()
