import React from 'react';
import Button from './ui/button';
import Input from './ui/input';
import { Plus, MoreHorizontal } from 'lucide-react';

const VideoScoring = () => {
  const [videos, setVideos] = React.useState([
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
    }
  ]);

  const [filters, setFilters] = React.useState({
    video: '',
    teachingDate: '',
    mentor: '',
    score: ''
  });

  const handleFilterChange = (field, value) => {
    setFilters(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const filteredVideos = videos.filter(video => {
    return (
      video.title.toLowerCase().includes(filters.video.toLowerCase()) &&
      (!filters.teachingDate || video.teachingDate === filters.teachingDate) &&
      video.mentor.toLowerCase().includes(filters.mentor.toLowerCase()) &&
      (!filters.score || video.score === Number(filters.score))
    );
  });

  return (
    <div className="w-full p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Chấm điểm Video</h1>
      </div>

      <div className="mb-4">
        <Button 
          variant="outline" 
          size="sm"
          className="flex items-center gap-1 border-gray-300"
        >
          <Plus className="h-4 w-4" />
          Import video
        </Button>
      </div>

      <div className="flex gap-2 items-center mb-4">
        <Input 
          placeholder="Video" 
          className="w-64"
          value={filters.video}
          onChange={(e) => handleFilterChange('video', e.target.value)}
        />
        <Input 
          placeholder="Ngày dạy" 
          type="date"
          className="w-32"
          value={filters.teachingDate}
          onChange={(e) => handleFilterChange('teachingDate', e.target.value)}
        />
        <Input 
          placeholder="Mentor" 
          className="w-32"
          value={filters.mentor}
          onChange={(e) => handleFilterChange('mentor', e.target.value)}
        />
        <Input 
          placeholder="Điểm" 
          type="number"
          className="w-24"
          value={filters.score}
          onChange={(e) => handleFilterChange('score', e.target.value)}
        />
        <Button variant="ghost" size="icon">
          <MoreHorizontal className="h-5 w-5" />
        </Button>
      </div>

      <div className="space-y-2">
        {filteredVideos.map((video) => (
          <div 
            key={video.id}
            className="flex items-center justify-between p-3 bg-white rounded border border-gray-200 hover:bg-gray-50"
          >
            <div className="flex items-center gap-4 flex-1">
              <span className="min-w-64">{video.title}</span>
              <span className="min-w-32">{video.teachingDate}</span>
              <span className="min-w-32">{video.mentor}</span>
              <span className="min-w-24">{video.score}</span>
            </div>
            <div className="flex gap-2">
              <Button 
                size="sm" 
                variant="ghost"
                className="text-gray-500 hover:text-gray-700"
              >
                <MoreHorizontal className="h-4 w-4" />
              </Button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VideoScoring;