# To-Do List

A web-based To-Do List application built with **Django**. This website allows you to manage your tasks efficiently through a clean and intuitive interface.

## How to run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/to-do-list.git
   cd to-do-list
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

   Once started, you can access the website at `http://localhost:8000`

## Deployment

The website is available on Railway at: https://django-todo-list-production.up.railway.app/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


