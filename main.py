import os
import time
import requests
import pytz
from datetime import datetime

# --- CONFIGURACIÓN ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

LINK_CITAS = "https://verificentros.sedema.cdmx.gob.mx/DVC/"
LINK_MULTAS = "https://tramites.cdmx.gob.mx/infracciones/"

def enviar_telegram(mensaje):
    if not TOKEN or not CHAT_ID: return
    # Sistema de reintentos profesional
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

    # Lógica de Semestres (Mismos colores para ambos periodos)
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
    
    # --- CONSTRUCCIÓN DEL MENSAJE (Estilo System Log) ---
    msg = f"📡 <i>Sincronizando calendario de emisiones y trámites vehiculares...</i>\n\n"
    msg += f"📅 <b>CALENDARIO: {mes_nombre} 2026</b>\n"
    msg += "──────────────────\n"

    if vence:
        msg += f"🚨 <b>FECHA LÍMITE (Vence este mes):</b>\n{vence}\n\n"
    
    if inicia:
        msg += f"✨ <b>INICIA PERIODO:</b>\n{inicia}\n\n"

    msg += "📝 <b>REQUISITOS CLAVE:</b>\n"
    msg += f"• No tener adeudos: <a href='{LINK_MULTAS}'>Consultar Multas aquí</a>\n"
    msg += "• Estar al corriente con la Tenencia.\n\n"
    
    msg += f"<b>🗓️ AGENDAR CITA:</b>\n<a href='{LINK_citas}'>Sistema de Verificentros CDMX</a>\n"
    msg += "──────────────────\n"
    msg += "<i>Evita multas por verificación extemporánea ($2,171+ MXN).</i>"

    enviar_telegram(msg)

if __name__ == "__main__":
    main()
