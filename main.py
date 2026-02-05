import os
import requests
import pytz
from datetime import datetime

# --- CONFIGURACIÓN ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def enviar_telegram(mensaje):
    if not TOKEN or not CHAT_ID: return
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        # Usamos Markdown para negritas y formato limpio
        data = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error enviando mensaje: {e}")

def obtener_info_verificacion():
    tz_mx = pytz.timezone('America/Mexico_City')
    fecha_hoy = datetime.now(tz_mx)
    mes = fecha_hoy.month
    
    # Mapeo de meses
    nombres_meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    nombre_mes = nombres_meses[mes].upper()

    # --- LÓGICA DEL CALENDARIO CDMX ---
    # Formato: "Mensaje de alerta"
    
    info = ""
    
    if mes == 1: # Enero
        info = "🟡 **Amarillo (5 y 6)**: Inicia periodo de verificación."
    elif mes == 2: # Febrero
        info = "🚨 **Amarillo (5 y 6)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🌸 **Rosa (7 y 8)**: Inicia periodo."
    elif mes == 3: # Marzo
        info = "🚨 **Rosa (7 y 8)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🔴 **Rojo (3 y 4)**: Inicia periodo."
    elif mes == 4: # Abril
        info = "🚨 **Rojo (3 y 4)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🟢 **Verde (1 y 2)**: Inicia periodo."
    elif mes == 5: # Mayo
        info = "🚨 **Verde (1 y 2)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🔵 **Azul (9 y 0)**: Inicia periodo."
    elif mes == 6: # Junio
        info = "🚨 **Azul (9 y 0)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes."
        
    # --- SEGUNDO SEMESTRE ---
    elif mes == 7: # Julio
        info = "🟡 **Amarillo (5 y 6)**: Inicia periodo (2do Semestre)."
    elif mes == 8: # Agosto
        info = "🚨 **Amarillo (5 y 6)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🌸 **Rosa (7 y 8)**: Inicia periodo."
    elif mes == 9: # Septiembre
        info = "🚨 **Rosa (7 y 8)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🔴 **Rojo (3 y 4)**: Inicia periodo."
    elif mes == 10: # Octubre
        info = "🚨 **Rojo (3 y 4)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🟢 **Verde (1 y 2)**: Inicia periodo."
    elif mes == 11: # Noviembre
        info = "🚨 **Verde (1 y 2)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes.\n🔵 **Azul (9 y 0)**: Inicia periodo."
    elif mes == 12: # Diciembre
        info = "🚨 **Azul (9 y 0)**: ¡ÚLTIMOS DÍAS! Vence a fin de mes."

    return nombre_mes, info

def main():
    mes_actual, detalle = obtener_info_verificacion()
    
    if detalle:
        mensaje = (
            f"📅 **CALENDARIO DE VERIFICACIÓN - {mes_actual}**\n\n"
            f"{detalle}\n\n"
            f"🚗 _Recuerda revisar que no tengas multas antes de ir._"
        )
        enviar_telegram(mensaje)
        print("✅ Aviso enviado.")
    else:
        print("No hay avisos programados para este mes.")

if __name__ == "__main__":
    main()
