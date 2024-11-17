import subprocess
import os

# WebDAV-Server-Details
username = "christopher.schieszl"
password = "60145720210430"
base_url = "https://cloud.bulme.at/remote.php/webdav/"
folder_name = "ownCloudCloudUploads"
file_path = r"C:\Users\chris\OneDrive\Desktop\Private\owncloud"


# 1. Ordner auf dem WebDAV-Server erstellen
def create_webdav_folder():
    create_folder_cmd = [
        "curl",
        "-u", f"{username}:{password}",
        "-X", "MKCOL",
        f"{base_url}{folder_name}/"
    ]
    try:
        print("Erstelle Ordner auf dem WebDAV-Server...")
        result = subprocess.run(create_folder_cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("Ordner erfolgreich erstellt!")
        else:
            print(f"Fehler beim Erstellen des Ordners: {result.stderr}")
    except Exception as e:
        print(f"Fehler: {e}")


# 2. Rekursiv alle Dateien und Unterordner hochladen
def upload_files_to_webdav(local_dir, remote_dir):
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_file_path = os.path.join(root, file)
            remote_file_path = os.path.join(remote_dir, os.path.relpath(local_file_path, local_dir))

            # Entferne den Windows-Pfad von der relativen Datei und ersetze \ durch /
            remote_file_path = remote_file_path.replace(os.sep, "/")

            upload_file_cmd = [
                "curl",
                "-u", f"{username}:{password}",
                "-T", local_file_path,
                f"{base_url}{remote_file_path}"
            ]
            try:
                print(f"Lade Datei hoch: {local_file_path} -> {remote_file_path}")
                result = subprocess.run(upload_file_cmd, capture_output=True, text=True)
                print(result.stdout)
                if result.returncode == 0:
                    print(f"Datei erfolgreich hochgeladen: {local_file_path}")
                else:
                    print(f"Fehler beim Hochladen der Datei {local_file_path}: {result.stderr}")
            except Exception as e:
                print(f"Fehler beim Hochladen der Datei {local_file_path}: {e}")


# Hauptprogramm
if __name__ == "__main__":
    create_webdav_folder()
    upload_files_to_webdav(file_path, folder_name)
