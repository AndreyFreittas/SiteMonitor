import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Verificar Site")
print(ascii_banner)
print("by AndreyFreittas (4Study)")
print("[!] Coloque o site abaixo (ex: https://example.com)\n")

url = input(" > ").strip()

try:
    resposta = requests.get(url, timeout=10)
    status = resposta.status_code

    if status == 200:
        print("[+] Site online (200 OK)")
    elif status in [301, 302]:
        print(f"[!] Redirecionamento detectado ({status})")
    elif status == 403:
        print("[!] Acesso proibido (403 Forbidden)")
    elif status == 404:
        print("[!] Página não encontrada (404)")
    elif status == 500:
        print("[!] Erro interno do servidor (500)")
    elif status == 503:
        print("[!] Serviço indisponível (503)")
    else:
        print(f"[?] Código de status retornado: {status}")

except requests.exceptions.MissingSchema:
    print("[X] URL inválida. Use http:// ou https://")

except requests.exceptions.ConnectionError:
    print("[X] Erro de conexão. O site pode estar offline.")

except requests.exceptions.Timeout:
    print("[X] Tempo de conexão excedido.")

except requests.exceptions.RequestException as erro:
    print(f"[X] Erro inesperado: {erro}")
