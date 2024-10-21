import { videoTranscripts } from './videoTranscripts.js'; // Adjust the path as necessary

document.getElementById('loadVideo').addEventListener('click', () => {
    const videoLink = document.getElementById('videoLink').value.trim(); // Get the input value and trim whitespace
    
    // Find the corresponding transcript
    const videoData = videoTranscripts.find(video => video.videoLink === videoLink);
    
    if (videoData) {
        // Update the video player
        document.getElementById('video').src = videoData.videoLink;

        // Update the transcript area
        updateTranscript(videoData.transcript);
        
        // Add event listeners for criteria buttons
        addCriteriaListeners(videoData.criteria);
    } else {
        alert('Invalid video link. Please provide a valid video link from the list.');
    }
});

// Function to update the transcript area
function updateTranscript(transcript) {
    const transcriptContent = document.getElementById('transcriptContent');
    const formattedTranscript = formatTranscript(transcript); // Format the transcript
    transcriptContent.innerHTML = formattedTranscript || 'No transcript available.'; // Set the inner HTML to the formatted transcript
}

// Function to format the transcript by adding <br> at the start of each line
function formatTranscript(transcript) {
    // Split the transcript into lines, trim whitespace, and filter out empty lines
    const lines = transcript.split('\n').map(line => line.trim()).filter(line => line.length > 0);
    
    // Join the lines with <br> tags
    return lines.map(line => `<br>${line}`).join('');
}

function addCriteriaListeners(criteria) {
    const buttons = document.querySelectorAll('.criteria-button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const criterion = button.getAttribute('data-criteria');
            highlightTranscript(criteria[criterion]);
        });
    });
}

// Function to highlight the transcript based on the selected criterion
function highlightTranscript(criterion) {
    const transcriptContent = document.getElementById('transcriptContent');
    
    // Clear any existing highlights
    const existingHighlights = transcriptContent.querySelectorAll('.highlight');
    existingHighlights.forEach(highlight => {
        highlight.classList.remove('highlight'); // Remove the highlight class
        highlight.outerHTML = highlight.innerHTML; // Replace the highlight element with its inner HTML
    });

    const transcriptText = transcriptContent.innerHTML;

    // Extract start and end timestamps
    const start = criterion.timestamp.start;
    const end = criterion.timestamp.end;

    // Create a regex to find the lines between the start and end timestamps
    const regex = new RegExp(`(${start}.*?)(?=${end}|$)`, 'g');
    
    // Highlight the matched text with a card view and include the criteria name
    const highlightedTranscript = transcriptText.replace(regex, `<div class="highlight" data-criteria="${criterion.recommendationScore.reason}">$1</div>`);
    transcriptContent.innerHTML = highlightedTranscript;

    // Scroll to the highlighted section
    const highlightedElement = transcriptContent.querySelector('.highlight');
    if (highlightedElement) {
        highlightedElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

// Function to display the selected criteria's score and reason
function displayCriteriaInfo(criterion) {
    const scoreElement = document.getElementById('criteriaScore');
    const reasonElement = document.getElementById('criteriaReason');

    // Update the score and reason display
    scoreElement.textContent = `Score: ${criterion.recommendationScore.score !== null ? criterion.recommendationScore.score : 'N/A'}`;
    reasonElement.textContent = `Reason: ${criterion.recommendationScore.reason}`;
}
