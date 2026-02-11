# 🚗 Bot de Verificación Vehicular

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![Region](https://img.shields.io/badge/Config-Morelos-green)

Este bot automatiza los recordatorios del calendario de verificación vehicular, notificando semanalmente qué engomados inician periodo y cuáles están por vencer. 

---

## 🧠 Inteligencia de Monitoreo

El sistema está configurado actualmente con la lógica y portales oficiales del estado de **Morelos**, aunque mantiene un lenguaje visual discreto y profesional en sus reportes para integrarse con otros bots de movilidad.

### Configuración Actual:
* **Estado:** Morelos.
* **Sistema de Citas:** Aire Puro Morelos.
* **Portal de Pagos:** Hacienda del Estado de Morelos (Tenencia y Multas).
* **Frecuencia:** Todos los **lunes a las 8:05 AM CDMX** (14:05 UTC).

---

## ⚡ Cómo cambiar el bot a otro Estado (Ej. CDMX o Edomex)

Si deseas utilizar este bot para una entidad distinta a Morelos, solo debes realizar los siguientes cambios en el archivo `main.py`:

1. **Actualizar Enlaces Oficiales:**
   Busca la sección de configuración al inicio del código y reemplaza las URLs:
   ```python
   LINK_CITAS = "URL_SISTEMA_CITAS_NUEVO"
   LINK_PAGOS = "URL_PORTAL_ADEUDOS_NUEVO"

   Validar el Calendario: Aunque la mayoría de los estados de la CAMe comparten el mismo calendario, verifica la función obtener_info_verificacion() por si existiera alguna prórroga específica en el nuevo estado.

Ajustar Requisitos: Puedes editar la lista de pasos en la sección 📝 PASOS A SEGUIR dentro de la función main() para incluir menciones a Fotocívicas o reglamentos locales.

🚀 Instalación y Despliegue
Este bot funciona de forma 100% gratuita mediante GitHub Actions.

Realiza un Fork de este repositorio.

Configura tus secretos en Settings > Secrets and variables > Actions:

TELEGRAM_TOKEN: El token de tu bot de @BotFather.

TELEGRAM_CHAT_ID: Tu ID de chat personal.

Habilita los flujos de trabajo en la pestaña Actions.

Nota: El bot se ejecutará automáticamente con cada Push que realices al código y de forma programada cada inicio de semana.

📸 Ejemplo de Notificación
📡 Sincronizando calendario de emisiones y trámites vehiculares...

📅 CALENDARIO: FEBRERO 2026 ────────────────── 🚨 FECHA LÍMITE (Vence este mes): 🟡 Engomado Amarillo (Placas 5 y 6)

✨ INICIA PERIODO: 🌸 Engomado Rosa (Placas 7 y 8)

📝 PASOS A SEGUIR:

Verificar adeudos de Tenencia/Multas.

Confirmar que no existan infracciones pendientes.

🗓️ AGENDAR CITA: [Enlace al Sistema de Verificación] ──────────────────

<p align="center"> <i>Evita multas extemporáneas con monitoreo preventivo. 🚗</i> </p>
