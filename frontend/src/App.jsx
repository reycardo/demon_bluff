import React from 'react';
import CardCircle from './CardCircle';
import { edge_padding } from './config';

function App() {
  const [cards, setCards] = React.useState([]);
  const [selected, setSelected] = React.useState(null);

  React.useEffect(() => {
    fetch('game.json')
      .then((res) => res.json())
      .then(setCards)
      .catch(() => setCards([]));
  }, []);

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

export default App
