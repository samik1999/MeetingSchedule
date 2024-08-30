import argparse
import requests

def schedule_meeting():
    parser = argparse.ArgumentParser(description='Schedule a meeting.')
    parser.add_argument('--title', required=True, help='Title of the meeting')
    parser.add_argument('--start_time', required=True, help='Start time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('--end_time', required=True, help='End time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('--room_id', type=int, help='Room ID')
    parser.add_argument('--creator_id', required=True, type=int, help='Creator ID')
    parser.add_argument('--participants', nargs='+', required=True, help='List of participant IDs')
    
    args = parser.parse_args()
    
    response = requests.post('http://localhost:5000/schedule', json={
        'title': args.title,
        'start_time': args.start_time,
        'end_time': args.end_time,
        'room_id': args.room_id,
        'creator_id': args.creator_id,
        'participants': list(map(int, args.participants))
    })
    
    print(response.json())

if __name__ == '__main__':
    schedule_meeting()
