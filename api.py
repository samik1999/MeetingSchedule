from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Initialize database connection
def get_db_connection():
    conn = sqlite3.connect('scheduler.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.json
    title = data['title']
    start_time = datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M:%S')
    room_id = data.get('room_id')
    participants = data['participants']
    
    conn = get_db_connection()
    
    # Check room availability
    if room_id:
        cursor = conn.execute('''
            SELECT * FROM Meetings WHERE room_id = ? AND 
            (start_time < ? AND end_time > ?)
        ''', (room_id, end_time, start_time))
        if cursor.fetchone():
            return jsonify({"error": "Room is not available"}), 400
    
    # Check participants availability
    for participant in participants:
        cursor = conn.execute('''
            SELECT * FROM Meetings WHERE creator_id = ? AND 
            (start_time < ? AND end_time > ?)
        ''', (participant, end_time, start_time))
        if cursor.fetchone():
            return jsonify({"error": f"Participant {participant} is not available"}), 400
    
    # Insert meeting
    conn.execute('''
        INSERT INTO Meetings (title, start_time, end_time, room_id, creator_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, start_time, end_time, room_id, request.json['creator_id']))
    
    # Insert participants
    meeting_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    for participant in participants:
        conn.execute('''
            INSERT INTO Participants (meeting_id, user_id)
            VALUES (?, ?)
        ''', (meeting_id, participant))
    
    conn.commit()
    conn.close()
    
    return jsonify({"status": "Meeting scheduled successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
