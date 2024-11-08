// Sample data
const videos = [
    {
        id: 1,
        title: "Giới thiệu về JavaScript cơ bản",
        teachingDate: "2024-03-15",
        mentor: "Nguyễn Văn A",
        score: 8.5,
    },
    {
        id: 2,
        title: "Hướng dẫn React Hooks",
        teachingDate: "2024-03-18",
        mentor: "Trần Thị B",
        score: 9.0,
    },
    {
        id: 3,
        title: "Khám phá Node.js",
        teachingDate: "2024-03-20",
        mentor: "Lê Văn C",
        score: 8.0,
    },
    {
        id: 4,
        title: "Tìm hiểu về TypeScript",
        teachingDate: "2024-03-22",
        mentor: "Nguyễn Thị D",
        score: 9.5,
    },
    {
        id: 5,
        title: "Giới thiệu về GraphQL",
        teachingDate: "2024-03-25",
        mentor: "Trần Văn E",
        score: 8.8,
    }
];

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
        <div class="video-item">
            <div class="video-info">
                <span class="video-title">${video.title}</span>
                <span class="video-date">${video.teachingDate}</span>
                <span class="video-mentor">${video.mentor}</span>
                <span class="video-score">${video.score}</span>
            </div>
            <div class="video-actions">
                <button class="action-btn">
                    <i data-lucide="more-horizontal" style="width: 16px; height: 16px;"></i>
                </button>
            </div>
        </div>
    `).join('');

    // Reinitialize Lucide icons for newly added elements
    lucide.createIcons();
}

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
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
});