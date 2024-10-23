import { videoTranscripts } from './videoTranscripts.js'; // Adjust the path as necessary
import { baremScore } from './baremScore.js'; 

initializeResultTable();
let currentCriteria = '';
document.getElementById('loadVideo').addEventListener('click', () => {
    const videoLink = document.getElementById('videoLink').value.trim(); // Get the input value and trim whitespace
    
    // Find the corresponding transcript
    const fileId = videoLink.match(/\/d\/(.+?)\//)[1];
    const videoData = videoTranscripts.find(video => video.videoId === fileId); // Change videoLink to videoId
        
    if (videoData) {
        // Create the preview link using the extracted file ID
        const previewLink = `https://drive.google.com/file/d/${fileId}/preview`;
        // Update the video player
        document.getElementById('video').src = previewLink;

        // Update the transcript area
        updateTranscript(videoData.transcript);
        
        // Add event listeners for criteria buttons
        addCriteriaListeners(videoData.criteria, fileId);
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

function addCriteriaListeners(criteria, videoId) {
    const buttons = document.querySelectorAll('.criteria-button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const criterionKey = button.getAttribute('data-criteria'); // Get the criterion key
            currentCriteria = criterionKey
            const criterion = criteria[criterionKey]; // Get the corresponding criterion object
            if (criterion) {
                highlightTranscript(criterion); // Highlight the transcript
                displayCriteriaInfo(criterion, criterionKey); // Show score, reason, and description
                displayCriteriaRecommendation(criterionKey, videoId);
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

// Function to display results in the result table
function displayResults(criteria, note, score) {
    const resultTableBody = document.getElementById('resultTableBody');
    
    // Find the row corresponding to the criteria
    const rows = resultTableBody.getElementsByTagName('tr');
    for (let row of rows) {
        const criteriaCell = row.cells[0];
        if (criteriaCell.textContent === criteria) {
            // Update the note and score for the corresponding criteria
            row.cells[1].textContent = note; // Set note text
            row.cells[2].textContent = score; // Set score text
            break; // Exit the loop once found
        }
    }
}

// Add event listener for the Save button
document.getElementById('saveScoreButton').addEventListener('click', () => {
    const scoreInput = document.getElementById('scoreInput').value; // Get the score input value
    const noteInput = document.getElementById('noteInput').value; // Get the note input value

    // Assuming you have a way to determine the current criteria (e.g., from a selected button)
    const currentCriteria = "Warm-up"; // Replace with the actual criteria name as needed

    // Call the function to display results
    displayResults(currentCriteria, noteInput, scoreInput); // Update the result table

    // Optionally, clear the input fields after saving
    document.getElementById('scoreInput').value = '';
    document.getElementById('noteInput').value = '';
});

// Function to initialize the result table with evaluation criteria
function initializeResultTable() {
    const resultTableBody = document.getElementById('resultTableBody');
    
    // Clear previous rows
    resultTableBody.innerHTML = '';

    // Get the evaluation keys from baremScore
    const evaluationKeys = Object.keys(baremScore.evaluation);

    // Populate the table with evaluation criteria
    evaluationKeys.forEach(key => {
        const row = document.createElement('tr');

        // Create cells for Criteria, Note, and Score
        const criteriaCell = document.createElement('td');
        criteriaCell.textContent = key; // Set criteria text
        row.appendChild(criteriaCell);

        const noteCell = document.createElement('td');
        noteCell.textContent = ''; // Initially empty note
        row.appendChild(noteCell);

        const scoreCell = document.createElement('td');
        scoreCell.textContent = ''; // Initially empty score
        row.appendChild(scoreCell);

        // Append the row to the table body
        resultTableBody.appendChild(row);
    });

    // Show the table
    document.getElementById('resultTable').style.display = 'table';
}

// Call this function when the page loads or when you want to initialize the table





function displayCriteriaRecommendation(criterionKey, videoId) {
    const scoreElement = document.getElementById('criteriaScore');
    const reasonElement = document.getElementById('criteriaReason');

    // Clear previous recommendations
    scoreElement.textContent = 'Score: N/A';
    reasonElement.textContent = 'Reason: N/A';

    // Find the video data by videoId
    const videoData = videoTranscripts.find(video => video.videoId === videoId);

    if (videoData) {
        // Get the selected criterion's recommendation score
        const criterion = videoData.criteria[criterionKey]; // Use the currentCriteria to get the selected criterion

        if (criterion) {
            const recommendationScore = criterion.recommendationScore; // Get the recommendation score object
            if (recommendationScore) {
                scoreElement.textContent = `Score: ${recommendationScore.score}`; // Update score
                reasonElement.textContent = `Reason: ${recommendationScore.reason}`; // Update reason
            }
        } else {
            console.warn(`No criterion found for: ${currentCriteria}`);
        }
    } else {
        console.warn(`No video found with videoId: ${videoId}`);
    }
}
