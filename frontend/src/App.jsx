import React from 'react';
import CardCircle from './CardCircle';

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
      justifyContent: 'center'
    }}>
      <CardCircle
        cards={cards}
        selected={selected}
        onSelect={setSelected}
        size={600}
        cardSize={200}
      />
    </div>
  );
}

export default App
