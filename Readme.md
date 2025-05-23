## Web Playground
¡Bienvenido a Web Playground! Este es un sitio web dinámico y personalizable que permite a los usuarios crear y gestionar sus propias páginas, establecer y personalizar sus perfiles, y comunicarse con otros usuarios a través de un sistema de mensajería interno.

## 🚀 Características Principales
* Gestión de Páginas Personalizadas (pages):  
Cada usuario puede crear, editar y organizar sus propias páginas web dentro de la plataforma, personalizando su contenido.
* Autenticación y Registro (registration):  
- Registro de Usuarios: Proceso intuitivo para que nuevos usuarios se unan a la plataforma.
- Inicio y Cierre de Sesión: Gestión segura de sesiones de usuario.
- Recuperación de Contraseña: (Si aplica) Permite a los usuarios restablecer sus credenciales.
- Perfiles de Usuario Personalizables (profiles): Los usuarios pueden crear y gestionar sus propios perfiles, añadir información personal, fotos, y otros detalles relevantes.
- Sistema de Mensajería Interna (messenger): Chatea en tiempo real y envía mensajes privados a otros usuarios registrados en la plataforma.
- Funcionalidades Core (core): Módulo central que gestiona las funcionalidades esenciales y la lógica base del sitio.
  
## 🛠️ Tecnologías Utilizadas
* Este proyecto está construido principalmente con:

- Django: El framework web de Python que proporciona una base robusta y escalable.
- Python: El lenguaje de programación principal utilizado en el backend.
- HTML, CSS, JavaScript: Para la estructura, estilo e interactividad del frontend.
- Base de Datos: (Por favor, especifica aquí la base de datos que usas, por ejemplo: SQLite para desarrollo, PostgreSQL, MySQL, etc.)
  
## ⚙️ Instalación y Ejecución Local
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

Clona el repositorio:
Bash

git clone https://github.com/Mai-de-jerez/proyecto_avanzado_django.git
cd proyecto_avanzado_django/webplayground
Crea y activa un entorno virtual (muy recomendable):
Bash

python -m venv venv
source venv/bin/activate # En Linux/macOS
# venv\Scripts\activate # En Windows
Instala las dependencias del proyecto:
Bash

pip install -r requirements.txt
(Si no tienes un archivo requirements.txt, asegúrate de crearlo con pip freeze > requirements.txt o lista las dependencias principales que Django y tus apps necesitan).
Aplica las migraciones de la base de datos:
Bash

python manage.py migrate
Crea un superusuario (opcional, para acceder al panel de administración de Django):

```Bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para definir las credenciales.
Inicia el servidor de desarrollo:
Bash

python manage.py runserver
Abre tu navegador web y visita http://127.0.0.1:8000/.
🤝 Contribución
¡Nos encantaría que contribuyeras a este proyecto! Si deseas ayudar a mejorarlo:

Haz un "fork" de este repositorio.
Crea una nueva rama para tu característica o corrección: git checkout -b feature/nombre-de-tu-caracteristica
Realiza tus cambios y haz "commit" de ellos: git commit -m 'feat: Describe tu nueva funcionalidad o corrección'
Sube tus cambios a tu rama: git push origin feature/nombre-de-tu-caracteristica
Abre un "Pull Request" hacia la rama main de este repositorio.
Espero que esta versión te guste mucho más y sea realmente útil para tu proyecto. ¿Hay algo más que quieras añadir o modificar?


Fuentes





