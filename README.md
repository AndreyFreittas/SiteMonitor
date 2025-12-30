# 🛠️ SiteMonitor

Uma ferramenta simples em **Python** para verificar se um site está online e mostrar o **status HTTP** retornado.  
Esse script pode ser útil para monitorar disponibilidade de sites ou aprender sobre requisições web em Python.

---

## 📌 Descrição

O **SiteMonitor** solicita uma URL ao usuário, faz uma requisição HTTP e exibe se o site está ativo ou não, além de interpretar os principais códigos de resposta (como 200, 403, 404, 503).  
Ideal para estudos de networking, scripts CLI ou projetos de automação.  

---

## 🚀 Funcionalidades

✔ Verifica se o site está online  
✔ Exibe status HTTP mais comuns  
✔ Tratamento de erros de conexão e formato de URL  
✔ Fácil de usar e modificar

---

## 🧰 Tecnologias

- Python 3.x  
- Biblioteca `requests`  
- Biblioteca `pyfiglet`

---

## 📥 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/xyzfreitas/SiteMonitor.git
cd SiteMonitor
pip install -r requirements.txt
pip install requests pyfiglet
```

## ▶️ Como usar

Execute o script com o Python:
```bash
python site_monitor.py
```
Digite a URL que deseja verificar (ex: https://example.com) quando solicitado.
