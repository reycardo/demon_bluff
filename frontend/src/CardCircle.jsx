import CardButton from './CardButton';
import React from 'react';
import { cardSize as configCardSize, size as configSize, edge_padding as configEdgePadding } from './config';
import { killButtonStyle, selectedCardInfoStyle } from './styles/styles';

export default function CardCircle({ cards, selected, onSelect, size = configSize, cardSize = configCardSize, edge_padding = configEdgePadding, onKill }) {
  // Dynamic radius based on viewport size
  const [radius, setRadius] = React.useState(() => {
    const minDim = Math.min(window.innerWidth, window.innerHeight);
    return (minDim - cardSize) / 2 - edge_padding;
  });
  const center = size / 2;

  React.useEffect(() => {
    function handleResize() {
      const minDim = Math.min(window.innerWidth, window.innerHeight);
      setRadius((minDim - cardSize) / 2 - edge_padding);
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
            card={card}
            x={x}
            y={y}
            cardSize={cardSize}
            selected={selected}
            onSelect={onSelect}
          />
        );
      })}
      {selected !== null && (() => {
        const card = cards.find(card => card.position === selected);        
        if (!card) return null;
        const mask = card.masked_card;
        return (
          <div style={selectedCardInfoStyle}>
            <div><strong>Description:</strong> {mask ? mask.description : card.description}</div>
            <div><strong>Type:</strong> {mask ? mask.type : card.type}</div>
            <div><strong>Alignment:</strong> {mask ? mask.alignment : card.alignment}</div>
            <button
              style={killButtonStyle}
              onClick={() => onKill(card.position)}
            >
              Kill Selected Card
            </button>
          </div>
        );
      })()}
    </div>
  );
}
