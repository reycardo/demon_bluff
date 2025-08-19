import React from 'react';

function App() {
  const [cards, setCards] = React.useState([]);
  const [selected, setSelected] = React.useState(null);

  React.useEffect(() => {
    fetch('game.json')
      .then((res) => res.json())
      .then(setCards)
      .catch(() => setCards([]));
  }, []);

  // Responsive circle layout
  const size = 500;
  const cardSize = 140; // Easily adjust card button size
  const imageSize = 120; // Easily adjust image size
  const radius = size / 2 - cardSize / 2 - 15;
  const center = size / 2;

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
      <div style={{ position: 'relative', width: size, height: size }}>
        {/* Template textbox above each button, positioned relative to its button */}
        {cards.map((card, i) => {
          const angle = (2 * Math.PI * i) / cards.length;
          const x = center + radius * Math.cos(angle) - cardSize / 2;
          const y = center + radius * Math.sin(angle) - cardSize / 2;
          // Center the textbox and button on the same y-axis
          return (
            <input
              key={card.name + '-template'}
              type="text"
              value={card.template}
              readOnly
              style={{
                position: 'absolute',
                left: x + cardSize / 2 - 60, // 60px is half the textbox width
                top: y - 44, // 44px above the button, adjust for vertical centering
                width: '120px',
                textAlign: 'center',
                fontSize: '1rem',
                background: '#000000ff',
                border: '1px solid #ccc',
                borderRadius: '8px',
                marginBottom: '8px',
                padding: '4px 8px',
                zIndex: 2
              }}
            />
          );
        })}
        {cards.map((card, i) => {
          const angle = (2 * Math.PI * i) / cards.length;
          const x = center + radius * Math.cos(angle) - cardSize / 2;
          const y = center + radius * Math.sin(angle) - cardSize / 2;
          return (
            <button
              key={card.name}
              style={{
                position: 'absolute',
                left: x,
                top: y,
                width: cardSize,
                height: cardSize,
                borderRadius: '50%',
                fontSize: '1.1rem',
                cursor: 'pointer',
                background: selected === card.name ? '#e0e0ff' : '#fff',
                border: '2px solid #888',
                boxShadow: '0 2px 6px rgba(0,0,0,0.1)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                overflow: 'hidden',
                transition: 'background 0.2s'
              }}
              onClick={() => setSelected(card.name)}
            >
              <img src={card.image} alt={card.name} style={{ width: imageSize, height: imageSize, objectFit: 'contain', marginBottom: 4 }} />
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
            background: '#000000ff',
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
