import os
import time
import requests
import pytz
from datetime import datetime

# --- CONFIGURACIÓN ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def enviar_telegram(mensaje):
    if not TOKEN or not CHAT_ID: return
    
    # SISTEMA DE REINTENTOS ANTI-SATURACIÓN
    # Intentará 3 veces mandar el mensaje si la red falla
    max_intentos = 3
    for i in range(1, max_intentos + 1):
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
            response = requests.post(url, data=data, timeout=10) # 10s timeout
            
            if response.status_code == 200:
                print("✅ Mensaje entregado con éxito.")
                break # Éxito, salimos del bucle
            else:
                print(f"⚠️ Error Telegram (Intento {i}): {response.text}")
                time.sleep(5) # Esperar 5 seg antes de reintentar
                
        except Exception as e:
            print(f"❌ Fallo de conexión (Intento {i}): {e}")
            time.sleep(5)

def obtener_info_verificacion():
    tz_mx = pytz.timezone('America/Mexico_City')
    fecha_hoy = datetime.now(tz_mx)
    mes = fecha_hoy.month
    
    nombres_meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    nombre_mes = nombres_meses[mes].upper()
    
    info = ""
    # PRIMER SEMESTRE
    if mes == 1: info = "🟡 **Amarillo (5 y 6)**: Inicia periodo."
    elif mes == 2: info = "🚨 **Amarillo (5 y 6)**: ¡ÚLTIMOS DÍAS! Vence 28 Feb.\n🌸 **Rosa (7 y 8)**: Inicia periodo."
    elif mes == 3: info = "🚨 **Rosa (7 y 8)**: ¡ÚLTIMOS DÍAS! Vence 31 Mar.\n🔴 **Rojo (3 y 4)**: Inicia periodo."
    elif mes == 4: info = "🚨 **Rojo (3 y 4)**: ¡ÚLTIMOS DÍAS! Vence 30 Abr.\n🟢 **Verde (1 y 2)**: Inicia periodo."
    elif mes == 5: info = "🚨 **Verde (1 y 2)**: ¡ÚLTIMOS DÍAS! Vence 31 May.\n🔵 **Azul (9 y 0)**: Inicia periodo."
    elif mes == 6: info = "🚨 **Azul (9 y 0)**: ¡ÚLTIMOS DÍAS! Vence 30 Jun."
    # SEGUNDO SEMESTRE
    elif mes == 7: info = "🟡 **Amarillo (5 y 6)**: Inicia periodo (2do Semestre)."
    elif mes == 8: info = "🚨 **Amarillo (5 y 6)**: ¡ÚLTIMOS DÍAS! Vence 31 Ago.\n🌸 **Rosa (7 y 8)**: Inicia periodo."
    elif mes == 9: info = "🚨 **Rosa (7 y 8)**: ¡ÚLTIMOS DÍAS! Vence 30 Sep.\n🔴 **Rojo (3 y 4)**: Inicia periodo."
    elif mes == 10: info = "🚨 **Rojo (3 y 4)**: ¡ÚLTIMOS DÍAS! Vence 31 Oct.\n🟢 **Verde (1 y 2)**: Inicia periodo."
    elif mes == 11: info = "🚨 **Verde (1 y 2)**: ¡ÚLTIMOS DÍAS! Vence 30 Nov.\n🔵 **Azul (9 y 0)**: Inicia periodo."
    elif mes == 12: info = "🚨 **Azul (9 y 0)**: ¡ÚLTIMOS DÍAS! Vence 31 Dic."

    return nombre_mes, info

def main():
    mes_actual, detalle = obtener_info_verificacion()
    
    if detalle:
        mensaje = (
            f"📅 **CALENDARIO DE VERIFICACIÓN - {mes_actual}**\n\n"
            f"{detalle}\n\n"
            f"🚗 _Recuerda revisar multas y fotocívicas antes de agendar._"
        )
        enviar_telegram(mensaje)
    else:
        print("Sin avisos.")

if __name__ == "__main__":
    main()
