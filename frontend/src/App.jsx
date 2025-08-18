import React, { useState, useEffect } from 'react';

function App() {
  const [cards, setCards] = useState([]);
  const [selected, setSelected] = useState(null);
  const [descriptions, setDescriptions] = useState({});

  useEffect(() => {
    fetch('game.json')
      .then((res) => res.json())
      .then((data) => {
        setCards(data);
      })
      .catch(() => setCards([]));
  }, []);

  // Circle layout
  const radius = 120;
  const centerX = 150;
  const centerY = 150;

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100vw',
      height: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      <div style={{ position: 'relative', width: 350, height: 350 }}>
        {cards.map((card, i) => {
          const angle = (2 * Math.PI * i) / cards.length;
          const x = 175 + radius * Math.cos(angle) - 40;
          const y = 175 + radius * Math.sin(angle) - 20;
          return (
            <button
              key={card.name}
              style={{
                position: 'absolute',
                left: x,
                top: y,
                width: 80,
                height: 80,
                borderRadius: '40px',
                fontSize: '1.1rem',
                cursor: 'pointer',
                background: selected === card.name ? '#e0e0ff' : '#fff',
                border: '2px solid #888',
                boxShadow: '0 2px 6px rgba(0,0,0,0.1)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                overflow: 'hidden'
              }}
              onClick={() => setSelected(card.name)}
            >
              <img src={card.image} alt={card.name} style={{ width: 48, height: 48, objectFit: 'contain', marginBottom: 4 }} />
              <span>{card.name}</span>
            </button>
          );
        })}
        {selected && (
          <div style={{
            position: 'absolute',
            left: '50%',
            top: '50%',
            transform: 'translate(-50%, -50%)',
            textAlign: 'center',
            fontSize: '1.2rem',
            minHeight: '2rem',
            maxWidth: '260px',
            margin: '0 auto',
            background: '#fff',
            borderRadius: '12px',
            padding: '1rem',
            boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
          }}>
            {cards.find(card => card.name === selected)?.template}
          </div>
        )}
      </div>
    </div>
  );
}

export default App
