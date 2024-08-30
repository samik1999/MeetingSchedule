Meeting Scheduling System
Overview
The Meeting Scheduling System allows users to schedule meetings with options for room bookings and participant management. It features collision detection to prevent scheduling conflicts.

Features
Schedule a Meeting: Create meetings by specifying the date, time, room, and participants.
Collision Detection: Automatically checks for scheduling conflicts for rooms and participants.
Multiple Participant Support: Schedule meetings with multiple participants.
Room Booking: Book specific rooms for meetings.
Getting Started
Prerequisites
Python 3.x
Flask
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/samik1999/meeting-scheduler.git
cd meeting-scheduler
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install Flask
Set up the database:

bash
Copy code
sqlite3 scheduler.db < schema.sql
Run the Flask application:

bash
Copy code
python app.py
Usage
Schedule a Meeting:
bash
Copy code
curl -X POST http://localhost:5000/schedule \
-H "Content-Type: application/json" \
-d '{
  "title": "Team Meeting",
  "start_time": "2024-09-01 10:00:00",
  "end_time": "2024-09-01 11:00:00",
  "room_id": 1,
  "creator_id": 1,
  "participants": [2, 3]
}'
Database Schema
Users: Stores user information.
Rooms: Stores information about available meeting rooms.
Meetings: Stores scheduled meetings, including title, start/end time, room, and creator.
Participants: Stores the relationship between meetings and participants.
