import os
import time
import requests
import pytz
from datetime import datetime

# --- CONFIGURACIÓN ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# ENLACES OFICIALES DE MORELOS
LINK_CITAS = "https://airepuromorelos.com.mx/"
LINK_PAGOS = "http://hacienda.morelos.gob.mx/" # Portal de Hacienda Morelos para adeudos

def enviar_telegram(mensaje):
    if not TOKEN or not CHAT_ID: return
    for i in range(1, 4):
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = {
                "chat_id": CHAT_ID, 
                "text": mensaje, 
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            }
            r = requests.post(url, data=data, timeout=10)
            if r.status_code == 200: break
            time.sleep(5)
        except: time.sleep(5)

def obtener_info_verificacion():
    tz_mx = pytz.timezone('America/Mexico_City')
    fecha_hoy = datetime.now(tz_mx)
    mes = fecha_hoy.month
    
    nombres_meses = ["", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", 
                     "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    nombre_mes = nombres_meses[mes]
    
    vence = ""
    inicia = ""

    # Calendario Morelos (Homologado con la CAMe)
    if mes == 1 or mes == 7:
        inicia = "🟡 <b>Engomado Amarillo</b> (Placas 5 y 6)"
    elif mes == 2 or mes == 8:
        vence = "🟡 <b>Engomado Amarillo</b> (Placas 5 y 6)"
        inicia = "🌸 <b>Engomado Rosa</b> (Placas 7 y 8)"
    elif mes == 3 or mes == 9:
        vence = "🌸 <b>Engomado Rosa</b> (Placas 7 y 8)"
        inicia = "🔴 <b>Engomado Rojo</b> (Placas 3 y 4)"
    elif mes == 4 or mes == 10:
        vence = "🔴 <b>Engomado Rojo</b> (Placas 3 y 4)"
        inicia = "🟢 <b>Engomado Verde</b> (Placas 1 y 2)"
    elif mes == 5 or mes == 11:
        vence = "🟢 <b>Engomado Verde</b> (Placas 1 y 2)"
        inicia = "🔵 <b>Engomado Azul</b> (Placas 9 y 0)"
    elif mes == 6 or mes == 12:
        vence = "🔵 <b>Engomado Azul</b> (Placas 9 y 0)"

    return nombre_mes, vence, inicia

def main():
    mes_nombre, vence, inicia = obtener_info_verificacion()
    
    msg = f"📡 <i>Sincronizando calendario de emisiones y trámites (Morelos)...</i>\n\n"
    msg += f"📅 <b>CALENDARIO MORELOS: {mes_nombre} 2026</b>\n"
    msg += "──────────────────\n"

    if vence:
        msg += f"🚨 <b>FECHA LÍMITE (Vence este mes):</b>\n{vence}\n\n"
    
    if inicia:
        msg += f"✨ <b>INICIA PERIODO:</b>\n{inicia}\n\n"

    msg += "📝 <b>PASOS PARA MORELOS:</b>\n"
    msg += f"1. Verifica adeudos de Tenencia/Multas:\n<a href='{LINK_PAGOS}'>Portal de Hacienda Morelos</a>\n"
    msg += "2. No tener infracciones pendientes.\n\n"
    
    msg += f"<b>🗓️ AGENDAR CITA (Morelos):</b>\n<a href='{LINK_CITAS}'>Aire Puro Morelos</a>\n"
    msg += "──────────────────\n"
    msg += "<i>Evita la multa por verificación extemporánea en el estado.</i>"

    enviar_telegram(msg)

if __name__ == "__main__":
    main()
