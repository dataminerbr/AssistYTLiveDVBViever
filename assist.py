import sys
import subprocess

# Pega URL do stream usando yt-dlp
def pegar_stream(url):
    try:
        resultado = subprocess.run(
            ["yt-dlp.exe", "-g", "-f", "best", url],
            capture_output=True,
            text=True
        )

        if resultado.returncode != 0:
            print("Error running yt-dlp:")
            return None

        return resultado.stdout.strip()

    except FileNotFoundError:
        print("\nERROR: yt-dlp was not found on this system.")
        print("Please download yt-dlp and place yt-dlp.exe in the same folder as this program.")
        print("Download link: https://github.com/yt-dlp/yt-dlp/releases/latest\n")
        sys.exit(1)

    except Exception as e:
        print("Unexpected error:", e)
        return None


# Abre no DVBViewer
def abrir_no_dvbviewer(url):
    caminho_dvbviewer = r"C:\Program Files (x86)\DVBViewer\DVBViewer.exe"
    subprocess.run(['start', '', caminho_dvbviewer, url], shell=True)


def main():

    if len(sys.argv) >= 2:
        entrada = sys.argv[1].strip()
    else:
        entrada = input("Enter the username '@SkyNews' or the live stream link: ").strip()

    # Detecta se é usuario ou link
    if entrada.startswith("@"):
        url = f"https://www.youtube.com/{entrada}/live"
    elif entrada.startswith("http"):
        url = entrada
    else:
        print("Invalid entry. Use @channel or live stream link.")
        sys.exit(1)

    print("Obtaining stream with yt-dlp...")
    stream = pegar_stream(url)

    if stream:
        #print(f"Stream found: {stream}")
        abrir_no_dvbviewer(stream)
    else:
        print("The stream could not be obtained.")
        sys.exit(1)


if __name__ == "__main__":
    main()