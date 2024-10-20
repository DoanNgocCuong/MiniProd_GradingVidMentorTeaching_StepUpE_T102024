document.getElementById('loadVideo').addEventListener('click', async () => {
    const videoLink = document.getElementById('videoLink').value;
    const videoId = getVideoId(videoLink);
    
    if (videoId) {
        // Update the video player
        const videoSrc = `https://drive.google.com/file/d/${videoId}/preview`;
        document.getElementById('video').src = videoSrc;

        // Call the function to generate transcript
        // const transcript = await generateTranscript(videoId);
        updateTranscript(transcript);
    } else {
        alert('Invalid video link. Please provide a valid Google Drive link.');
    }
});

// Function to extract video ID from Google Drive link
function getVideoId(link) {
    const match = link.match(/[-\w]{25,}/);
    return match ? match[0] : null;
}

// Function to call the custom API to generate transcript
async function generateTranscript(videoId) {
    const formData = new FormData();
    // Assuming you have the audio file available, replace with actual audio file
    const audioFile = new File([""], "Mentee.m4a", { type: "audio/m4a" });
    formData.append("audio", audioFile);
    formData.append("secret_key", "codedongian");
    formData.append("language", "en");

    try {
        const response = await fetch("http://103.253.20.13:25029/role_assign", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Failed to fetch transcript from the audio processing API');
        }

        const data = await response.json();
        return data.transcript || 'No transcript available.'; // Adjust based on the API response structure
    } catch (error) {
        console.error("Error:", error);
        return 'Error generating transcript.';
    }
}

// Function to update the transcript area
function updateTranscript(transcript) {
    const transcriptContent = document.getElementById('transcriptContent');
    transcriptContent.innerHTML = transcript || 'No transcript available.';
}
