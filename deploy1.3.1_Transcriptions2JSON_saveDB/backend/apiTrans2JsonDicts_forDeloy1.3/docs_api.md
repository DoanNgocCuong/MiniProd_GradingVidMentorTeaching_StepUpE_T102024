```bash
curl --location 'http://localhost:5000/analyze' \
--header 'Content-Type: application/json' \
--data '{"transcription": "[00:04:15] Mentee: Oh, good afternoon.\n[00:04:32] Mentor: Hello.\n[00:04:35] Mentor: Good afternoon."}'
```


=========
Output: 

{critical: {...}}