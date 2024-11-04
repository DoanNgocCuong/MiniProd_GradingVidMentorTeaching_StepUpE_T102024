import sqlite3

# Kết nối đến database
conn = sqlite3.connect('video_database.db')
cursor = conn.cursor()

# Thực thi các câu lệnh SQL từ file trên
cursor.execute('''
CREATE TABLE IF NOT EXISTS video_transcripts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_url TEXT NOT NULL, 
    transcription TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_video_url ON video_transcripts(video_url)
''')

cursor.execute('''
INSERT INTO video_transcripts (video_url, transcription)
VALUES (
    'https://drive.google.com/file/d/10qe6DkNX6up7-oG69HRG3B4j1A-WiI_o/view',
    '[00:00:00] Speaker 1: Okay, so the day before, we solved that problem together.
[00:00:07] Speaker 1: We... Alright, how do I say?
[00:00:10] Speaker 1: We expanded ideas for the Vietnam Food Contest, right?
[00:00:15] Speaker 1: Yes, okay.
[00:00:16] Speaker 1: So after that day, when I got home, I had time to online or when I was preparing a new song.
[00:00:41] Speaker 1: Or do you know how to prepare it?
[00:00:44] Speaker 1: I still have to answer.
[00:00:46] Speaker 1: But when you read a question, you need to think a little bit further.
[00:00:52] Speaker 1: Like, okay, how do I need to explain the answer?
[00:00:55] Speaker 1: Is that okay?
[00:01:04] Speaker 1: For A1, the requirement will be lower, so it will only go that far.
[00:01:12] Speaker 1: We still need more content later.
[00:01:24] Speaker 1: Okay, for this sentence, after I answer like this, what should I answer next?
[00:01:29] Speaker 1: Something like that, okay?
[00:01:30] Speaker 1: And in front of your eyes, I will only ask you to give me one more answer.
[00:01:37] Speaker 1: That is, your total answer will be two small sentences, okay?
[00:01:48] Speaker 1: Okay, so as a local from Hanoi, you are meeting your foreign friend who is visiting Vietnam for the very first time.
[00:02:02] Speaker 1: Okay, and I will ask you about Vietnamese cuisine.
[00:02:05] Speaker 1: You got it?
[00:02:07] Speaker 1: Yes, okay, so are you ready for the conversation together?
[00:02:16] Speaker 1: Okay, so why are you smiling?
[00:02:26] Speaker 1: Okay, so bây giờ cái chị cần nói là mình sẽ có phần conversation và chị sẽ dựa vào những câu hỏi ở trên đây nhé.
[00:03:28] Speaker 1: Yes, okay, so how much does this cost?
[00:03:41] Speaker 1: Okay, 50 or 15?
[00:03:44] Speaker 2: Fifty.
[00:03:45] Speaker 1: Okay, 50.
[00:03:46] Speaker 2: Under 50.
[00:03:46] Speaker 1: Okay.
[00:03:47] Speaker 1: Yes.
[00:03:47] Speaker 1: Okay.
[00:03:48] Speaker 1: So do you think that the price is different when you buy in different places?

[00:28:49] Speaker 1: Đó, mình có từ atmosphere nữa ấy.
[00:28:52] Speaker 1: Được không ạ?
[00:28:53] Speaker 2: Yeah.
[00:28:54] Speaker 1: Okay, rồi, good.
[00:28:56] Speaker 1: Nice.
[00:28:56] Speaker 1: Okay, thế thì mình đã nắm được phần homework của mình chưa ạ?
[00:29:00] Speaker 2: No, I... Well, goodbye.
[00:29:00] Speaker 1: Okay, rồi, thế thì chị hẹn Kim Anh vào thứ 7 tuần này nhé.
[00:29:03] Speaker 1: Alright?
[00:29:05] Speaker 1: Yes, okay, so, yes, thank you and goodbye.
[00:29:07] Speaker 2: I did you.
[00:29:08] Speaker 1: See you.
[00:29:09] Speaker 1: Bye-bye.'
)
''')

# Lưu thay đổi
conn.commit()

# Đóng kết nối
conn.close()



