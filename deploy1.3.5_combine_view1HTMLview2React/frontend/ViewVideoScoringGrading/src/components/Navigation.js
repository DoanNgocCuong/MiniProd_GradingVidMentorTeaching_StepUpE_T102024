 

const Navigation = () => {
  return (
    <nav style={{
      backgroundColor: '#333',
      padding: '1rem',
      marginBottom: '1rem'
    }}>
      <ul style={{
        listStyle: 'none',
        display: 'flex',
        gap: '2rem',
        margin: 0,
        padding: 0
      }}>
        <li>
          <a 
            href="/scoring"
            style={{
              color: 'white',
              textDecoration: 'none'
            }}
          >
            Scoring Results
          </a>
        </li>
        <li>
          <a 
            href="/grading"
            style={{
              color: 'white',
              textDecoration: 'none'
            }}
          >
            Video Scoring
          </a>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;