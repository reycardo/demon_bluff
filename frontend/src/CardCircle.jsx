import CardButton from './CardButton';

import React from 'react';

export default function CardCircle({ cards, selected, onSelect, size = 500, cardSize = 80 }) {
  // Dynamic radius based on viewport size
  const [radius, setRadius] = React.useState(() => {
    const minDim = Math.min(window.innerWidth, window.innerHeight);
    return (minDim - cardSize) / 2 - 150; // 150px padding from edge
  });
  const center = size / 2;

  React.useEffect(() => {
    function handleResize() {
      const minDim = Math.min(window.innerWidth, window.innerHeight);
      setRadius((minDim - cardSize) / 2 - 60);
    }
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [cardSize]);

  return (
    <div style={{ position: 'relative', width: size, height: size }}>
      {cards.map((card, i) => {
        // Start with a card at the top (angle -Math.PI/2)
        const angle = (2 * Math.PI * i) / cards.length - Math.PI / 2;
        const x = center + radius * Math.cos(angle) - cardSize / 2;
        const y = center + radius * Math.sin(angle) - cardSize / 2;
        return (
          <CardButton
            key={card.name}
            card={card}
            x={x}
            y={y}
            cardSize={cardSize}
            selected={selected}
            onSelect={onSelect}
          />
        );
      })}
      {selected && (() => {
        const card = cards.find(card => card.name === selected);
        if (!card) return null;
        return (
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
            border: '1px solid #ccc',
            borderRadius: '20px',
            padding: '1rem',
            boxShadow: '0 2px 8px rgba(0,0,0,0.08)'
          }}>
            <div><strong>Description:</strong> {card.description}</div>
            <div><strong>Type:</strong> {card.type}</div>
            <div><strong>Alignment:</strong> {card.alignment}</div>
          </div>
        );
      })()}
    </div>
  );
}
