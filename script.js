import { videoTranscripts } from './videoTranscripts.js'; // Adjust the path as necessary
import { baremScore } from './baremScore.js'; 

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
            const criterionKey = button.getAttribute('data-criteria'); // Get the criterion key
            const criterion = criteria[criterionKey]; // Get the corresponding criterion object
            
            if (criterion) {
                highlightTranscript(criterion); // Highlight the transcript
                displayCriteriaInfo(criterion, criterionKey); // Show score, reason, and description
            }
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

// Function to display the selected criteria's score, reason, and description
function displayCriteriaInfo(criterion,criterionKey) {
    const criteriaTableBody = document.getElementById('criteriaTableBody');
    const descriptionRow = document.getElementById('descriptionRow');
    const evaluationRow = document.getElementById('evaluationRow');

    // Clear previous rows
    descriptionRow.innerHTML = '';
    evaluationRow.innerHTML = '';

    // Get the criteria descriptions from baremScore
    const criteriaDescriptions = baremScore.criteria;

    // Populate the description row
    // criteriaDescriptions.forEach(item => {
    //     const cell = document.createElement('td');
    //     cell.textContent = item.description; // Use the description from baremScore
    //     descriptionRow.appendChild(cell);
    // });

    // Get the evaluation data for the selected criterion
    // const evaluationData = baremScore.evaluation[criterion.recommendationScore.reason];

    const evaluationData = baremScore.evaluation[criterionKey];
    // Populate the evaluation row
    if (evaluationData) {
        for (let i = 1; i <= 5; i++) {
            const cell = document.createElement('td');
            cell.textContent = evaluationData[i.toString()]; // Get evaluation text
            evaluationRow.appendChild(cell);
        }
    } else {
        console.warn(`No evaluation data found for: ${criterion.recommendationScore.reason}`);
    }

    // Show the table
    document.getElementById('criteriaTable').style.display = 'table';
}

// Function to handle score input and notes
function handleScoreInput() {
    const scoreInput = document.getElementById('scoreInput');
    const noteInput = document.getElementById('noteInput');

    // Example: Log the score and notes when the score is updated
    scoreInput.addEventListener('change', () => {
        console.log(`Score entered: ${scoreInput.value}`);
    });

    noteInput.addEventListener('input', () => {
        console.log(`Notes entered: ${noteInput.value}`);
    });
}

// Call the function to set up event listeners
handleScoreInput();
