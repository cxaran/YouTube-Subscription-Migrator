### README - YouTube Subscription Migrator

---

## Descripción en Español

**YouTube Subscription Migrator** es una herramienta en Python diseñada para ayudarte a migrar tus suscripciones de YouTube de una cuenta a otra. Con esta herramienta, puedes exportar las suscripciones de tu cuenta actual a un archivo de texto y luego suscribirte automáticamente a esos mismos canales desde otra cuenta de YouTube.

### Características

- **Exportación de Suscripciones**: Guarda todas las suscripciones actuales de tu cuenta de YouTube en un archivo de texto (`canales_subscritos.txt`).
- **Migración de Suscripciones**: Usa el archivo generado (`canales_subscritos.txt`) para suscribirte automáticamente a esos canales desde una nueva cuenta de YouTube.

### Requisitos

1. **Creación del Archivo `client_secret.json`**:
   - Crea un proyecto en [Google Cloud Console](https://console.cloud.google.com/) y habilita la API de YouTube Data v3.
   - Genera un nuevo archivo de credenciales `client_secret.json` desde la consola de Google Cloud. Este archivo contendrá tu **Client ID** y **Client Secret** necesarios para la autenticación.
   - Descarga el archivo `client_secret.json` y colócalo en el directorio del proyecto.

2. **Python 3.x**
3. **Dependencias de Python**:
   - `google-auth-oauthlib`
   - `google-auth`
   - `google-api-python-client`

### Instalación

1. Clona este repositorio o descarga el archivo ZIP y extrae el contenido.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```

4. **Configuración de la API de YouTube y Auth0**:

   - Si estás utilizando Auth0 para gestionar la autenticación, asegúrate de que las credenciales de Auth0 estén correctamente configuradas en tu archivo `client_secret.json`. Esto puede implicar descargar o crear un nuevo cliente en Auth0 y actualizar `client_secret.json` con la información de **Client ID** y **Client Secret** proporcionada por Auth0.

### Uso

1. Ejecuta el script:

   ```bash
   python youtube_subscription_migrator.py
   ```

2. Autentícate en tu cuenta de YouTube a través de la interfaz que se abrirá en tu navegador.

3. Selecciona la opción deseada:
   - **Opción 1**: Exportar tus suscripciones actuales a `canales_subscritos.txt`.
   - **Opción 2**: Suscribirse a los canales listados en `canales_subscritos.txt` desde otra cuenta.

### Migración de Suscripciones de una Cuenta a Otra

Para migrar tus suscripciones de YouTube de una cuenta a otra, sigue estos pasos:

1. **Exportar Suscripciones desde la Cuenta Original**:
   - Ejecuta el script con la cuenta de YouTube desde la que deseas exportar las suscripciones.
   - Selecciona la opción 1 para guardar las suscripciones en `canales_subscritos.txt`.

2. **Importar Suscripciones en la Nueva Cuenta**:
   - Inicia sesión en la nueva cuenta de YouTube.
   - Ejecuta el script nuevamente y selecciona la opción 2 para suscribirte automáticamente a los canales listados en `canales_subscritos.txt`.

---

## Description in English

**YouTube Subscription Migrator** is a Python tool designed to help you migrate your YouTube subscriptions from one account to another. With this tool, you can export your current YouTube subscriptions to a text file and then automatically subscribe to those same channels from another YouTube account.

### Features

- **Subscription Export**: Save all your current YouTube subscriptions to a text file (`canales_subscritos.txt`).
- **Subscription Migration**: Use the generated file (`canales_subscritos.txt`) to automatically subscribe to those channels from a new YouTube account.

### Requirements

1. **Create the `client_secret.json` File**:
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/) and enable the YouTube Data API v3.
   - Generate a new `client_secret.json` credentials file from the Google Cloud Console. This file will contain your **Client ID** and **Client Secret** needed for authentication.
   - Download the `client_secret.json` file and place it in the project directory.

2. **Python 3.x**
3. **Python Dependencies**:
   - `google-auth-oauthlib`
   - `google-auth`
   - `google-api-python-client`

### Installation

1. Clone this repository or download the ZIP file and extract the contents.
2. Navigate to the project directory.
3. Install the necessary dependencies by running:

   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```

4. **YouTube API and Auth0 Setup**:

   - If you are using Auth0 for authentication management, ensure your Auth0 credentials are correctly configured in your `client_secret.json`. This may involve downloading or creating a new client in Auth0 and updating your `client_secret.json` with the **Client ID** and **Client Secret** provided by Auth0.

### Usage

1. Run the script:

   ```bash
   python youtube_subscription_migrator.py
   ```

2. Authenticate with your YouTube account through the interface that will open in your browser.

3. Choose the desired option:
   - **Option 1**: Export your current subscriptions to `canales_subscritos.txt`.
   - **Option 2**: Subscribe to the channels listed in `canales_subscritos.txt` from another account.

### Migrating Subscriptions from One Account to Another

To migrate your YouTube subscriptions from one account to another, follow these steps:

1. **Export Subscriptions from the Original Account**:
   - Run the script with the YouTube account from which you want to export the subscriptions.
   - Choose option 1 to save the subscriptions to `canales_subscritos.txt`.

2. **Import Subscriptions into the New Account**:
   - Sign in to the new YouTube account.
   - Run the script again and choose option 2 to automatically subscribe to the channels listed in `canales_subscritos.txt`.
