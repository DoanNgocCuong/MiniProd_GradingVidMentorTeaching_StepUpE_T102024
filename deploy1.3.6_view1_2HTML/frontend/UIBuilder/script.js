// Replace the sample data with API calls
let videos = [];

// Function to fetch scores from API
async function fetchScores(urlVideo) {
    try {
        const response = await fetch(`http://localhost:25035/get_scores?url_video=${encodeURIComponent(urlVideo)}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching scores:', error);
        return [];
    }
}

// Add new function to fetch video data
async function fetchVideoData(urlVideo) {
    try {
        const response = await fetch(`http://localhost:25035/get_video_data?url=${encodeURIComponent(urlVideo)}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching video data:', error);
        return null;
    }
}

// Update the processVideoData function
async function processVideoData(videoList) {
    if (!videoList.length) return [];
    
    return videoList.map(video => ({
        url_video: video.url_video,
        title: video.name_video || 'Unknown Video',
        timestamp: new Date().toISOString(), // You might want to add timestamp to your API response
        criteria: video.criteria.split(',').map(c => c.trim()) // Convert criteria string to array
    }));
}

// Filter state
let filters = {
    title: '',
    teachingDate: '',
    mentor: '',
    score: ''
};

// Filter videos based on current filters
function filterVideos() {
    return videos.filter(video => {
        // Chuyển đổi giá trị để so sánh
        const titleMatch = !filters.title || 
            video.title.toLowerCase().includes(filters.title.toLowerCase());
        
        const dateMatch = !filters.teachingDate || 
            video.teachingDate === filters.teachingDate;
        
        const mentorMatch = !filters.mentor || 
            video.mentor.toLowerCase().includes(filters.mentor.toLowerCase());
        
        const scoreMatch = !filters.score || 
            Math.abs(video.score - Number(filters.score)) < 0.01;

        console.log('Filter check for video:', video.title, {
            titleMatch,
            dateMatch,
            mentorMatch,
            scoreMatch,
            currentScore: video.score,
            filterScore: Number(filters.score)
        });

        return titleMatch && dateMatch && mentorMatch && scoreMatch;
    });
}

// Render video list
function renderVideos() {
    const videoList = document.getElementById('videoList');
    const filteredVideos = filterVideos();
    
    videoList.innerHTML = filteredVideos.map(video => `
        <tr class="video-row" data-url="${encodeURIComponent(video.url_video)}">
            <td class="video-title">
                <span>${video.title}</span>
            </td>
            <td>${formatDate(video.timestamp)}</td>
            <td>Mentor Name</td>
            <td>
                <button class="action-btn">
                    <i data-lucide="more-horizontal" style="width: 16px; height: 16px;"></i>
                </button>
            </td>
        </tr>
    `).join('');

    // Update click handler
    document.querySelectorAll('.video-row').forEach(row => {
        row.addEventListener('click', async () => {
            const videoUrl = decodeURIComponent(row.dataset.url);
            
            try {
                // Chuyển sang trang chấm điểm với video URL là parameter
                window.location.href = `../index.html?video=${encodeURIComponent(videoUrl)}`;
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });

    lucide.createIcons();
}

// Helper function to format date
function formatDate(timestamp) {
    if (!timestamp) return '-';
    return new Date(timestamp).toLocaleDateString('vi-VN');
}

// Update the fetchVideos function to get all videos
async function fetchVideos() {
    try {
        const response = await fetch('http://localhost:25035/get_videos');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching videos:', error);
        return [];
    }
}
// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', async function() {
    try {
        // Fetch all videos instead of just one
        const videoList = await fetchVideos();
        videos = await processVideoData(videoList);
        
        // Initial render
        renderVideos();
        lucide.createIcons();

        // Setup event listeners for filters
        document.querySelectorAll('.input').forEach(input => {
            input.addEventListener('input', (e) => {
                try {
                    const filterKey = e.target.dataset.filter;
                    const oldValue = filters[filterKey];
                    filters[filterKey] = e.target.value;
                    
                    console.log('Filter updated:', {
                        filter: filterKey,
                        oldValue: oldValue,
                        newValue: e.target.value,
                        allFilters: {...filters}
                    });
                    
                    renderVideos();
                } catch (error) {
                    console.error('Error updating filters:', error);
                }
            });
        });

        // Add at the top with other event listeners
        document.getElementById('backToScoring').addEventListener('click', () => {
            try {
                window.location.href = '../index.html';
            } catch (error) {
                console.error('Navigation error:', error);
            }
        });
    } catch (error) {
        console.error('Error initializing app:', error);
    }
});
