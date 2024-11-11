import os
import sqlite3
import json
import requests
import logging
from typing import Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CriteriaUpdater:
    def __init__(self, db_path: str, analyze_url: str):
        self.db_path = db_path
        self.analyze_url = analyze_url
        
    def get_all_records(self):
        """Get all records from database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT id, transcription FROM videos')
            return cursor.fetchall()
            
    def analyze_transcript(self, transcript: str) -> Optional[str]:
        """Get new criteria from API"""
        try:
            response = requests.post(
                self.analyze_url,
                headers={'Content-Type': 'application/json'},
                json={"transcription": transcript},
                timeout=60
            )
            
            if response.status_code != 200:
                logger.error(f"Error response: {response.text}")
                return None
                
            result = response.json()
            if 'criteria' in result:
                return json.dumps(result['criteria'], ensure_ascii=False, indent=2)
            return None
            
        except Exception as e:
            logger.error(f"Error analyzing transcript: {str(e)}")
            return None
            
    def update_criteria(self, video_id: int, criteria: str):
        """Update criteria in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    'UPDATE videos SET criteria = ? WHERE id = ?',
                    (criteria, video_id)
                )
            return True
        except Exception as e:
            logger.error(f"Error updating database: {str(e)}")
            return False
            
    def process_all(self):
        """Process all records"""
        records = self.get_all_records()
        logger.info(f"Found {len(records)} records to process")
        
        for video_id, transcript in records:
            logger.info(f"Processing video ID: {video_id}")
            
            # Get new criteria
            new_criteria = self.analyze_transcript(transcript)
            if not new_criteria:
                logger.error(f"Failed to get criteria for video {video_id}")
                continue
                
            # Update database
            if self.update_criteria(video_id, new_criteria):
                logger.info(f"Successfully updated criteria for video {video_id}")
            else:
                logger.error(f"Failed to update criteria for video {video_id}")

def main():
    # Configuration
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, 'video_database.db')
    ANALYZE_URL = 'http://localhost:25034/analyze'
    
    # Initialize and run updater
    updater = CriteriaUpdater(DB_PATH, ANALYZE_URL)
    updater.process_all()
    
    logger.info("Update process completed")

if __name__ == '__main__':
    main()