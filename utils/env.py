import os

base_url = os.getenv("BASE_URL", "http://fastapi-service:8000/")
base_url_ui = os.getenv("BASE_URL_UI", "https://pythoninventory-st.streamlit.app/")
admin_username = os.getenv("ADMIN_USERNAME", "testuser")
admin_password = os.getenv("ADMIN_PASSWORD", "secret")
view_username = os.getenv("VIEW_USERNAME", "testuser2")
view_password = os.getenv("VIEW_PASSWORD", "secret")  