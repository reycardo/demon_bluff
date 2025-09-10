import React from 'react';
import CardCircle from './CardCircle';
import { edge_padding } from './config';
import { generateGameButtonStyle } from './buttonStyles';

function App() {
  const [cards, setCards] = React.useState([]);
  const [selected, setSelected] = React.useState(null);

  // Fetch initial game disposition
  React.useEffect(() => {
    fetchGameDisposition();
  }, []);

  // Function to fetch game disposition from backend
  const fetchGameDisposition = async () => {    
    const res = await fetch('http://localhost:8000/api/game_disposition', { method: 'POST' });
    const data = await res.json();
    setCards(data);
    setSelected(null);
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100vw',
      height: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column'
    }}>
      <button
        style={generateGameButtonStyle}
        onClick={fetchGameDisposition}
      >
        Generate Game
      </button>
      <CardCircle
        cards={cards}
        selected={selected}
        onSelect={setSelected}
        edge_padding={edge_padding}
        onKill={position => {
          setCards(cards.map(card =>
            card.position === position ? { ...card, killed: true } : card
          ));
          setSelected(null);
        }}
        size={500}
        cardSize={180}
      />
    </div>
  );
}

export default App;