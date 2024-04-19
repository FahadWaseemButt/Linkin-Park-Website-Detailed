import React, { useState, useEffect } from 'react';

function App() {
  const [members, setMembers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/members')
      .then(res => res.json())
      .then(data => {
        setMembers(data.members);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching members:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {members.map((member, index) => (
            <li key={index}>{member}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;