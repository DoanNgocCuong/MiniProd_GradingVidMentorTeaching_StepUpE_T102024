// frontend/scripts.js

import { videoTranscripts } from './videoTranscripts.js'; // Adjust the path as necessary
import { baremScore } from './baremScore.js'; 

initializeResultTable();
let currentCriteria = ''; // Declare currentCriteria at the top

// document.getElementById('loadVideo').addEventListener('click', () => {
//     const videoLink = document.getElementById('videoLink').value.trim(); // Get the input value and trim whitespace
    
//     // Find the corresponding transcript
//     const fileId = videoLink.match(/\/d\/(.+?)\//)[1];
//     const videoData = videoTranscripts.find(video => video.videoId === fileId); // Change videoLink to videoId
        
//     if (videoData) {
//         // Create the preview link using the extracted file ID
//         const previewLink = `https://drive.google.com/file/d/${fileId}/preview`;
//         // Update the video player
//         document.getElementById('video').src = previewLink;

//         // Update the transcript area
//         updateTranscript(videoData.transcript);
        
//         // Add event listeners for criteria buttons
//         addCriteriaListeners(videoData.criteria, fileId);
//     } else {
//         alert('Invalid video link. Please provide a valid video link from the list.');
//     }
// });


document.getElementById('loadVideo').addEventListener('click', async () => {
    const videoLink = document.getElementById('videoLink').value.trim();
    const fileId = videoLink.match(/\/d\/(.+?)\//)[1];

    try {
        const response = await fetch(`http://localhost:5000/get_video_data?url=${videoLink}`);
        const data = await response.json();

        if (response.ok) {
            // Update video preview
            const previewLink = `https://drive.google.com/file/d/${fileId}/preview`;
            document.getElementById('video').src = previewLink;
            
            // Update transcript
            updateTranscript(data.transcript);
            
            // Parse criteria string to object and get inner criteria object
            const criteriaObj = JSON.parse(data.criteria);
            const criteria = criteriaObj.criteria;
            
            // Add event listeners
            addCriteriaListeners(criteria, fileId);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error loading video data');
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

// Function to add event listeners for criteria buttons
function addCriteriaListeners(criteria, videoId) {
    console.log("Criteria object:", criteria); // Debug log
    
    const buttons = document.querySelectorAll('.criteria-button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const criterionKey = button.getAttribute('data-criteria');
            console.log("Clicked:", criterionKey); // Debug log
            
            currentCriteria = criterionKey;
            const criterion = criteria[criterionKey];
            console.log("Found criterion:", criterion); // Debug log
            
            if (criterion) {
                highlightTranscript(criterion);
                displayCriteriaInfo(criterion, criterionKey);
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
function displayCriteriaInfo(criterion, criterionKey) {
    const criteriaTableBody = document.getElementById('criteriaTableBody');
    const descriptionRow = document.getElementById('descriptionRow');
    const evaluationRow = document.getElementById('evaluationRow');
    
    // Add this line to update the criteria title
    document.getElementById('selectedCriteriaTitle').textContent = `Selected Criteria: ${criterionKey}`;

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
    let found = false; // Flag to check if criteria row is found
    for (let row of rows) {
        const criteriaCell = row.cells[0];
        if (criteriaCell.textContent === currentCriteria) {
            // Update the note and score for the corresponding criteria
            row.cells[1].textContent = note; // Set note text
            row.cells[2].textContent = score; // Set score text
            found = true; // Set found flag to true
            break; // Exit the loop once found
        }
    }

    // If the criteria row was not found, add a new row
    if (!found) {
        const newRow = document.createElement('tr');
        const criteriaCell = document.createElement('td');
        criteriaCell.textContent = criteria; // Set criteria text
        newRow.appendChild(criteriaCell);

        const noteCell = document.createElement('td');
        noteCell.textContent = note; // Set note text
        newRow.appendChild(noteCell);

        const scoreCell = document.createElement('td');
        scoreCell.textContent = score; // Set score text
        newRow.appendChild(scoreCell);

        // Append the new row to the table body
        resultTableBody.appendChild(newRow);
    }

    // Show the table if it was hidden
    document.getElementById('resultTable').style.display = 'table';
}

// Add event listener for the Save button
document.getElementById('saveScoreButton').addEventListener('click', () => {
    const scoreInput = document.getElementById('scoreInput').value; // Get the score input value
    const noteInput = document.getElementById('noteInput').value; // Get the note input value

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





async function displayCriteriaRecommendation(criterionKey, videoId) {
    const scoreElement = document.getElementById('criteriaScore');
    const reasonElement = document.getElementById('criteriaReason');

    // Clear previous recommendations
    scoreElement.textContent = 'Score: N/A';
    reasonElement.textContent = 'Reason: N/A';

    try {
        // Get data from server again (or you could store it in a variable)
        const response = await fetch(`http://localhost:5000/get_video_data?url=https://drive.google.com/file/d/${videoId}/view`);
        const data = await response.json();

        if (response.ok) {
            const criteria = JSON.parse(data.criteria).criteria;
            const criterion = criteria[criterionKey];

            if (criterion) {
                const recommendationScore = criterion.recommendationScore;
                if (recommendationScore) {
                    scoreElement.textContent = `Score: ${recommendationScore.score}`;
                    reasonElement.innerHTML = `Reason: ${recommendationScore.reason.replace(/\n/g, '<br>')}`;
                }
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
}