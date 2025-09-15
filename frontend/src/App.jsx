import React from 'react';
import CardCircle from './CardCircle';
import { edge_padding, cardSize, size } from './config';
import { generateGameButtonStyle, appContainerStyle, hpCircleContainerStyle } from './styles/styles';

function App() {
  const [cards, setCards] = React.useState([]);
  const [selected, setSelected] = React.useState(null);
  const [hp, setHp] = React.useState(10);


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
    setHp(10);
  };

  return (
    <div style={appContainerStyle}>
      {/* HP Circle Bar - bottom left */}
  <div style={hpCircleContainerStyle}>
        <svg width={80} height={80}>
          <circle
            cx={40}
            cy={40}
            r={36}
            stroke="#eee"
            strokeWidth={8}
            fill="none"
          />
          <circle
            cx={40}
            cy={40}
            r={36}
            stroke={hp > 3 ? 'green' : 'red'}
            strokeWidth={8}
            fill="none"
            strokeDasharray={2 * Math.PI * 36}
            strokeDashoffset={2 * Math.PI * 36 * (1 - hp / 10)}
            style={{ transition: 'stroke-dashoffset 0.3s' }}
          />
          <text
            x={40}
            y={46}
            textAnchor="middle"
            fontSize={22}
            fill="#ffffffff"
            fontWeight="bold"
          >
            {hp}
          </text>
        </svg>
      </div>
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
          const card = cards.find(c => c.position === position);
          if (card.alignment === 'good' && !card.is_dead) {
            setHp(hp => Math.max(hp - 5, 0));
          }
          setCards(cards.map(card =>
            card.position === position ? { ...card, is_dead: true } : card
          ));
          setSelected(null);
        }}
        size={size}
        cardSize={cardSize}
      />
    </div>
  );
}

export default App;