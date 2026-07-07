# Event manager system - Carolina Cecchi

**Project Type:** Full-Stack Web Application  
**Framework Used:** Django  

## Application description

This event manager system allows users to publicize and host their own events while providing a seamless way for others to search for and attend events.  At signup time, every user must chose one of the two roles implemented in the system: **Organizer** or **Attendee**.


Every organizer can:
- create, modify, delete events;
- see all their events;
- see the attendee list for each event.

Every attendee can:
- see all the events;
- register to an event / cancel their reservation;
- see all their current reservations.

## Local installation procedure

Follow these steps to set up and run the application locally:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder-name>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   * **Windows:** `venv\Scripts\activate`
   * **macOS/Linux:** `source venv/bin/activate`

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   The application will be accessible locally at `http://127.0.0.1:8000/`.

## Database and Demo accounts
This project includes a pre-populated **SQLite database** (`db.sqlite3`) filled with demo data for immediate testing and evaluation. 

The application core relies on three primary models:
- Event
- Registration
- CustomUser

### Demo accounts
- Attendee: user_demo / user12345
- Organizer: manager_demo / manager12345
- Admin: admin_demo / admin1234 (this is the superuser)

## Online deployment link
The live production version of this application can be accessed online here: [Deployment link]().
