import { videoTranscripts } from './videoTranscripts.js';
import { baremScore } from './baremScore.js'; 

initializeResultTable();
let currentCriteria = '';
let currentVideoUrl = '';

document.getElementById('loadVideo').addEventListener('click', async () => {
    const videoLink = document.getElementById('videoLink').value.trim();
    currentVideoUrl = videoLink;
    
    try {
        const fileIdMatch = videoLink.match(/\/d\/(.+?)\//);
        if (!fileIdMatch) {
            throw new Error('Invalid Google Drive URL format');
        }
        const fileId = fileIdMatch[1];

        const response = await fetch(`http://localhost:25035/get_video_data?url=${encodeURIComponent(videoLink)}`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        const previewLink = `https://drive.google.com/file/d/${fileId}/preview`;
        const videoFrame = document.getElementById('video');
        videoFrame.src = previewLink;
        videoFrame.setAttribute('sandbox', 'allow-same-origin allow-scripts');
        
        updateTranscript(data.transcript);
        const criteriaObj = JSON.parse(data.criteria);
        addCriteriaListeners(criteriaObj, fileId);
        await loadSavedScores(currentVideoUrl);
        
    } catch (error) {
        console.error('Error:', error);
        showNotification('warning', `Error loading video data: ${error.message}`);
    }
});

function updateTranscript(transcript) {
    const transcriptContent = document.getElementById('transcriptContent');
    const formattedTranscript = formatTranscript(transcript);
    transcriptContent.innerHTML = formattedTranscript || 'No transcript available.';
}

function formatTranscript(transcript) {
    const lines = transcript.split('\n').map(line => line.trim()).filter(line => line.length > 0);
    return lines.map(line => `<br>${line}`).join('');
}

function addCriteriaListeners(criteriaObj, videoId) {
    console.log("Criteria object:", criteriaObj);
    
    const buttons = document.querySelectorAll('.criteria-button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const criterionKey = button.getAttribute('data-criteria');
            console.log("Clicked:", criterionKey);
            
            currentCriteria = criterionKey;
            const criterion = criteriaObj[criterionKey];
            console.log("Found criterion:", criterion);
            
            if (criterion) {
                highlightTranscript(criterion);
                displayCriteriaInfo(criterion, criterionKey);
                displayCriteriaRecommendation(criterionKey, videoId);
            }
        });
    });
}

function highlightTranscript(criterion) {
    const transcriptContent = document.getElementById('transcriptContent');
    
    const existingHighlights = transcriptContent.querySelectorAll('.highlight');
    existingHighlights.forEach(highlight => {
        highlight.classList.remove('highlight');
        highlight.outerHTML = highlight.innerHTML;
    });

    const transcriptText = transcriptContent.innerHTML;
    const start = criterion.timestamp.start;
    const end = criterion.timestamp.end;
    const regex = new RegExp(`(${start}.*?)(?=${end}|$)`, 'g');
    
    const highlightedTranscript = transcriptText.replace(regex, `<div class="highlight" data-criteria="${criterion.recommendationScore.reason}">$1</div>`);
    transcriptContent.innerHTML = highlightedTranscript;

    const highlightedElement = transcriptContent.querySelector('.highlight');
    if (highlightedElement) {
        highlightedElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function displayCriteriaInfo(criterion, criterionKey) {
    const criteriaTableBody = document.getElementById('criteriaTableBody');
    const descriptionRow = document.getElementById('descriptionRow');
    const evaluationRow = document.getElementById('evaluationRow');
    
    document.getElementById('selectedCriteriaTitle').textContent = `Selected Criteria: ${criterionKey}`;

    descriptionRow.innerHTML = '';
    evaluationRow.innerHTML = '';

    const evaluationData = baremScore.evaluation[criterionKey];
    if (evaluationData) {
        for (let i = 1; i <= 5; i++) {
            const cell = document.createElement('td');
            cell.textContent = evaluationData[i.toString()];
            evaluationRow.appendChild(cell);
        }
    } else {
        console.warn(`No evaluation data found for: ${criterion.recommendationScore.reason}`);
    }

    document.getElementById('criteriaTable').style.display = 'table';
}

function handleScoreInput() {
    const scoreInput = document.getElementById('scoreInput');
    const noteInput = document.getElementById('noteInput');

    scoreInput.addEventListener('change', () => {
        console.log(`Score entered: ${scoreInput.value}`);
    });

    noteInput.addEventListener('input', () => {
        console.log(`Notes entered: ${noteInput.value}`);
    });
}

handleScoreInput();

function displayResults(criteria, note, score) {
    const resultTableBody = document.getElementById('resultTableBody');
    
    const rows = resultTableBody.getElementsByTagName('tr');
    let found = false;
    
    for (let row of rows) {
        const criteriaCell = row.cells[0];
        if (criteriaCell.textContent === criteria) {
            row.cells[1].textContent = note;
            row.cells[2].textContent = score;
            found = true;
            break;
        }
    }

    if (!found) {
        const newRow = document.createElement('tr');
        
        const criteriaCell = document.createElement('td');
        criteriaCell.textContent = criteria;
        newRow.appendChild(criteriaCell);

        const noteCell = document.createElement('td');
        noteCell.textContent = note;
        newRow.appendChild(noteCell);

        const scoreCell = document.createElement('td');
        scoreCell.textContent = score;
        newRow.appendChild(scoreCell);

        resultTableBody.appendChild(newRow);
    }

    document.getElementById('resultTable').style.display = 'table';
}

// Update save button event listener
document.getElementById('saveScoreButton').addEventListener('click', async (event) => {
    // Prevent any default behavior
    event.preventDefault();
    event.stopPropagation();
    
    const scoreInput = document.getElementById('scoreInput').value;
    const noteInput = document.getElementById('noteInput').value;
    
    // Validation
    if (!scoreInput || !currentCriteria || !currentVideoUrl) {
        showNotification('warning', 'Please ensure all fields are filled and a video is loaded');
        return;
    }

    const scoreData = {
        url_video: currentVideoUrl,
        criteria: currentCriteria,
        score: parseInt(scoreInput),
        note: noteInput,
        timestamp: new Date().toISOString()
    };

    try {
        const response = await fetch('http://localhost:25035/save_score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(scoreData)
        });

        if (response.ok) {
            // Update UI without page refresh
            displayResults(currentCriteria, noteInput, scoreInput);
            
            // Clear inputs
            document.getElementById('scoreInput').value = '';
            document.getElementById('noteInput').value = '';
        } else {
            throw new Error('Failed to save score');
        }
    } catch (error) {
        console.error('Error saving score:', error);
        showNotification('warning', 'Failed to save score. Please try again.');
    }
    
    // Prevent any form submission
    return false;
});

// Utility functions for notifications
function showNotification(type, message) {
    const overlay = document.createElement('div');
    overlay.className = 'modal-overlay';
    document.body.appendChild(overlay);
    overlay.style.display = 'block';

    const notification = document.getElementById(type === 'success' ? 'saveNotification' : 'warningNotification');
    
    if (type === 'warning') {
        document.getElementById('warningMessage').textContent = message;
    }
    
    notification.style.display = 'block';

    const closeNotification = () => {
        notification.style.display = 'none';
        overlay.style.display = 'none';
        overlay.remove();
    };

    // Close on button click
    notification.querySelector('button').onclick = closeNotification;
    
    // Close on overlay click
    overlay.onclick = closeNotification;
}

function initializeResultTable() {
    const resultTableBody = document.getElementById('resultTableBody');
    resultTableBody.innerHTML = '';

    const evaluationKeys = Object.keys(baremScore.evaluation);

    evaluationKeys.forEach(key => {
        const row = document.createElement('tr');

        const criteriaCell = document.createElement('td');
        criteriaCell.textContent = key;
        row.appendChild(criteriaCell);

        const noteCell = document.createElement('td');
        noteCell.textContent = '';
        row.appendChild(noteCell);

        const scoreCell = document.createElement('td');
        scoreCell.textContent = '';
        row.appendChild(scoreCell);

        resultTableBody.appendChild(row);
    });

    document.getElementById('resultTable').style.display = 'table';
}

// Update error handling in other functions
async function loadSavedScores(videoUrl) {
    try {
        const encodedUrl = encodeURIComponent(videoUrl);
        const response = await fetch(`http://localhost:25035/get_scores?url_video=${encodedUrl}`);
        const scores = await response.json();
        
        if (Array.isArray(scores)) {
            scores.forEach(score => {
                displayResults(score.criteria, score.note, score.score);
            });
        } else {
            console.warn('Received scores is not an array:', scores);
        }
    } catch (error) {
        console.error('Error loading saved scores:', error);
        showNotification('warning', 'Error loading saved scores');
    }
}

async function displayCriteriaRecommendation(criterionKey, videoId) {
    const scoreElement = document.getElementById('criteriaScore');
    const reasonElement = document.getElementById('criteriaReason');

    try {
        const response = await fetch(`http://localhost:25035/get_video_data?url=https://drive.google.com/file/d/${videoId}/view`);
        const data = await response.json();

        if (response.ok) {
            const criteriaObj = JSON.parse(data.criteria);
            const criterion = criteriaObj[criterionKey];

            if (criterion && criterion.recommendationScore) {
                scoreElement.textContent = `Score: ${criterion.recommendationScore.score}`;
                reasonElement.innerHTML = `Reason: ${criterion.recommendationScore.reason}`;
            } else {
                scoreElement.textContent = 'Score: N/A';
                reasonElement.textContent = 'Reason: N/A';
            }
        }
    } catch (error) {
        console.error('Error:', error);
        scoreElement.textContent = 'Score: Error';
        reasonElement.textContent = 'Reason: Error loading data';
    }
}